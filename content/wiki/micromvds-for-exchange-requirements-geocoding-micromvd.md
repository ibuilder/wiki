---
title: "Geocoding MicroMVD"
url: "/micromvds-for-exchange-requirements-geocoding-micromvd/"
aliases: ["/Geocoding_MicroMVD/", "/MicroMVDs_for_exchange_requirements/Geocoding_MicroMVD/"]
categories: ["BIMTester", "MicroMVD", "Model View Definitions (MVD)"]
lastmod: "2022-07-28T11:22:30Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure geolocation information is set.

<pre>
Feature: Geocoding

In order to relate the BIM model to a unique physical address
As a model recipient who is managing and organising a real estate portfolio
Address metadata must be assigned to the relevant BIM objects

Scenario: The site is tied to a physical building address
 * The site &quot;{guid}&quot; has a name of &quot;{name}&quot;
 * The site &quot;{guid}&quot; has a description of &quot;{description}&quot;
 * The site &quot;{guid}&quot; has a land title number of &quot;{land_title_number}&quot;
 * The site &quot;{guid}&quot; has the address &quot;{address_lines}&quot;
 * The site &quot;{guid}&quot; has a postal box of &quot;{postal_box}&quot;
 * The site &quot;{guid}&quot; is in the town &quot;{town}&quot;
 * The site &quot;{guid}&quot; is in the region &quot;{region}&quot;
 * The site &quot;{guid}&quot; has a post code of &quot;{post_code}&quot;
 * The site &quot;{guid}&quot; is in the country &quot;{country}&quot;
 * The site &quot;{guid}&quot; has an address description of &quot;{description}&quot;

Scenario: The building is tied to a physical building address
 * The building &quot;{guid}&quot; has a name of &quot;{name}&quot;
 * The building &quot;{guid}&quot; has a description of &quot;{description}&quot;
 * The building &quot;{guid}&quot; has the address &quot;{address_lines}&quot;
 * The building &quot;{guid}&quot; has a postal box of &quot;{postal_box}&quot;
 * The building &quot;{guid}&quot; is in the town &quot;{town}&quot;
 * The building &quot;{guid}&quot; is in the region &quot;{region}&quot;
 * The building &quot;{guid}&quot; has a post code of &quot;{post_code}&quot;
 * The building &quot;{guid}&quot; is in the country &quot;{country}&quot;
 * The building &quot;{guid}&quot; has an address description of &quot;{description}&quot;
</pre>

Note that if you are using the newer IFC 4.3 version, which includes <code>IfcFacility</code>, you may extend this MicroMVD with the following:

<pre>
Scenario: Infrastructure facilities have a physical name
 * The facility &quot;{guid}&quot; has a name of &quot;{name}&quot;
 * The facility &quot;{guid}&quot; has a description of &quot;{description}&quot;
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{guid}</code> | 28q3AgmxP5cepIweO5Of$o | This is a 22 character GlobalId for a particular IFC element. |
| <code>{name}</code> | Parliament House | For sites or buildings, this may refer to a standardised, short human reference that would be used to label it on a map, that is not the same as an address. For infrastructure facilities such as roads, bridges, marine facilities, and so on, this would be the road name, bridge name, or facility name. |
| <code>{description}</code> | Anything | If there is some particular nature of the site or building that requires description, it may be specified. |
| <code>{land_title_number}</code> | LP12345 | This is a standardised, legislative, government code for specifying a particular land parcel or building ID. |
| <code>{address_lines}</code> | 221B Baker Street | The full address lines, not using any short forms such as "St". If the address is split into multiple lines, separate each line with <code>\n</code>. |
| <code>{postal_box}</code> | ABC123 | The postal box code of the site or building, if it exists. |
| <code>{town}</code> | Sydney | The city or town name. |
| <code>{region}</code> | New South Wales | The region, state, province, or county. |
| <code>{country}</code> | Australia | The country. |
## Software guides
| Icon | Software | Certified Version | Notes | Guides | Import | Export |
| --- | --- | --- | --- | --- | --- | --- |
| {{< wiki-image src="/media/icon-archi-cad.jpg" alt="Icon ArchiCAD.jpg" mode="inline" width="64" height="64" >}} | ArchiCAD |  | ArchiCAD 23 | It is not possible to export a description associated with the address. Addresses can only be defined for the site, which is then assigned to both the site and the building. It is not possible to assign separate addresses to the site and the building. |  |  |
| {{< wiki-image src="/media/bonsai-logo.png" alt="Bonsai logo.png" mode="inline" width="64" height="64" >}} | [Bonsai](/bonsai/) | v0.0.200829 | v0.0.200829 |  |  |  |
| {{< wiki-image src="/media/icon-freecad.png" alt="Icon FreeCAD.png" mode="inline" >}} | [FreeCAD](/freecad/) |  |  |  |  |  |
| {{< wiki-image src="/media/icon-revit.png" alt="Icon Revit.png" mode="inline" width="64" height="64" >}} | [Revit](/autodesk-revit/) |  |  |  |  |  |
| {{< wiki-image src="/media/tekla-logo.png" alt="Tekla-logo.png" mode="inline" width="64" height="64" >}} | [Tekla](/tekla/) |  |  |  |  |  |
