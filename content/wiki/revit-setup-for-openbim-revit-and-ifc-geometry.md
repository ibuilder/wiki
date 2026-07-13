---
title: "Revit and IFC Geometry"
url: "/revit-setup-for-openbim-revit-and-ifc-geometry/"
aliases: ["/Revit_and_IFC_Geometry/", "/Revit_setup_for_OpenBIM/Revit_and_IFC_Geometry/"]
categories: ["Autodesk Revit"]
lastmod: "2023-07-06T13:15:42Z"
---

When Revit exports geometry to IFC, it may process it in a way that may lead to loss of information or inefficient data storage. Optimising geometry is highly advised to maintain quick workflows between OpenBIM and Revit.

## Optimising geometry in Revit
## Detecting complex geometry
Within Revit, the currently exported Element ID will be shown in the status bar on the bottom left during the export process. Watching this at export time and making a note of any Element IDs that take a particularly long time to export will help identify those with geometric issues that Revit is struggling with.

As an alternative, the [Geometric detail MicroMVD](/micromvds-for-exchange-requirements-geometric-detail-micromvd/) may be used to audit the geometry. It checks by auditing the number of polygons physically present in the IFC definition of the geometry. This type of check is very fast, as it does not require the geometry to be computed.

Sometimes, it is also necessary to check the resultant polygon count, not just the IFC definition. This is useful if there are many parametric definitions that are computationally expensive to display. [Bonsai](/bonsai/) contains a "Select all high polygon meshes" operator, allowing you to select and visually inspect complex geometry. The IFC CSV tool may then be used to export these objects into a spreadsheet format.

## Using IFC4
IFC4 contains much more efficient ways of storing both mesh and non mesh geometry. Whenever possible, it is advised to export IFC files in the IFC4 format. This can result in significant filesize reductions. As an example, an IFC produced from Revit of a single object resulted in a filesize of 16,098kB. The same object re-exported to IFC4 using [Bonsai](/bonsai/) reduced the object to 4,487kb with no loss in geometric detail.

This filesize reduction occurs due to two improvements in the IFC4 data format. The first is the new tesselated shape supports, which allow a much more efficient description of meshes compared to the IFC2X3 faceted BREPs. The second is due to the improved support in Revit of exporting parametric geometry in IFC.

## Mitigating the Revit type duplication bug
Revit has a bug which invisibly duplicates types unknown to the end user. For example, given a table that is symmetrical, if you mirror it in Revit, it will still show as one type in Revit. However, under the hood, Revit will invisibly create a new type that you cannot see through the Revit interface. When exported to IFC, Revit will generate two types, with two geometries: one of the original and one of the mirrored table. This doubles the size of your type.

Multiplying the size of a type is especially problematic when the type has fillets (see next section) and is already 10-30 times the size of a properly modelled mesh. Mirroring along one axis will double your type filesize. Mirroring along two axes will quadruple your filesize. If it's a door or window, placement on a hosted element with different thicknesses will also duplicate the time again, leading to a single door's geometry filesize being multiplied easily to 8 or more times, depending on how many different walls you put it in.

There is no known fix for this at the moment due to the complexity of this bug and the risk in patching vertex coordinates. More reading [here](https://github.com/Autodesk/revit-ifc/issues/326).

Though issue can be solved to some degree by [MergeDuplicateTypes](https://bonsaibim.org/docs-python/autoapi/ifcpatch/recipes/MergeDuplicateTypes/index.html) patch in IFC Patch, example of the executing this IFC Patch through Bonsai can be found [here](https://youtu.be/Op7PS3aM6bw?t=661).

## Reducing curves in profiles that are swept, revolved, or blended
If possible, if you have a profile which has any curves in it (including filleted corners), it is advised to only create an <code>Extrusion</code>. If other forms are created, such as a <code>Blend</code>, <code>Revolve</code>, <code>Sweep</code>, or a <code>Swept Blend</code>, Revit is not able to efficiently translate this geometry into IFC due to limitations in the Revit software.

This may result in shapes that look relatively simple in Revit, but lead to slow model coordination, slow file exports, large filesizes, and increased bandwidth usage in CDEs.

{{< wiki-image src="/media/revit-fillet-sweep.png" alt="A swept profile with a single fillet" mode="thumb" caption="A swept profile with a single fillet" align="right" width="200" >}}

As an example, consider the following swept profile. The profile has a single filleted corner. Without the filleted corner, the exported filesize is 10kb. With the filleted corner, the resulting IFC2X3 filesize increases to 270kb. This is an increase of 27 times the filesize.

{{< wiki-image src="/media/revit-door-geometry.png" alt="An innocent looking door" mode="thumb" caption="An innocent looking door" align="right" width="200" >}}

This is especially relevant to the architectural discipline. A common example can be seen in door and window frames, hardware, and furniture. For example, the following door object. The door contains a frame which is a profile swept along a path. The profile contains multiple fillets.

{{< wiki-image src="/media/revit-door-geometry-zoom.png" alt="A door with over 8,000 vertices" mode="thumb" caption="A door with over 8,000 vertices" align="right" width="200" >}}

[Bonsai](/bonsai/) lets you inspect the details of how Revit generates shapes. In mesh edit mode, it is revealed that this door contains more than 8,000 vertices. Zooming into the door frame reveals the strange meshing artifacts that Revit has generated. You will notice that the artifacts do not occur in simple extrusions, such as in the door leaf.

It is not currently possible to modify the number of facets created in a curve. If it is necessary to do this, it is advised to switch to another software application.

## Remodeling in other software
{{< wiki-image src="/media/revit-object-blender-remodel.png" alt="An object remodeled in Blender" mode="thumb" caption="An object remodeled in Blender" align="right" width="200" >}}

In some scenarios, when it is not acceptable to reduce the geometric fidelity in Revit, it is necessary to switch to alternative software to generate IFCs, which either have improved mesh support, or improved ability to store parametric information in the IFC format.

In one example, a single object originally exported into a 16,098kB IFC file from Revit was remodeled in Blender, with a resulting IFC filesize when re-exported from Bonsai of 455kb.
