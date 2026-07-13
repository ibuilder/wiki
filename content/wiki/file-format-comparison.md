---
title: "File format comparison"
url: "/file-format-comparison/"
aliases: ["/File_format_comparison/"]
categories: ["File formats"]
lastmod: "2020-12-10T12:18:40Z"
---

This is a file format comparison of popular and widely used file formats for geometry and AEC related data storage.

For descriptions see [AEC Open Data Standards Directory](/aec-open-data-standards-directory/)

| Format | Open Format? | Support | Stores metadata | Stores materials | Stores parametric controls |
| --- | --- | --- | --- | --- | --- |
| GSM | No | [ArchiCAD](/archicad/) | Yes (proprietary) | Yes (proprietary) | Yes (proprietary) |
| IFC | [Yes](/ifc-industry-foundation-classes/) | [ArchiCAD](/archicad/), [Autodesk Revit](/autodesk-revit/), [Blender](/blender/), [FreeCAD](/freecad/), Rhino, SketchUp, Tekla, and [over 300 other software](https://technical.buildingsmart.org/resources/software-implementations/). | Yes (ISO-compliant) | Yes (ISO-compliant) | Basic (ISO-compliant) |
| RFA | No | [Revit](/autodesk-revit/), [bimrv](https://www.opendesign.com/products/bimrv) | Yes (proprietary) | Yes (proprietary) | Yes (proprietary) |
| DWG | No | Most proprietary CAD, not compatible with most open source CAD | Basic (proprietary) | Basic (proprietary) | No |
| DXF | [Yes](http://help.autodesk.com/view/OARX/2018/ENU/?guid=GUID-235B22E0-A567-4CF6-92D3-38A2306D73F3) | Supported by all that support DWG, plus all open source CAD | Basic | Basic | No |
| STL | Yes | [Blender](/blender/), [FreeCAD](/freecad/), Rhino, SketchUp | No | Possible, but inconvenient | No |
| [STEP](https://en.wikipedia.org/wiki/ISO_10303-21) | [No](https://en.wikipedia.org/wiki/ISO_10303-21) | Good | Yes (Most vendor exports don't) | Yes (Most vendors have not implemented) | Yes (Most vendors have not implemented) |
| OBJ | [Yes](https://en.wikipedia.org/wiki/Wavefront_.obj_file) | Good | ? | Yes (.mtl) |  |
| FBX | No | Good | ? |  |  |
| SKP | No | [SketchUp](https://en.wikipedia.org/wiki/SketchUp) | Yes (proprietary) | Yes (proprietary) | Yes (proprietary) |
| BLEND | Yes | [Blender](/blender/) [Bonsai](/bonsai/) | Yes | Yes | Yes |
