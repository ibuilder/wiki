---
title: "FreeCAD setting up a model for IFC export"
url: "/freecad-freecad-setting-up-a-model-for-ifc-export/"
parent: "/freecad/"
aliases: ["/FreeCAD/FreeCAD_setting_up_a_model_for_IFC_export/", "/FreeCAD_setting_up_a_model_for_IFC_export/"]
categories: ["FreeCAD", "Industry Foundation Classes (IFC)"]
lastmod: "2022-02-15T08:53:47Z"
---

Read [FreeCAD setup](/freecad-freecad-setup/) first to get [FreeCAD](/freecad/) and install everything you need

[FreeCAD](/freecad/) being at its base a generic, non-BIM oriented modelling platform, it allows to model and organize your model pretty much the way you want, using not only the tools from the [BIM workbench](https://wiki.freecadweb.org/BIM_Workbench), but just any other tool provided by other FreeCAD workbenches.

FreeCAD is, however, a first-class [IFC](/ifc-industry-foundation-classes/) citizen, and unlike many commercial applications, allows a very high level of control of the IFC files you produce from it. Everything, from the model structure, objects names, tagging and classification, materials and IFC-specific properties is accessible and customizable.

When exporting to IFC, several best practices should be kept in mind. There are several IFC export-related options settable under menu **Edit -> Preferences -> Import/Export -> IFC export**, and the BIM workbench also features a [Preflight tool](https://wiki.freecadweb.org/BIM_Preflight) that can help you detect possible issues in your model, prior to exporting.

- Anything can be exported to IFC. Just select the objects you wish to export, or their top-level containers (group, building, level, site, project) then the use menu **File -> Export -> Industry Foundation Classes**.

- The IFC standard require one IfcProject (or IfcProjectLibrary) in every IFC file. In FreeCAD, you can add a [Project](https://wiki.freecadweb.org/Arch_Project) object yourself in your model, but if you don't, one will automatically be added to any IFC file exported from FreeCAD.

- The IFC standard requires at least one building container (such as IfcBuilding or IfcBuildingStorey) to be present in your model. Usually, IFC files almost always contain one IfcSite, which contains one IfcBuilding and at least one IfcBuildingStorey. In FreeCAD, you can add yourself [sites](https://wiki.freecadweb.org/Arch_Site), [buildings](https://wiki.freecadweb.org/Arch_Building) and [levels](https://wiki.freecadweb.org/Arch_BuildingPart) (storeys), preferentially each part dragged into the former (and the site inside the project)

- All building objects, such as walls or windows, should always be placed inside a building container.

- If you don't follow the above structure, with the default IFC export options, all this structure will be added automatically to your IFC file on export, and all objects not inside a container will be added to one. In the IFC export options, however, you can disable all this, and export an IFC file that reflects exactly how you organized your model in FreeCAD. Note that this can lead to producing a non-standard IFC file (if you disable automatic structure creation and don't add your objects to a building container yourself. But at FreeCAD we believe this structure is not always necessary and it should be your right to decide if you need it or not, and should be able to export a file with just the objects and no building structure).

- Only [BIM objects](https://wiki.freecadweb.org/BIM_Workbench) have support for BIM types (wall, window, etc), [IFC properties](https://wiki.freecadweb.org/BIM_IfcProperties) and [materials](https://wiki.freecadweb.org/Arch_SetMaterial). Any other FreeCAD object will be exported to IFC as a default IfcBuildingElementProxy, and you won't be able to change its type, add IFC properties to it or set its material.

- Any non-BIM object can easily be converted to a BIM object using the [turn to BIM component](https://wiki.freecadweb.org/Arch_Component) tool. The object will still be editable but it will gain all the IFC properties of other BIM objects.

- If an object has a material, the material will be exported to IFC both as an IfcMaterial and IfcSurfaceStyle. If an object doesn't have a material, an IfcSurfaceStyle will be automatically be created from its color.

- Most objects that are the result of an extrusion, such as [walls](https://wiki.freecadweb.org/Arch_Wall), [columns](https://wiki.freecadweb.org/Arch_Structure) or [simple extrusions](https://wiki.freecadweb.org/Part_Extrude) will be stored as extrusions (IfcSweptAreaSolid, or IfcExtrudedAreaSolid) inside the IFC file. Any other object which cannot be described as a simple extrusion, will be stored as IfcFacetedBrep.

- IfcOpenShell v0.6 onwards features a serializer able to create IfcAdvancedBrep objects, that can contain curved surfaces. if using the correct version, and the use of the serializer is turned on in the FreeCAD IFC export preferences, IfcAdvancedBrep objects will be created for objects that contain curved faces. Otherwise, they will be triangulated and exported as IfcFacetedBrep.

- Any object with IFC type as Element Assembly, will be exported as an IfcElementAssembly, which allows it to contain other BIM objects. [building parts (levels)](https://wiki.freecadweb.org/Arch_BuildingPart) are a convenient tool to use to create assemblies.

- Some other BIM applications sometimes have limitations and specific requirements. The [Preflight tool](https://wiki.freecadweb.org/BIM_Preflight) is able to notify you of several of them.
