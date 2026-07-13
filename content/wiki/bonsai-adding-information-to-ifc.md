---
title: "Bonsai adding information to IFC"
url: "/bonsai-adding-information-to-ifc/"
aliases: ["/Adding_IFC_properties_and_quantities/", "/BlenderBIM_Add-on_adding_information_to_IFC/", "/blenderbim-add-on-adding-information-to-ifc/"]
categories: ["Blender", "Bonsai", "Industry Foundation Classes (IFC)"]
lastmod: "2022-01-25T15:04:42Z"
---

## The I in BIM
A building information model usually consists of a 3-dimensional digital model, which provides spatial data, and of a large amount of other information linked in some way either to the whole model or most often to the particular elements. The most common way of doing this is to use object attributes, properties and quantities.

## Adding IFC attributes
Attributes are the basic object information and their structure comes hardcoded in the IFC schema. They contain the most rudimental data like Name, Description and Object type.

An Attribute can be added by selecting an object, going to Object properties >IFC Object > Attributes and picking a predefined Attribute name from the drop-down menu. A new line with the Attribute name is then added and the Attribute value can be filled in.
{{< wiki-image src="/media/bonsai-attributes.jpg" alt="Object IFC attributes UI" mode="frame" caption="Object IFC attributes UI" align="center" >}}

## Adding IFC properties
Properties are often defined by users. There are predefined Property sets which add a batch of properties, but the users are also free to create their own.

A Property set can be added by selecting an object, going to Object properties >IFC Object Property sets and picking a predefined property set or a Custom_Pset from the drop-down menu. A new batch of lines with the properties is then added and the values can be filled in.

{{< wiki-image src="/media/bonsai-properties.jpg" alt="Object IFC properties UI" mode="frame" caption="Object IFC properties UI" align="center" >}}

It is possible to store the required "information" as a template as a .JSON. This file can be read with a text editor and, if required, items can be added or removed from the template.
Properties stored under a Pset, can be exported by PsetName.PropertyName.
NOTE: It is important to follow the official list of building smart standardised pset. "Pset_Revit_Other" or similar are not legal and custom psets are not allowed to use the "pset_" prefix

[Needs Image?](/Needs_Image%3F/)

The template can now be loaded into Bonsai to speedup the setup process.

## Adding IFC quantities
Quantities are linked to the IfcElement Class. There are predefined Quantity Take Off sets which add a batch of Quantities.

A QTO set can be added by selecting an object, going to Object properties >IFC Object Quantity sets and picking a predefined Quantity set. A new batch of lines with the Quantitie is then added and the values can be filled in.

Bonsai provides also a guessing feature to fill the quantities automatically. By clicking the button next to the quantity field, the quantity will be calculated and filled in. However, this feature has its obvious limits: the quantity in question has to be clearly defined by the geometry.

{{< wiki-image src="/media/bonsai-quantities.jpg" alt="Object IFC quantities UI" mode="frame" caption="Object IFC quantities UI" align="center" >}}
