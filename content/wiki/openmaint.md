---
title: "OpenMAINT"
url: "/openmaint/"
aliases: ["/OpenMAINT/"]
categories: []
lastmod: "2023-10-14T13:10:23Z"
---

> **Stub:** This article needs expansion.
<aside class="software-infobox">
<img src="/media/logo-openmaint.png" alt="">
<dl>
<dt>Website</dt><dd><a href="https://www.openmaint.org/en">openmaint.org</a></dd>
<dt>Source</dt><dd><a href="https://sourceforge.net/projects/cmdbuild/">CMDBuild source</a></dd>
<dt>License</dt><dd><a href="https://www.cmdbuild.org/en/project/license">AGPL-3.0</a></dd>
<dt>Issues</dt><dd>Only paid support</dd>
<dt>Community</dt><dd><a href="https://forum.cmdbuild.org/">CMDBuild Forum</a> <a href="https://www.cmdbuild.org/en/documentation/manuals">PDF manuals</a></dd>
<dt>Maturity</dt><dd>Mature</dd>
<dt>Support</dt><dd><a href="https://www.openmaint.org/en/services">Subscription Enterprise Solution</a></dd>
</dl>
</aside>


openMAINT is the application for the management of mobile assets, plants and technical devices, furniture, etc., and the related logistical, economical and maintenance activities, scheduled and breakdown ones.

openMAINT is based on the software CMDBuild from which it inherits the basic functionalities and the configuration mechanisms.
CMDBuild is a web environment for the configuration of custom applications for the Asset Management.

CMDBuild documentation contains sections about openMAINT as well.

## Installation
## Official
Only bare metal installation is documented from prebuilt WAR files. Download from [SourceForge](https://sourceforge.net/projects/openmaint/files/). More info in the [CMDBuild Technical Manual](https://www.cmdbuild.org/file/manuali/technical-manual-in-english)

On the [official forum](https://forum.cmdbuild.org/) maintainers rarely reply to installation problems, but there are some helpful forum members.

There is an online demo available without BIM features, after registration: [Request Demo](https://www.openmaint.org/en/contacts/request-demo)

Paid support and help is available from the maintainer: [Support from Tecnoteca](https://www.tecnoteca.com/en/services/openmaint/pay-per-use)

## Docker
Community built Docker images are available:

- Images built from the official prebuilt WAR files: https://github.com/itmicus/cmdbuild_docker
- Images built from source with other fixes: https://gitlab.com/infeeeee/cmdbuild-community

## BIM features
BIM features related documentation is not very detailed. Most BIM features require a connection to a running [BIMServer](/bimserver/)

{{< wiki-image src="/media/open-maint-screenshot.jpg" alt="IFC file displayed with BIMSurfer on the OpenMAINT UI" mode="thumb" caption="IFC file displayed with BIMSurfer on the OpenMAINT UI" >}}

## Display IFC Files in OpenMaint
OpenMAINT contains [BIMSurfer](/BIMSurfer/) and [Xeokit](/xeokit/) viewers. Linked IFC files can be displayed on the OpenMAINT UI.

## Import data from IFC files
Any data can be imported from IFC files with IFC import templates. Documentation about setting up an IFC import template is available in the [CMDBuild Administration Manual](https://www.cmdbuild.org/file/manuali/administrator-manual-in-english)

### Import filters
IFC entities can be imported as any OpenMAINT class. On the *IFC Entity Path* option a filter can be also set up, to import only specific entities.

To filter by Pset values, a query like this can be used:

 IfcFlowTerminal[IsDefinedBy[RelatingPropertyDefinition/Name="PSet_Revit_Type_Identity Data"]/RelatingPropertyDefinition/HasProperties[Name="OmniClass Number"]/NominalValue[wrappedValue="23.40.20.21.21"]]

This will import only *IfcFlowTerminal* entities where *OmniClass Number* parameter in the pset *PSet_Revit_Type_Identity Data* is *23.40.20.21.21*.

On a simple IFC class  name all entities of the class will be imported, e.g. this will import all *IfcSpace*s:

 IfcSpace

### Map Pset parameters to OpenMAINT attributes
IFC parameters can be mapped to OpenMAINT attribute values. These parameters can be updated if a newer version of the file is imported again.

A query like this can be used in the *IFC property* column:

 IsDefinedBy[RelatingPropertyDefinition/Name="PSet_Revit_Dimensions"]/RelatingPropertyDefinition/HasProperties[Name="Area"]/NominalValue/wrappedValue

This will return the value of the *Area* parameter from the pset *PSet_Revit_Dimensions*.
