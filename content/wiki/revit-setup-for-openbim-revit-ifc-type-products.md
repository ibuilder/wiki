---
title: "Revit IFC type products"
url: "/revit-setup-for-openbim-revit-ifc-type-products/"
aliases: ["/Revit_IFC_type_products/", "/Revit_setup_for_OpenBIM/Revit_IFC_type_products/", "/Revit_type_products/"]
categories: ["Autodesk Revit"]
lastmod: "2022-01-31T10:41:35Z"
---

The following attributes may be filled.

Note that the shared parameter names used for these parameters, such as <code>IfcName[Type]</code>, need to have <code>[Type]</code> as a suffix. It may be required to update to the latest IFC exporter, as the one shipped by Revit has a bug where type attributes are ignored.

| **Attribute Name** | **Required** | **Procedure** |
| --- | --- | --- |
| <code>Name</code> | Yes | By default, Revit exports the family's type joined with the <code>Type Name</code> value (e.g. <code>Basic Wall:Block Wall - 140</code>). If you enable the <code>Use Type name only for IFCType name</code> option in the export <code>Advanced</code> settings tab, this will be simplified to just the type name (e.g. <code>Block Wall - 140</code>). The IFC requirement is to fill in the <code>Name</code> attribute with the codes used in schedules and annotation tags (e.g. <code>BLK140</code>). In the likely event that this isn't the case (e.g. you are tagging a <code>Type Mark</code> field or other custom parameter), you will need to create a new <code>IfcName[Type]</code> type parameter, assigned to the object, and tag that in your drawings instead of <code>Type Mark</code> or otherwise. |
| <code>Description</code> | Recommended | Create a new <code>IfcDescription[Type]</code> type parameter, assigned to the object. |
| <code>ApplicableOccurrence</code> |  | It seems not possible to assign this, despite the <code>IfcApplicableOccurrence[Type]</code> shared parameter being distributed by Autodesk. |
| <code>ElementType</code> |  | Create a new <code>IfcElementType[Type]</code> type parameter, assigned to the object. |
| <code>PredefinedType</code> | Recommended | Create a new <code>IfcExportType[Type]</code> type parameter, assigned to the object. The value is case insensitive. |
