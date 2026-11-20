"""Render STEP and USDZ previews with CadQuery, usd-core, NumPy and Blender's bpy."""
import argparse
import math
from pathlib import Path

import bpy
import cadquery as cq
from mathutils import Vector
import numpy as np
from OCP.BRep import BRep_Tool
from OCP.TopAbs import TopAbs_REVERSED
from OCP.TopLoc import TopLoc_Location
from pxr import Gf, Usd, UsdGeom, UsdShade

ROOT = Path(__file__).resolve().parents[1]
V2 = "data-collection-camera-mount-v2"
BOX = ROOT / "data-collection-environment/box.usdz"
TALL_MOUNTS = {"mount-1", "mount-2", "mount-3", "mount-4"}
# Convert Y-up geometry to Z-up without flipping the winding.
Y_UP_TO_Z_UP = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])


def preview_target(source):
    folder = ROOT / "images"
    if source.parent.name == "V1" and source.parent.parent.name == "b601-camera-mounts":
        folder /= "b601-v1"
    return folder / f"{source.stem}.png"


def tessellate(part):
    part.mesh(0.05, 0.1)
    points, triangles = [], []
    for face in part.Faces():
        location = TopLoc_Location()
        surface = BRep_Tool.Triangulation_s(face.wrapped, location)
        if surface is None:
            # Some STEP adapters contain degenerate faces with zero area.
            if abs(face.Area()) < 1e-8:
                continue
            raise ValueError("Unable to tessellate a nondegenerate STEP face")

        transform = location.Transformation()
        offset = len(points) - 1  # OpenCascade nodes are 1-based.
        for index in range(1, surface.NbNodes() + 1):
            point = surface.Node(index).Transformed(transform)
            points.append((point.X(), point.Y(), point.Z()))
        reversed_face = face.wrapped.Orientation() == TopAbs_REVERSED
        for triangle in surface.Triangles():
            a, b, c = triangle.Get()
            if reversed_face:
                b, c = c, b
            triangles.append((a + offset, b + offset, c + offset))
    return np.array(points), triangles


def step_meshes(source):
    shape = cq.importers.importStep(str(source)).val()
    if source.stem != V2:
        parts = [(shape, "Polymer")]
    else:
        parts = []
        for solid in shape.Solids():
            bounds = solid.BoundingBox()
            # The source assembly uses four 20 × 20 mm extrusion segments.
            profile = math.isclose(bounds.xlen, 20, abs_tol=0.01) and math.isclose(
                bounds.zlen, 20, abs_tol=0.01
            )
            parts.append((solid, "Aluminum" if profile and bounds.ylen > 100 else "Polymer"))

    for part, finish in parts:
        points, triangles = tessellate(part)
        if source.stem == V2:
            points = points @ Y_UP_TO_Z_UP.T
        yield points, triangles, finish


def usd_meshes(source):
    stage = Usd.Stage.Open(str(source))
    cache = UsdGeom.XformCache()
    y_up = UsdGeom.GetStageUpAxis(stage) == "Y"
    for prim in stage.Traverse():
        if not prim.IsA(UsdGeom.Mesh):
            continue
        mesh = UsdGeom.Mesh(prim)
        transform = cache.GetLocalToWorldTransform(prim)
        points = np.array([
            tuple(transform.Transform(Gf.Vec3d(*point))) for point in mesh.GetPointsAttr().Get()
        ])
        if y_up:
            points = points @ Y_UP_TO_Z_UP.T
        indices = mesh.GetFaceVertexIndicesAttr().Get()
        faces = []
        offset = 0
        left_handed = mesh.GetOrientationAttr().Get() == UsdGeom.Tokens.leftHanded
        for count in mesh.GetFaceVertexCountsAttr().Get():
            face = list(indices[offset:offset + count])
            if left_handed:
                face.reverse()
            faces.append(face)
            offset += count
        bound, _ = UsdShade.MaterialBindingAPI(prim).ComputeBoundMaterial()
        name = bound.GetPrim().GetName() if bound else ""
        finish = {
            "Diffuse": "Box",
            "green": "Green lettering",
            "PreviewSurface": "Dark lettering",
        }.get(name, "Box markers")
        yield points, faces, finish


def material(name, color, roughness, metallic=0, edge_radius=0):
    result = bpy.data.materials.new(name)
    result.use_nodes = True
    shader = result.node_tree.nodes.get("Principled BSDF")
    shader.inputs["Base Color"].default_value = (*color, 1)
    shader.inputs["Roughness"].default_value = roughness
    shader.inputs["Metallic"].default_value = metallic
    if edge_radius:
        bevel = result.node_tree.nodes.new("ShaderNodeBevel")
        bevel.inputs["Radius"].default_value = edge_radius
        result.node_tree.links.new(bevel.outputs["Normal"], shader.inputs["Normal"])
    return result


def add_model(points, faces, finish):
    mesh = bpy.data.meshes.new(finish.name)
    mesh.from_pydata(points.tolist(), [], faces)
    # Each STEP surface has its own vertices. Keeping those seams preserves
    # sharp edges and avoids welding thin or near-coincident surfaces together.
    for face in mesh.polygons:
        face.use_smooth = True
    mesh.set_sharp_from_angle(angle=math.radians(32))
    mesh.materials.append(finish)
    model = bpy.data.objects.new(finish.name, mesh)
    bpy.context.collection.objects.link(model)


