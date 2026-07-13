---
title: "Geolocation MicroMVD"
url: "/micromvds-for-exchange-requirements-geolocation-micromvd/"
parent: "/micromvds-for-exchange-requirements/"
aliases: ["/Geolocation_MicroMVD/", "/MicroMVDs_for_exchange_requirements/Geolocation_MicroMVD/"]
categories: ["BIMTester", "MicroMVD", "Model View Definitions (MVD)"]
lastmod: "2022-07-28T11:22:30Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure geolocation information is set.

<pre>
Feature: Geolocation

In order to query data in real world coordinates
As a recipient expecting to integrate BIM and GIS datasets
Geolocation data must be stored correctly in received files

Scenario: Geometry is georeferenced to a coordinate reference system
 * There must be at least one &quot;IfcSite&quot; element
 * The project must have coordinate reference system data
 * The name of the CRS must be &quot;{coordinate_reference_name}&quot;
 * The description of the CRS must be &quot;{value}&quot;
 * The geodetic datum must be &quot;{coordinate_reference_name}&quot;
 * The vertical datum must be &quot;{coordinate_reference_name}&quot;
 * The map projection must be &quot;{coordinate_reference_name}&quot;
 * The map zone must be &quot;{coordinate_reference_name}&quot;
 * The map unit must be &quot;{unit}&quot;

Scenario: Local coordinate systems are specified relative to a global system
 * The project must have coordinate transformations to convert from local to global coordinates
 * The eastings of the model must be offset by &quot;{number}&quot; to derive its global coordinates
 * The northings of the model must be offset by &quot;{number}&quot; to derive its global coordinates
 * The height of the model must be offset by &quot;{number}&quot; to derive its global coordinates
 * The model must be rotated clockwise by &quot;{number}&quot; to derive its global coordinates
 * The model must be scaled along the horizontal axis by &quot;{number}&quot; to derive its global coordinates

Scenario: A true north rotation of the project origin is provided for convenient reference
 * The model must be rotated clockwise by &quot;{number}&quot; for true north to point up

Scenario: Global coordinates of the site origins are provided for convenient reference
 * The site &quot;{guid}&quot; has a longitude of &quot;{longlat}&quot;
 * The site &quot;{guid}&quot; has a latitude of &quot;{longlat}&quot;
 * The site &quot;{guid}&quot; has an elevation of &quot;{number}&quot;
 * The site &quot;{guid}&quot; must be coincident with the project origin 
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{value}</code> | Anything | Any arbitrary value if it adds meaning required by the project. |
| <code>{coordinate_reference_name}</code> | EPSG:7856 | If this exists in the EPSG registry, the EPSG identifier must be provided. If not, it may be arbitrarily specified as a custom text name. |
| <code>{unit}</code> | Metre | This case insensitive text value may contain an optional [prefix](https://standards.buildingsmart.org/IFC/DEV/IFC4_3/RC1/HTML/link/ifcsiprefix.htm) followed by an [SI unit](https://standards.buildingsmart.org/IFC/DEV/IFC4_3/RC1/HTML/link/ifcsiunitname.htm) or an [converted unit](https://standards.buildingsmart.org/IFC/DEV/IFC4_3/RC1/HTML/link/ifcconversionbasedunit.htm) |
| <code>{number}</code> | 42.12 | Any numerical value you expect for a particular attribute or property. |
| <code>{longlat}</code> | 42.12 | Either a longitude or latitude expressed in a decimal degrees. |
| <code>{guid}</code> | 28q3AgmxP5cepIweO5Of$o | This is a 22 character GlobalId for a particular IFC element. |
## Software guides
| Icon | Software | Certified Version | Notes | Guides | Import | Export |
| --- | --- | --- | --- | --- | --- | --- |
| {{< wiki-image src="/media/icon-archi-cad.jpg" alt="Icon ArchiCAD.jpg" mode="inline" width="64" height="64" >}} | ArchiCAD | ArchiCAD 23 | ArchiCAD 23 | You cannot export a unit for the coordinate reference system. Also, when exporting to IFC, it may apply the true north rotation, but retain the rotation in the geolocation properties, thus effectively defining the rotation twice. This leads to an incorrectly geolocated model which needs to be patched. Upon importing such a file with a doubly defined rotation, the map conversion seems to be ignored. This can cause problems with correctly geolocated files coming from other software. | [ArchiCAD geolocation](/archicad-ifc-geolocation/) describes how to set these attributes |  |
| {{< wiki-image src="/media/bonsai-logo.png" alt="Bonsai logo.png" mode="inline" width="64" height="64" >}} | [Bonsai](/bonsai/) | v0.0.200829 | v0.0.200829 |  |  |  |
| {{< wiki-image src="/media/icon-freecad.png" alt="Icon FreeCAD.png" mode="inline" >}} | [FreeCAD](/freecad/) | 0.19pre | 0.19pre | When exporting, the true north rotation is incorrectly rotated by 90 degrees. When importing, the units of the site reference elevation may be incorrectly converted. |  |  |
| {{< wiki-image src="/media/icon-revit.png" alt="Icon Revit.png" mode="inline" width="64" height="64" >}} | [Revit](/autodesk-revit/) | Revit 2020.2 IFC 8/5/2020 | Revit 2020.2 IFC 8/5/2020 | During import, all geolocation information is lost. During export, workarounds are required using external patching tools to achieve the desired outcome. | [Revit geolocation](/revit-setup-for-openbim-revit-ifc-geolocation/) describes how to set these attributes |  |
| {{< wiki-image src="/media/tekla-logo.png" alt="Tekla-logo.png" mode="inline" width="64" height="64" >}} | [Tekla](/tekla/) |  |  |  |  |  |
