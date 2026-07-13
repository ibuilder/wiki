---
title: "Bonsai for building and exporting an IFC model"
url: "/bonsai-for-building-and-exporting-an-ifc-model/"
aliases: ["/BlenderBIM_Add-on/BlenderBIM_Add-on_for_building_and_exporting_an_IFC_model/", "/BlenderBIM_Add-on_for_building_and_exporting_an_IFC_model/", "/Building_and_exporting_an_IFC_model_with_BlenderBIM_Add-on/", "/Exporting_an_IFC_model_with_BlenderBIM_Add-on/", "/blenderbim-add-on-blenderbim-add-on-for-building-and-exporting-an-ifc-model/"]
categories: ["Blender", "Bonsai", "Industry Foundation Classes (IFC)"]
lastmod: "2022-07-27T14:03:32Z"
---

## Building a BIM model
Following the [project structure](/bonsai-setting-up-a-bim-project/#project-structure) set up either manually or with [Quick project setup](/bonsai-setting-up-a-bim-project/#quick-project-setup), you can build your model in any way you are used to in Blender. The most common modelling workflows for architecture are:
- Using [Archipack](https://blender-archipack.org/) plugin
- Using [Sverchok](http://nortikin.github.io/sverchok/) plugin
- Extruding 2D drawing
- Building with boxes
In the end, all the objects in your model need to be properly  [nested](https://docs.blender.org/manual/en/latest/scene_layout/collections/introduction.html), to the correct project spaces - Project, Site, Building and Storey. Whether you do this after you are finished modelling, or already in the course of your work is up to you. It is, however, strongly recommended to adapt it into your workflow and to work with the parent spaces directly for anything but very simple, or existing projects, as it greatly helps managing the complexity of building models.

Any object not attached and nested to a project space parent and collection will be ignored on export.

## Classifying Objects
Apart from the correct spatial relation, defined by the project space nesting, each object needs to have a proper [IFC class](/Introduction_to_IFC/#ifc-classes). You can set the class of an object either by manually renaming it to "ifcNameOfClass/NameOfObject" or by using the <code>&quot;Assign IFC Class&quot;</code> command provided by Bonsai.

To utilize the <code>&quot;Assign IFC Class&quot;</code> found under Scene > Building Information Modeling > IFC Categorization, you first need to select the object to be changed and select a proper Product, Class and Type from the respective lists. After running the command the object's name is updated and the class is applied.

Any object without an IFC class will be ignored on export.

## Exporting to IFC
The correctly set up model can be easily exported as an [IFC file](/Introduction_to_IFC/#ifc-formats) with File > Export > Industry Foundation Classes (.ifc/.ifczip).

Currently only selected objects are exported.

## Exporting from archipack
The add-on provide a modified exporter in order to pre-process geometry and automatically create structure on the fly when missing with File > Export > Industry Foundation Classes (archipack) (.ifc).

The exporter takes care of selecting archipack's objects for you.

In order to create project structure skeleton by hand for complex projects, finer classification, or export non archipack objects, you may build a collection structure by hand using Tools-> Ifc structure utility. 
The tool create collections and assign proper object's class names and basic default ifc properties.
