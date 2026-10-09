# Camera Mounts

English | [简体中文](README_zh.md)

Camera mount CAD files for B601 robots and data collection setups, plus a USDZ environment asset.

## Choose an asset

| Collection | Assets | Format |
| --- | --- | --- |
| [B601 camera mounts](#b601-camera-mounts) | 4 camera mount designs | STEP (`.step`) |
| [Data collection camera mounts](#data-collection-camera-mounts) | V1: 4 mount designs and 4 adapter parts; V2: 1 assembly | STEP (`.stp`) |
| [Data collection environment](#data-collection-environment) | 1 box model | USDZ (`.usdz`) |

The catalog below covers every CAD/model file in this repository. Camera and robot names follow the upstream filenames; dimensions, fasteners, print settings, and verified compatibility are not supplied here. Check the CAD geometry against your hardware before fabrication.

## B601 camera mounts

These four wrist camera mounts are shared by **B601-RS and B601-DM**. Their STEP files have been moved here from `hardware/reBot_B601_DM/3D_Printed_Parts/` with identical contents.

These files originate from the B601-DM 3D printed parts collection in [reBot-DevArm](https://github.com/Seeed-Projects/reBot-DevArm/tree/main/hardware/reBot_B601_DM/3D_Printed_Parts).

### D405 / 305 mount

![CAD preview: D405_305_Mount](images/D405_305_Mount.png)

*D405_305_Mount: preview rendered from the supplied STEP file.*

![Upstream CAD rendering of the D405 mount](images/b601-d405.jpg)

[Download D405_305_Mount.step](b601-camera-mounts/D405_305_Mount.step)

Camera mount identified as D405 / 305 in the source filename. The upstream D405 rendering shows a camera support plate connected to a curved mounting base. The image is a CAD rendering, not a finished-part photograph; the main reBot-DevArm README identifies “305” as Gemini 305.

### D435 / Gemini 2 mount

![CAD preview: D435_Gemini2_Mount](images/D435_Gemini2_Mount.png)

*D435_Gemini2_Mount: preview rendered from the supplied STEP file.*

![Upstream D435i CAD rendering associated with the D435 mount family](images/b601-d435i.jpg)

[Download D435_Gemini2_Mount.step](b601-camera-mounts/D435_Gemini2_Mount.step)

Camera mount identified as D435 / Gemini 2 in the source filename. The upstream image is labeled D435i and shows an elongated camera support plate and curved mounting base. It is a CAD reference rendering, not proof of fit for every named camera or a finished-part photograph.

### D455f mount

![CAD preview: D455f_Mount](images/D455f_Mount.png)

*D455f_Mount: preview rendered from the supplied STEP file.*

[Download D455f_Mount.step](b601-camera-mounts/D455f_Mount.step)

Camera mount identified as D455f in the source filename. The model shows an elongated support with mounting holes and a reinforcing section underneath. Open the STEP model to inspect the mounting geometry. The preview above is rendered directly from the supplied STEP geometry.

### UVC32 mount

![CAD preview: UVC32_mount](images/UVC32_mount.png)

*UVC32_mount: preview rendered from the supplied STEP file.*

[Download UVC32_mount.step](b601-camera-mounts/UVC32_mount.step)

Camera mount identified as UVC32 in the source filename. The model shows a camera plate with a rectangular opening, connected to a curved mounting base. Open the STEP model to inspect the mounting geometry. The preview above is rendered directly from the supplied STEP geometry.

## Data collection camera mounts

Two construction versions are available:

| Version | Construction | Files |
| --- | --- | --- |
| [V1](data-collection-camera-mounts/V1/) | 3D-printed support body and camera adapters | Four numbered mounts and four adapter parts listed below |
| [V2](#v2-aluminum-extrusion-camera-mount) | Aluminum extrusion support body with a 3D-printed camera bracket | One complete STEP assembly |

V1 comes from the upstream [Camera-Mount repository](https://github.com/xiehuangbao888/Camera-Mount). Its four numbered mounts and four associated adapters retain the associations in the original filenames. Upstream does not include assembly instructions or photographs; completed assemblies and camera compatibility have not been verified. V2 is supplied by [Yang-Ci/Camera-Mounts](https://github.com/Yang-Ci/Camera-Mounts) and uses aluminum extrusions for the support body.

### Mount 1

![CAD preview: mount-1](images/mount-1.png)

*mount-1: preview rendered from the supplied STEP file.*

![CAD preview: mount-1-rebot-adapter](images/mount-1-rebot-adapter.png)

*mount-1-rebot-adapter: preview rendered from the supplied STEP file.*

![CAD preview: mount-1-soarm-adapter](images/mount-1-soarm-adapter.png)

*mount-1-soarm-adapter: preview rendered from the supplied STEP file.*

[Download mount-1.stp](data-collection-camera-mounts/V1/mount-1.stp)

Camera mount design 1 has a tall, tapered support body with a stepped upper interface. Two separate adapter variants are supplied:

- [reBot adapter](data-collection-camera-mounts/V1/mount-1-rebot-adapter.stp): a plate-shaped insert with an opening and an offset attachment section, named “mount 1 rebot insert” upstream.
- [SO-ARM adapter](data-collection-camera-mounts/V1/mount-1-soarm-adapter.stp): an offset plate-shaped insert, named “mount 1 soarm insert” upstream.

Select the adapter corresponding to your setup and inspect the interface in CAD. The previews above show the mount and each adapter as separate CAD parts.

### Mount 2

![CAD preview: mount-2](images/mount-2.png)

*mount-2: preview rendered from the supplied STEP file.*

![CAD preview: mount-2-soarm-adapter](images/mount-2-soarm-adapter.png)

*mount-2-soarm-adapter: preview rendered from the supplied STEP file.*

[Download mount-2.stp](data-collection-camera-mounts/V1/mount-2.stp)

Camera mount design 2 has a tapered support body with a different upper interface from design 1. A separate [SO-ARM adapter](data-collection-camera-mounts/V1/mount-2-soarm-adapter.stp) is supplied, identified upstream as the mount 2 soarm insert. Inspect the two models together to determine how they connect. The previews above show the mount and its adapter as separate CAD parts.

### Mount 3

![CAD preview: mount-3](images/mount-3.png)

*mount-3: preview rendered from the supplied STEP file.*

![CAD preview: mount-3-4-adapter](images/mount-3-4-adapter.png)

*mount-3-4-adapter: preview rendered from the supplied STEP file.*

[Download mount-3.stp](data-collection-camera-mounts/V1/mount-3.stp)

Camera mount design 3 has a tapered support body and a rectangular raised section at the top. The [mount 3 / 4 adapter](data-collection-camera-mounts/V1/mount-3-4-adapter.stp) is identified by its upstream filename as the shared insert for designs 3 and 4. The previews above show this mount and the shared adapter as separate CAD parts.

### Mount 4

![CAD preview: mount-4](images/mount-4.png)

*mount-4: preview rendered from the supplied STEP file.*

[Download mount-4.stp](data-collection-camera-mounts/V1/mount-4.stp)

Camera mount design 4 has a tapered support body with a broad, recessed top interface. Its associated part is the same [mount 3 / 4 adapter](data-collection-camera-mounts/V1/mount-3-4-adapter.stp). Inspect the CAD geometry to compare designs 3 and 4 before choosing one. The preview above shows the supplied CAD part.

### V2: Aluminum extrusion camera mount

![CAD preview: V2 data collection camera mount](images/data-collection-camera-mount-v2.png)

*Complete assembly preview rendered from the supplied STEP geometry.*

[Download data-collection-camera-mount-v2.stp](data-collection-camera-mounts/data-collection-camera-mount-v2.stp)

V2 is a data collection camera mount with an aluminum extrusion support body and a 3D-printed camera bracket. V1 uses a 3D-printed support body. The supplied V2 assembly includes the support and camera mounting components together; it is an assembly CAD file, not a set of ready-to-print STL files. Inspect the assembly in CAD to identify the printed components and check the camera interface before fabrication.

### Original-to-English filename mapping

Only filenames have changed; the CAD file contents are preserved. V1 mount numbers and adapter associations remain traceable to upstream; the V2 assembly was supplied locally by the maintainer.

| Original filename | English filename |
| --- | --- |
| `数据采集摄像头支架_支架1.stp` | [`mount-1.stp`](data-collection-camera-mounts/V1/mount-1.stp) |
| `数据采集摄像头支架_支架1插件rebot.stp` | [`mount-1-rebot-adapter.stp`](data-collection-camera-mounts/V1/mount-1-rebot-adapter.stp) |
| `数据采集摄像头支架_支架1插件soarm.stp` | [`mount-1-soarm-adapter.stp`](data-collection-camera-mounts/V1/mount-1-soarm-adapter.stp) |
| `数据采集摄像头支架_支架2.stp` | [`mount-2.stp`](data-collection-camera-mounts/V1/mount-2.stp) |
| `数据采集摄像头支架_支架2插件soarm.stp` | [`mount-2-soarm-adapter.stp`](data-collection-camera-mounts/V1/mount-2-soarm-adapter.stp) |
| `数据采集摄像头支架_支架3.stp` | [`mount-3.stp`](data-collection-camera-mounts/V1/mount-3.stp) |
| `数据采集摄像头支架_支架3_4插件.stp` | [`mount-3-4-adapter.stp`](data-collection-camera-mounts/V1/mount-3-4-adapter.stp) |
| `数据采集摄像头支架_支架4.stp` | [`mount-4.stp`](data-collection-camera-mounts/V1/mount-4.stp) |
| `数据采集摄像头支架.stp` (V2, maintainer-supplied) | [`data-collection-camera-mount-v2.stp`](data-collection-camera-mounts/data-collection-camera-mount-v2.stp) |

## Data collection environment

![Box environment model preview](images/box.png)

*Box: preview rendered from mesh geometry in the supplied USDZ file.*

[Download box.usdz](data-collection-environment/box.usdz)

A box model from [rebot-arm-dli-isaacsim](https://github.com/yuyoujiang/rebot-arm-dli-isaacsim), supplied as a USDZ asset for a data collection environment. This is an environment model rather than a camera mount. Open it in a USDZ-compatible viewer to inspect its geometry; no physical build photograph is supplied.

## Working with the files

1. Download the mount and any associated adapter using the links above.
2. Open STEP/STP files in a CAD tool and inspect dimensions, clearances, and mounting holes.
3. Prepare fabrication files for your chosen process. STL files, print settings, and a hardware bill of materials are not included.
4. For the environment asset, use a viewer or tool that supports USDZ.

## Image sources and model previews

Every model file has a preview rendered directly from its source STEP or USDZ geometry. These are model previews, not physical-product photographs. V1 adapter parts are shown separately; the images do not imply verified assembly or fit.

Two additional B601 reference images come from upstream: [D405.jpg](https://github.com/Seeed-Projects/reBot-DevArm/blob/main/hardware/reBot_B601_DM/3D_Printed_Parts/images/D405.jpg) and [D435i.jpg](https://github.com/Seeed-Projects/reBot-DevArm/blob/main/hardware/reBot_B601_DM/3D_Printed_Parts/images/D435i.jpg). Both are CAD renderings.

To regenerate the previews, install `cadquery`, `matplotlib`, `numpy`, and `usd-core` in a Python environment, then run `cd hardware/camera-mounts && python tools/render_previews.py` from the repository root. To render only V2, run `python tools/render_previews.py data-collection-camera-mounts/data-collection-camera-mount-v2.stp` from `hardware/camera-mounts/`.

## Sources and licensing

- B601 camera mounts and reference renderings: [Seeed-Projects/reBot-DevArm](https://github.com/Seeed-Projects/reBot-DevArm), CERN OHL-W-2.0.
- V2 data collection camera mount: supplied by [Yang-Ci/Camera-Mounts](https://github.com/Yang-Ci/Camera-Mounts); see [NOTICE.md](NOTICE.md).
- V1 data collection camera mounts: [xiehuangbao888/Camera-Mount](https://github.com/xiehuangbao888/Camera-Mount). No upstream license was declared when these assets were copied.
- Data collection environment: [yuyoujiang/rebot-arm-dli-isaacsim](https://github.com/yuyoujiang/rebot-arm-dli-isaacsim), MIT.

See [NOTICE.md](NOTICE.md), [LICENSE](LICENSE), and [licenses/](licenses/) for details.
