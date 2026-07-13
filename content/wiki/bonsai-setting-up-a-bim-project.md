---
title: "Bonsai Setting up a BIM Project"
url: "/bonsai-setting-up-a-bim-project/"
aliases: ["/BlenderBIM_Add-on/BlenderBIM_Add-on_Setting_up_a_BIM_Project/", "/BlenderBIM_Add-on_Setting_up_a_BIM_Project/", "/Setting_up_a_BIM_Project_with_BlenderBIM_Add-on/", "/blenderbim-add-on-blenderbim-add-on-setting-up-a-bim-project/"]
categories: ["Blender", "Bonsai"]
lastmod: "2022-07-27T14:40:28Z"
---

## Project structure
Each Project using BIM needs to be set up with the proper structure. Bonsai uses the open data structure of [IFC](/Introduction_to_IFC/). As with almost everything with Bonsai, you can do that either manually from Blender itself, or use the specialized commands provided by the add-on.

## Project schema directory
The fastest way to create the project structure is to use Bonsai "Quick project setup" feature. To do that, you first need to select the proper template to be applied when the project structure is set up. This template lies in the so-called project schema directory, which is by default set to <code>BLENDER_ADDONS_DIR⁄bonsai⁄schema⁄</code>. You can choose the project schema directory in Blender under Scene > Building Information Modeling > Schema Directory.

The default folder is prepackaged with the IFC4 schema and you can download different schema from the buildingSMART website. However, unless you are an IFC guru, you shouldn’t have to touch this.

## Project data directory
You can choose the project data directory in Blender under Scene > Building Information Modeling > Data Directory.

The data directory holds the auxiliary data related to your IFC model. Examples include related property definitions, documents, and classification systems. Each project should have its own data directory. It defaults to the data directory in the <code>BLENDER_ADDONS_DIR⁄bonsai⁄data⁄</code> folder, which comes with some example preset data. You are encouraged to copy this template and set your own.

## Quick project setup
You can find the command in Blender under Scene > Building Information Modeling > System Setup.
This will create a basic spatial tree. It will create a tree of collections with the structure IfcProject > IfcSite > IfcBuilding > IfcStorey This is merely for convenience instead of having to create it all by yourself, since all IFC exports require a valid spatial tree. You can see the tree of collections in the outliner when this is done.
{{< wiki-image src="/media/bonsai-quick-project-setup-01.jpg" alt="Quick Project Setup, Schema and Data directories" mode="frame" caption="Quick Project Setup, Schema and Data directories" align="center" >}}

## Standard project structure
The standard project structure, as proposed by Building Smart (the developer of IFC) and currently default in Bonsai, is following:
- site as IfcSite
- building as IfcBuilding
- storey as IfcBuildingStorey
- space as IfcSpace
A project can include any number of sites, a site any number of buildings and so on.
The abstract spaces, converted to their respective IFC counterparts on export, are represented by a hierarchy of collections. Any objects outside a IfcSite collection will be ignored on export.

Empty axes objects, with names identical to those of their container collections,  are automatically placed in the project structure created by the Quick project setup command and they serve several purposes:

They hold the IFC properties for the spatial elements. IFC spatial elements (e.g. sites, buildings, elements) can store properties (attributes / psets / qtos / etc). In Blender, if you click on an object, you can see the object panel and manipulate it via the UI. However, for a collection, there is no UI panel associated with the collection. So for convenience, an object is provided that people can click on.

They define the IFC placement of the spatial element. IFC spatial elements almost always have a placement. E.g. a building storey has an elevation value (e.g. a Z coordinate). Blender collections do not have physical locations. Therefore, at the very least, an empty is required, so you can set the placement.

They serve as a placeholder for IFC representations of the spatial element. IFC spatial elements may have representations. E.g. a building or site can actually have geometry associated with it. Therefore, we need an object. In this case, we need more than an empty - we need an actual mesh object.

Note that the name of the Representation object (empty axes or anything else you use) has to be kept identical to the name of the collection it belongs to. So if you rename a storey for example, the empty must be renamed as well.
