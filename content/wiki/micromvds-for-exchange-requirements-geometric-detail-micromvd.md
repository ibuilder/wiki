---
title: "Geometric detail MicroMVD"
url: "/micromvds-for-exchange-requirements-geometric-detail-micromvd/"
parent: "/micromvds-for-exchange-requirements/"
aliases: ["/Geometric_detail_MicroMVD/", "/MicroMVDs_for_exchange_requirements/Geometric_detail_MicroMVD/"]
categories: ["BIMTester", "MicroMVD", "Model View Definitions (MVD)"]
lastmod: "2022-07-28T11:22:30Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure that geometry is efficiently and appropriately stored in the IFC. Geometry has the single largest impact on file imports, exports, and coordination time.

<pre>
Feature: Geometric detail

To allow for the efficient transfer of geometry
For any stakeholder using 3D geometry
Geometry shall use the appropriate modeling techniques

Scenario: Geometry must be efficiently modeled
 * All elements must be under &quot;{number}&quot; polygons
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{number}</code> | 500 | Given that the vast majority of objects in AEC are box-like or cylindrical, most objects should not be above 500 polygons. For context, a single box is 6 polygons, and a cylinder, depending on its size, may be faceted into 18 polygons. However, many proprietary AEC applications have poor mesh support and may inefficiently translate geometry into a large number of polygons without the users intention. |
## Software guides
| Icon | Software | Certified Version | Notes | Guides | Import | Export |
| --- | --- | --- | --- | --- | --- | --- |
| {{< wiki-image src="/media/icon-archi-cad.jpg" alt="Icon ArchiCAD.jpg" mode="inline" width="64" height="64" >}} | ArchiCAD | N/A | ArchiCAD 23 |  |  |  |
| {{< wiki-image src="/media/bonsai-logo.png" alt="Bonsai logo.png" mode="inline" width="64" height="64" >}} | [Bonsai](/bonsai/) | N/A | v0.0.200829 |  |  |  |
| {{< wiki-image src="/media/icon-freecad.png" alt="Icon FreeCAD.png" mode="inline" >}} | [FreeCAD](/freecad/) | N/A | 0.19pre |  |  |  |
| {{< wiki-image src="/media/icon-revit.png" alt="Icon Revit.png" mode="inline" width="64" height="64" >}} | [Revit](/autodesk-revit/) | N/A | Revit 2020.2 IFC 8/5/2020 | Due to the lack of control in geometry export in Revit, and due to the serious bugs resulting in extreme filesize bloat during export, Revit is considered to have failed this MicroMVD in practice. | Refer to [Revit and IFC Geometry](/revit-setup-for-openbim-revit-and-ifc-geometry/) |  |
| {{< wiki-image src="/media/tekla-logo.png" alt="Tekla-logo.png" mode="inline" width="64" height="64" >}} | [Tekla](/tekla/) |  |  |  |  |  |
