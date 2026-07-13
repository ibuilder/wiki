---
title: "IFC attributes and properties"
url: "/ifc-attributes-and-properties/"
aliases: ["/IFC_attributes_and_properties/"]
categories: ["Industry Foundation Classes (IFC)"]
lastmod: "2020-11-28T17:30:54Z"
---

Attributes and properties are two ways to assign extra metadata to an IFC class. Although they sound similar, they are not the same.

## IFC attributes
All IFC classes have attributes. Attributes contain a name, as well as a value. An example attribute is the <code>Name</code> attribute that all *rooted* classes inherit. For example, an <code>IfcDoor</code> might have a <code>Name</code> attribute with the value "D01". Attributes may be optional or mandatory. They may store simple text, like the <code>Name</code> attribute, or more complex data, like the <code>OwnerHistory</code> attribute, which can store who is responsible for changing an object, including their name, which application they use, which organisation they are part of, and how to contact them.

Attributes cannot be separated from their IFC classes. When an IFC class is defined, their attributes must be defined as well, or marked as empty if it is optional. The list of attributes that can be created for each IFC classes is fixed and specified in the IFC specification. It is not possible to add or remove attributes as an end-user. For this reason, there are usually only a small number of attributes associated with each IFC class, and they usually hold very common data that is useful to everybody internationally. They also remain relatively stable between IFC versions.

## IFC properties
In contrast, properties may be also assigned to an IFC class. Unlike attributes, which are defined with each IFC class, properties themselves are an IFC class, and properties themselves have attributes. Also unlike attributes, related properties can be grouped into a property set, or Pset, for short. This Pset can exist as its own IFC class, and then be linked to one or more relevant IFC classes. For instance, there might be a property named <code>FireRating</code> which has an attribute which stores a value of "2 Hours". This property is grouped in the Pset called <code>Pset_WallCommon</code>, which is then linked to multiple <code>IfcWall</code> objects. Names like <code>FireRating</code> and <code>Pset_WallCommon</code> are defined in the IFC specification and cannot be changed by the end-user, similar to how attributes cannot be changed. However, users are able, and encouraged to add their own project-specific properties and group it into their own Psets if it does not exist in the IFC specification.

A special type of property is known as a quantity. Quantities are specialised to store information that can be quantified, like a length, area, volume, weight, time, or monetary value. Quantities and properties are very similar, in that they can be grouped, and then linked to multiple IFC classes, and users can add custom quantities if the ones in the IFC specification do not suit their needs. A group of quantities may also be referred to as a quantity set, or Qto for short. BIM authoring tools may also display quantities in a separate area of the interface, or offers special functions to calculate them automatically.

Unlike attributes, which exist on all IFC classes, not all Psets or Qtos can be assigned to any IFC class. For example, the <code>Pset_WallCommon</code> Pset can only be assigned to <code>IfcWall</code> classes. In contrast, the <code>Pset_ConcreteElementGeneral</code> Pset can be assigned to more than 10 different types of IFC classes, which include <code>IfcWall</code>, as well as others like <code>IfcBeam</code> and <code>IfcColumn</code>. The specification defines which Psets and Qtos can be assigned to which IFC classes. If you have created your own Pset, you are free to assign it to any class.

## List of IFC property sets
There are multiple versions of IFC in use in the industry, and each version has hundreds of IFC property sets. This makes it impractical to describe them in their entirety in a separate community wiki. However, there are some resources available for those who do want a list:

- [Official IFC4.2 specification list of all Psets](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/annex/annex-b/alphabeticalorder_psets.htm)
- [Official IFC4.2 specification list of all Qtos](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/annex/annex-b/alphabeticalorder_qsets.htm)
- [IFC4.2 classes and property sets in spreadsheet format](/media/Ifc-4.2.0.0.ods)
- [Official IFC2x3 TC1 specification list of all Psets](https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/psd/psd_index.htm)
