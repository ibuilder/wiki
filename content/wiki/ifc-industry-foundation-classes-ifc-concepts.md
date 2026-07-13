---
title: "IFC concepts"
url: "/ifc-industry-foundation-classes-ifc-concepts/"
parent: "/ifc-industry-foundation-classes/"
aliases: ["/IFC_-_Industry_Foundation_Classes/IFC_concepts/", "/IFC_concepts/", "/Industry_Foundation_Classes_(IFC)/IFC_concepts/"]
categories: ["Industry Foundation Classes (IFC)"]
lastmod: "2022-07-28T10:21:41Z"
---

{{< wiki-image src="/media/ifc-concept-spatial-decomposition.png" alt="Ifc-concept-spatial-decomposition.png" mode="inline" align="right" >}}

The IFC specification defines how [IFC classes](/ifc-industry-foundation-classes-ifc-classes/) may reference one another using attributes to describe concepts that have meaning in the AEC industry. There are hundreds of IFC classes, and hundreds of ways they may be combined to describe different concepts. An example of two IFC classes is an <code>IfcSite</code> and an <code>IfcBuilding</code>. If a third IFC class <code>IfcRelAggregates</code> is added which references <code>IfcSite</code> and <code>IfcBuilding</code>, it is effectively creating a relationship that describes to the computer "My site has a building", or inversely, "My building is within a site". This is one of hundreds of concepts.

The concepts and their nuances are described in full in the IFC documentation, but this is often difficult to understand. This IFC concept guide offers a crash course, similar to a phrasebook for learning native IFC.

## Subpages
{{< subpages >}}

Pages we'd like to see
- [IFC concepts/IFC spatial concepts](/IFC_concepts/IFC_spatial_concepts/)
- [IFC concepts/IFC facility management concepts](/IFC_concepts/IFC_facility_management_concepts/)
