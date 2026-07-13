---
title: "IFC spatial tree"
url: "/ifc-industry-foundation-classes-ifc-spatial-tree/"
parent: "/ifc-industry-foundation-classes/"
aliases: ["/IFC_-_Industry_Foundation_Classes/IFC_spatial_tree/", "/IFC_spatial_tree/", "/Industry_Foundation_Classes_(IFC)/IFC_spatial_tree/"]
categories: ["Industry Foundation Classes (IFC)"]
lastmod: "2022-07-28T10:21:43Z"
---

{{< wiki-image src="/media/ifc-spatial-tree.png" alt="An example spatial tree. Orange classes belong to IFC context, blue classes belong to <code>IfcSpatialElement</code>, and green classes belong to <code>IfcElement</code>. Blue arrows represent an *aggregation* relationship, and green arrows represent a *spatial containment* relationship." mode="thumb" caption="An example spatial tree. Orange classes belong to IFC context, blue classes belong to <code>IfcSpatialElement</code>, and green classes belong to <code>IfcElement</code>. Blue arrows represent an *aggregation* relationship, and green arrows represent a *spatial containment* relationship." align="right" width="300" >}}

IFC data often, but not always, contains what is known as a spatial tree or spatial hierarchy. This is a tree of classes that inherit from <code>IfcSpatialElement</code> that describe the spatial organisation of a building. For example, it might describe that a site contains two buildings, and each building contains 5 storeys, and each storey contains 3 spaces.

As all IFC data must start from an [IFC context](/ifc-projects-and-contexts/), such as an <code>IfcProject</code>, the top level of the spatial tree is assigned to the IFC context. If the context is an <code>IfcProjectLibrary</code>, a spatial tree may not exist. This top level of the spatial tree may be any <code>IfcSpatialElement</code>, but is commonly an <code>IfcSite</code> class. The relationship between the top level of the spatial tree and the IFC context is known as an *aggregation* relationship, or as *spatial (de)composition*.

Within the spatial tree itself, a <code>IfcSpatialElement</code> subclass may then contain zero or more <code>IfcSpatialElement</code> subclasses. This builds up a spatial hierarchy. For example, <code>IfcSite</code> may contain multiple <code>IfcBuilding</code>. This relationship between <code>IfcSpatialElement</code> subclasses is also known as an *aggregation* relationship, or as *spatial (de)composition*.

Usually at the bottom of the spatial hierarchy, the spatial tree may end and contain actual physical built elements, such as walls and columns. Walls and columns are *not* <code>IfcSpatialElement</code>, but instead belong to <code>IfcElement</code>. To an end-user, a space containing a wall and column is similar to how a site contains a building, but in IFC, this is known as a *spatial containment* relationship.

A list of possible subclasses of <code>IfcSpatialElement</code> is shown below.

| IFC Class | Description |
| --- | --- |
| <code>IfcExternalSpatialElement</code> | The external spatial element defines external regions at the building site. Examples include external air space around the building, a volume covered by earth or water around the building, or a neighbouring fire risk. |
| <code>IfcBridge</code> | A Bridge is civil engineering works that affords passage to pedestrians, animals, vehicles, and services above obstacles or between two points at a height above ground. |
| <code>IfcBuilding</code> | A building represents a structure that provides shelter for its occupants or contents and stands in one place. |
| <code>IfcBridgePart</code> | In a bridge, <code>IfcBridgePart</code> represents the parts according to local practices (e.g. Superstructure, Substructure, Foundation). |
| <code>IfcBuildingStorey</code> | The building storey has an elevation and typically represents a (nearly) horizontal aggregation of spaces that are vertically bound. |
| <code>IfcSite</code> | A site is a defined area of land, possibly covered with water, on which the project construction is to be completed. A site may be used to erect, retrofit or turn down building(s), or for other construction related developments. |
| <code>IfcSpace</code> | A space represents an area or volume bounded actually or theoretically. Spaces are areas or volumes that provide for certain functions within a building, like a room. |
| <code>IfcSpatialZone</code> | A spatial zone is a non-hierarchical and potentially overlapping decomposition of the project under some functional consideration. A spatial zone might be used to represent a thermal zone, a construction zone, a lighting zone, a usable area zone. |
