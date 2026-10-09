"""Render source geometry. Requires cadquery, matplotlib, usd-core, numpy."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import cadquery as cq
from pxr import Usd, UsdGeom, Gf

ROOT = Path(__file__).resolve().parents[1]

def render(polys, target, title):
    points = np.concatenate(polys)
    lo, hi = points.min(axis=0), points.max(axis=0)
    center = (lo + hi) / 2
    radius = max(hi - lo) * .6
    fig = plt.figure(figsize=(9, 7), facecolor='#f3f5f7')
    ax = fig.add_subplot(111, projection='3d', computed_zorder=False)
    ax.set_facecolor('#f3f5f7')
    light = np.array([.4, -.6, .7])
    normals = np.array([np.cross(p[1]-p[0], p[2]-p[0]) for p in polys])
    normals /= np.maximum(np.linalg.norm(normals, axis=1)[:,None], 1e-12)
    shade = .45 + .5 * np.abs(normals @ light)
    colors = np.column_stack([shade*.18, shade*.65, shade*.78, np.ones(len(shade))])
    ax.add_collection3d(Poly3DCollection(polys, facecolors=colors, linewidths=0, rasterized=True))
    for setter, c in zip([ax.set_xlim, ax.set_ylim, ax.set_zlim], center):
        setter(c-radius, c+radius)
    ax.set_box_aspect((1,1,1), zoom=1.65)
    ax.view_init(elev=25, azim=-55)
    ax.set_proj_type('ortho')
    ax.set_axis_off()
    fig.suptitle(title, fontsize=18, y=.94)
    fig.text(.5, .06, 'CAD / model preview · source geometry', ha='center', color='#53616b')
    fig.savefig(target, dpi=140, bbox_inches='tight')
    plt.close(fig)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('sources', nargs='*', type=Path,
                    help='Render selected STEP/STP files; omit to render all assets.')
args = parser.parse_args()
sources = args.sources or [source for folder in ['b601-camera-mounts', 'data-collection-camera-mounts']
                          for source in sorted((ROOT/folder).rglob('*'))
                          if source.suffix.lower() in {'.step', '.stp'}]
for source in sources:
    shape = cq.importers.importStep(str(source)).val()
    vertices, triangles = shape.tessellate(.15, .15)
    vertices = np.array([v.toTuple() for v in vertices])
    if source.stem == 'data-collection-camera-mount-v2':
        # The supplied assembly is modeled along Y. Show it upright in the preview.
        vertices = vertices[:, [0, 2, 1]] * np.array([1, -1, 1])
    polys = [vertices[list(t)] for t in triangles]
    target = ROOT/'images'/f'{source.stem}.png'
    render(polys, target, source.stem.replace('_',' ').replace('-',' '))
    print(source.name, len(triangles), flush=True)

if args.sources:
    raise SystemExit(0)

stage = Usd.Stage.Open(str(ROOT/'data-collection-environment/box.usdz'))
polys=[]
cache=UsdGeom.XformCache()
for prim in stage.Traverse():
    if not prim.IsA(UsdGeom.Mesh): continue
    mesh=UsdGeom.Mesh(prim)
    xf=cache.GetLocalToWorldTransform(prim)
    points=np.array([tuple(xf.Transform(Gf.Vec3d(*p))) for p in mesh.GetPointsAttr().Get()])
    ids=mesh.GetFaceVertexIndicesAttr().Get()
    offset=0
    for count in mesh.GetFaceVertexCountsAttr().Get():
        face=list(ids[offset:offset+count]); offset+=count
        for i in range(1,count-1): polys.append(points[[face[0],face[i],face[i+1]]])
if UsdGeom.GetStageUpAxis(stage)=='Y':
    polys=[p[:,[0,2,1]]*np.array([1,-1,1]) for p in polys]
assert polys, 'No mesh geometry in box.usdz'
render(polys, ROOT/'images/box.png', 'Box environment model')
print('box.usdz',len(polys),flush=True)
