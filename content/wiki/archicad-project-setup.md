---
title: "ArchiCAD project setup"
url: "/archicad-project-setup/"
aliases: ["/ArchiCAD_project_setup/"]
categories: ["Graphisoft Archicad"]
lastmod: "2021-07-18T19:59:45Z"
---

To meet the MVD requirement, prior to exporting your IFC4 file please setup Archicad as below.

Open the **Project Info** dialogue by navigating to **File** > **Info** > **Project Info...** and complete the following fields:

| MVD Variable | Archicad Attribute | Description |
| --- | --- | --- |
| <code>{name}</code> | Project Name | A short project code or name used to uniquely identify the project, either specified by the client or the BIM author |
| <code>{description}</code> | Project Description | A description of what the project is about, to help clarify the project scope |
| <code>{phase}</code> | Project Status | If the project is phased or staged, the phase or stage name may be placed here. |
Then open the **IFC Project Manager** dialogue by navigating to **File** > **Interoperability** > **IFC** > **IFC Project Manager** and complete the following:

1. In the top left window in this dialogue, click the topmost level of the hierarchy (with the IFC logo) and ensure the following five attributes (Name, Description, ObjectType, LongName, Phase) are checked in the right window.
1. The variable <code>{long_name}</code> is represented in the right window of this dialogue by the Archicad attribute **LongName**. In here add the full project name used to uniquely identify the project, either specified by the client or the BIM author.
1. The variable <code>{object_type}</code> is represented also in the right window of this dialogue by the Archicad attribute **ObjectType**. In here add the category of project type such as "Residential", "Retail", "Commercial", "Health" and "Defence". Alternatively, it could be categorised as "Civic", "Infrastructure".

**NOTE:** The variable <code>{guid}</code> also appears in the right window of this dialogue by the Archicad attribute **GlobalId**. This is greyed and is not able to be modified. Refer to [GRAPHISOFT Help Center](https://helpcenter.graphisoft.com/user-guide/89335/#XREF_83086_How_to_Control) for further information.
