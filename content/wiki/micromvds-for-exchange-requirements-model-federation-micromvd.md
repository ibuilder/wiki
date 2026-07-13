---
title: "Model federation MicroMVD"
url: "/micromvds-for-exchange-requirements-model-federation-micromvd/"
aliases: ["/MicroMVDs_for_exchange_requirements/Model_federation_MicroMVD/", "/Model_federation_MicroMVD/"]
categories: ["BIMTester", "MicroMVD", "Model View Definitions (MVD)"]
lastmod: "2022-07-28T11:22:31Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure IFC elements belong to the correct IFC class.

<pre>
Feature: Model federation

In order to coordinate multiple models that are produced separately
For all model coordinators and recipients of the final built environment
The location of each model&#x27;s origin point must be specifically set to a coordinated value

Scenario: Ensure that an agreed datum for the project is in the right location
 * There is a datum element &quot;{guid}&quot; as an &quot;{ifc_class}&quot;
 * The element &quot;{guid}&quot; has a global easting, northing, and elevation of &quot;{number}&quot;, &quot;{number}&quot;, and &quot;{number}&quot; respectively
 * The element &quot;{guid}&quot; has a local X, Y, and Z coordinate of &quot;{number}&quot;, &quot;{number}&quot;, and &quot;{number}&quot; respectively
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{guid}</code> | 28q3AgmxP5cepIweO5Of$o | This is a 22 character GlobalId for a particular IFC element. |
| <code>{ifc_class}</code> | IfcSite | This case insensitive text value must correspond to the full name of an IFC class. It is recommended for the purposes of this MicroMVD that this should be an IfcSite, or IfcBuilding, or other spatial element that all other objects are related to. |
| <code>{number}</code> | 42 | Any valid number. Note that eastings, northings, and elevations, are not angular measures, such as latitude and longitude, but are instead based on a coordinate reference system. If global coordinates are specified, the element will be checked with its map conversion applied. If local coordinates are specified, CRS map conversions will not be specified. |
## Software guides
| Icon | Software | Certified Version | Notes | Guides | Import | Export |
| --- | --- | --- | --- | --- | --- | --- |
| {{< wiki-image src="/media/icon-archi-cad.jpg" alt="Icon ArchiCAD.jpg" mode="inline" width="64" height="64" >}} | ArchiCAD | ArchiCAD 23 | ArchiCAD 23 | See the [Geolocation MicroMVD](/micromvds-for-exchange-requirements-geolocation-micromvd/) for caveats related to federating geolocated data. |  |  |
| {{< wiki-image src="/media/bonsai-logo.png" alt="Bonsai logo.png" mode="inline" width="64" height="64" >}} | [Bonsai](/bonsai/) | v0.0.200829 | v0.0.200829 |  |  |  |
| {{< wiki-image src="/media/icon-freecad.png" alt="Icon FreeCAD.png" mode="inline" >}} | [FreeCAD](/freecad/) | 0.19pre | 0.19pre | See the [Geolocation MicroMVD](/micromvds-for-exchange-requirements-geolocation-micromvd/) for caveats related to federating geolocated data. |  |  |
| {{< wiki-image src="/media/icon-revit.png" alt="Icon Revit.png" mode="inline" width="64" height="64" >}} | [Revit](/autodesk-revit/) | Revit 2020.2 IFC 8/5/2020 | Revit 2020.2 IFC 8/5/2020 | Note: see the [Revit geolocation](/revit-setup-for-openbim-revit-ifc-geolocation/) guide for caveats related to checking global coordinates | [IFC Coordinate Reference Systems and Revit](https://thinkmoult.com/ifc-coordinate-reference-systems-and-revit.html) describes the relationship between Revit coordinates and IFC coordinates |  |
| {{< wiki-image src="/media/tekla-logo.png" alt="Tekla-logo.png" mode="inline" width="64" height="64" >}} | [Tekla](/tekla/) |  |  |  |  |  |
