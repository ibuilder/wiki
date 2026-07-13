---
title: "The OpenBIM Pledge"
url: "/the-openbim-pledge/"
aliases: ["/The_OpenBIM_Pledge/"]
categories: []
lastmod: "2025-10-26T00:24:57Z"
---

The OpenBIM pledge is a no-nonsense, step-by-step practical strategy to raise adoption of international, open data standards based BIM. If all companies agree to incrementally implement these principles, we can move towards standardised data across the world, and a strong foundation to build all digital processes, workflows, and future visions of our built environment.

This pledge is inspired by the pledge signed by browser vendors who stopped fighting and instead worked together to implement standards-compliant web technologies. This is a technical document, aimed at a technical audience of digital engineers. It's intended to be signed by the lead / head of digital engineering for a project, department, region, company, or government department. Signing this document is entirely voluntary. That said, you'd assume anybody who is a buildingSMART member is probably at least tier 1.

This is a draft. I did a braindump at 1am without holding back and haven't digested anything. Please braindump your own ideas by editing this page and we can collectively polish this.

The following tiers are aimed at both those requesting and providing BIM.

## Common metadata and exchange stream
### Tier 0
This is basically the participation trophy. It's better than nothing.

- I solemnly swear to require "IFC" (as vague as that is) as part of a deliverable. I will actually check that I've received something, and at least open it to make sure it contains information relevant to the project.

### Tier 1
A specific schema is required, properties are available, and the IFC is contractually significant.

- I will require and check for a specific IFC schema version (IFC2X3, IFC4, IFC4X3), acknowledging [practical differences between IFC versions](/practical_differences_between_IFC_versions/).
- If I require properties attached to objects, I will specify and check for a property name, property set name and IFC data type (e.g. IfcLabel, IfcIdentifier, IfcPositiveLengthMeasure) of the data.
- I will not penalise any stakeholder from using any software they want, giving them freedom of using the best tool for the job, so long as OpenBIM deliverables are provided.
- If an IFC is not delivered, I will withold payment if it is within my power to do so.

### Tier 2
IFC classifications are correct, properties are standardised, and requirements are specified filtered by IFC classifications in IDS form.

- All IfcProduct and IfcTypeProducts must be assigned to the correct IFC class. This means that regardless of people's favourite classification flavour of the day, there is a fallback "broad" classification that anybody can use for any process. This does not stop you from using additional classifications on top of IFC's built-in classes. This is also the first step in order to use any sort of standardised property or quantity.
- If I require properties or quantities that already exist as part of a buildingSMART standardised template (i.e. those prefixed with Pset or Qto), I will use that instead of reinventing my own.
- I will specify the applicable IFC class for all properties that I require. This ensures people understand which objects need which properties, and it can be automatically checked.
- I will provide an IDS for simple property requirements so that audits are standardised and there are no ambiguities or nasty surprises.
- I will validate IFCs and report validation bugs to software vendors. This provides a reliable technical foundation that we can build systems upon.

### Tier 3
- If anything is named in documentation (drawing, schedule, specification, etc), that name must be stored in the Name attribute (not a property!) of the relevant IfcTypeProduct and/or IfcProduct and/or IfcSpatialElement. This ensures that documentation at least correlates to BIM data (otherwise everything else becomes almost meaningless).
- If any name is not self-explanatory (e.g. a coded naming or numbering system), then a Description attribute (not a property!) must be provided of all IfcTypeProduct and/or IfcProduct and/or IfcSpatialElement (LongName instead of Description). Descriptions should be sufficient so that those reading a schedule of my objects can understand what the object is without visually looking at a 3D model. This provides a strong foundation to any non-graphical scheduling or query.
- If I require an external classification system, it must be stored as a classification reference in an IfcClassification, not as a property. This means that filtering of classifiations can actually benefit from understanding the hierarchical nature of classifications.
- All physical products must additionally have a predefined type assigned. If any user defined values are used, it must be documented and audited. The rules of inheritance and override of predefined types must be followed. This leads to a more granular option of an international classification.
- If the project documentation or asset strategy refers to types of objects (e.g. wall types, beam types, pit types, pipe types, equipment types, etc) then IfcTypeProduct must be used to reflect this with the appropriate type relationship to occurrences. For example, if there are 10 documented door types, there must be exactly 10 IfcDoorType objects.
- I will use object types and occurrences effectively using their ability to inherit properties and classifications. I will not explicitly require properties on every single occurrence. This prevents obscene duplication of data where data can be intelligently inherited.
- I will blacklist properties that are not explicitly required or part of the execution plan. This will prevent high quality, audited properties from being mixed in with untrustworthy, misleading "garbage" properties that create the risk of "garbage in, garbage out".
- I will specify the "Category" attribute for all IfcMaterials, using only one of the keywords listed in the IFC documentation. This allows you to identify basic things consistently like "concrete objects" or "steel objects" at a high level.
- If I want quantity data, it must be stored as a quantity set, not as a property. This allows us to separate calculable or geometry-derived data from semantic data so we can recalculate and check quantities and later connect parametrically to costs.

