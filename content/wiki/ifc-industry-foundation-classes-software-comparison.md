---
title: "Software Comparison"
url: "/ifc-industry-foundation-classes-software-comparison/"
aliases: ["/IFC_-_Industry_Foundation_Classes/Software_Comparison/"]
categories: []
lastmod: "2023-01-17T13:49:27Z"
---

This is the start of a page comparing the implementation of Industry Foundation Classes in different software. The main purpose is to be able to understand the differences in the implementation rather than making a direct comparison of features.

Unfortunately different software uses different terminology for the same IFC terms. Here are some examples, please help to expand the list.

| IFC terminology | Example | BIMcollabZOOM | Bonsai | OpenIfcViewer | Revit | Solibri | Navisworks Manage |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IFC Class | IfcFooting | IFC Element | IFC Class |  | IfcExportAs | IFC Element | Missing? |  |
| IFC Predefined Type | STRIP_FOOTING | Predefined Type | PredefinedType |  | IfcExportType | Predefined Type | IfcExportAs |  |
This table can be useful when checking if your export settings are giving you the desired results.

## See Also
- [Revit setup for OpenBIM](/revit-setup-for-openbim/)
