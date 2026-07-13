---
title: "Element classes MicroMVD"
url: "/micromvds-for-exchange-requirements-element-classes-micromvd/"
parent: "/micromvds-for-exchange-requirements/"
aliases: ["/Element_classes_MicroMVD/", "/MicroMVDs_for_exchange_requirements/Element_classes_MicroMVD/"]
categories: ["BIMTester", "MicroMVD", "Model View Definitions (MVD)"]
lastmod: "2022-07-28T11:22:29Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure [Industry Foundation Classes (IFC)](/ifc-industry-foundation-classes/) elements belong to the correct IFC class.

<pre>
Feature: Element classes

In order to correctly identify objects
As any interested stakeholder filtering objects for a particular purpose
All IFC elements must belong to the appropriate IFC class

Scenario: Ensure all IFC type elements use the correct IFC class
 * The element &quot;{guid}&quot; is an &quot;{ifc_class}&quot;
 * The element &quot;{guid}&quot; is an &quot;{ifc_class}&quot; only
 * The element &quot;{guid}&quot; is further defined as a &quot;{predefined_type}&quot;
 * The element &quot;{guid}&quot; should not exist because &quot;{reason}&quot;
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{guid}</code> | 28q3AgmxP5cepIweO5Of$o | This is a 22 character GlobalId for a particular IFC element. |
| <code>{ifc_class}</code> | IfcWall | This case insensitive text value must correspond to the full name of an IFC class. |
| <code>{predefined_type}</code> | BEAM | This case insensitive text value must correspond to the predefined type of an IFC class, or a custom object type. |
| <code>{reason}</code> | we don't need it | You can write anything here to describe any reason. |
## Software guides
| Icon | Software | Certified Version | Notes | Guides | Import | Export |
| --- | --- | --- | --- | --- | --- | --- |
| {{< wiki-image src="/media/logo-graphisoft-archicad.png" alt="Logo-graphisoft-archicad.png" mode="inline" width="64" height="64" >}} | [ArchiCAD](/archicad/) | ArchiCAD 23 | ArchiCAD 23 |  |  |  |
| {{< wiki-image src="/media/bonsai-logo.png" alt="Bonsai logo.png" mode="inline" width="64" height="64" >}} | [Bonsai](/bonsai/) | v0.0.200829 | v0.0.200829 |  |  |  |
| {{< wiki-image src="/media/icon-freecad.png" alt="Icon FreeCAD.png" mode="inline" >}} | [FreeCAD](/freecad/) | 0.19pre | 0.19pre |  |  |  |
| {{< wiki-image src="/media/icon-revit.png" alt="Icon Revit.png" mode="inline" width="64" height="64" >}} | [Revit](/autodesk-revit/) | Revit 2020.2 IFC 8/5/2020 | Revit 2020.2 IFC 8/5/2020 | For import, opening an IFC does not retain any element class information. Linking IFCs do retain this information. For export, some Revit family categories have restrictions on which element classes they can be exported to, and the user cannot override it. | Refer to [Revit and IFC classes](/revit-setup-for-openbim-revit-and-ifc-classes/) |  |
| {{< wiki-image src="/media/tekla-logo.png" alt="Tekla-logo.png" mode="inline" width="64" height="64" >}} | [Tekla](/tekla/) |  |  |  |  |  |