### Tier 4
- If I have my own invented classifications, properties, or materials, I will submit and maintain a register of the in the bSDD. This allows tools to integrate with my data schemas in a standardised manner.
- I will not request spreadsheets of information where all that information is stored in the IFC. Instead, I will audit data in IFC directly. This prevents duplication of data, ensures a single source of truth, and does not downgrade smart semantic data to dumb tabular form. You can of course later on generate tabular datasets, but it must not be a primary deliverable.
- I will not require any properties that can be derived from counting classes (e.g. total building storeys). This removes duplication of data and possibility of mistakes.
- I will not require any properties on an occurrence (e.g. room number) that can instead by stored on the relating container (e.g. space, storey, etc) or relating system (e.g. distribution system, circuit) or relating material. This removes duplication of data and is a good first step away from dumb properties and towards intelligent, related semantic objects.
- I will represent geometry of coverings, walls, slabs, beams, members, and columns using standard case material layer sets and profile sets if applicable to the design phase and geometric nature of the object. This is the first step towards allowing parametric modification and continuous updating of the IFC dataset during the project and building lifecycle.

### Tier 5
At this tier onwards, it is acknowledged that this is only achievable by experts and advanced users in OpenBIM. This is the bridging point between using IFC in a superficial or secondary manner, towards truly using IFC as the primary data schema for the built environment.

- All documentation forming a deliverable will be provided in IFC using IfcDocumentInformation.

Note: as tiers increase, further elaborate on the data relationships in IFC that have the biggest cost, time, carbon impacts. Highlight the biggest capabilities of working with IFC that allow for real time logistical tracking, visualisation, and data exchange.

## Design stream
### Tier 1
- If I require anything to be georeferenced, I will require at least IFC4, and correctly implement IfcProjectedCRS and IfcMapConversion following the best practices of the buildingSMART user guide to georeferencing for vertical and horizontal projects. This is the first step to federating across models, GIS environments, and infra projects of the future.

### Tier 2
- I will audit and guarantee that the spatial hierarchy reflects all documentation. This ensures that all documented rooms, storeys, spaces, buildings, infrastructure corridors, etc are also available for analysis in the model. Spatial breakdowns have many usecases and this is a required first step to any sort of spatial-based analysis.
- I will audit and guarantee that all products are contained in the correct spatial element in the spatial hierarchy. This will ensure that any spatial division or filtering can be reliably performed in the model. This is critical for any sort of cost / carbon / facility management quantification or further auditing breakdown (phasing, clash detection, etc).

### Tier 3
- I will specify all geometric LOD and clash detection priorities / rules in terms of data in IFC (e.g. IFC classes and predefined types, or IFC classifications) similar to the filter facets available in IDS. This means that geometric reliability and tolerance can be analysed in a standardised manner.

## Structural stream
### Tier 1
- All physical elements will be associated with an IfcMaterial to specify its material (as opposed to using a property).
- I will specify the "Category" attribute for all IfcMaterials, using only one of the keywords listed in the IFC documentation. This allows you to identify basic things consistently like "concrete objects" or "steel objects" at a high level.

### Tier 2
- All standardised steel profiles will come from an IFC library managed by my local buildingSMART chapter ideally including critical structural, quantification, and environmental data. This library must at a minimum include standardised names. This ensures highly standardised primary building components can be identified explicitly, and encourages sharing of industry standards.

### Tier 3
- I will provide any structural analytical models in IFC, using IfcStructuralAnalysisModel. The quality may vary at this tier.

### Tier 4
... stuff about load forces / reaction forces / load cases / etc.