def studio_light(name, position, energy, size, color):
    light = bpy.data.lights.new(name, "AREA")
    light.energy = energy
    light.shape = "DISK"
    light.size = size
    light.color = color
    lamp = bpy.data.objects.new(name, light)
    bpy.context.collection.objects.link(lamp)
    lamp.location = position
    lamp.rotation_euler = (Vector((0, 0, 0.35)) - lamp.location).to_track_quat("-Z", "Y").to_euler()


def frame_camera(vertices, direction, width, height):
    rotation = Vector(direction).to_track_quat("Z", "Y")
    right = rotation @ Vector((1, 0, 0))
    up = rotation @ Vector((0, 1, 0))
    projection = vertices @ np.array([right, up]).T
    low, high = projection.min(axis=0), projection.max(axis=0)
    middle = (low + high) / 2
    span_x, span_y = high - low

    camera = bpy.data.cameras.new("Orthographic")
    camera.type = "ORTHO"
    camera.ortho_scale = max(span_x * 1.26 / width, span_y * 1.24 / height) * max(width, height)
    camera_object = bpy.data.objects.new("Orthographic", camera)
    bpy.context.collection.objects.link(camera_object)
    camera_object.rotation_euler = rotation.to_euler()
    camera_object.location = (
        right * middle[0] + up * (middle[1] - span_y * 0.025) + Vector(direction).normalized() * 4
    )
    bpy.context.scene.camera = camera_object


def render(source, target, draft=False):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    is_box = source.suffix.lower() == ".usdz"
    meshes = list(usd_meshes(source) if is_box else step_meshes(source))
    vertices = np.concatenate([points for points, _, _ in meshes])
    low, high = vertices.min(axis=0), vertices.max(axis=0)
    center = (low + high) / 2
    center[2] = low[2]
    scale = float(max(high - low))
    finishes = {
        "Polymer": material("Polymer", (0.022, 0.064, 0.095), 0.40),
        "Aluminum": material("Aluminum", (0.29, 0.33, 0.38), 0.39, metallic=0.74),
        "Box": material("Box", (0.37, 0.44, 0.48), 0.46, edge_radius=0.0015),
        "Box markers": material("Box markers", (0.14, 0.21, 0.24), 0.65),
        "Green lettering": material("Green lettering", (0.08, 0.38, 0.12), 0.50),
        "Dark lettering": material("Dark lettering", (0.024, 0.030, 0.038), 0.50),
    }
    for points, faces, finish in meshes:
        add_model((points - center) / scale, faces, finishes[finish])

    bpy.ops.mesh.primitive_plane_add(size=200, location=(0, 0, -0.002))
    bpy.context.object.data.materials.append(material("Backdrop", (0.86, 0.89, 0.94), 0.85))

    scene = bpy.context.scene
    scene.world = bpy.data.worlds.new("Studio ambient")
    scene.world.use_nodes = True
    background = scene.world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.72, 0.81, 1.0, 1)
    background.inputs["Strength"].default_value = 0.33
    side = -1 if is_box else 1
    studio_light("Key", (-2.4 * side, -3 * side, 4), 490, 4.0, (1.0, 0.93, 0.84))
    studio_light("Fill", (3.0 * side, -1.0 * side, 2.1), 145, 3.0, (0.78, 0.88, 1.0))
    studio_light("Rim", (1.4 * side, 2.9 * side, 3.2), 360, 2.4, (1.0, 1.0, 1.0))

    width, height = 1040, 680
    direction = (1.2, -1.0, 1.18)
    if source.stem == V2:
        width, height = 580, 940
        direction = (1.4, -1.0, 0.48)
    elif source.stem in TALL_MOUNTS:
        width, height = 650, 740
        direction = (0.82, -1.2, 0.66)
    elif is_box:
        direction = (-0.84, 1.7, 0.64)

    frame_camera((vertices - center) / scale, direction, width, height)
    scene.render.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = 20 if draft else 72
    scene.cycles.use_denoising = True
    scene.cycles.max_bounces = 6
    scene.view_settings.view_transform = "AgX"
    scene.render.resolution_x = width
    scene.render.resolution_y = height
    scene.render.resolution_percentage = 55 if draft else 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    scene.render.image_settings.compression = 80
    target.parent.mkdir(parents=True, exist_ok=True)
    scene.render.filepath = str(target)
    bpy.ops.render.render(write_still=True)
    print(f"{source.name} → {target.name}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "sources", nargs="*", type=Path, help="Render selected STEP/STP or USDZ assets."
    )
    parser.add_argument("--draft", type=Path, metavar="DIR", help="Write quick previews to DIR.")
    args = parser.parse_args()
    sources = args.sources or [
        source
        for folder in ("b601-camera-mounts", "data-collection-camera-mounts")
        for source in sorted((ROOT / folder).glob("**/*"))
        if source.suffix.lower() in {".step", ".stp"}
        and preview_target(source).parent == ROOT / "images"
    ] + [BOX]
    for source in sources:
        target = preview_target(source)
        if args.draft:
            target = args.draft.resolve() / target.relative_to(ROOT / "images")
        render(source, target, draft=bool(args.draft))


if __name__ == "__main__":
    main()
