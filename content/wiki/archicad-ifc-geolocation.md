---
title: "ArchiCAD IFC geolocation"
url: "/archicad-ifc-geolocation/"
aliases: ["/ArchiCAD_IFC_geolocation/", "/ArchiCAD_geolocation/"]
categories: ["Graphisoft Archicad"]
lastmod: "2021-09-20T08:04:01Z"
---

This guide describes the process to meet the IFC geolocation MVD requirement from **Archicad (versions 23 and 24)**.

Note that currently, only the IFC4 schema meets the MVD requirement by locating the data in specific geolocation entities. While IFC 2x3 doesn't include these entities, it does still export the data, but only into two property sets called 'ePSet_ProjectedCRS' and 'ePSet_MapConversion'.

Firstly you will need to locate the 'latitude' and 'longitude' position of the project (at Archicad's origin). Open the **Project Location** dialogue by navigating to **Options** > **Project Preferences** > **Project Location...** and completing the following fields:

| MVD Variable | Project Location Attribute | Description |
| --- | --- | --- |
| <code>{latitude_longlat}</code> | Latitude | The latitude of the project (be sure to choose North(ern) or South(ern) hemisphere depending on your project location) |
| <code>{longitude_longlat}</code> | Longitude | The longitude of the project (be sure to choose East(ern) or West(ern) hemisphere depending on your project location) |
| <code>{elevation_number}</code> | Altitude (Sea Level) | The elevation of the project in either meters or decimal feet |
Confirm the data you entered is correct by clicking 'Show in Google Maps' and reviewing the location in your browser.

Next, it is necessary to place an Archicad **Survey Point** object in your project. This must be located at a known point. After placing and while the **Survey Point** is selected, open the **Object Selection Settings** dialogue. Under the **Survey Point Settings** tab, navigate to **Geo Referencing Map...** and enter corresponding values from the below table.

| MVD Variable | Survey Point Attribute | Description |
| --- | --- | --- |
| <code>{coordinate_reference_name}</code> | Name | The name of the CRS |
| <code>{description_value}</code> | Description | The description of the CRS |
| <code>{geodetic_datum_coordinate_reference_name}</code> | Geodetic Datum | The geodetic datum of the CRS |
| <code>{vertical_datum_coordinate_reference_name}</code> | Vertical Datum | The vertical datum of the CRS |
| <code>{map_projection_coordinate_reference_name}</code> | Map Projection | The map projection of the CRS |
| <code>{map_zone_coordinate_reference_name}</code> | Map Zone | The map zone of the CRS |
| <code>{eastings_number}</code> | Eastings | The eastings of the model must be offset by this value to derive its global coordinates |
| <code>{northings_number}</code> | Northings | The northings of the model must be offset by this value to derive its global coordinates |
| <code>{height_number}</code> | Orthogonal Height | The height of the model must be offset by this value to derive its global coordinates |
| <code>{rotation_number}</code> | X Axis Abscissa, X Axia Ordinate | Using a Polar Coordinate calculator, transform the required project north rotation to 3 o-clock into the **X Axis Abscissa** and **X Axia Ordinate**. Clockwise rotation clockwise is negative, anti-clockwise is positive |
| <code>{scale_number}</code> | Scale | The model must be scaled along the horizontal axis by value to derive its global coordinates |