## Services stream
### Tier 1
- If I require information about the system that a product is part of, I will use IfcSystem classes appropriately, instead of storing this information in a property set. All elements that are part of a system must be assigned to the system. This is the first step to semantically storing useful system connectivity.

### Tier 2
- The directionality of port connectivity must be correct and represent the distribution flow of systems. This allows the ability to do automated upstream and downstream impacts when systems fail or know what is serviced by other systems.
- Circuits must be represented using IfcDistributionCircuit.

### Tier 3
- The system type of all ports must be correctly identified. This is the first step in allowing for users to determine correct port connectivity and do optioneering.
- I will not require any property that can be derived through traversing port connectivity of system elements. This ensures that systems are not just geometry, but start to represent connected topologies.

## Costing stream
- If I require a cost breakdown structure, I will provide it in IFC, using IfcCostItem and IfcCostValue. The quality may vary at this tier.

## Construction scheduling stream
- If I require a work breakdown structure, I will provide it in IFC, using IfcWorkPlan, IfcWorkSchedule, IfcWorkCalendar, and IfcTask. The quality may vary at this tier.
- All project milestones must be reflected in IfcTask with correct scheduled dates.
- All IfcProducts with geometric representations must be assigned to an IfcTask as either an input or an output.
- Non-geometric IfcProducts must be created and assigned to IfcTask if they have a significant impact on duration.
- Construction resources must be identified using IfcConstructionResource. Quality may vary at this tier.

## Sustainability stream
- If EPDs are used on the project, all EPDs must be related using IfcDocumentReference, and correlate with the unit environmental impact values such that if multiplied by the unit quantity in the IfcElementQuantity, the total environmental impact can be derived.

## Asset and facility management stream
### Tier 1
- If I require COBie 2.4 or COBie 3.0, it must be extracted from the IFC in compliance with the COBie mapping table and COBie IFC class lists, not delivered as a separate spreadsheet. This ensures that IFCs are consistent with facility management data.

### Tier 2
- Smart building schemas such as Brickschema must correlate with (or be derived from) IFC. By ensuring design and construction datasets align with operational datasets, this is the first step towards connecting to smart building sensors, IfcEvent, IfcProcedure, etc.
- If requested on the project, I will be able to provide BACNet object identifiers and Brickschema URIs, referenced using IfcLibraryReference as a first step towards connecting live sensor data and building telemetry for building management.

## But why?
For those new to this concept, "OpenBIM" is a term meaning an international open data standard for BIM. The benefits of using open data standards regardless of industry are already elucidated in many sources online. That said, here's a summary of key technical features having practical implications on your project workflows and company digital strategy. As our in-house digital capabilities increase over time, the benefit of having the flexibility and ability to manipulate data using standards multiplies.

