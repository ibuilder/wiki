---
title: "List of known invalid IFC practices"
url: "/list-of-known-invalid-ifc-practices/"
aliases: ["/List_of_known_invalid_IFC_practices/"]
categories: ["Autodesk Revit", "IFC invalid practices", "Industry Foundation Classes (IFC)"]
lastmod: "2022-08-04T19:19:48Z"
---

See also [IFC invalid practices](/categories/ifc-invalid-practices/) 

## Autodesk Revit
| Summary | Last Verified |
| --- | --- |
| Using <code>Open IFC</code>, any objects using Tessellations are not supported. For example, if you export an IFC4 from ArchiCAD, unless you force it to use parametric solids, Revit will be unable to show the geometry in these IFCs. | 2021-04-12 |
| Using <code>Link IFC</code>, IfcSpace will convert into Revit generic models, which is hardcoded. This makes it impossible for rooms to contain elements. The only workaround is to use <code>Open IFC</code> instead. | 2021-04-12 |
| When exporting, Revit will not record metric units correctly for the geolocation map conversion. This makes geolocation useless. | 2021-04-12 |
## Bentley OpenBuildings Designer
| Summary | Last Verified |
| --- | --- |
| <code>IfcSurfaceStyleShading</code> is still exported without an a <code>Transparency</code> attribute, even if an IFC4 export is done. This is technically correct if you check in a pre-addendum version of IFC4, but is not useful to users or updated IFC4 parsers. | 2019-05-23 |
