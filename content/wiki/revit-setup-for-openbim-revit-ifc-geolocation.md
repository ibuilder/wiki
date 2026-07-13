---
title: "Revit IFC geolocation"
url: "/revit-setup-for-openbim-revit-ifc-geolocation/"
parent: "/revit-setup-for-openbim/"
aliases: ["/Revit_IFC_geolocation/", "/Revit_geolocation/", "/Revit_setup_for_OpenBIM/Revit_IFC_geolocation/"]
categories: ["Autodesk Revit"]
lastmod: "2022-06-16T04:56:48Z"
---

## From Revit IFC 19.4.0.0 / 20.2.0.0 / 21.1.0.0
> **Warning:** [An issue](https://github.com/Autodesk/revit-ifc/issues/290) with units mismatch has been raised by Jon Mirtschin

Native input of global coordinates has been implemented in Revit IFC [19.4.0.0](https://github.com/Autodesk/revit-ifc/releases/tag/IFC_v19.4.0.0) / [20.2.0.0](https://github.com/Autodesk/revit-ifc/releases/tag/IFC_v20.2.0.0) / [21.1.0.0](https://github.com/Autodesk/revit-ifc/releases/tag/IFC_v21.1.0.0). Although only for IFC4.

## Set coordinates
Specify your <code>Project Base Point</code> coordinates according to data given by your surveyor :

{{< wiki-image src="/media/revit-set-coordinates.png" alt="RevitSetCoordinates.png" mode="inline" >}}

Your <code>Project Base Point</code> should not move relatively to your building / elements. You might also want to apply coordinates to <code>Survey Point</code> to keep both at same location.

Alternatively, you can unclip <code>Survey Point</code>, set coordinates in properties, re-clip it then move it to your <code>Project Base Point</code>. You still need to set angle to north in <code>Project Base Point</code>.

You will also need to set the combined scale factor. This scale factor * surface distance = grid distance. Sometimes, surveyors will give you the opposite. The scale factor will be close to 1. Then, download the [Revit IFC shared parameters file](https://raw.githubusercontent.com/Autodesk/revit-ifc/master/Install/Program%20Files%20to%20Install/IFC%20Shared%20Parameters-RevitIFCBuiltIn_ALL.txt), and add ProjectGlobalPositioning.Scale as a project parameter and make it apply to the Project Information category as an Instance parameter grouped under the "IFC Parameters" group. Insert the scale factor in the Project Information dialog when done.

## Specify global positioning information during export
1. Modify your export setup
1. Select <code>Coordinate Base</code> -> <code>Project Base Point</code>
1. Input <code>EPSG Code</code>. It should be a valid EPSG number see [EPSG website](https://epsg.org) or ask your surveyor.

{{< wiki-image src="/media/revit-global-positioning.png" alt="RevitGlobalPositioning.png" mode="inline" >}}

## Result
You should see an <code>IfcMapConversion</code> in your ifc file after export under <code>IfcProject.RepresentationContexts[0].HasCoordinateOperation[0]</code> :

{{< wiki-image src="/media/revit-ifc-map-conversion.png" alt="RevitIfcMapConversion.png" mode="inline" >}}

## Before Revit IFC 19.4.0.0 / 20.2.0.0 / 21.1.0.0
Revit natively does not allow input of geolocated coordinates. Most users set the <code>N/S</code>, <code>E/W</code>, <code>Elev</code>, and <code>Angle to True North</code> parameters on the <code>Project Base Point</code> and <code>Survey Point</code> objects. Because this workaround is so common and many workflows depend on it, you may continue to apply this workaround without any modification. It is highly advised that the location in Revit of the <code>Project Base Point</code> and the <code>Survey Point</code> is the same.

If your project is primarily vertical, i.e. only one CRS is used, then setting geolocation data is relatively straightforward. If the project is primarily horizontal, i.e. has multiple CRSes, there is currently no established workaround. A standard has yet to be developed. This guide is only for single CRSes. The process is different for IFC2X3 and IFC4.

## IFC2X3 Geolocation
If your project is IFC2X3, you must create a <code>Toposurface</code> object. It must be set to export as an <code>IfcSite</code> object as shown below. When it is set, it will override the auto-generated <code>IfcSite</code> entity that the Revit exporter creates.

{{< wiki-image src="/media/revit-geolocation-topoexport.png" alt="Revit-geolocation-topoexport.png" mode="inline" >}}

> **Warning:** When a <code>Toposurface</code> object overrides the generated <code>IfcSite</code> object, it will also override any parameters you have set in the <code>Project Information</code> object related to the site. For example, if the <code>Project Information</code> contains a <code>SiteName</code> parameter and the <code>Toposurface</code> object contains an <code>IfcName</code> parameter, the <code>IfcName</code> will take priority. You will be required to transfer all your attributes to the <code>Toposurface</code> object.

This <code>Toposurface</code> must be assigned the instance properties as shown below.

| **Property Name** | **Required** |
| --- | --- |
| <code>EPset_ProjectedCRS.Name</code> | Yes |
| <code>EPset_ProjectedCRS.Description</code> |  |
| <code>EPset_ProjectedCRS.GeodeticDatum</code> |  |
| <code>EPset_ProjectedCRS.VerticalDatum</code> |  |
| <code>EPset_ProjectedCRS.MapProjection</code> |  |
| <code>EPset_ProjectedCRS.MapZone</code> |  |
| <code>EPset_ProjectedCRS.MapUnit</code> |  |
| <code>EPset_MapConversion.Eastings</code> | Yes |
| <code>EPset_MapConversion.Northings</code> | Yes |
| <code>EPset_MapConversion.OrthogonalHeight</code> | Yes |
| <code>EPset_MapConversion.XAxisAbscissa</code> | Yes |
| <code>EPset_MapConversion.XAxisOrdinate</code> | Yes |
| <code>EPset_MapConversion.Scale</code> | Yes |
Once applying these properties in IFC2X3, you will be required to define property sets for export in the default IFC exporter. This is data filled in a text file, which is referenced in the IFC export settings as shown below.

{{< wiki-image src="/media/revit-geolocation-settings.png" alt="Revit-geolocation-settings.png" mode="inline" >}}

The text file must contain the following listing.

<pre>PropertySet:	EPset_ProjectedCRS	I	IfcSite
	Name	Text	EPset_ProjectedCRS.Name
	Description	Text	EPset_ProjectedCRS.Description
	GeodeticDatum	Text	EPset_ProjectedCRS.GeodeticDatum
	VerticalDatum	Text	EPset_ProjectedCRS.VerticalDatum
	MapProjection	Text	EPset_ProjectedCRS.MapProjection
	MapZone	Text	EPset_ProjectedCRS.MapZone
	MapUnit	Text	EPset_ProjectedCRS.MapUnit

PropertySet:	EPset_MapConversion	I	IfcSite
	Eastings	Real	EPset_MapConversion.Eastings
	Northings	Real	EPset_MapConversion.Northings
	OrthogonalHeight	Real	EPset_MapConversion.OrthogonalHeight
	XAxisAbscissa	Real	EPset_MapConversion.XAxisAbscissa
	XAxisOrdinate	Real	EPset_MapConversion.XAxisOrdinate
	Scale	Real	EPset_MapConversion.Scale
</pre>

The downside with this is that this workaround only works with <code>Toposurface</code> objects. This means other disciplines will be required to create an arbitrary <code>Toposurface</code> object. This would allow geolocation to be correctly set, but creates an unnecessary shape representation of the <code>IfcSite</code>. This representation can be removed as follows.

<pre>$ ifcpatch -i input.ifc -r RemoveSiteRepresentation</pre>


> **Warning:** There is currently an inconsistency in naming convention in buildingSMART international [User Guide for Geo-referencing in IFC](https://buildingsmart-1xbd3ajdayi.netdna-ssl.com/wp-content/uploads/2020/02/User-Guide-for-Geo-referencing-in-IFC-v2.0.pdf). See [bsi forum thread](https://forums.buildingsmart.org/t/geolocation-standards-in-ifc2x3-and-ifc4/2329/16) for more information.

## IFC4 Geolocation
If your project is IFC4, you must set the properties shown below as instance properties to the <code>Project Information</code> object. There is no need to define any property sets for exports in the IFC export settings, as these parameters will be automatically detected. Currently <code>ProjectGlobalPositioning.CRSMapUnit</code> will be blank as it is not yet implemented in Revits exporter.

| **Property Name** | **Required** |
| --- | --- |
| <code>ProjectGlobalPositioning.CRSName</code> | Yes |
| <code>ProjectGlobalPositioning.CRSDescription</code> |  |
| <code>ProjectGlobalPositioning.CRSGeodeticDatum</code> |  |
| <code>ProjectGlobalPositioning.CRSVerticalDatum</code> |  |
| <code>ProjectGlobalPositioning.CRSMapProjection</code> |  |
| <code>ProjectGlobalPositioning.CRSMapZone</code> |  |
| <code>ProjectGlobalPositioning.CRSMapUnit</code> |  |
| <code>ProjectGlobalPositioning.Eastings</code> | Yes |
| <code>ProjectGlobalPositioning.Northings</code> | Yes |
| <code>ProjectGlobalPositioning.OrthogonalHeight</code> | Yes |
| <code>ProjectGlobalPositioning.XAxisAbscissa</code> | Yes |
| <code>ProjectGlobalPositioning.XAxisOrdinate</code> | Yes |
| <code>ProjectGlobalPositioning.Scale</code> | Yes |
## IFC2X3 and IFC4 geolocation patching
> **Warning:** If you do not patch your IFC file, your IFC file will not be correctly geolocated. This applies to both IFC2X3 and IFC4.

When this process is complete of adding parameters either to IFC2X3 Psets or to IFC4 CRS entities, it is assumed that these parameter values are identical to the parameters on the <code>Project Base Point</code> object.  This means that any exported IFC will contain a double-up of coordinates: once in the <code>IfcMapConversion</code> entity and another in the <code>Location</code> of the <code>IfcSite</code> entity. Sometimes, this coordinates are recorded in the <code>Location</code> of the <code>IfcBuilding</code> entity. For further reading of how these coordinates are exported, see [IFC Coordinate Reference Systems and Revit](https://thinkmoult.com/ifc-coordinate-reference-systems-and-revit.html) by Dion Moult.

To fix the double-up of coordinates, you will be required to patch the IFC file exported by Revit. You can patch it using the following <code>IFCPatch</code> recipe:

<pre>$ ifcpatch -i input.ifc -r ResetSpatialElementLocations -a IfcSite
$ ifcpatch -i input.ifc -r ResetSpatialElementLocations -a IfcBuilding
</pre>

A second issue is that the heights of your building storeys are now potentially doubly offset by the map conversion as well as their own absolute coordinates. This can be solved by offsetting all building storeys by a value equivalent to <code>-Orthogonalheight</code>. The following patch applies it, where <code>12345</code> is the <code>Orthogonalheight</code>.

<pre>$ ifcpatch -i input.ifc -r OffsetStoreyElevations -a &quot;-12345&quot;</pre>

## IFC2X3 and IFC4 geolocation reference information
IFC also stores some "reference point" geolocation data. This data includes the latitude and longitude in WGS84. This data is a double up of the more detailed CRS-specific coordinates created above, and is therefore superseded. However, in Revit, it is often incorrectly set, so it is important to ensure that it is correctly defined and corresponds to the CRS-specific coordinates, to prevent unnecessary misunderstandings.

To store the <code>RefLatitude</code> and <code>RefLongitude</code> correctly in the <code>IfcSite</code> object, the CRS coordinates must be converted into WGS84, or EPSG:4326 coordinates. [EPSG.io](https://epsg.io) is one online service that provides this, but no guarantee of correctness is provided.

Once converted, they may be entered in the format <code>{latitude},{longitude}</code> in the Revit location dialog as shown below. Once entered, press the <code>Search</code> button to confirm the selection.

{{< wiki-image src="/media/revit-geolocation-refcoords.png" alt="Revit-geolocation-refcoords.png" mode="inline" >}}

When the <code>Search</code> button is pressed, Revit will attempt to reverse geocode the coordinates. This is not guaranteed to result in a human address that corresponds to the legal address that represents the project entry. It is highly likely that you will be required to override this address. Simply replace the address, and ensure Revit doesn't save over it, as shown below.

{{< wiki-image src="/media/revit-geolocation-addressoverride.png" alt="Revit-geolocation-addressoverride.png" mode="inline" >}}

It is not currently possible to customise the export of the <code>RefElevation</code> attribute of the <code>IfcSite</code> object, but we must fix it as it is likely to be wrong. After calculating the conversion of your <code>OrthogonalHeight</code> in your chosen vertical datum to MSL (Mean Sea Level), you may patch it as follows, where <code>12345</code> is the value you want to set.

<pre>$ ifcpatch -i input.ifc -r SetRefElevation -a 12345</pre>

Revit does not by default export the <code>ElevationOfRefHeight</code> or <code>ElevationOfTerrain</code> attributes of the <code>IfcBuilding</code>.  This is not ideal, but not technically illegal, so it may be overlooked.
