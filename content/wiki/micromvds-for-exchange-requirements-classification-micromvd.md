---
title: "Classification MicroMVD"
url: "/micromvds-for-exchange-requirements-classification-micromvd/"
parent: "/micromvds-for-exchange-requirements/"
aliases: ["/Classification_MicroMVD/", "/MicroMVDs_for_exchange_requirements/Classification_MicroMVD/"]
categories: ["BIMTester", "MicroMVD", "Model View Definitions (MVD)"]
lastmod: "2022-07-28T11:22:29Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure classification system standards are correctly applied.

For guidance on what values should be filled in for standardised classification systems, refer to [IFC classifications](/ifc-industry-foundation-classes-ifc-classifications/).

<pre>
Feature: Classification

For BIM objects to be filtered and categorised in facility management system
As someone who needs to catalogue BIM data in a structured and organised manner
Classification systems data must be assigned to each relevant element

Scenario: The appropriate classification systems are referenced in the model
 * The classification &quot;{name}&quot; must be used
 * The classification &quot;{name}&quot; is published by &quot;{source}&quot;
 * The classification &quot;{name}&quot; is the edition &quot;{edition}&quot; on &quot;{edition_date}&quot;
 * The classification &quot;{name}&quot; has the description &quot;{description}&quot;
 * The classification &quot;{name}&quot; is referenced by the website &quot;{location}&quot;
 * The classification &quot;{name}&quot; has a hierarchy denoted by the tokens &quot;{tokens}&quot;

Scenario: The relevant elements are assigned to the classification system
 * The element &quot;{guid}&quot; is classified as a &quot;{identification}&quot; with name &quot;{reference_name}&quot;
</pre>

Note that for IFC2X3, the following rules will not apply, as the data cannot be stored in IFC2X3.

<pre>
 * The classification &quot;{name}&quot; has the description &quot;{description}&quot;
 * The classification &quot;{name}&quot; is referenced by the website &quot;{location}&quot;
 * The classification &quot;{name}&quot; has a hierarchy denoted by the tokens &quot;{tokens}&quot;
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{guid}</code> | 28q3AgmxP5cepIweO5Of$o | This is a 22 character GlobalId for a particular IFC element. |
| <code>{name}</code> | Uniclass 2015 | The name of the classification system, taken from the standard list if it exists. |
| <code>{source}</code> | RIBA Enterprises Ltd | The source or publisher of the classification system, taken from the standard list if it exists. |
| <code>{edition}</code> | January 2020 | Classifications are often revised, this refers to the standard edition name, taken from the standard list if it exists. |
| <code>{edition_date}</code> | 2020-02-07 | A YYYY-MM-DD value of when the edition was released. |
| <code>{description}</code> | Uniclass 2015 is a unified classification for the UK industry covering all construction sectors. | The official description of the classification system, taken from the standard list if it exists. |
| <code>{location}</code> | https://toolkit.thenbs.com/articles/classification | The official website to refer to the classification online, taken from the standard list if it exists. |
| <code>{tokens}</code> | ["_"] | A JSON list of of all of the separating tokens which denote hierarchy in the classification system, taken from the standard list if it exists. |
| <code>{identification}</code> | Co_20_10_60 | A single classification reference identification for the particular classification system, taken from the standard list if it exists. |
| <code>{reference_name}</code> | Governmental complexes | A single classification reference name for the particular classification system, taken from the standard list if it exists. |
## Software guides
| Icon | Software | Certified Version | Notes | Guides | Import | Export |
| --- | --- | --- | --- | --- | --- | --- |
| {{< wiki-image src="/media/icon-archi-cad.jpg" alt="Icon ArchiCAD.jpg" mode="inline" width="64" height="64" >}} | ArchiCAD |  | ArchiCAD 23 | Some work is required to set up the export, but it is possible. However, the description, location, and reference tokens for the <code>IfcClassification</code> cannot be exported. It should also be noted that the Graphisoft classification XMLs tend to store the location data in the source field, which is incorrect. |  |  |
| {{< wiki-image src="/media/bonsai-logo.png" alt="Bonsai logo.png" mode="inline" width="64" height="64" >}} | [Bonsai](/bonsai/) | v0.0.200829 | v0.0.200829 |  |  |  |
| {{< wiki-image src="/media/icon-freecad.png" alt="Icon FreeCAD.png" mode="inline" >}} | [FreeCAD](/freecad/) |  |  |  |  |  |
| {{< wiki-image src="/media/icon-revit.png" alt="Icon Revit.png" mode="inline" width="64" height="64" >}} | [Revit](/autodesk-revit/) |  |  |  |  |  |
| {{< wiki-image src="/media/tekla-logo.png" alt="Tekla-logo.png" mode="inline" width="64" height="64" >}} | [Tekla](/tekla/) |  |  |  |  |  |
