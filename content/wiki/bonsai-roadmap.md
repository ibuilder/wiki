---
title: "Bonsai Roadmap"
url: "/bonsai-roadmap/"
parent: "/bonsai/"
aliases: ["/BlenderBIM_Add-on/BlenderBIM_Add-on_Roadmap/", "/BlenderBIM_Add-on_Roadmap/", "/blenderbim-add-on-blenderbim-add-on-roadmap/"]
categories: ["BIM Collaboration Format (BCF)", "Blender", "Bonsai"]
lastmod: "2023-08-29T02:18:48Z"
---

The objective of [Bonsai](/bonsai/) project is to provide a complete free software workflow in an [OpenBIM](/openbim/) production pipeline. The ability to work from early feasibility and concept phase, project coordination, detailed design, fabrication & construction, facility management and building maintenance, post-occupancy evaluation, and tear-down.

In addition to providing features equivalent to existing proprietary software, the new tools will be different in two ways. First, they will be highly modular, allowing users to mix and match to create their own pipelines tailored to their needs, and easily modify or extend the pipeline if it does not suit their needs. The user should have full control over their tools. Secondly, the tools will uphold the highest standards possible of open data standards, exchange, and interoperability conventions, allowing us to integrate data across disciplines to make wiser decisions in the design and management of the built environment.

This is an ambitious goal, and some of these responsibilities lie outside the scope of the Blender package. The end-result will be a toolkit of Unix-style utilities which offer all of the required functionality, some of which integrate into the Blender interface, and others which will not (a "Swiss Army Knife of OpenBIM Utilities"). A roadmap is provided here for those who want to know where the project is headed.

## History
A small commercial building project was first designed in [Blender](/blender/). We were then faced with the task of remodeling it in [Autodesk Revit](/autodesk-revit/). We figured it would be easier to build an entire BIM application and construction documentation tool from scratch rather than face the pain of remodeling it in [Revit](/autodesk-revit/). It turned out that it was.

