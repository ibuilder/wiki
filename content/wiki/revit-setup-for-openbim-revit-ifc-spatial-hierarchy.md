---
title: "Revit IFC spatial hierarchy"
url: "/revit-setup-for-openbim-revit-ifc-spatial-hierarchy/"
aliases: ["/Revit_IFC_spatial_hierarchy/", "/Revit_setup_for_OpenBIM/Revit_IFC_spatial_hierarchy/", "/Revit_spatial_hierarchy/"]
categories: ["Autodesk Revit"]
lastmod: "2022-01-31T10:41:00Z"
---

## IfcSite
The following attributes may be set on the <code>IfcSite</code>. If you have a <code>Toposurface</code> object overriding your <code>IfcSite</code> object representation as detailed in [Revit geolocation](/revit-setup-for-openbim-revit-ifc-geolocation/), the procedure is slightly different. Do not implement both procedures simultaneously. Note that in Revit, only a single <code>IfcSite</code> may exist. It is not possible to create multiple sites.

| **Attribute Name** | **Required** | **Procedure with <code>Toposurface</code>** | **Procedure without <code>Toposurface</code>** |
| --- | --- | --- | --- |
| <code>Name</code> | Yes | Create a new <code>IfcName</code> instance parameter, assigned to the <code>Toposurface</code> object. | Create a new <code>SiteName</code> instance parameter, assigned to the <code>Project Information</code> object. |
| <code>Description</code> |  | Create a new <code>IfcDescription</code> instance parameter, assigned to the <code>Toposurface</code> object. | Create a new <code>SiteDescription</code> instance parameter, assigned to the <code>Project Information</code> object. |
| <code>ObjectType</code> |  | Create a new <code>IfcObjectType</code> instance parameter, assigned to the <code>Toposurface</code> object. | Create a new <code>SiteObjectType</code> instance parameter, assigned to the <code>Project Information</code> object. |
| <code>LongName</code> | Yes | Create a new <code>IfcLongName</code> instance parameter, assigned to the <code>Toposurface</code> object. | Create a new <code>SiteLongName</code> instance parameter, assigned to the <code>Project Information</code> object. |
| <code>LandTitleNumber</code> | Yes | Create a new <code>IfcLandTitleNumber</code> instance parameter, assigned to the <code>Toposurface</code> object. | Create a new <code>SiteLandTitleNumber</code> instance parameter, assigned to the <code>Project Information</code> object. |
| <code>SiteAddress</code> |  | This may be set via <code>File &gt; Export &gt; IFC &gt; Modify setup &gt; General &gt; Project Address</code> and checking <code>Assign address to site</code>. | Same procedure as with <code>Toposurface</code>. |
## IfcBuilding
The following attributes may be set on the <code>IfcBuilding</code>. Note that in Revit, only a single <code>IfcBuilding</code> may exist. It is not possible to create multiple buildings.

| **Attribute Name** | **Required** | **Procedure** |
| --- | --- | --- |
| <code>Name</code> | Yes | Fill out the <code>Building Name</code> field in the <code>Project Information</code> dialog. |
| <code>Description</code> |  | Create a new <code>BuildingDescription</code> instance parameter, assigned to the <code>Project Information</code> object. |
| <code>ObjectType</code> |  | Create a new <code>BuildingObjectType</code> instance parameter, assigned to the <code>Project Information</code> object. |
| <code>LongName</code> | Yes | Create a new <code>BuildingLongName</code> instance parameter, assigned to the <code>Project Information</code> object. |
| <code>ElevationOfRefHeight</code> |  | Does not seem possible to change this value. Defaults to null. |
| <code>ElevationOfTerrain</code> |  | Does not seem possible to change this value. Defaults to null. |
| <code>BuildingAddress</code> |  | This may be set via <code>File &gt; Export &gt; IFC &gt; Modify setup &gt; General &gt; Project Address</code> and checking <code>Assign address to building</code>. |
An example of the building address settings to be provided is shown below.

{{< wiki-image src="/media/revit-building-address.png" alt="Revit-building-address.PNG" mode="inline" >}}

Note that if you fill out address details in <code>File &gt; Export &gt; IFC &gt; Modify setup &gt; General &gt; Project Address</code>, then that address will be exported twice in your IFC: once for the site and another for the building. This behaviour cannot be changed. Even unchecking <code>Assign address to building/site</code> will not remove this information, but only remove the link between the address and the building/site.

## IfcBuildingStorey
<code>IfcBuildingStorey</code> elements are generated for each Revit level which has the checkbox <code>Building Storey</code> checked in properties. The following attributes can be set:

| **Attribute Name** | **Required** | **Procedure** |
| --- | --- | --- |
| <code>Name</code> | Yes | This defaults to the <code>Name</code> parameter in the <code>Identity Data</code> parameter group. This is usually incorrect, as IFC names are usually short codes, not long descriptions. You can override this by creating a new <code>IfcName</code> instance parameter. |
| <code>Description</code> |  | Create a new <code>IfcDescription</code> instance parameter. |
| <code>ObjectType</code> |  | Create a new <code>IfcObjectType</code> instance parameter. |
| <code>LongName</code> | Yes | Create a new <code>IfcLongName</code> instance parameter. This should typically contain the same value as the <code>Name</code> parameter in the <code>Identity Data</code> parameter group. |
| <code>CompositionType</code> |  | This is asserted by default to <code>ELEMENT</code>. It is not possible to override this. It is not possible to nest spatial structures in Revit. |
| <code>Elevation</code> |  | This is automatically derived from the <code>Elevation</code> parameter in the <code>Constraints</code> parameter group. Although not obviously wrong, this does not match the current intention by buildingSMART. This is fundamentally broken in Revit. |
## IfcSpace
In Revit, there are <code>Room</code> objects, <code>Space</code> objects. Both of these objects translate into <code>IfcSpace</code> entities. Revit <code>Area</code> objects do *not* translate into IFC and are lost.

