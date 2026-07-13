---
title: "Revit IFC project metadata"
url: "/revit-setup-for-openbim-revit-ifc-project-metadata/"
parent: "/revit-setup-for-openbim/"
aliases: ["/Revit_IFC_project_metadata/", "/Revit_project_metadata/", "/Revit_setup_for_OpenBIM/Revit_IFC_project_metadata/"]
categories: ["Autodesk Revit"]
lastmod: "2022-01-31T10:40:29Z"
---

This page describes how to assign information about your Revit project for your .ifc export.

The following attributes may be set on the <code>IfcProject</code>.

| **Attribute Name** | **Required** | **Procedure** |
| --- | --- | --- |
| <code>GlobalId</code> | Yes | Create a new <code>IfcProject GUID</code> instance parameter, assigned to the <code>Project Information</code> object. |
| <code>Name</code> | Yes | Fill out the (Revit standard) <code>Project Number</code> field in the <code>Project Information</code> dialog. |
| <code>Description</code> | Yes | Create a new <code>IfcDescription</code> instance parameter, assigned to the <code>Project Information</code> object. |
| <code>ObjectType</code> |  | Create a new <code>IfcObjectType</code> instance parameter, assigned to the <code>Project Information</code> object. |
| <code>LongName</code> | Yes | Fill out the (Revit standard) <code>Project Name</code> field in the <code>Project Information</code> dialog. |
| <code>Phase</code> |  | Fill out the (Revit standard) <code>Project Status</code> field in the <code>Project Information</code> dialog. |
The project information properties for an .ifc export are described on the [IfcRoot attributes page](https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcproject.htm) of the IFC 2x3 documentation.

Do not fill out Project GUID. Revit will do this on export. Be aware that a [Revit Project GUID may not be unique](https://github.com/Autodesk/revit-ifc/issues/378).
