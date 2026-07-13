---
title: "Project setup MicroMVD"
url: "/micromvds-for-exchange-requirements-project-setup-micromvd/"
aliases: ["/MicroMVDs_for_exchange_requirements/Project_setup_MicroMVD/", "/Project_setup_MicroMVD/"]
categories: ["Autodesk Revit", "BIMTester", "MicroMVD", "Model View Definitions (MVD)"]
lastmod: "2022-07-28T11:22:32Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure basic project metadata is set, as a minimum requirement for all BIM projects.

<pre>
Feature: Project setup

In order to ensure quality of the digital built environment
As a responsible digital citizen
We expect compliant OpenBIM deliverables

Scenario: Receiving a file
 * IFC data must use the &quot;{schema}&quot; schema

Scenario: Exempt files
 * The IFC file &quot;{file}&quot; is exempt from being provided
 * No further requirements are specified because &quot;{reason}&quot;

Scenario: Project metadata is organised and correct
 * The project must have an identifier of &quot;{guid}&quot;
 * The project name, code, or short identifier must be &quot;{name}&quot;
 * The project must have a longer form name of &quot;{long_name}&quot;
 * The project must be described as &quot;{description}&quot;
 * The project must be categorised under &quot;{object_type}&quot;
 * The project must contain information about the &quot;{phase}&quot; phase

Scenario: Project geometry is stored
 * The project must contain 3D geometry representing the shape of objects
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{file}</code> | project.ifc | The filename or path to any IFC file. |
| <code>{schema}</code> | IFC4 | The schema version. At the moment, these are likely to be either IFC4 or IFC2X3. |
| <code>{reason}</code> | we don't need it | You can write anything here to describe any reason. |
| <code>{guid}</code> | 28q3AgmxP5cepIweO5Of$o | This is a 22 character GlobalId for a particular IFC element. |
| <code>{name}</code> | 123FOO | A short project code or name used to uniquely identify the project, either specified by the client or the BIM author |
| <code>{long_name}</code> | 123 Foo Street, Tower B Redevelopment | The full project name used to uniquely identify the project, either specified by the client or the BIM author |
| <code>{description}</code> | Redesign of southwest atrium of Tower B to a two-storey space with new interior fitout | A description of what the project is about, to help clarify the project scope |
| <code>{object_type}</code> | Commercial | If the project is categorised as a particular arbitrary type, it may be described here. Example categories could be "Residential", "Retail", "Commercial", "Health" and "Defence". Alternatively, it could be categorised as "Civic", "Infrastructure". |
| <code>{phase}</code> | A | If the project is phased or staged, the phase or stage name may be placed here. |
## Software guides
| Icon | Software | Certified Version | Notes | Guides | Import | Export |
| --- | --- | --- | --- | --- | --- | --- |
| {{< wiki-image src="/media/icon-archi-cad.jpg" alt="Icon ArchiCAD.jpg" mode="inline" width="64" height="64" >}} | [ArchiCAD](/archicad/) | ArchiCAD 23 | ArchiCAD 23 | <code>GlobalId</code> cannot be overridden during export | [ArchiCAD project setup](/archicad-project-setup/) describes how to set these project attributes |  |
| {{< wiki-image src="/media/bonsai-logo.png" alt="Bonsai logo.png" mode="inline" width="64" height="64" >}} | [Bonsai](/bonsai/) | v0.0.200722 | v0.0.200722 |  |  |  |
| {{< wiki-image src="/media/icon-freecad.png" alt="Icon FreeCAD.png" mode="inline" >}} | [FreeCAD](/freecad/) | 0.19pre | 0.19pre | <code>GlobalId</code> cannot be overridden during export. The project <code>Name</code> is not maintained during import. |  |  |
| {{< wiki-image src="/media/icon-revit.png" alt="Icon Revit.png" mode="inline" width="64" height="64" >}} | [Revit](/autodesk-revit/) | Revit 2019.2 IFC 8/5/2020 | Revit 2019.2 IFC 8/5/2020 | During import, the project <code>GlobalId</code> is maintained, but all other metadata is lost. | [Revit project metadata](/revit-setup-for-openbim-revit-ifc-project-metadata/) describes how to set these project attributes |  |
| {{< wiki-image src="/media/tekla-logo.png" alt="Tekla-logo.png" mode="inline" width="64" height="64" >}} | [Tekla](/tekla/) |  |  |  |  |  |
