---
title: "Revit IFC import pitfalls"
url: "/revit-setup-for-openbim-revit-ifc-import-pitfalls/"
parent: "/revit-setup-for-openbim/"
aliases: ["/Revit_IFC_import_pitfalls/", "/Revit_import_pitfalls/", "/Revit_setup_for_OpenBIM/Revit_IFC_import_pitfalls/"]
categories: ["Autodesk Revit", "IFC invalid practices", "Industry Foundation Classes (IFC)", "Proprietary software"]
lastmod: "2022-01-31T10:40:04Z"
---

If you intend an IFC file to be opened/imported with Revit things get complicated, just as they are for export from Revit (see: [Revit setup](/revit-setup-for-openbim/)). This page list some pitfalls to avoid.

## Mandatory conditions
Having an <code>IfcBuildingStorey</code> is optional in IFC standards but mandatory for Revit (Last test: revit-ifc 21.1). Else an empty file will be created. Building elements like walls will be missing. [^1]

In IFC standards an <code>IfcProduct</code> can be contained in an <code>IfcSite</code>, <code>IfcBuilding</code>, <code>IfcBuildingStorey</code> or <code>IfcSpace</code> [^2]. However if you do so, Revit will link element to a newly created <code>Level</code> called *Default* on import. 

## Geolocation / Model far from origin
Revit has currently no option to choose which base point an IFC model should be positioned by, it will be placed at the internal origin. If the IFC model is placed to far from this origin, Revit will not import your model correctly. Although in any software it is not a good idea to have large coordinates. Use relative placement as much as possible.

You might be able to see the model by linking the IFC instead of importing it, but if the coordinates are large (world-coordinates) the IFC needs to be pathced before it kan be linked in to Revit. This can be done in Bonsai:
- Go to the scene pane and look for "IFC Patch"
- Choose either "ResetAbsoluteCoordinates" or "OffsetObjectPlacements" in the Recipie dropdown.
- Choose filepaths to patch and patched
- If you choose "OffsetObjectPlacement" add in the "arguments"-field the Shared Coordinates in Revit in opposite direcion seperated by comma. <code>x, y, z, rotation</code> E.g: <code>-128900, -1532260, 0, -19.5</code>

## IfcSpace
When linking <code>IfcSpace</code> are converted into Generic Model and it is not possible to fix this. See issue [revit-ifc/issues/15](https://github.com/Autodesk/revit-ifc/issues/15). A [workaround](https://github.com/Autodesk/revit-ifc/issues/15#issuecomment-558748917) is to create a model with spaces only and import it instead.

## Workarounds
<references group="workarounds" />

## References

[^1]: Link the IFC file instead of importing it. Some elements behaviour might change eg. a wall geometry become not modifiable by hand
[^2]: ''[https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD2/HTML/schema/ifcproductextension/lexical/ifcrelcontainedinspatialstructure.htm IfcRelContainedInSpatialStructure]'', IFC documentation