If you are exporting from a 3D view which has filters to turn certain objects on and off, you may have enabled the <code>Export only elements visible in view</code> option in <code>File &gt; Export &gt; IFC &gt; Modify Setup &gt; Additional Content</code>. If this is enabled, you must enable the <code>Export rooms in 3D views</code> option, or <code>IfcSpace</code> entities will not be created in your IFC file. Despite the use of the word "rooms", the option applies to both Revit <code>Room</code> and <code>Space</code> objects.

{{< wiki-image src="/media/revit-export-spaces.png" alt="Revit-export-spaces.PNG" mode="inline" >}}

The following attributes may be set:

| **Attribute Name** | **Required** | **Procedure** |
| --- | --- | --- |
| <code>Name</code> | Yes | This defaults to the <code>Number</code> parameter in the <code>Identity Data</code> parameter group. You can override this by creating a new <code>IfcName</code> instance parameter. |
| <code>Description</code> |  | Create a new <code>IfcDescription</code> instance parameter. |
| <code>ObjectType</code> |  | Create a new <code>IfcObjectType</code> instance parameter. |
| <code>LongName</code> | Yes | This defaults to the <code>Name</code> parameter in the <code>Identity Data</code> parameter group. You can override this by creating a new <code>IfcLongName</code> instance parameter. |
| <code>CompositionType</code> |  | This is asserted by default to <code>ELEMENT</code>. It is not possible to override this. It is not possible to nest spatial structures in Revit. |
| <code>PredefinedType</code> |  | This defaults to <code>INTERNAL</code> with IFC2x3 and <code>SPACE</code> with IFC4. It is not possible to override this. |
| <code>ElevationWithFlooring</code> |  | This is null by default. Create a new <code>IfcElevationWithFlooring</code> instance parameter. |
## IfcZone
The Revit <code>HVAC Zone</code> object translates into IFC <code>IfcZone</code> entities. In addition, it is also possible to group Revit <code>Room</code> objects into <code>IfcZone</code> entities. To do this, create a new <code>ZoneName</code> instance parameter assigned to a Revit <code>Room</code> object. For each unique string supplied in this parameter, an <code>IfcZone</code> entity will be created.[^1]

> **Warning:** Virtual <code>IfcZones</code> created by grouping multiple Revit <code>Room</code> objects will not maintain their <code>GlobalId</code> values on subsequent exports. Additionally, if two <code>ZoneName</code> parameters have the same value, but their other attributes, such as <code>ZoneDescription</code> are different, then only one will be exported, and the rest of the data will be lost. It is not clear to the user which will be retained and which will be lost, so care must be taken to manually ensure data consistency between all these fields.

The following attributes may be set:

| **Attribute Name** | **Required** | **Procedure with Revit <code>HVAC Zone</code>** | **Procedure with virtual zone from Revit <code>Room</code>** |
| --- | --- | --- | --- |
| <code>Name</code> | Yes | This defaults to the <code>Name</code> parameter in the <code>Identity Data</code> parameter group, concatenated with the Revit <code>Element ID</code>. This concatenation usually results in an undesirable value. You can override this by creating a new <code>IfcName</code> instance parameter. | Create a new <code>ZoneName</code> instance parameter, assigned to the <code>Room</code> object. |
| <code>Description</code> |  | Create a new <code>IfcDescription</code> instance parameter, assigned to the <code>HVAC Zone</code> object. | Create a new <code>ZoneDescription</code> instance parameter, assigned to the <code>Room</code> object. |
| <code>ObjectType</code> |  | Create a new <code>IfcObjectType</code> instance parameter, assigned to the <code>HVAC Zone</code> object. | Create a new <code>ZoneObjectType</code> instance parameter, assigned to the <code>Room</code> object. |
| <code>LongName</code> | Yes | Create a new <code>IfcLongName</code> instance parameter, assigned to the <code>HVAC Zone</code> object. | Create a new <code>ZoneLongName</code> instance parameter, assigned to the <code>Room</code> object. |
Resources :
- [IFC for Revit wiki - Exporting Zones](https://sourceforge.net/p/ifcexporter/wiki/Exporting%20Zones/)
- [bim42 IFC from Revit - Part 1](https://www.bim42.com/2018/03/ifc-for-revit-1/#ifczones)

## Element placement in Spatial Container
Most elements in Revit will on export be assigned to an IfcBuildingStorey based on the value of parameters like <code>Base Level</code> for columns, <code>Base Constraint</code> for walls, <code>Level</code> for floors and <code>Reference Level</code> for beams. For Face Based families the parameter <code>Schedule Level</code> is used, which has to be set manually and is often forgotten.

It is possible to override the spatial container of an element by adding an instance parameter <code>IfcSpatialContainer</code>

The valid values are:
- <code>IfcSite</code> - for assigning objects to IfcSite, useful for objects outside the building
- <code>IfcBuilding</code> – for assigning objects to IfcBuilding
- <code>name of the level</code> - for assignment to a specific IfcBuildingStorey (= Level in Revit). Please note that the Level must be checked for export as Building Story


[^1]: IFC for Revit wiki - Exporting Zones