- Given an OpenBIM dataset, you can view/edit it with any software (or build your own) with no need for subscriptions, terms of use restrictions, or limited to APIs. This has both a cost and capability implication on digital strategies. Primarily, it means that your digital strategy is no longer vendor-centric and limited to "what tool X lets me do", and can instead be data-centric and optimised for business needs.
- You can use OpenBIM datasets on any platform (Windows, Mac, Linux, server, web, desktop, phone). You may serialise it in any form you wish (text, database, binary, JSON, XML, SQL, HDF5, TTL) or pair it with any development language (C++, C#, Python, Javascript, Perl, Pascal). No matter what your IT technology stack, open data standards can integrate. This opens up flexibility and future proofing for changing technologies, increased hiring pools, and external system integration.
- OpenBIM datasets won't expire or corrupt even in 50 years with no maintenance at all. As a case in point, IGES and STEP (which IFC has heavily evolved from) are still available from 40 years ago. This makes it useful for archival, data lakes, and for those managing large real estate portfolios where the cost and risk of proprietary version upgrades and corruption are high.
- Information is stored in standardised locations. This is perhaps the biggest advantage that most people are missing out on. OpenBIM defines a data dictionary with standardised names and data types for most common properties. For example, storing the "wall type name" or "fire rating" of a wall, is stored in a different property name, data type, or data schema in every single software, company, or project. (e.g. Revit users will inconsistently use "Type Mark", "Keynote", "Comment", "Description", "Type Name" to name or label an object). Data inconsistency means that you cannot automate or audit systems without mapping data on every job. You may have a company standard that recognises this problem and mitigates the issue, but is really reinventing the wheel where international data dictionaries already exist. Imagine your current difficulty (i.e. you have to create a bespoke filter or query) asking simple questions like "where is the fire rating of a wall stored" or "how do I find how much reinforcement is inside my beams" or "how do I isolate all precast concrete elements" or "how does the critical path differ between planned and actual work schedules"? The answers are standardised with OpenBIM and will work with any project, even if it's in French or Japanese and you don't speak the language.
- All projects are interdisciplinary. Despite this, most of us still work with siloed discipline datasets (i.e. one dataset for architectural models, another for energy analytical models, another for cost schedules, etc). In OpenBIM, this limitation falls away and the data schema can store both data and inter-relationships across many disciplines (structural analysis, energy, construction sequencing, asset management and inventories, cost, work orders, etc). This is akin to that "holy grail" stuff promised about BIM that people never thought was possible, because their vendor-centric digital capabilities still revolved around tool X and tool Y limited to specific capabilities for specific disciplines. For example, most people don't know that IFC can handle "smart building" stuff like sensors connected to event triggers and procedures.
- OpenBIM datasets integrates with other ISO standards and data schemas like Brickschema, glTF, X3D, BCF, IDS, OpenCDE, etc. This is important because naturally the dataset is only one part of a larger picture of technological solutions.
- There's a lot that IFC can do that proprietary systems cannot (and vice versa, more on that later), but one critical one to single out is that IFC can actually be georeferenced. Most BIM data have no standardised way to store coordinate data (e.g. Revit can store coordinates, but cannot store the coordinate system) or are unitless (DWG/DXF).
- OpenBIM data is highly "semantic" and "object oriented". What this means is that the data is more meaningful than a name-value pair attached to an object. For example, if the material of an object was stored as a property named "Material", that means you need to know the keyword "Material", and you're limited to storing a single value for the material. In contrast, if materials were a semantic object, then you don't need to know the keyword "Material" beforehand, and you can store lots of meta-information about the material (colour, compressive strength of concrete, reinforcement density, steel grade, young's modulus, etc), as well as have N:N relationships (e.g. composite materials). This means that when you build digital systems and workflows, your ways of creating and analysing data can be more sophisticated. Other examples include hierarchical classifications, document URI references, proper distinctions between visual style and materials, element connectivity, etc.

## But why not?
- If you need to upskill to learn about OpenBIM, organisations like buildingSMART, OSArch, and consultancies who have signed the OpenBIM pledge are a great place to start. There are a variety of channels including structured learning courses, personal consultancy, or self-guided learning including live chats or long-form forums.
- As OpenBIM is international, it lacks country or government specific data standards. The best thing to do is to reach out to your local buildingSMART chapter to develop, maintain, and provide local data dictionaries. Help can be provided from the above channels.
- As OpenBIM focuses on semantics, and is agnostic of how those semantics are produced, you need to be aware that the means of delivery is deliberately out of scope. It is still valuable to request "the authoring format" (sometimes called the "native format", this is the format where data is authored). You should not mandate a particular authoring format (see Tier 1), as that would limit the best tool being used for the job. As digital authoring gets more sophisticated, authoring formats may be a combination, including spreadsheets, scripts, and tools (Revit, ArchiCAD, etc). Note that IFC itself can be the native authoring format, in which case there is nothing further to request.
- There are current known limitations or unknown in OpenBIM standards regarding 2D documentation (drawings, schedules, etc), lifecycle analysis, parametric task/cost to product associations, among others. This is an area of active development and research. That said, this type of stuff is around the more advanced tiers so there's plenty to catch up on in the meantime.

## Signatories
Aiming to get signatories finalised by November 15th. Signatories will:

- Attend a (virtual online) meeting twice a year on the Equinox (20th March 2026 and 23rd September 2026)
- Present a project and identify the stream-tiers they have achieved on that project. That will be added to the projects list below.
- Share lessons learned so we can all get better
- Share complaints about how the OpenBIM pledge sucks so we can improve the pledge too for next time
- Bring pizza because some of us will meet in person

- Acciona (Max Labecki)
- DKO (Moiyez Buksh)
- Gamuda (Yatong Nie)
- GeometryGym (Scott Beazley)
- Lendlease (Dion Moult)
- Transport and Main Roads (Gavin Cairns)
- Transport for NSW (David Bayliss)
- McConnell Dowell? (J?)
- AECO.dev (Yassine Oualid)
- BIMvoice (Petru Conduraru)
