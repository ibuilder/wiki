---
title: "ArchiCAD IFC setup"
url: "/archicad-ifc-setup/"
aliases: ["/ArchiCAD_IFC_setup/", "/ArchiCAD_setup/"]
categories: ["Graphisoft Archicad"]
lastmod: "2020-12-23T10:44:38Z"
---

## IFC GlobalId
The IFC <code>GlobalId</code> generated for the <code>IfcProject</code>, <code>IfcSite</code>, <code>IfcBuilding</code>, and <code>IfcBuildingStorey</code> depends on the values you put in the <code>File &gt; Info</code> Project Info dialog box. This means that it is important to fill out these values correctly with project specific information. If these are left blank, or have data from a different project, it will run the risk of generating a <code>GlobalId</code> which is not unique to the project.

Read more at [How to Control Global ID (IFC Attribute) Based on ARCHICAD Project Info](https://helpcenter.graphisoft.com/user-guide/89335/#XREF_83086_How_to_Control).
