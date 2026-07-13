---
title: "AutoCAD"
url: "/autocad/"
aliases: ["/AutoCAD/"]
categories: ["AutoCAD", "Proprietary software"]
lastmod: "2023-03-07T16:51:48Z"
---

AutoCAD is a 2D/3D drafting software developed by [Autodesk](https://www.autodesk.com/).

A good place to look for alternatives is https://alternativeto.net/software/autocad/

## Getting data out of AutoCAD
## File formats
AutoCAD has industry specific versions, called verticals, some formats are supported only by one of them

- [DXF](/drawing-exchange-format-dxf/) - Recommended, although not every features can be saved
- [DWG](/drawing-dwg/) - Everything is saved, but not readable by other applications
- [IFC](/ifc-industry-foundation-classes/) - Only in AutoCAD Architecture, Civil3D and MEP

## Accessing data in AutoCAD with free software
- [Speckle](/speckle/) has an [AutoCAD connector](https://speckle.systems/tag/autocad/)
- [CADPythonShell](https://github.com/chuongmep/CadPythonShell) is an AutoCAD addon for running python code inside AutoCAD. It uses IronPython, MIT license
- AutoCAD Civil3D comes with [Dynamo](/dynamo/) since version 2022. Data in other verticals can be accessed via .NET interop services, more info [in this forum](https://forums.autodesk.com/t5/net/integrate-dynamo-with-autocad/m-p/6676235/highlight/true#M50930)

## Limitations
Dynamic block custom parameters are not accessible via any method, and not readable from dxf files, visual representation are saved though. This data can be exported with [DATAEXTRACTION](https://knowledge.autodesk.com/support/autocad/learn-explore/caas/CloudHelp/cloudhelp/2021/ENU/AutoCAD-Core/files/GUID-5A39FFE8-10AC-4AE5-8EF4-D097C8261D1A-htm.html) command to csv or xls files.

## See also
- [LibreCAD](/librecad/) is a free/libre alternative to AutoCAD
- [QCAD](/qcad/) is a free/libre alternative to AutoCAD

## External Resources
- https://www.autodesk.com/products/autocad/overview
- https://en.wikipedia.org/wiki/AutoCAD
