---
title: "Drawing Exchange Format (DXF)"
url: "/drawing-exchange-format-dxf/"
aliases: ["/Drawing_Exchange_Format_(DXF)/"]
categories: ["Drawing Exchange Format (DXF)", "File formats"]
lastmod: "2021-04-12T20:16:51Z"
---

> **Stub:** This article needs expansion.

Drawing Exchange Format (DXF) is a file format designed by Autodesk to allow exchange with their AutoCAD software. While they publish specs it is not an open format as they alone control iterations to the format. Autodesk and the Open Design Alliance sell commercial licenses for accessing DXF files. There is generally better support for DXF in free/libre software, compared to [Drawing (DWG)](/drawing-dwg/) format.

DXF can be thought of as an exchange version of the [Drawing (DWG)](/drawing-dwg/) format developed by Autodesk. File sizes may be larger, as it is in plaintext, whereas DWG is binary, and it may not contains data of proprietary AutoCAD extensions. Autodesk has discouraged the use of DWG, by inserting an encrypted proprietary signature that determines whether or not a DWG comes from Autodesk software. However, despite this discouragement, DWG creation is commonplace. Large parts of the DXF specs are undocumented, only the common basic entities are described, but not any advanced like dynamic blocks, 3d solids, 3d surfaces or parametric blocks. Likewise no free external library supports these.

The [Open Design Alliance](https://www.opendesign.com) has a freely available proprietary [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) for converting between different versions of .dwg and .dxf. It has very good support for most objects and entities.

## Support for DXFs in free software
The [LibreDWG](/libredwg/) project has an example application for SVG and Postscript conversion, converters from and to DXF.

2D and 3D DXFs can be imported and exported by [Blender](/blender/) and [FreeCAD](/freecad/). 2D DXFs are supported in [LibreCAD](/librecad/), and [QCAD](/qcad/).

Blender is capable of importing DXFs with absolute coordinates with the [BlenderGIS add-on](/blendergis-add-on/). However, this workflow may have issues in recent releases. Blender's support for DXF is based on an older DXF library, and therefore may have compatibility issues with newer DXFs being produced.

## Libraries for Software Development
- [dxflib by panjh](https://github.com/panjh/dxflib) is an open source C++ library mainly for parsing DXFTM files.
- [dxflib by Ribbonsoft](https://qcad.org/en/90-dxflib) is a C++ GPLv2-or-later library used in [QCAD](/qcad/) 
- dxflibrw is an open source library for reading DWG files (pre 2018) and readgin /writing DXF files. It is used in many separate forks, importantly by [LibreCAD](/librecad/)[github](https://github.com/LibreCAD/libdxfrw) and [Solvespace](/solvespace/) [reference](https://github.com/solvespace/libdxfrw)
- [LibreDWG](/libredwg/) supports DXF & DWG (details are on the linked page)
- [ezdxf](https://ezdxf.mozman.at/) is a python library supporting DXF versions up to 2018

## Advantages and Disadvantages
For the purpose of documentation is worth comparing DXF to [Scalable Vector Graphics (SVG)](/scalable-vector-graphics-svg/)

Pros of DXF:
- Is designed to capture the same data that [Drawing (DWG)](/drawing-dwg/) can capture. So if DWG is your native format, DXF ensures a minimum of data loss.
- Data in 3 dimensions ([Scalable Vector Graphics (SVG)](/scalable-vector-graphics-svg/) files are only two dimensions)
- Easy to read, easy to write, and a variety of data types of play with (blocks, polylines, polyfaces...)
- Layers with styles baked into it
- Model space. Paper space. Multiple paper spaces.

Cons of DXF:
- No units information in the file
- Requires a DXF viewer.
- Is an "open" standard, but at the same time it's kinda like Autodesk's less favourite cousin that has to follow [Drawing (DWG)](/drawing-dwg/) but lacks some of the proprietary add-ons that DWG has.
- Very hard to parse, many parts are undocumented, very irregular.

## Resources
- Discussion on documentation formats on the OSArch discussion forum [What is best for documentation when svg, dxf, dwg?](https://community.osarch.org/discussion/170/what-is-best-for-documentation-when-svg-dxf-dwg)
- [DXF at Wikipedia](https://en.wikipedia.org/wiki/AutoCAD_DXF)
- [Autodesk DXF Reference](https://www.google.com/search?client=firefox-b-d&q=autodesk+dxf+reference)