A day later, the project began on [August 29, 2019](https://github.com/IfcOpenShell/IfcOpenShell/commit/e9649a52177bc5895a1de470acd0dea8166cbaf3), with 83 lines of code that demonstrated that Blender geometry could be exported into [Industry Foundation Classes (IFC)](/ifc-industry-foundation-classes/).

The first packaged build for the public, changing it from an experimental set of scripts into a distributed package was done a month and a half later, on October 13, 2019. A week later, we were surprised to learn that our package was being used to visualise data from a compactor machine being used to build a highway. This was the first tangible evidence that Bonsai had great potential.

Over the next nine months, the small building went from concept to detailed design to construction to handover. As the small building progressed, new capabilities were added to Bonsai on a daily basis to meet our evolving needs.

In parallel, we started supporting a large multidisciplinary project with stringent BIM requirements. To support the team members, we built a suite of BIM tools. These tools were like a Swiss army knife of BIM utilities which could be launched from Bonsai environment.

The heart of any open source software project is a vibrant community. On 4 February 2020, the Open Source Architecture (OSArch) community forum and chat group were launched with a mission to "create a built environment with free software, increased transparency, and a more ethical approach". A wiki was created as a knowledge base related to open source software in the AEC industry. We were surprised to discover that more than 100 FOSS were already available for the AEC industry. Monthly information sharing sessions and a news portal related to FOSS in the AEC industry were set up.

Soon, new features in Bonsai were being driven by not only the problems that we were facing, but also by the problems faced by members of the community. Members of the community play an important role of battle-testing Bonsai and identifying bugs to be fixed.

In September 2020, the 1,000th issue was tracked on the issue tracker.

In October 2020, Bonsai and its related utilities won the prestigious 2020 Technology Award by buildingSMART International.

In December 2020, the OpenSourceBIM OpenCollective was created as a fiscal host to start collecting donations.

In January 2021, Bonsai was rewritten, making three major changes.

The first change made Bonsai native IFC, removing all Blender information from the database. Blender was still used as a user interface, but portions of the code could now be ported to work with other user interfaces such as FreeCAD.

The second change put a wrapper around the IfcOpenShell library to convert it into an API, simplifying some of the complexity of the IFC specification. This makes it easy for developers to build apps on top of IfcOpenShell, expanding the ecosystem of native IFC applications.

The third change was to split Bonsai code into almost 40 modules. This makes it easy for new developers to add code because they can now concentrate on a single module.

Prior to these changes, Bonsai features were primarily focused on architects (the "A" of AEC). Once these changes were in place, a small team from the community started adding features related to structural analysis (the "E" of AEC) and another small team started adding features related to scheduling and costing (the "C" of AEC).

In March 2021, Bonsai, under IfcOpenShell, [joined the OpenCAx umbrella for Google Summer of Code](https://osarch.org/2021/06/09/google-summer-of-code-students-announced-for-opencax/) for the first time. Artur Tomczak helped develop the initial prototypes of IDS, which would later be released as a buildingSMART standard in 2022. Prabhat Singh built the first BCF-XML 3.0 and OpenCDE libraries.

In May 2021, [Bonsai received a 15,000 USD Epic MegaGrant](https://osarch.org/2021/05/25/epic-megagrants-funding-awarded-to-blenderbim-add-on/). This was split across three developers, Johan Luttun, Thomas Krijnen, and Dion Moult to develop three features: an automated geometry test suite to maximise long-term stability, a Python-accessible 2D drawing engine, and ability to author 80% of all IFC schema capabilities. This work took roughly a year.

In January 2022, the 2,000th issue was tracked in the issue tracker.

In March 2022, the second GSoC event took place, with Martina Jakubowska building the initial prototypes of IfcSverchok.

By May 2022, as part of the Epic Megagrant timeline, IfcOpenShell had upgraded to v0.7.0, a new basic drawing system with smart references was released, and Bonsai had more coverage of the IFC schema than any other tool in the industry, including parametric 4D and 5D, and basic MEP features.

In August 2022, the IfcOpenShell Github repository surpassed 1,000 stars.

In November 2022, the IfcOpenShell and Bonsai websites were rebranded under a common brand, and funding targets were set in the OpenSourceBIM fiscal host, aiming for 500USD per month. This target was quickly achieved.

In March 2023, Andre was fully sponsored to work on Bonsai as a developer.

In March 2023, the third GSoC event took place, with Riley Wong building undo / redo, save, IFC conversion, and upgrading the BrickSchema interface.

In July 2023, Thomas received a Cesium Ecosystem Grant to work on Cesium integration.

## Version 0.0.X
The version 0.0.X series are rapidly changing, alpha-quality software. The X will be substituted with the current date. This is the current state of the project.

At this stage, Bonsai is very new, but we encourage early adopters and people who want to push the boundaries of what's possible in BIM. While portions of the software are more stable and mature, there are other portions of the software that are still in the "experimental stages". Users should expect bugs, and changing behaviour. Users are highly encouraged to try to push the tool and report bugs. 

The primary objective during this version series is to build features, find some early adopters, start a community, and make it possible to achieve productive, commercial-grade output. We're going to release early, release often, and don't mind if we break a few things along the way, so long as we move towards a better future. During this, we hope to demonstrate to the industry what free software is capable of, and build the world's most advanced OpenBIM authoring package.

For the first year, priority was given to developing features that allowed my colleagues and me to resolve BIM-related problems that we faced on a daily basis, dealing with a wide variety of construction projects. Now, with that foundation largely in place, we are turning our attention to adding features that will allow us to replace proprietary software in our workflow.

## Version 0.X.X
The first 0.X.X release will mean that most of the basic features are there, and we know we can produce output. The objective then shifts to polishing, increased testing, improving stability, improving usability, writing tutorials and documentation, and optimisation. We also aim to battle test the package in as many commercial projects as possible, and build up small teams of people heavily using Bonsai and IfcOpenShell suite of tools. This is loosely scheduled for 2024.

By this stage, there will also be increasingly tangible costs involved, such as server costs for hosting, build servers, asset libraries, and so on. This is only set to grow, and so there needs to be an added focus on a community development model. For the community to sustainably grow and to support free software developer participation, models for funding developer resources will need to be developed. The concept for this is not commercial, but similar to the Blender Foundation approach, or KDE Community Fund approach. It could also be based on free software payment initiatives like Liberapay.

## Version X.X.X
The first version 1.0.0, and subsequent releases, will mean that Bonsai is now a stable product. A company should now be able to replace their entire proprietary toolset with free software. A bright future for the industry where we can now easily collaborate with high quality open data standards and a culture of openness and transparency.

The priority is now placed on optimising the workflow to create better buildings. To improve sustainable design, more beautiful buildings, happier places, with informed quantitative and qualitative decision-making that spans between GIS, BIM, environmental sciences, design psychology, and more.

## The current roadmap
Right from the beginning, the development priorities for Bonsai have been driven by solving immediate user problems. It has never been the objective of Bonsai to complete a checklist of features to compete with a specific proprietary software application. This is why the current feature set of Bonsai partially overlaps the capabilities of many proprietary software packages and in some cases has features not found in any other software. Addressing user's pain points will continue to drive the future development direction of Bonsai. Users have always been, and always will be, at the heart of Bonsai. If you are a user and have a problem, let us know and you could help to determine a future enhancement to Bonsai. If you are also a Python programmer, you could add code yourself.

Bonsai is divided into a number of decoupled modules. The intention is that for the project to grow, different developers may take ownership over the development of a module, allowing for a way to distribute the work. The development of all modules must, however, follow certain core rules of system architecture, which govern how everything interoperates together into a coherent package, both within, and external to the Blender environment.

There are currently nearly 40 distinct modules that comprise Bonsai. Ones that have known initiatives are listed below. Each initiative contains the name of the developer who is leading that initiative.

Note: this is working document. Changes are expected.

### core architecture
Note: this is not a module, but spans across the entire project.

- The system is being fully decoupled into ifcopenshell.api + bonsai.bim.module. This still needs documentation and representation adding interfaces + adapters. (Moult)
- A prototype of a client-server model for distributed, multi-user, cross-application simultaneous authoring needs to be built. (Moult)

### aggregate
- You cannot currently author element aggregates. (Moult)

### bcf
- GSoC student prabhat01 is undertaking the challenge to add support for BCF-API 3.0. (prabhat01, Moult)

### bimtester
- There are tests underway to make BIMTester accept the new upcoming IDS specification (aothms, Moult)

### bsdd
- Note: this module does not currently exist. A UI needs to be built to interact with the new bSDD library (Moult)

### cobie
- There are early discussions to develop all of the capabilities required for the potential upcoming FM Handover related standards, including conversion from IFC SPF to Spreadsheet ML, validation of FM deliverables, sample files, relating authoring tools, and utilities for portions of the FM workflow (e.g. site technicians reporting data). It probably won't be called COBie, though, so this module will be renamed to "fm". (Moult)

### cost
- Work has started (yassineSIGMA, iosvarms, AldoMontanari, Moult)
- Expand / contract all in tree feature
- Export to OOXML spreadsheet
- Export to CSV
- Implement a schedule of rates
- Show a final cost for the entire schedule depending on the type of schedule
- Show an indicator of calculated vs explicit costs
- Support classifications for cost items
- Restrict quantities to a single type once defined
- Support defining a unit of currency for the project
- Support detecting the unit of quantity
- Add support for approval assignment to cost schedules (requires development of approval module)
- Add support for actor assignment to cost schedules
- Assign processes to cost items (and type equivalents for schedules of rates)
- Assign resources to cost items (and type equivalents for schedules of rates)

### drawing
- There is an ambitious plan to rebuild this using IfcConvert as the core, but progress is slow. Here's an extended list of [planned functionality](https://github.com/IfcOpenShell/IfcOpenShell/issues/1153). Please considering funding these features.  Details about the funding campaign can be found [here](https://github.com/IfcOpenShell/IfcOpenShell/issues/1153#issuecomment-743405481) (aothms, Moult)

### geometry
- We need to solve how to edit portions of the representation tree. (Moult)

### io
- Firstly, the import / export needs to be refactored into a module to improve maintainability. (Moult)
- For imports of large files, we should give the user the option to filter by spatial hierarchy. This promotes highly responsive, query-based editing rather than monolithic models. (Moult)
- Sometimes, IfcOpenShell has a runaway process when handling meshes. This includes faceted breps, triangulated face sets, and tessellations. Bypassing OCC and parsing these meshes natively is vital to ensuring practical, scalable, mesh based workflows. (Moult)
- User friendly asset imports, especially from project libaries, and product types, is required to turn Bonsai into a proper authoring tool. (Moult)

### project
- Support for authoring project libraries needs to be made explicit in the UI. This is a necessary problem to solve, to build a mature authoring environment, otherwise we cannot expect people to rebuild all their BIM assets from scratch on every project. (Moult)

### resource
- Support type resources
- Assign resource to actors
- Assign resources to groups
- Assign resources to controls like calendars
- Assign resources to products
- Assign resources to processes like tasks
- Assign resource relationships to both products (done) and actors
- Support related resources upon "copying" baseline schedules
- Assign documents to resources
- Assign psets to resources

### sequence
- Work has started: Usecases and UI to author entities related to Construction Sequencing and Resources (yassineSIGMA, Moult)
- Preserve P6 ObjectIds and IFC GlobalIds to do smart relinking upon P6 or IFC updates
- Sort task tree by start date
- Support import of MS Project - Ongoing (Missing: LagTime, calendar assignement to tasks, calendar exception times, Resources) 
- Support import of LibreProject
- Support document association to tasks
- Support recurring task time tasks
- Support task typing
- Support tasks types and inclusion in a project library
- Assign task classification references
- Support Duplicating workschedule ( baselines )
- Support Actual vs Planned

### structural
- Work has started to have full support for structural authoring (Jesusbill)

**Structural Analysis Model**
- Add/Edit/Remove model: OK
- Assign/Unassign members and connections to model: OK
- Assign Load Cases and Load Combinations to model: X
- Batch operations of Assign/Unassign members and connections to model: X

**Structural Members**
- Add/Edit/Remove members: OK (standard BBIM functionality for IfcProduct)
- Edit Local Coordinate System for curve members: OK
- Edit Local Coordinate System for surface members: X
- Assign MaterialProfileSet for surface members: OK
- Assign Material/MaterialLayerSet for surface members: OK
- Select MaterialProfileSet and MaterialLayerSet from a list: X
- UI panel with connections and actions related to selected members: X
- Batch operations of Assign/Unassign materials and derivatives to members: X

**Structural Connections**
- Add/Edit/Remove connections: OK (standard BBIM functionality for IfcProduct)
- Edit Local Coordinate System for point and curve connections: OK
- Edit Local Coordinate System for surface connections: X
- Add/Edit/Remove boundary conditions (supports) for connections: OK
- Consider elastic (spring) support for each degree-of-freedom in boundary conditions: OK
- Assign/Unassign members to connections: OK
- Add/Edit/Remove connection conditions between member and connection: OK
- Edit Local Coordinate System for connection conditions between member and connection: OK
- Select boundary and connection condition from a list: X
- Batch operations of editing boundary and connection conditions: X
- Show stiffness units for elastic conditions: X
- Consider connections with eccentricity: X

**Structural Loads**
- Add/Edit/Remove structural loads in "Scene" properties: OK
- Show units for structural loads: X

**Load Cases and Structural Actions**
- Add/Edit/Remove load cases: OK
- UI Panel to batch create for selected objects and selected load case a load group with a single type of structural action: X
- Implement a way to visualize structural actions: X

**Load Combinations**
- Add/Edit/Remove load combinations: X
- Assign/Unassign factored load cases to combinations: X

### Other ideas on the backburner
- We can probably generate a ton of useful IfcSverchok nodes quite easily based on the new IfcOpenShell API.
- Allow the creation of searching a combination of filters in the IFC search panel
- Allow IFC search filters to be saved into a "search sets" which can be reused
- Allow remembered IFC search filters to be imported and exported
- Implement a search to the classifications UI to make it easy to find a single classification reference
- Scrape buildingSMART pset and attribute documentation to allow for descriptive tooltips
- Add support for importing and exporting IFC CSV headers so you don't need to keep on typing them manually
- Create a proof of concept of (proper) BIM and GIS integration with OGC datasets and a web viewer
- Create a UI in Blender to integrate with a Git repository
- Add support for OpenCDE API integration
- Support autodetection of arc extrusions
- Add common modeling tools to the tool menu for easy access and usability from other apps
- Visualise diffs in IFC data within Blender
- Add support for IfcSystem
- Add support for port connections and traversal to discover connected systems
- Add support for importing IfcPort
- Add support for Honeybee as part of the Ladybug-blender initiative
- Build a proof of concept of quantity take off based on NRM
- Create an option for column summaries in IFCCSV
- Create an option for group by counts in IFCCSV
- Formalise the DXF2IFC script
- Grouping together a series of mesh cleanup tools related to authoring BEM would be awesome
- Create an IFC2HoneybeeJSON script
- Stabilise and package the gbXML export script
- Portions of Bonsai are starting to mature. It's time to start thinking about a proper documentation manual.

## Bonsai Changelog
A summary of the changes in all versions released so far can be found in the [Bonsai Changelog](/bonsai-changelog/).

## See also
- [BIM Collaboration Format (BCF)](/categories/bim-collaboration-format-bcf/)
