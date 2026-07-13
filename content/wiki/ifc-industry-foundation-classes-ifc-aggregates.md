---
title: "IFC aggregates"
url: "/ifc-industry-foundation-classes-ifc-aggregates/"
parent: "/ifc-industry-foundation-classes/"
aliases: ["/IFC_-_Industry_Foundation_Classes/IFC_aggregates/", "/IFC_aggregates/", "/Industry_Foundation_Classes_(IFC)/IFC_aggregates/"]
categories: ["Industry Foundation Classes (IFC)"]
lastmod: "2022-07-28T10:21:40Z"
---

> **Stub:** This article needs expansion.


{{< wiki-image src="/media/at2-fixme.png" alt="At2 Fixme" mode="inline" >}} TODO

- Aggregate meaning 
    - An IFC entity that does not have its own body geometry. Its components hold geometry and structure-related data. 
    - a whole formed by combining several separate elements

In IFC, it is possible to describe how a particular element is made out of many sub elements of the same type. This description is called an "aggregation". 


Types of elements that represent objects, like walls and doors, can be aggregated, or collected. 

Examples:
- Roofs
    - Roofs can consist of many beams, insulation layers, fixings, and coverings. 
- Stairs
    - Stairs may include multiple stair flights, some landings, and railings.

{{< wiki-image src="/media/at2-tip.png" alt="At2 Tip.png" mode="inline" >}}Note that aggregations only apply to elements of the same type. You cannot mix element types. For example, you cannot say a space consists of furniture - as the space element is a different type of element to the furniture element.

How to create aggregates in:
- Bonsai {{< wiki-image src="/media/at2-fixme.png" alt="At2 Fixme" mode="inline" >}} 
- FreeCAD {{< wiki-image src="/media/at2-fixme.png" alt="At2 Fixme" mode="inline" >}} 


Further reading:
- [OSArch Community](https://community.osarch.org/discussion/comment/3657#Comment_3657)
- [BuildingSmart Semantic definitions at the entity](https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD2/HTML/schema/ifckernel/lexical/ifcrelaggregates.htm)
- [BIMvoice live: Dion Moult on how to group sub objects in IFC Jan.2021](https://www.youtube.com/watch?v=0csmFH1glik)
