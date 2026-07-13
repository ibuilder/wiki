---
title: "Bonsai Changelog"
url: "/bonsai-changelog/"
aliases: ["/BlenderBIM_Add-on/BlenderBIM_Add-on_Changelog/", "/BlenderBIM_Add-on_Changelog/", "/blenderbim-add-on-blenderbim-add-on-changelog/"]
categories: ["Bonsai"]
lastmod: "2022-08-22T20:03:01Z"
---

## v0.0.190905
- Supports writing IFC4 files first and foremost.
- Lots of clever reuse of representations to create efficient and small IFC files and you have full control over exactly how you optimise the IFC file, including generating products from parametric arrays and object group instances
- Supports the spatial tree including multiple buildings, multiple sites, and so on
- Create product compositions including extremely granular breakdowns
- Create project libraries, not just projects
- Quantity take-off calculations
- Property sets
- Modeling abilities are completely separate from BIM data. In contrast to other tools where the type of object governs how you can model it, in Blender it is totally separate and you can instantly convert an object from one type to another, change its aggregation, change its spatial location such as changing floors, etc without any fear or breaking your model
- Export with/without quantities, or with/without representations (hint: an export without geometry retains all of the useful BIM data but is extremely fast to export, and creates a tiny IFC filesize!)
- Blender’s native Python API allows you to script it heavily doing bulk IFC data management very easily
- Obviously you get immediate access to all of Blender’s amazing features like modeling in real-time rendered view like a game engine. Beautiful visuals. Animation. File linking. Proxy objects. Virtual reality. Light simulation, CFD analysis, energy modeling. Huge ecosystem of add-ons. The list just goes on and on.

## v0.0.190910
- Improved support of project libraries, so you can have multiple project libraries, and easily relate/unrelate them to projects
- Property sets now detect data types from the property set templates, so you can define your own property set templates, and it will read them that to allow you to enter in data quickly. I am not aware of other vendors using property set templates, so this is exciting news!
- Implement IFC georeferencing through map conversions and target CRS definitions. This makes three vendors that I am aware of that do this properly: ArchiCAD, FreeCAD, and now Blender.
- Allow you to export 2D / 3D wireframe geometry, this allows some very efficient filesize savings where a full solid representation is not required.
- Export basic material colours and rendering styles including transparency.
- Allow export of an externally defined material, such as a .blend file, .vrmat file, or even .mat Radiance file for lighting simulation!
- Units are no longer hardcoded, and now support different types of metric units which can be set through the Blender UI, so you can choose to work in metres, millimetres, etc.
- Allow property sets to be assigned to types, and have object property sets override type property sets.
- Some optimisations and bugfixes

## v0.0.190914
- Objects and types can now be associated with external documents, such as plans, brochures, specifications, warranties, etc.
- Objects and types can now be classified using classifications such as Uniclass / Omniclass / anything you choose.
- Objects and types can now record qualitative constraints in the form of objectives. This can help record design intentions and health and safety strategies, among other things like code compliance requirements.

## v0.0.190921
- Documents and classifications are related to the project itself.
- Support for multiple representations are created. Previously, only a ‘Body’ representation was created. Now, you can add or remove multiple representations, some of which may be automatically generated from the ‘Body’ representation, and some which you have full custom control over their content. The supported representations are: Body Axis Clearance Footprint Reference Box CoG
- Although Blender has first-class support for manipulating breps, you can now choose to export simple extrusions of any angle (i.e. not necessarily normal to the profile curve) as a SweptSolid, giving the first steps towards supporting IFC roundtripping with programs like [Revit](/autodesk-revit/) which support these types of geometries but not other types.

## v0.0.190930
- You can now create nested element relationships: for hosted objects and nested components.
- Material layer sets can be defined
- Material constituent sets can be defined
- Predefined door attributes can now be defined and assigned to door types
- Predefined window attributes can now be defined and assigned to window types
- It’s now packaged for more end-user testing! See below:

## v0.0.191010
- You can now create nested element relationships: for hosted objects and nested components.
- Material layer sets can be defined
- Material constituent sets can be defined
- Predefined door attributes can now be defined and assigned to door types
- Predefined window attributes can now be defined and assigned to window types
- It’s now packaged for more end-user testing! See below:
- The QA module includes a feature to allow applying a temporary colourscheme to the model based of a property. For now, the interface allows you to colour it by IfcClass, but you could theoretically colour by anything (fire ratings, acoustic ratings, any property …). Here is an example, showing walls, doors, columns, slabs, and some floating building element proxies:
- You can bulk approve or reject classifications and keep track of what elements you’ve audited for various properties. Any IFC property auditing will get tracked in plaintext format in Gherkin syntax, so it reads like English:

## v0.0.191019
- You can now select objects by GlobalId
- New basic UI for georeferencing data
- Custom psets are now supported - it can also support complex data types and you can load in your own pset templates too!
- New UI for adding in attributes, with drop down selection of possible attributes taken from the spec. Now everyone can easily add attributes!
- New UI for adding / removing property sets (and you can set them in bulk!)
- New quick project setup button to add site / building / storeys.
- Bugfixes for importing, assigning classes, and roundtripping geometry with Revit (Revit seems to expect normalised direction vectors, even though the IFC spec doesn’t require this)
- Now supports assigning surface colours directly to object representations via styled items, as well as assigning surface colours via materials - and as the user, you have the choice which way you want to do it. To my knowledge no other BIM authoring tool supports this feature!
- New BIMTester tool is now packaged and available for Windows 11. It audits your BIM file to customised rules, and generates HTML reports!
- New UI to explicitly assign how swept solids are represented, to make it easy to round trip with Revit.
- New UI to assign externally defined materials - more on how this allows people to create incredibly detailed CG rendering workflows soon!
- IFC import has been somewhat rewritten in preparation to start supporting the ability to import this data too, not just geometry and basic materials and ID. The importer has been merged with the exporter and packaged as a single package to make it easy to install.

## v0.0.191106
- Importing IFCs now have improved mesh reuse and optimisations on shape creation leading to much faster imports! Also some bugfixes thanks to @Hans_Lammerts
- New interface to assign documents to IFC objects
- New interface to assign classification systems (Uniclass / Omniclass) to IFC objects
- IFC importing now also imports object attributes
- Bugfix in BIMTester to run and re-run multiple test suites
- IFC COBie packaged with minor bugfixes
- Experimental gbXML export now supports creating openings, as well as some bugfixes
- New IFC Diff tool (basically git diff for IFC files) - this allows you to take two different IFC files and it will compare them and tell you what changed. It will tell you if geometry has changed, or
- utes, and also the previous value of the attribute and the new value of the attribute. It writes it out to a json file which can be visualised with Bonsai so you can overlay changed models.
- New experimental sectioning tool to create construction documentation. You can cut sections direct from IFC files and create view hatching / line weight stylesheets with CSS which can be mass applied across objects. Objects are smart vectors, so unlike other documentation tools, 2D documentation have SVG classes applied so each object knows the IFC GlobalId, material, and IFC class.
- New interface to create, edit, and save IFC aggregates
- Import now supports curves, so you can import survey point geometry that might come from 12D, for example.
- Export now supports Blender curve objects, not just mesh objects, so you can do profile extrusions along vector curves and export them
- A whole bunch of geometry processing fixes in the underlying IfcOpenShell library by @aothms (which are quite technical but it looks like a great job!)

## v0.0.191116
- New support for importing and exporting imperial units, and you can choose your primary LENGTHUNIT.
- You can create geometry specifically for the PLAN geometric representation context now, and choose the TARGET_VIEW enum to do plans, sections, RCPs …
- New export options to export materials as styled items. This is useful for exporting to Revit (and a few others), which seems to completely ignore IfcMaterial, but instead treats the styled item name as the material name, and ignores any colours assigned via IfcMaterial. Ideally, this should be fixed on their end, but is a workaround.
- New import options to import 2D curve elements
- Parametrically generated geometry from Blender now maintain their GlobalId value, even if you generate less or more of the geometry.
- New import option to ignore site locations, so that non-geolocated IFC2X3 files or incorrectly geolocated IFC4 files (almost every single Revit export that we come across) can import with a sensible project origin.
- New UI and improved support for specifying multiple swept solid extrusions per object, for geometric round-tripping with programs like Revit
- Stephen Leger from Archipack has started contributing code! He has done some neat cleanups and optimisations on the Blender UI.
- IFC BIMTester now has a feature where you can choose to purge tests for elements which have been since deleted since you wrote your test suite.
- You can now specify IfcPerson and IfcOrganization details including postal and telecom addresses for export.
- As usual, bugfixes, most notably for the export location of swept solids and parented Blender objects.

## v0.0.191129
- Bugfix for IFC locations of objects which have a parent relationship or constraints in Blender
- Plugin renamed to Bonsai
- Version number now shows on the add-on
- Objects can now be arbitrarily scaled in any axis
- Under the hood code clean-up and PEP8 improvements
- You can now specify an IFC Diff and do an incremental import. No need to reimport an entire file, just import the things which have changed!
- Bugfix for BIMTester to prevent overwriting existing feature files
- Optimisation for the “select audited elements” function. Much faster.
- Add support for element voids and fill elements relationship. You can now properly do doors in walls and stuff like that.
- Bugfix for IFC “select by type” function which wasn’t working.
- Implement support for IFC library (not project library, which already existed - this new feature lets you specify if your project is on a BIM server, such as Git)
- A couple new sentences added to the BIMTester vocabulary to mark elements as exempt from testing
- Bugfix when shape representations are reused in their mapped item entity.
- Support for parametric mirroring of geometry (aka the mirror modifier in Blender) to export out to IFC - it can halve your modeling time and export filesizes for symmetrical portions of your building!
- New dropdown for audit class in the audit panel, instead of having to navigate to other panels to approve or reject IFC classes.

## v0.0.191219
- Imports now support styled item colours, and differentiates between material surface colours and object surface colours
- Support a “material passport”, essentially you store externally defined surface styles, and Blender can detect if any Cycles or Eevee shaders exist in it, and will load them. This allows for IFC models with complex textures and materials for CG renderings. No other BIM program can do this.
- New IFC Clash utility, to perform clash detection, with a specified dimensional tolerance. This data can be exported into JSON so you can visualise clash results and analyse them. Clash detection is done directly on the IFC so you can run it on your BIM server. Can run from command line. This replicates functionality from Navisworks or Solibri.
- You can proxy one shape for another using associated documents. If you associate another mesh object, Blender can replace the IFC shape representation with another Blender native file format. This way you can have low-fidelity models in the IFC file but retain higher polygon models elsewhere.
- Import now supports document associations
- New UI to choose exactly what geometric representation contexts to export.
- IFC diff utility can now run from command line input so that it is easier to run from a BIM server.
- New support for construction documentation. More on this below.
- Bunch of under the hood fixes with IfcOpenShell thanks to @aothms and other IfcOpenShell contributors like AdriScho and mieszk

## v0.0.200109
- Be less strict about requiring BIM objects to be selected when exporting, to make it more user-friendly. Now you can just bulk select everything.
- New workaround for importing materials from Revit, since Revit has a funny way of storing materials. Models being imported from Revit will now be much more colourful!
- You can now create geometry and export spatial elements, such as an IfcSpace.
- BIMTester now has a variety of new unit tests, including:
- * all IfcFoo elements have a name matching a particular pattern - useful to check whether the BIM author has followed a naming scheme in your BIM execution plans.
- * all IfcFoo elements have a particular shape representation - useful to check if the BIM author has their geometry in a representation that you can edit, for round-tripping between Blender, FreeCAD, Revit, and others.
- * all IfcFoo elements have a particular attribute - useful to check if BIM authors have correctly filled out an attribute
- * all IfcFoo elements have a particular property / property matching a pattern - useful to check if BIM authors have correctly filled out a property in a pset that you need for your exchange requirements
- * all IfcFoo elements have a particular quantity - useful to check if BIM authors have filled out sensible quantity values for something you need to quantify
- BIMTester can be run now both as a standalone CLI app in your BIMServer, or as a library, and allow you to set custom unit testing parameters for greater testing control
- Have a “force recut” feature to regenerate a new section / view of a model in construction documentation.
- New experimental collection of 50 hatch types for construction documentation, including various drafting standards
- New interface to select a person and organisation to properly set ownership history, with detailed information like addresses and so on
- New interface to quickly create a new view / section of the model
- Each view / section now stores its own view scale, instead of it being an export-time setting for convenience
- New UI to easily switch between views / sections
- IFC Diff utility, to compare the difference between two IFC files is now packaged for Windows as a standalone executable
- The IFC Diff utility has also been packaged within Bonsai, so you can run it from the Blender interface to compare files
- Application and IFC header metadata is now (almost) properly filled out, just to be neat.
- Importing now specially treats aggregations and displays them as aggregates
- Opening elements are now stored in an import in their own collection for you to do with them what you please
- New feature to explode aggregations into parts
- Cleaner geometric representation context UI
- New interface to quickly assign any representation to a particular context, subcontext, or target view.
- Automatic vendor hack mode is enabled by default: it detects a particular vendor when importing and auto applies various workarounds for their quirks in their IFC files. Currently enabled for Revit’s lack of IFC geolocation and funny materials. This should help a lot of people who aren’t aware that these workarounds need to be applied and would otherwise get a bad impression of IFC files and Bonsai.
- Bunch of under the hood bug fixes for more reliable importing.

## v0.0.200123
- Documentation added for the context panel
- Site objects are now imported
- Bugfix to export different types of curve objects
- All non-polygonal extrusions now have an Axis representation exported
- Material properties are now exported (like density, youngs modulus, etc)
- New sample attributes for doors and windows shipped with the add-on
- Point clouds now can be exported to IFC
- IFC structural objects are now exported
- UI improvement to only show predefined types and userdefined types if it is possible
- Structural objects now export a topological reference representation
- Parametric material profiles are now supported (rectangular, circular, I-Beam, etc)
- New UI to manage material attributes
- New UI to change material assignment (single / layer / constituent / profile set)
- New UI to create a property set override instead of having to write properties in separate CSV files
- BIMTester now includes model setup vocabulary, drafted in collaboration with BuildingSMART Australasia co-founder @john.mitchell - it tests basic project attributes and geolocation for both IFC2X3 and IFC4.
- BIMTester now allows custom JUnit directories for better cloud integration
- Bugfix where some context representations were not exported now fixed
- UI to specify structural boundary conditions
- New UI to specify structural member connections
- Can export a group of structural objects into a Structural Analysis Model
- Importing now has a progress bar and more consistent logging
- Documentation for Bonsai and IfcOpenShell merged and restructured
- New workaround for Revit incorrect geolocation being placed on the building object - enabled by default
- Assigning product types is now done by a property instead of the Blender parent relationship to allow it to scale on large files
- New experimental script to convert IFC into Code_Aster input for 100% free and open source structural analysis

## v0.0.200228
- 12D files, which usually have absolute coordinates, are now imported into Blender with an offset to allow you to work in local coordinates for vertical BIM
- The BIM audit panel now allows you to select a particular BIMTester feature, and write tests directly from the UI instead of needing a text editor
- Your spatial tree can now have geometric representations (most importantly, this allows you to export an IfcSite terrain)
- Quick project setup button now sets up spatial objects too
- Sites can now export a reference long/lat attribute
- When importing, it now remembers what IFC file the data came from (in preparation for partial writes)
- Minor bugfixes related to missing items in dropdown menus, curve orientations upon export
- Import now associates type products
- Bugfix allowing you to import multiple spatial structure elements with identical names
- New option to toggle import of opening elements
- Improved IFC-to-Code_Aster script
- Preset render settings for creating documentation and diagrams
- Create dimension annotations in 3D from any orientation instead of for a particular view
- New support for IFC projection elements (opposite of void elements)
- Allow you to create other types of leaders and section levels from any orientation instead of for a particular view
- IfcPolygonalFaceSets are now imported with the correct units (useful for sites and terrains)
- Extra checks to ensure exports don’t create GlobalId collisions
- Allow duplicate names for both mesh and curve data
- New option allowing people to maintain parametric behaviour to generate multiple IFC objects, or to bake the results into a single IFC object
- New IFCPatch tool, allowing you to patch the data in an IFC file based on a series of preloaded “recipes”. These allow you to workaround various limitations in other IFC authoring exports in a safe way without breaking the rest of the IFC data. Recipies include:
- * Reset spatial element object placement locations
- * Offset from absolute coordinates to a local system
- * Remove representations from sites
- * Offset IfcBuildingStorey elevations
- * Set reference elevation
- BIMTester now shows test results with a percentage success rate
- IFC import now imports pset data
- 2D grids are now imported even though curve data isn’t enabled, given the importance of grids. Support added for IfcGrid and IfcGridAxis
- New ability to search for IFC objects by their attribute or pset property values with a case insensitive string, with support for regex for super advanced searching
- You can select any IFC attribute or pset property and colour code the model by the value for a visual cue when auditing IFC data
- Minor UI clean-up to hide panels by default
- New import option to toggle import of IfcSpace objects
- Handle import coordinate offsetting of IFC2X3 files created from Tekla which are poorly geolocated
- Version bump to the latest IfcOpenShell library, which includes fixes for more stable geometry import

## v0.0.200328
- Latest IfcOpenShell version, with various stability fixes to import more files!
- BIMTester can now just generate reports if required
- BIMTester can run a single test instead of the entire test suite
- Fix import bug with some IFC object types aren’t related correctly
- New BIMTester test to check if an element doesn’t exist
- Improved support for IFC2X3 materials without transparency
- Fix import bug where IFC spaces with the same name might not be in the right location in the spatial tree
- New import option to auto-merge geometry by IFC class
- New import option to auto-merge geometry by IFC material
- New import option to disable element aggregation
- Hidden lines in construction documentation may now be in 3D, useful for showing exploded axonometric views
- New IFCCSV tool allows querying an IFC file and exporting attributes and psets and reimporting an updated CSV to the IFC model
- IFCCSV tool allows querying using IFC class, attribute, pset, and qto filters, with multiple operators, AND and OR statements
- Export fix where sometimes you could create an abstract IFC class
- All IfcSpatialElements are now supported including obscure ones like IfcSpatialZone and IfcExternalSpatialElement
- IFC exports now support multiple materials on a single object
- Fix export bug where some aggregates don’t export
- Fix import bug where some objects inside a space won’t import
- New import feature to automatically clean meshes to get nicer topologies
- New export feature to export objects inside spaces and any spatial element
- New import feature to record the spatial relationship of objects inside spaces (with ability to scale for large projects)
- New import feature where quantity take-off quantities are imported
- New export feature where you can manually fill out quantities and export them
- Fix import bug where materials may be on multiple shape representations
- New support for BCF XML 2.1!
- View list of BCF topics in the UI, showing basic metadata about each topic
- New button to uninstall add-on, to improve the upgrade process
- See multiple viewpoints for each BCF topic and launch a camera view for each viewpoint
- Any type of curve object is now supported for construction documentation annotation objects
- Spatial containers are auto-detected when exporting making it more convenient for users to do quick exports
- Support for BCF topic comments
- BCF topic reference links, BIM snippets, document references, and related topics are supported with buttons to quickly open both external and internal references
- New buttons to quickly view Bonsai homepage, docs, wiki, and forum
- Documentation titleblock and view templates heavily optimised to a fraction of the filesize - mere kilobytes!
- New UI feature to add new sheets and add views to sheets
- New UI features to quickly open sheets and views in external SVG programs / viewers
- Views now store view scale in their vector output - in an indsutry where our vector output is non-semantic, which really changes things!
- Fix IfcPatch bug for broken ResetAbsoluteCoordinates recipe
- New feature to publish sheets with automatic view titles, scales, view numbers, and sheet names

## v0.0.200413
- New feature to validate the syntax of IFC files, in case you receive a broken IFC file
- New support for viewing and overlaying BCF snapshot images on top of the model to compare issues
- More stabilisation fixes on multicore IFC import
- Support added for BCF header files
- IFC import now supports multiple materials for a single object
- More robust material imports for BIM authoring tools that still use the deprecated IfcPresentationStyleAssignment or have missing styles (yes, Revit, that’s you!)
- Experimental multicore support added to IFCClash
- The IFC2CA project has joined the IfcOpenShell umbrella!
- BIMTester now bundles test definitions so you get tests out of the box!
- IFCDiff now checks inverse relationships for changes too
- IFCDiff lets you specify filters for checking specific inverse relationships
- BCF snapshots with varying aspect ratios are now supported
- The IfcProject entity is now a real object in Blender, which can be queried and exported with all of its metadata
- BIMTester now supports the full Project setup MicroMVD definition
- New optional GUI in BIMTester for people who don’t like command line
- IFCCOBie has various fixes for strange formatting on wrapped data
- Bonsai dependencies repackaged inside add-on, to allow for native Blender install and uninstall procedures
- Bonsai Uninstall feature removed, as it is now obsolete in favour of native Blender uninstall process
- IFC spatial elements without any geometric representation are now imported
- Invalid Psets without any properties (as created by Solidworks) are now imported
- Diff import support has now been upgraded to the non-legacy import mechanism
- Rebar is now treated specially to prevent BREP faceting, so it retains its parametric swept disk solid behaviour, and is easier to edit, imports 10 times faster and is 10 times smaller in terms of filesize
- IFC import has an optimised spatial tree processing algorithm to handle files which have hundreds of sites and buildings for precinct BIM models
- Psets and Qtos can be selected from a filtered list for easy user discoverability instead of having to know the IFC spec
- New IfcExportSettings factory to let Bonsai be integrated with other Blender add-ons like ArchiPack
- Improved ArchiPack compatibility - export parametric IFC objects from Archipack!
- Repository code cleanup of old experimental files
- Fix for potential infinite loop during export
- Fixed some invalid schema exports related to void/fill/projection relationships, and material assignment related to linked duplicate objects
- New support for import and export of the IFCZIP format
- New support for BCF component visibility settings, colouring options, and selection sets when viewing BCF topics
- New support for BCF orthogonal camera scale factor

## v0.0.200428
- IFC export now supports assigning objects to CAD presentation layers
- Fix for incorrect grid placement in some scenarios
- IFC group objects are now imported
- Rebar profiles now share instances if it has the same radius to optimise rebar imports
- Attributes or pset values can now be copied across to objects in bulk
- IfcDiff now checks model precision when determining tolerances
- IfcPatch now has a recipe to offset and rotate an entire model
- Graphisoft XMLs can now be parsed into IFC, now maintained by OSArch
- New hierarchical classification system interface, which can read IFC files as input
- Uniclass and Omniclass are now bundled with Bonsai, but a repository is provided to download many more classification systems
- IFC files for property set templates can now be loaded and viewed
- You can now author property set definitions and property templates in Blender and export them
- New workaround for importing Civil 3D files with absolute coordinates
- Old CSV-based pset definitions deprecated in favour of IFC template definitions
- New feature to create/remove a section plane in real time
- Support for as many section planes as you want at any angle
- Section planes can be applied to a subset of objects, not all objects
- Crash fix to IFCCSV when exporting non-existant attributes
- IFCCSV is now able to be loaded as a library to be used in other applications
- Bonsai now has a built-in UI to export and import from IFC and CSV
- IFCCSV now supports exporting IfcClass as a data column
- IFCCSV now supports querying inverse spatial and type relationships (e.g. all objects in this container, or all objects of this type)
- Import workaround for vendors like DDS-CAD who create widely duplicated style items
- UI to visually select objects to be exported to CSV
- Section plane colour can now be changed
- Support for viewing BCF line annotations
- Support for viewing BCF clipping planes
- Support for viewing BCF bitmaps
- IfcDiff panel now prompts for export folder if you haven’t set one already
- New feature to reload an existing IFC file

## v0.0.200511
Features:

- Artists now have an option to merge aggregates into a single object to easier object manipulation
- Metadata about aggregates themselves are imported, including attributes, psets, and relationships
- New option to select all objects of the same object type
- Classification hierarchies are now imported and can be browsed in a tree viewer
- Element classification references are now imported
- All document metadata is now imported, not just location
- Document information metadata can now be authored and exported
- Document information metadata can now be imported
- Documents that are not related to objects can now be imported and managed in a UI
- New feature to relate document information and reference entities
- Classifications maintain their hierarchy and do not flatten upon export, allowing for richer (i.e. semi-lightweight) classification exports
- Users can specify a list of IFC files to be cut in a section / plan / view
- Exclude rooms from being cut by default in a section
- New style preset for creating construction documentation graphics
- Grid annotations now work in 3D
- IFC metadata (like materials) is now cached when doing a section cut to improve performance
- New UI to add annotation objects to a view like dimensions, leaders, text, levels, etc
- New font size support for text sizes 1.8, 2.5, 3.5, 5, and 7.
- Rebar is more efficiently created without the need for distinct circle profile objects
- Background renders can be cached when doing a section cut to improve performance, if you are only changing annotation
- Users can now specify a symbol for text annotation, like a label box
- Text annotation now supports variables to extract data from IFC files
- Geometric representation context and subcontext definitions are now imported
- Relevant types are now auto-selected for export for convenience
- Export feature is now more granular to export only specific contexts
- 2D axis representations (i.e. not 3D) are now also supported from both meshes and curves
- Authoring and exporting footprint geomset geometry contexts is now supported
- Authoring and exporting 2D and 3D annotation geometry contexts is now supported
- Authoring and exporting 3D profile geometry contexts is now supported
- Text annotations with variables can have functions applied to them - e.g. to concatenate data, format data, or anything, for example to round text annotation to the nearest decimal point, or force uppercase formatting
- Bonsai importing and exporting can now be done headlessly on a server, to allow for remote server processing of BIM data. There is now a Bonsai continuous integration server, to process IFC test cases: https://ci.blenderbim.org/
- You can now bulk-add smart annotations to many objects at once
- You can now manage the geometric representation contexts per object or object type, to switch, lazy-load representations from an IFC, and create new contexts
- IFC unit settings are now preserved on import, instead of using your Blender settings
- You can now export _just_ a single representation to an IFC file, leaving the rest of the IFC data untouched
- Type representations are now imported as well instead of just elements, with support for mapped geometries
- IfcDoorStyle and IfcWindowStyle metadata (attributes, etc) from IFC2X3 are now imported
- Annotation objects are recognised in the section cutting procedure, and not processed for a boolean cut for a more optimised cut
- Solid line annotation objects are now supported (previously only hidden lines were supported)
- A list of contexts are now imported for each object, and you can switch between them with a new UI
- Section / plan / documentation cuts now recognise annotation objects, and will draw them as 2D linework
- Stair annotations now work in 3D
- New hatch patterns! Sexy.
- New door tag symbol support.
- New breakline annotation.
- IfcAnnotation entities are now supported, to be used as you see fit.
- Documentation sections / plans / views are now exported into IFC as groups
- Text annotation is now exported as IfcAnnotation, with new support for IfcTextLiteralWithExtents
- All other annotation objects (dimensions / leaders / levels / symbols / etc) are now created and exported into IfcAnnotation by default.

Fixes:

- Fix section planes sometimes not cutting through aggregates and appearing at the cursor
- Bug where poor material data may cause a bad section cut fixed
- Lat/longs are now converted to decimal degrees from DMS format
- Materials are re-used on subsequent imports if they already exist to prevent material duplication

## v0.0.200525
Features:

- New feature to convert from local to global (georeferenced) coordinates
- Custom Qto definitions can now be exported
- IfcClash can now patch global coordinates to aid in accuracy of clashes
- IfcClash can now be used standalone or as a library in any project
- IfcClash is now bundled with Bonsai for Windows and Linux (any Mac volunteers who want to build it?)
- Exporting two IfcProjects will now merge them into a single IFC project
- Experimental IFCXML can now be imported
- The relative placements of the spatial hierarchy are now imported and exported
- IfcClash now supports clashing many-to-many / multiple IFC files at once
- IfcClash now lets users configure clash tolerance
- IfcClash now reports the worst-case distance clash in the case of multiple clashes with the same two objects
- IfcOpenShell now has a utility module to let you conveniently do geolocation, element filtering, and getting element properties
- IfcClash now supports element filtering, with filter rules, and/or statements, inclusion and exclusion rules
- IfcClash now supports internal collision checks - to check for collisions within a single group of objects
- IfcClash now supports clash sets to be defined so you don't need to setup the rules again each time
- Bonsai has a new UI to create and run clash sets with IfcClash
- Bonsai now has a feature to export and import clash sets
- Simple integration with cove.tool for basic energy and daylight analysis
- You can now export experimentally to IFCJSON format (Thanks Ioannis!)
- BIMTester updated to latest MicroMVD syntax specification
- Bonsai now allows you to specific relationship checks during IFC Diff execution
- When importing the same file or updated files twice, existing rooted elements (spatial elements, objects, types, etc) are reused instead of duplicating
- You can now export psets related to spatial elements
- Users can now switch easily between IFC4 and IFC2X3 when exporting
- New feature to select / highlight all clash results in your current 3D viewport

Fixes:

- Rewrite IfcClash system to drastically increase quality of clash detection results
- Fix bug where monetary units can cause an import to fail
- Fix bug where an IFC without a subcontext can cause an import to fail
- Fix bug when exporting / round-tripping IFC2X3 to IFC4 classifications
- Fix broken export when object names are too long
- Fix bug where importing mapped type representations may accidentally reuse other meshes
- More lenient parsing to skip invalid representations and not stop halfway (as discovered in ArchiCAD-produced files)

## v0.0.200621
Features:

- A project is now setup automatically at export-time if you haven't done so already
- cove.tool integration now supports submitting custom geometry for bespoke designs
- cove.tool integration now reads north angle from project geolocation
- Improved stability on multiprocessing import, for much faster importing, give it a spin!
- Both materials and style overrides are retains on import, so you can see the full hierarchy of materials and styles
- IFC geometry type is stored on import
- IFC4 georeferencing data is now imported
- Users are now prompted to assign a class before accessing IFC metadata
- UI panel names are now a bit more standardised
- Rebar is now imported without needing to enable curve import
- New user option to enable native element geometry processing on import
- Not just rebar, but all generic IfcSweptDiskSolid is now processed as native geometry
- Extrusions which use IfcArbitraryClosedProfileDef is now imported as native geometry instead of being meshed
- Extrusions which use IfcRectangleProfileDef is now imported as native geometry instead of being meshed
- Bundled latest IfcOpenShell which a ton of new improvements
- Native geometry now supports surface styles
- The division between distinct representation items is now stored on import for native elements
- It is now possible for opening elements to create a boolean relationship on import
- Support partial importing, with whitelisting and blacklisting using IFC query / selector syntax
- Native elements now have multiprocessing support
- New IFCPatch recipe to split up an IFC file by building storey without data loss
- Mesh cleaning is now disabled for large files for optimising import times
- Optimise the creation of material slots to prevent duplicates, especially for BIM programs which abuse surface styles like Revit
- Big optimisations to importing files - like, much, much faster
- Faceted BREPs are now imported as native geometry instead of being meshed
- Components of a representation, like an extrusion profile or direction are now stored on import
- Export of extrusions are now supported, allowing native geometry round-tripping

Fixes:

- Objects without any placements can now be imported
- Switching contexts are now more tolerant of invalid IFC files
- Fix bug where types can be incorrectly assigned on export if names aren't unique
- Disable limited dissolve during mesh cleaning, which can lead to invalid material assignments
- Fix crash when doing an "undo" operation after adding annotations
- Fix invalid materials being potentially created when using the temporary section plane tool
- Don't fail importing case insensitive file extensions
- Fix issue where IfcGroup subclasses can be imported as the wrong class

## v0.0.200722
Features:

- Objects now have an IFC class assignment panel for convenience
- New "unassign class" to convert from a BIM object to non-BIM
- Improved absolute coordinate import from DDS-CAD based IFCs
- You can now remove a representation subcontext
- Object proxying now works in a simplified manner, letting you directly reference Blender files with high poly geometry
- New UI to manage IFC constraints
- You can now export IFC constraints based on the UI, making the older CSV definitions obsolete
- You can now assign constraints to individual objects and export them
- New UI for managing and creating IfcPeople
- New UI for managing and creating IfcOrganisation
- Support invalid grids coming from Revit
- Support import of triangular grids
- Support export of IfcSpatialElementTypes
- You can now export IFC2X3 "Style" classes in IFC4
- IfcOpenShell utilities now comes with geolocation functions
- All aggregates are now grouped in their own collection for convenience
- No need to manually select types for collections when exporting
- New feature when producing documentation, to recut the entire model or only selected objects
- Materials assigned to portions of an object no longer need to be using object links
- Support export of IfcPositioningElements
- You can now define an owner history from your collection of people and organisations, or have no history at all
- New feature to allow users to profile the import procedure
- BIMTester UI updated to new Gherkin conventions
- The IfcOpenShell selector utility now supports selecting COBie classes as its own selector
- IfcObjective constraints are now imported
- TK interface for BIMTester has been removed
- Quantity UI now provides manual calculation buttons for generating lengths, areas, and volumes
- You can now export a mesh edge for structural curve members
- The geometry type data field now supports "None", if it has no body representation
- New feature to automatically calculate quantities during export
- Allow for wildcard expansion in IFCCSV exports, allowing you to export a series of properties belonging to the same set
- Failed BIMTester tests now have improved error reporting
- BIMTester test reporting is now super sexy
- BIMTester can now be run without packaging as a simple library
- BIMTester can now be run from the Blender UI
- BIMTester can now audit predefined types

Fixes:

- Booleaned native objects will fall back to non-native import to support it
- Fix bug where a slot without materials won't export
- Fix bug where some absolute coordinates would not properly be converted to local coordinates
- IFCPatch ResetAbsoluteCoordinates has improved absolute coordinate handling
- Allow for empty data in non-mandatory georeferencing data
- Fix incorrect dimension export of rectangle profiles
- Scaled curve bevel objects are now properly exported
- Invalid psets now are no longer exported with empty relationships
- Fix bug where imported materials with the same name as an existing material could be incorrectly assigned
- Fix bug where IfcOpenShell selector utility was just broken
- Fix bug where truncated material names can cause import failure

## v0.0.200810
Features:

- Better command line interface for IFC COBie tool
- IFC COBie now no longer creates CSVs if you only need an XLSX file
- IFC COBie now supports the ODS format, as well as XLSX and CSV, for more interoperability
- New GUI in Bonsai to run IFC COBie
- IFC Patch can now be used as a library as well as a CLI
- New support for pythonocc-core 7.4.0
- BIMTester now colour codes undefined/unspecified test lines
- Check BIM project exchange requirements with the newly published "Project setup" MicroMVD
- Check BIM project exchange requirements with the newly published "Geolocation" MicroMVD
- IfcOpenShell utility module now lets you convert true north angles and IFC geolocation vectors
- Improved documentation on what dependencies are used by Bonsai
- Check BIM project exchange requirements with the newly published "Element classes" MicroMVD
- BIMTester can now explicitly audit NULL attributes and properties
- New export support for IfcSweptDiskSolid for curves with no bevel profile geometry
- Blank qto names are accomodated in invalid IFCs
- When absolute coordinates are offset during an import, the offset is now recorded
- Allow keyboard shortcuts for both import and export
- Dimensions from MeasureIt-Arch addon are now supported in SVG drawing export
- New feature to visualise IFC Diff changes
- IfcOpenShell util.element.get_psets() now supports IfcComplexProperty
- New IfcOpenShell utility function to replace attributes from one to another entity
- New IFC Patch recipe to losslessly compress / optimise IFCs by recycling non-rooted elements, benchmarked with results similar to Solibri Optimiser (results may be slightly smaller or greater depending on the iterations run)
- New UI in Blender to run IFC Patch recipes graphically
- Check BIM project exchange requirements with the newly published "Geocoding" MicroMVD
- New IFC Patch recipe to merge two IFC-SPF files into a single file
- Quantity take-off tool now allows calculation of the depth (e.g. of an IfcSlab)
- Quantity take-off tool now allows calculation of perimeter (e.g. of an IfcSlab)
- Cleaned up object properties UI by splitting psets, qto, and structural relationships into their own panel
- New quantity take-off utility to get the total length of selected edges
- New support to import the area and volume unit settings of an IFC
- When calculating quantities, they are now auto-converted into IFC project settings instead of metric units only
- IFC CSV can now export type relationships
- Simplfy GlobalId generation by automating it on attribute addition, and providing an inline refresh button
- New quantity take-off utility to get the total area of selected faces
- New quantity take-off utility to get the total volume of selected objects
- New modeling utility to quickly add IfcOpeningElement relationships
- Non-node-based materials now have support for transparency
- IfcOpenShell updated, providing greater stability and geometric support for imports
- IfcOpenShell Python now lets you check by_type() excluding subclasses
- New support for exporting the latest IfcJSON format, with options for version 4 and version 5a, and compact / non-compact variants
- Add a new blank material for use in generating drawings
- Check BIM project exchange requirements with the newly published "Classifications" MicroMVD

Fixes:

- Fix bug where IFC COBie fails on empty names of related objects from assemblies
- Fix bug where IFC Clash would not run as a CLI, but only within Blender
- Fix bug where IFC CSV incorrectly stores boolean data types
- Fix bug where long, duplicate, material names fail to import
- Fix bug where IFC2X3 files may not have coordinates reset properly when an IFC file has absolute coordinates
- Fix import bug when getting a geometry type of an object with no representation attribute, like IfcGridAxis
- Add shebangs, so that all CLI utilities can now be more reliably run on all systems
- Fix import issue where some negative material IDs fail to import

## v0.0.200829
Features:

- All CPU cores are now used for shapes in drawings generated from IFC. This leads to much faster drawing creation!
- Users can now specify what objects should be cut in documentation with either a custom rule or with presets.
- Adding a new representation subcontext when you haven't yet defined a body auto-adds a body subcontext and clones the mesh
- New button for the camera to quickly open the relevant drawing
- Export now has an automatic bounding box representation being generated
- New dumb wall geometry creator tool
- New dumb stair geometry creator tool
- New dumb door geometry creator tool
- New dumb slab geometry creator tool
- New dumb window geometry creator tool
- 2D representations now support IfcIndexedPolyCurve so instead of just 2D curves you can have full 2D wireframes
- New utility to quickly set object colours
- New interface to manage different drawing styles
- Drawing styles can now remember basic rendering settings and let you switch between them
- New highly experimental DXF2IFC conversion script
- Managing drawings now is done in a list instead of a dropdown for user convenience
- You can now pick the vector CSS style and save it as a drawing style
- Support for importing IfcGrid itself, not just the individual axes.
- Importing IfcGridAxis now retain their UVW assignment and can store attributes
- Support exporting IfcGrid and IfcGridAxis with all of its relationships
- New grid creator tool for convenience
- Doors now can have 2D annotation representation subcontext symbols auto generated
- Windows now can have 2D annotation representation subcontext symbols auto generated
- New button to edit the CSS style within Blender itself for convenience
- Drawing styles can now store element filters to include / exclude elements in drawings
- More robust footprint area calculation, specifically targeting better results for IfcSpace
- Selecting multiple objects now lets you guess / fill out quantity sets in bulk
- Enforce directories when selecting a MicroMVD for BIMTester for convenience
- You can now purge project-specific IfcClassification hierarchies
- Newly impored IfcClassification hierarchy for a project will show up immediately
- IFC COBie will now launch the log as well as the spreadsheet when converting from IFC to spreadsheet
- New more user friendly UI for sheet creation
- Exports now auto detect curve / wireframe representations, so you no longer need to classify it manually
- Native element support for importing IfcCircleProfileDef
- Preset titleblock template now has a white background
- You can now convert generated sheets to PDFs on the fly
- New UI to manage schedules and link them to ODS spreadsheets (yes, this spreadsheet data can be generated from IFC too)
- You can now convert an ODS spreadsheet into a vector schedule to be included on a sheet
- Schedules can now be added to sheets
- At export-time, the exported IFC is automatically considered for drawing generation, for convenience
- You can now override the default COBie definition of a maintainable asset for both objects and object types
- You can now specify custom IFC attribute mappings for COBie spreadsheet views
- Support exporting tessellated polygonal face sets for much more efficient file sizes! (Suzanne shrinks from 84kb to 44kb)
- Improve error reporting for BIMTester when it audits a list of IFC attributes
- New dumb opening geometry creator tool
- Native element support for exporting IfcCircleProfileDef
- Grids in drawings now read from IfcGridAxis AxisTag attribute when available
- Types are now automatically categorised in the project tree when assigned for the first time
- Support IFC2X3 classification EditionDate CalenderDates
- New utility to extract all IFC documentation for all COBie-defined maintainable assets
- New utility to extract all relevant entity and enum descriptions from the IFC documentation
- Creating drawing sheets now understand templates in any CSS unit
- All SVG scales now are standardised to a human unit with improved spacing and placement.
- Views are now placed within the titleblock border by default
- Support for all known ODF units when creating schedules from different spreadsheet applications
- Add support for imperial drawing scales
- Add support for custom defined drawing scales
- Add support for custom titleblocks
- New preset title blocks for A1, A2, and A3 paper sizes
- Drawing boundaries can now have different aspect ratios
- Annotation tools are now in the viewport instead of properties tab for easier access
- Drawings can now be associated with an IFC geometric subcontext target view to guide the drawing generation process
- You can now generate annotation references for IfcBuildingStoreys
- Bumped IfcOpenShell build, resulting in more reliable geometry processing during imports

Fixes:

- Fix bug where parts of an aggregate are not placed relative to the whole in exports
- Fix bug where some annotation tags won't extract data correctly from IFC
- Fix bug where aggregate creation only works if the aggregate collection exists
- Fix bug where predefined types were not correctly audited by BIMTester
- Fix bug where mapped representations belonging to a context fails to import
- Fix bug where disabling the add-on triggered a error message

## v0.0.200912
Features:

- Creating drawings now works with OpenGL render mode, allowing for better wireframe / hidden line rendering
- New default site boundary CSS style
- Multiprocessing is now enabled by default. It's probably stable enough, so let's test it even more!
- You can now export to DXF automatically when creating sheets
- Nested IfcSpaces can now be imported
- Reloading IFCs now detects openings and projection changes, meaning it's more robust
- You can now set the viewport shadow from the sun position angle, useful for solar analysis
- You can now set the georeferenced north from the Blender sun position
- 2D annotation now extracts from IFC files directly instead of Blender, and checks for bounding box intersection to determine which annotation to show
- Switching cameras now also activates the correct drawing styles on the fly
- You can now add arbitrary annotation to a drawing, not just from a set of presets
- You can now store arbitrary IFC data (attributes, properties, quantities, and type relations) in the SVG data, per drawing style
- You can now copy properties to selected object even if the property set doesn't exist yet
- 3 new default hatch styles for square hatches
- New hatch pattern for demolition
- Show error message if attempting to add a drawing to a sheet that hasn't been generated yet
- You can now export quantities related to a spatial element, not just non-spatial elements
- New debug panel lets you create shapes per STEP ID, useful for analysis of IFC geometric data
- Dumb walls are now based on vertices by default, not edges, for faster, dumber, walls :)
- You no longer need to select the entire project when exporting. If you have nothing selected, everything is exported to IFC. If you select things, only selected items will export.
- New feature lets you select high polygon meshes to help pinpoint why IFC files are so huge (looking at you, Revit!)
- You can now switch between drawings with one click from the properties panel in the 3D view
- The drawing list can now be manually refreshed in case you are manually creating drawings
- Stroke linecaps are now rounded. Nicer looking drawings, you know.
- The preset for cut objects for overall plans now includes IfcSpace, as it's quite common
- Text annotations in drawings can now be rotated
- If the active object is a camera, a new temporary section plane will now match the camera
- Text annotation now supports storing classes and IFC metadata in the SVG, like all other objects
- Drawing dimensions now have support for imperial unit formatting
- BIMTester can now audit for high polygon IFC geometry
- Implement new Model Federation MicroMVD in BIMTester
- Drawing styles can now store settings for render type, outlines, shadows, and lighting
- You can now add openings by selecting the filling element, not just the opening element, for convenience.
- The plan representation context is now exported by default. Less steps for 2D documentation!
- Add support for exporting site and building addresses for IfcSite and IfcBuilding
- Remove some deprecated representation item operators in the mesh properties panel
- Creating drawings is now much easier with less manual workarounds
- Users can now specify their own app to open SVGs and PDFs
- Bump to the latest IfcOpenShell, for more robust geometry processing

Fixes:

- Fix bug where adding text didn't work with the new scale system
- Improved material name canonicalisation, which fixes some import failures
- Fix bug where 2D annotation curves weren't probably exported
- Fix bug where plan relative level annotations were not projected correctly onto drawings
- Fix bug where enum properties wouldn't be exported
- Fix inaccurate and incorrect conversion to imperial units in quantity take off
- Fix bug where sometimes you can't add a representation context to an object
- Fix incorrect auditing of geolocation MicroMVD in BIMTester
- Fix bug where some shapes that use Blender modifiers are incorrectly detected as a wireframe
- Fix incorrect auditing of geocoding MicroMVD in BIMTester
- Fix bug where multiple presentation style assignments in IFC2X3 would get ignored in import

## v0.0.201025
Features:

- Exporting now sets the IFC file if unset for convenience
- IFC CSV now supports modifying IFC classes
- You can now set facet tolerances when importing
- Experimental native roundtripping mode, for experimentation only, with style support
- Visit wiki link in the add-on now points to specific Bonsai pages
- Material property sets are now imported
- IFCClash now optimistically skips coincident collisions, resulting in less false positives
- Increased maximum contact threshold for IFC Clash allows clash detection to work for larger projects
- IFC clash now uses iterator when a filter is specified for faster clashing
- Auto add owner histories when the user exports IFC2X3 if none is specified
- Classification trees are now stored in the Blend file, increasing portabilty of project data
- 16 New IFC visual programming nodes for Sverchok, including:
- Read IFC node
- Create IFC node
- Write IFC node
- Create Entity node
- By ID node
- By Guid node
- By Type node
- By Query node
- Select Blender Objects node
- Create Shape node
- IFC Add node
- IFC Remove node
- Generate IFC Guide node
- Read entity node
- Get property node
- Get attribute node

Fixes:

- Fix bug where spatial elements with a representation would import twice
- Fix bug where box representations don't respect project units
- Fix IFC clash bug where spatial elements are unaffected by user filters
- Fix bug where you can't export if a classification is only applied to a type or spatial element
- Fix export bug where you can't export if project units aren't explicitly set

## v0.0.201115
Features:

- New import model offset workaround for Bentley ProStructures
- Implement workaround when importing invalid aggregates from Bentley ProStructures
- You can now specify user coordinates to the ResetAbsoluteCoordinates recipe
- The ResetAbsoluteCoordinates now attempts to avoid changing placements but only focuses on geometry coordinates, preventing coordinate double ups in tricky patching situations
- Support importing IFC2X3 documentation information & reference dates, times, and file format mimetypes
- The validator now validates whether you are using abstract IFC classes
- Auto set file format settings when creating drawings in case you are doing your own renders as well
- Add support for multiple dimension objects per view
- New ability to round to nearest X for metric and imperial units
- New drop down UI to select area and volume units (thanks theoryshaw!)
- Log error in case users try to export an abstract class
- Coding style standardised to help onboard new developers (thanks htlcnn!)
- Add support for case insensitive file units when importing
- New interface to manage presentation layers (e.g. CAD layers) in IFC (thanks Krande!)
- You can now add / delete attributes in bulk by selecting multiple prior to adding
- New utility class for Python coders to query which psets / qtos apply to an IFC class
- You can now add / delete psets in bulk
- You can now add / delete qtos in bulk
- Add tooltips describing how to set external commands in preferences window
- Improve intuitiveness of reassigning the IFC class of the active object
- New IfcPatch recipe to extract elements into a separate IFC
- New UI for material, material layer / constituent / profile set management
- You can now convert from global to local coordinates
- New category for IFC export workarounds for RIB iTwo costing program
- New IFC workaround to export only triangulated geometry to Navisworks
- IfcSverchok "By Type" node now has a dropdown UI to help select classes 
- You can now export attributes of the material layer set and constituent set itself
- BIMTester is now more forgiving to run from any directory (thanks berndhahnebach!)
- New IFC inspector interface to help debug, inspect IFC data, and be a teaching aid for IFC
- IFC inspector supports expanding attribute lists and following a breadcrumb trail of nested references
- Add import support for all attributes of the material layer set and constituent set itself
- Support exporting more label metadata for material profile sets
- Improved export support for presentation layers which assigns to representations (thanks Krande!)
- New import support for presentation layers
- Deprecated IFC material lists are now auto upgraded into constituent sets
- Types with no geometry can now have material data imported
- New workaround for incorrectly geolocated Revit files to auto detect the geolocation
- Blender materials are now clearly consolidated into either materials or styles
- New UI to manage material property sets instead of needing to use external CSV files
- IFCCSV now continues executing even though it fails to change an attribute
- IFCCSV now skips GlobalIds it cannot find
- Now materials that aren't also used as a styled item can be exported independently
- New IfcOpenShell, with many new bugfixes

Fixes:

- Fix bug where attributes wouldn't import for some IFC classes
- Fix bug where non uniform translations of spatial elements are exported with strange transformations
- Fix error message when you switch drawing styles and a style it was referencing was deleted
- Fix bug where Views wasn't allowed to be in the IfcProject which prevented round-tripping
- Don't crash if you get invalid IFCs with missing attributes (thanks aothms!)
- Fix bug where setting north angle from a geolocated IFC was wrong
- Fix BIMTester error when creating a report with empty steps (thanks berndhahnebach!)
- Fix bug where importing multiple grids with the same name fails
- Fix bug where a styled item could be incorrectly assigned if an element has more than one context

## v0.0.201207
Features:

- Add support for IFC2X3 material data imports
- Vendor workaround for "treat styled item as material" now deprecated, as new material and style system is much better
- Add support for importing IFC material description and category attributes
- Native element roundtripping now supports layer assignments
- Native representation roundtripping now auto-fixes representations that aren't using contexts properly
- Improved packaging and refactoring for BIMTester makes it easier for other devs, including FreeCAD integration (thanks berndhahnebach!)
- Native geometry roundtripping now decouples surface styles
- Native geometry roundtripping now lets you change styles independently from geometry
- New experimental utility to upgrade IFC2X3 to IFC4, and downgrade IFC4 to IFC2X3 automatically
- Native geometry roundtripping now works across different IFC versions, so you can roundtrip and change schema at the same time
- Exporting classifications to different IFC schemas (including graceful downgrading) is now supported
- Support graceful downgrading of material definitions from IFC4 to IFC2X3
- Support built-in vendor workaround for importing invalid IFC properties coming from ArchiCAD
- Roundtripping geometry now works for geometry which has one to many relationships between geometry and styles
- Handle and gracefully accept invalid IfcGrid elements coming from Revit. Sigh.
- New experimental support for Non-IFC, Blender object clash detection
- IfcOpeningElements now only show as wireframes by default for convenience
- Roundtripping now enables openings by default, which works much better with the latest Blender boolean modifier
- The object property sets panel now also shows inherited psets from the construction type
- Improved UI for psets and qtos with collapsible panels and improved readibility
- New UI that shows inherited materials from the construction type if available
- Add support for exporting material sets for construction types
- All representation contexts are now round-tripped in native roundtrip mode, not just the body context.
- New powerful and intuitive smart clash grouping feature (thanks vinnividivicci!)
- The Optimise IFC patch recipe is now packaged with Bonsai
- The ExtractElements IFC patch recipe is now packaged with Bonsai, letting you extract a subset of elements from a larger IFC file
- Dumb grids are now auto placed in an IfcSite if it can detect one
- Drawings now have classes for material layer set names
- Improved usage descriptions for IFCCSV to help new users
- You can now smart tag material attributes in drawings
- New utility function to check is_a() in the schema without needing a file first
- Auto add the currently loaded IFC when creating a drawing for the first time
- You can now apply drawing styles to elements with material set usages
- New vendor workaround for exporting to the DESITE BIM application
- The Migrate IFC patch recipe is now packaged with Bonsai, letting you upgrade or downgrade IFC versions
- IFCs with invalid attributes are now gracefully exported with warnings when exporting to a schema which doesn't allow it to let the user fix it easily
- You can now bake parametric geometry into meshes

Fixes:

- Fix bug where no colour is set if only a styled item has a style but a material has no representation
- Fix default category to none, not load bearing, in case we import IFC2X3 where this property doesn't exit
- Fix bug where a material wouldn't get assigned for multiple mapped representations
- Fix warnings in copy attribute to selection tool
- Fix import bug where some IfcOpeningElements aren't placed in the correct openings collection
- Fix regression where the section cutting plane doesn't work unless you've selected an object
- Fix bug where a drawing can't be created with a file that uses material set usages
- Fix issue where invalidly declared representation contexts from other vendors can confuse drawing creation
- Fix bug where sometimes thes IFC class and product dropdowns get out of sync
- Fix import bug where duplicate material names with accents fail to import
- Fix bug where some aggregates can cause drawing generation to fail
- Fixed example script in the IfcOpenShell Qt GUI viewer
- Fix bug where spatial elements didn't get styles exported correctly

## v0.0.210131
Features:

- New "clean wireframes" feature lets you easily apply edge split modifiers to elements to create technical drawings
- New "link IFC" feature lets you easily append IFCs from another blend file to create a master file, good for large scale projects
- BIMTester can now generate a report immediately after running a test in the same command (thanks rbertucat!)
- HTML reports from BIMTester now specify an encoding for fancy characters (thanks rbertucat!)
- BIMTester can now load in a custom IFC schema (thanks rbertucat!)
- BIMTester now has a set of steps for testing aggregations (thanks rbertucat!)
- Dimensions in drawings now show arrowheads and dimension text (thanks qwiglydee/BIMVoice!)
- Improved naming for smart clash groups (thanks vinnividivicci!)
- New feature to save a BCF project
- You can now view and edit the BCF project name
- You can now set the BCF author
- You can now create new BCF projects
- You can now add new BCF topics to a BCF project
- New BIMTester translations into German and French (thanks berndhahnebach!)
- New BCF library available for developers to supersede the older BCFPlugin library
- New BCF library now has full BCFXML write and editing capabilities
- Equal dimensions in drawings now show "EQ" annotations
- New "Path" argument for BIMTester (thanks rbertucat!)
- BIMTester HTML reports now shows skipped tests (thanks rbertucat!)
- BCF comments are now shown in the UI as a subpanel instead of in the text editor which was pretty poor
- Improved BCF UI
- Optimised import now only considers surface styles, not all random styles
- Import optimised for files which have loads of aggregations
- New feature to snap spaces separated by wall gaps together to help create building energy models
- New annotation decorations in 3D for leader lines (thanks qwiglydee/BIMVoice!)
- New annotation decorations in 3D for stair arrows (thanks qwiglydee/BIMVoice!)
- New annotation decorations in 3D for hidden lines (thanks qwiglydee/BIMVoice!)
- BCF comments is now no longer read-only, you can now add/edit/delete comments
- You can now add/delete BCF viewpoints
- You can now add/delete BCF header files
- BCF FoV ranges outside 45-60 degrees are now supported
- 3D annotation decorations now support imperial units
- New button to add, as well as annotation decorations in 3D for break lines (thanks qwiglydee/BIMVoice!)
- New feature to copy the 3D grid to to active 2D drawing (thanks qwiglydee/BIMVoice!)
- Misc annotation are now decorated in 3D (thanks qwiglydee/BIMVoice!)
- You can now add/delete BCF reference links
- You can now add/edit/delete BCF topic labels
- You can now add/delete BIM Snippets in BCF
- You can now customise the CSV delimiter in IfcCSV (thanks htlcnn!)
- You can now add/delete BCF document references
- You can now add/remove related BCF topics
- New button to quickly open the drawing camera in the sidebar for usability (thanks htlcnn!)
- IfcClash can now export to BCFXML, which is super awesome! You can now use the results in other collaboration apps and cloud platforms!
- Grids are now decorated with grid labels in 3D (thanks qwiglydee/BIMVoice!)
- IfcClash can now generate image snapshots of clashes and store them in BCFXML
- IFC exporting is now super optimised, by writing directly from IFC itself in memory. As a user, this basically means that exporting to IFC is super fast - as fast as saving a native file.
- Importing now stores STEP ID links for key rooted elements as well as key semantic elements, like elements, materials, and styles
- IfcOpenShell pset utility module now handles all the possible syntaxes for ApplicableEntity, so you can determine exactly what psets are avalable for each element (thanks CyrilWaechter!)
- 3D annotation decorations now support anti-aliasing
- All IFC editing completely rewritten and refactored to use partial editing. As a user, this means zero IFC data loss during imports and exports for all geometric information as well as all non-geometric information.
- IFC import heavily optimised due to new partial editing paradigm. Expect IFC files to import twice as fast as they did before (or four times as fast if you were affected by the presentation layer regression bug in the last release).
- Entire UI completely redesigned to a more consistent UX, which is easier on the eyes with less nested boxes, and shows more IFC information
- New IfcOpenShell placement utility module for calculating relative coordinates
- Representations can now be added to any context. This includes invalid ones or contexts (i.e. not subcontexts) themselves, or those with missing target views
- Switching representations will now change all linked data objects too, not just the active object
- Optimisations and caching improvements to IfcOpenShell pset utility module (thanks CyrilWaechter!)
- When viewing IFC attributes, now the UI will distinguish between NULL/None and simply empty attributes - this means as a user you know whether or not the data is truly empty or if the BIM author simply hasn't gotten to it yet
- All IFC attributes intelligently now have a new UI depending on the data type. This means number sliders, true/false checkboxes, and dropdown lists to make it easier for users to get BIM data right.
- All enumeration options are now shown when editing attributes, so you can pick from the list instead of checking the spec.
- All attributes are detected from the relevant IFC schema version, so you can't accidentally put IFC4 data in an IFC2X3 file or vice versa
- You can now create fresh IFC projects prior to exporting to a file
- BIMTester can now output Zoom SmartView to visually zoom to failed tests (thanks berndhahnebach!)
- Grids are now auto resized to the drawing boundaries upon adding (thanks qwiglydee/BIMVoice!)
- IFC class dropdowns are now generated specific to the IFC schema version
- Psets now respect shared STEP IDs, so the one-to-many mapping is preserved
- Like attributes, psets and qtos now are sensitive to schema, data type, and distinguish between null vs empty
- Aggregations no longer use collection instances, which was a bit silly and confused a lot of users
- IfcPerson data is now imported. Previously it wasn't.
- IfcOrganisation data is now imported. Previously it wasn't.
- You can now edit the IFC organisation Identification attribute, which was previously missing from the UI
- New feature in IfcCOBie to let you process the currently loaded IFC file (thanks ihabelaghoury!)
- New annotation decorations in 3D for sections (thanks qwiglydee/BIMVoice!)
- Drawings can now detect other drawings and generate section references (thanks qwiglydee/BIMVoice!)
- BIMTester now has a dedicated standalone GUI (thanks berndhahnebach!)
- BIMTester has improved CLI arguments (thanks berndhahnebach!)
- New feature in IfcCSV to let you process the currently loaded IFC file (thanks ihabelaghoury!)
- IfcPatch is now packaged so you can install it separately as a Python module (thanks CyrilWaechter!)
- Full support for editing IfcMaterialList added!
- The reusability of material set relationships are now round-tripped
- Like attributes, materials now are sensitive to schema, data type, and distinguish between null vs empty
- User is banned from creating IFC2X3 material psets because they are annoying
- Accomodate custom pset templates for materials
- BIMTester BIM auditing tools have started to be translated to Italian and Dutch (thanks berndhahnebach!)
- IfcOpenShell geolocation utility can now apply geolocation transformations to matrixes, not just vectors
- "Fake geolocation" from offending IFC files which are handled as Blender offsets are now stored with a dedicated UI so the user knows if the geolocation is correct
- New Project UI to show basic project metadata about the currently active IFC project
- IfcPatch extract elements recipe now supports bringing across openings as well, not just the elements you're interested in (thanks FreakTheMighty!)
- You can now load new classification libraries on the fly
- You can now mix classification libraries with project references
- Remove setting to merge or import aggregates as the new aggregate import improvements make it obsolete
- IfcCSV now supports exporting information about the related containing spatial structure element, useful for creating schedules related to floors, buildings, or spaces
- New IfcOpenShell date utility module, because dates shouldn't be something we need to think about
- Groups are no longer shown in the tree where they typically clutter things and don't add value
- Openings are always imported now using Blender booleans
- Qto utils now use the bmesh volume calculation method, which after the upstream Blender bug was fixed, leads to more accurate volumes for quantity take-off
- New "remove deep" function in the IfcOpenShell element utility module for purging IFC data selectively (thanks aothms!)
- The huge MVD panel completely removed and reorganised into import, export, and geometry editing UI locations for improved usability
- New pie menu (press shift-E in the 3D viewport!) for quickly reaching common geometric editing functions
- Nicer presentation layers UI, more what you'd expect out of traditional CAD layers.
- Owner histories are now supported for adding new products, with proper history timestamp
- Export time is now output to console for convenience
- Writing 2D or 3D IFC curves from a Blender mesh is now possible in IFC2X3
- Editing attributes now supports updating ownership histories, with proper history timestamp
- Updating aggregates now supports updating ownership histories, with proper history timestamp

Fixes:

- Fix bug where selecting the IFC file for drawing generation didn't work
- Fix bug where aggregates where accidentally hidden when generating drawings
- Fix crash when creating drawings on Windows with Blender versions >=2.91
- Fix issue in selector utility when filtering with boolean values (thanks c4rlosdias!)
- Fix bug where IfcSverchok's IfcGetAttribute node would not work (thanks htlcnn!)
- A huge ton of IfcOpenShell improvements which I cannot fully summarise like geometry generation stability fixes, as well as crash fixes when removing elements as well as manipulating inverse relationships (thanks aothms!)
- Improved snapshot filename checking in the new bcf library (thanks htlcnn!)

## v0.0.210221
Features:

- BIMTester now operates on single feature files, which heavily improves usability
- BIMTester custom schema is now specified as an argument, not as a tester requirement, which is where it belongs
- BIMTester sentence quote usage is now standardised and always enable translations
- You can now load the active IFC file into a BIMTester audit. No need to export first!
- Now, users don't need to consider include curves and 2D annotations as they are always imported
- You can now specify a set of custom step definitions to BIMTester, go and write your own test definitions!
- New BIMTester web app mockup https://bonsaibim.org/bimtester/
- Validating IFCs UI now moved over into debug panel
- New create shape debugging tool to help determine broken or crashing elements
- Type representation maps are now shown in the IFC Representations UI panel
- Type representations are now always imported (better for authoring), and also import super fast compared to before (before, enabling types being imported would significantly slow down import times)
- Only IFC files are now shown in the export file dialog for a less confusing user experience
- IfcPatch is now callable from the command line (thanks htlcnn!)
- New IfcOpenShell.util.type module for checking applicable type classes.
- You can now assign types with a smart type filter, without needing to first import types into Blender
- New build script for IfcPatch to distribute binaries (thanks htlcnn!)
- IfcOpenShell date util now supports converting to IFC2X3 date entities
- Highly experimental script to convert from P6 XML into an IFC task tree
- Highly experimental script to convert from IFC task trees into a Gantt chart JSON for jsgantt-improved
- You can now edit parameters of parametric profile definitions in geometry.
- New basic UI to view tasks in an IFC file
- You can now add type instances, and mapped representations are enforced.
- STEP IDs are now shown for non-rooted elements, like grid axes.
- Blender now helps prevent saving Blender without having an exported IFC
- Improve UI to change spatial container to prevent accidentally selecting incorrect objects

Fixes:

- Fix bunch of error messages (commonly seen in IFCCSV) when you try to get a property value which is null
- Fix bug where BIMTester audit classes dropdown wouldn't show.
- There is now an ID and GUID map to Blender objects for easy access especially for devs
- Fix bug where Blender booleans wasn't good enough. Now we're back to IfcOpenShell with optional Blender conversion on a case by case
- Fix bug where unable to install add-on in older Blender versions
- Fix bug where switching representations would not work or create duplicated meshes
- Fix error when importing consecutive files
- Fix bug so that users can now reassign the IFC file location if it moves.
- Fix bug where vertex welded happened across representations (thanks aothms!)
- Fix bug where spatial objects with representations didn't import correctly
- Fix import bug where loading existing elements wouldn't work
- Fix crash on Windows when removing property sets (thanks aothms!)
- Fix crash when reassigning class (thanks aothms!)
- Fix unable to load IfcPatch recipes (thanks htlcnn!)
- Fix regression where dumb objects didn't get an IFC class
- Fix ability to create grids which was totally broken
- Fix bug when adding grids to drawings, which also was totally broken
- Fix bug where product and type representations wouldn't be linked data in Blender when importing
- Fix bug where representations wouldn't be purged correctly if they were part of a layer with many items
- Fix bug where you could create mapped representations without having a type product
- Fix bug where removing a mapped representation did not properly consider all mapped usages
- Fix bug where switching construction type didn't enforce appropriate representation maps
- Fix bug where you couldn't import two different IFC files in succession in the same Blender file
- Fix bug where only a light removal occured when removing elements. Now, a full geometry purge is done as well
- Fix bug regression in the absolute coordinate offset feature where I forgot to convert non-meter units
- Fix bug where geolocation was lost if you tried to edit an absolutely positioned file
- Fix bug where unable to install add-on due to clash with Blender-OSM. 
- Fix bug where you couldn't copy classes without representations.
- Fix bug so that null ownership histories in IFC4 are now allowed
- Fix bug where you couldn't edit the geometry of a grid axis
- Fix bug where copying a class did not enforce mapped representations
- Fix bug where removing mapped representations leaving you with nothing was a poor user experience

## v0.0.210404
Features:

- During local <-> global coordinate conversions you can easily get and set the 3D cursor
- New documentation written for IfcPatch
- Meshes are auto updated in the IFC when you export, so you don't need to explicitly update mesh representations
- Changing the name of a Blender object now also changes the IFC name
- Aggregate creations when importing large files is now faster
- Rebuild pset template authoring UI to be way less confusing and match the UX paradigm of other modules
- IfcOpenShell now has preliminary support for IDS (thanks aothms!)
- You can now automagically convert meshes into rectangular solid extrusions
- You can now automagically convert meshes into circular profile solid extrusions
- You can now automagically convert meshes into arbitrary profile solid extrusions
- You can now automagically convert meshes into arbitrary profile with voids solid extrusions
- BIMTester now supports both MicroMVD features or IDS for your BIM audit specifications
- New module to integrate with Augin to easily upload your IFCs into an augmented reality (AR) platform!
- Experimental gizmo for changing parametric extrusion depths (thanks qwiglydee!)
- You can now reassign classes in bulk
- Minor usability fix to denote if a pset has no properties set
- Powerusers can now toggle hiding of null / empty properties
- Nullness auto-toggles when editing properties. Neat. One less click! (thanks BIMVoice for the suggestion!)
- We ship IfcConvert with the add-on now.
- IFC drawings now store camera extents as IfcBlock. Note: still experimental.
- You can now view, add, edit, and remove IFC groups.
- You can assign and unassign products to IFC groups.
- The "Allow non-element aggregates" workaround for ProStructures is now deprecated. It's handled automagically.
- Materials will now distinguish between IfcMaterialLayerSet and IfcMaterialLayerSetUsage
- Experimental support for Python 3.9 for those on custom or alpha builds of Blender 2.93 and above.
- Add support for square and cubic decimetre units.
- You can now add IfcMaterialLayerSetUsage to elements
- You can now reorder items in a material layer, constituent, or profile set
- You can now case insensitively search for psets, properties, and attribute names
- Automatic daily Blender developer builds are now available on Github for those who don't want to wait for stable releases for features / fixes (thanks krande!)
- You can now unlink objects and styles of elements that you've lost the original IFC of, to recover broken files
- You can now bulk assign / unassign construction types
- Upgrade / uninstall instructions are now provided in the add-on preferences UI to prevent users running into half upgraded issues
- Adding drawings now creates the necessary groups and psets, with an experimental integration with IfcConvert. Note: highly experimental and incomplete!
- Add support for nano and micro metre units. Who are these people using these units anyway? What is this, a house for ants?
- Reimplement support for creating structural curve representations
- You can now import structural curve members (again)
- You can now author (add / edit / remove / assign / unassign) structural analysis models (thanks Jesusbill!)
- You can now delete objects in bulk
- Experimental operator to do efficient deep purges for devs, if stable, will result in way faster object deletions in a future release (thanks aothms!)
- The IFC Debug inspector now also shows inverse references, great for debugging IFC2X3 files or style relationships for example
- You can now import structural curve connections (thanks Jesusbill!)
- Structural entities during import now don't spam spatial tree warnings (thanks Jesusbill!)
- Object placements are now updated on export automatically in case you forgot to sync them in authoring mode
- You can now import structural point connections
- Structural elements are now organised in collections (thanks Jesusbill!)
- ExtractElements IfcPatch recipe now retains aggregation relationships
- Swept solids are now natively handled again during imports for faster rebar imports
- You can now view / add / edit / remove structural boundary conditions for connections points
- Improve usability to run IfcPatch recipes without typing in arguments
- BCF now documents its requirements.txt file for devs (thanks TestPrab!)
- You can now import and export IfcCSV with the current active IFC in memory without first writing to disk. Nice. Bulk editing!
- You can now view structural member connections (thanks Jesusbill!)
- New utility function for getting primitive data types of attributes for devs
- Brand new ifcopenshell.api for devs. Basically, now you can easily automate any behaviour in the add-on via your own scripts. Also, you can use the entire capabilities of the add-on without even needing Blender.
- Upon export, it now synchronises any objects you've deleted from your scene, so you can just do regular Blender deletes instead of pressing the "X" button
- You can now select objects in the viewport from the IFC Debug Inspector via their GlobalID. (thanks ihabelaghoury!)
- Ownership history tracking is now implemented in roughly half of the operations now. Getting closer towards full coverage, where we can then start tackling version control!
- OCC is no longer loaded on startup, to prevent clashes with other add-ons.
- You can now edit structural boundary conditions on member connections themselves. (thanks Jesusbill!)
- You can now add and remove work plans for construction sequencing. (thanks bosonprojets and Jesusbill!)
- You can now remove structural connection conditions (thanks Jesusbill!)
- You can now add new structural connections to members
- Point connections are now supported as proper entities with a placement and vertex, instead of a special empty object (thanks Jesusbill!)
- A reference graph view is now auto created for convenience when creating a structural analysis model
- You can now view, add, and remove cost schedules.
- Geolocation utilities now supports converting either X or Y axes for checking grid north vs true north vectors
- You can now get and set true north rotation independently of grid north

Fixes:

- Fix bug where selecting high polygon meshes for debugging fails
- Fix bug where Blender offsets were not considered in local <-> global coordinate conversions
- Fix bug where cursor was not placed in the right unit after a local <-> global coordinate conversion
- Fix bug where undo operations might invalidate the internal ID map and break everything
- Fix regression where IFC files were loaded twice during import. What a waste.
- Fix bug where properties which IfcCountMeasure data types and similar were not editable
- Fix bug where existing Blender offsets weren't used when importing two offset models consecutively. This helps with model federation.
- Fix bug where you could add psets of the same name multiple times
- Fix bug where you couldn't do import profiling on Windows. (thanks erab!)
- Fix bug where sometimes cartesian point offsets wouldn't get correctly detected for poorly geolocated files.
- Fix bug where nested aggregates failed to import
- Fix bug where material / style UI was showing without a loaded IFC
- Fix bug where assigning new constituent or profiles to a material set was broken
- Fix bug where you couldn't assign a window or door type
- Fix bug where loading pset templates makes it unable to install on Windows
- Fix bug where you couldn't add layers to a fresh project
- Fix bug on Windows where sometimes the body representation wouldn't be loaded by default
- Fix bug where the iterator might not not know if a geometric set was 2D or 3D (thanks aothms!)
- Fix bug where quantities couldn't be extracted in IFCCSV (thanks plaes!)
- Fix fundamental bug in utilities where coordinate placements were not correctly resolved
- Fix bug where nested aggregates were not nested in the scene during import
- Fix bug where getting applicable psets didn't work on subsequent calls (thanks CyrilWaechter!)
- Fix bug in BCF where it treated project data as mandatory instead of optional, leading to failed BCF loading
- Fix bug in BIMTester where it doesn't run if you have multiple drives on Windows (thanks rbertucat!)
- Fix fatal bug where languages were not bundled with the add-on so you couldn't even run BIMTester
- Fix bug in IfcCSV where the delimiter was not specified correctly for non-English locales
- Fix bug where you couldn't set logical properties in psets.
- Fix bug where IFCXML support was seemingly not enabled. (thanks aothms!)
- Fix bug where the IFC schema had a typo which made it impossible to add IfcTransformers
- Fix bug where you couldn't even add IFC type instances for IFC4. Nasty.
- Fix bug where assigning a spatial container didn't also update the object placement tree
- Fix bug where Blender loses precision for geolocation metadata.

## v0.0.210605
Features:

- Add support for quads in meshes when converting from DXF to IFC. Thanks brunopostle!
- Work plan attributes can now be modified
- Work schedule attributes can now be modified
- Work calendar attributes can now be modified
- You can now assign and unassign project declarations for project libraries
- Geolocation MicroMVD now supports checking true north
- You can now add / remove material profiles in a profile set. Thanks Jesusbill!
- You can now assign parameterized profiles to material profiles. Thanks Jesusbill!
- You can now edit cost schedule attributes. Thanks Jesusbill and SigmaDimensions!
- Cost items can now be added to cost schedules, as well as child cost items. Thanks Jesusbill and SigmaDimensions!
- You can now just select doors / windows when adding voids for usability.
- You can now create IFC project libraries
- Assigning aggregates can now be done in bulk
- Structural member axis orientation can now be specified. Thanks Jesusbill!
- Spatial container assignment can now be done in bulk
- You can now assign summary tasks to a work schedule. Thanks SigmaDimensions!
- You can now toggle expansion of the cost schedule tree.
- Material profile set usages are now supported. Thanks Jesusbill!
- Spatial aggregations are now auto-assigned upon creation.
- Spaces are now always imported by default, using the same spatial tree structure for consistency.
- Multiple cost item summaries are allowed and you can now remove cost items.
- You can now assign task trees to work schedules. Thanks SigmaDimensions!
- Removing subgraphs of the IFC now uses batching by default. Thanks aothms!
- If you are already authoring a file, exporing no longer prompts for a file location
- You can now copy classes in bulk
- You can now edit task attributes. Thanks SigmaDimensions!
- New UI to edit both task trees and task attributes.
- You can assign task predecessors and successors. Thanks SigmaDimensions!
- Collection assignments for spatial structure are now auto synced on export
- You can now load project libraries and browse type products
- Selecting an IFC file dialog now only filters IFC files for convenience
- In a project library, you can now toggle declared products
- New support for task times. Thanks SigmaDimensions!
- Work schedule UI now shows start and finish times.
- You can now assign / unassign building elements as constructed products to tasks
- You can now generate gantt charts from work schedules
- You can now append product types from another project or project library into your project
- You can now assign products to cost items. Thanks SigmaDimensions!
- You can now import work schedules from P6 XML exports
- You can now add crew and subcontractor resources
- New bSDD library for developers
- Resources may now be assigned and unassigned to products. Thanks SigmaDimensions!
- You can now edit cost item quantities.
- You can now edit cost item values with subtotal calculations.
- New "cha-ching" noise when you're checking out cost schedules
- You can now assign derived quantities from products to cost items
- You can now import predecessors and successors from P6 XML
- "Counting" cost quantities now auto count the number of assigned products for convenience
- Work schedules can now be assigned to work plans. Thanks SigmaDimensions!
- OAuth support in bSDD now available.
- New work calendar UI.
- New system to modify calendar working and exception / holiday times, with support for recurring times.
- Improved time and date support in date utilities.
- Support all recurrence types and time periods in work schedules
- Pset API usecases are now decoupled from Bonsai
- P6 XML root level activities are now supported on import
- Support assign, edit, and unassign lag times for task sequence relationships
- Support importing calendars from P6
- Support multiple versions of P6 XML imports
- Support importing P6 sequence types
- You can now edit sequence relationship attributes. Thanks SigmaDimensions!
- You can now select all products assigned to a task. Thanks SigmaDimensions!
- New support for IfcDuration in date utility.
- Support purging when removing nested tasks in a schedule
- Grouped tasks now support deriving start, finish dates, and elapsed durations in the task tree
- Support importing activity and calendar assignments from P6
- You can now visualise construction progress at a particular date in your work schedule
- You can now generate construction sequencing animations within a date range
- You can now change animation speeds for generated construction sequences with different speed controls
- You can now add, edit, and remove structural load cases. Thanks Jesusbill!
- Microsoft Project XMLs can now be imported as construction sequencing schedules. Thanks SigmaDimensions!
- Support nested tasks in MS Project XML imports
- Add support for point orientations for structural analysis. Thanks Jesusbill!
- Implement support for adding / removing load groups. Thanks Jesusbill and ihabelaghoury!
- Arithmetic formulas are now supported for cost value components
- New IfcPatch recipe to clean up IFCs that store quantities in properties instead of quantity sets
- New IfcPatch recipe to convert units of an IFC file
- Calendars can now be shown in the work schedule task tree
- Derived durations now calculate working days based on the working calendar
- Calendar task inheritance is now supported
- P6 XML lag times are now imported
- Updating durations of task now auto refresh the finish dates based on the calendar
- New module structure for BCF XML v2.1 and v3. Thanks TestPrab!
- You can now edit a structural connection coordinate system. Thanks Jesusbill!
- User friendly drop down to select relevant quantities for associated products on cost items
- Links cost item products now auto update quantities when they are assigned or unassigned
- New utility functions for copying and deep copying IFC elements
- You can now copy cost values from one cost item to another
- You can now filter products assigned to a cost item or schedule
- Implement structural load management and assigning activities with named loads. Thanks Jesusbill!
- Importing IFC4 files with tessellation meshes are now significantly faster (like 8x). Thanks aothms!
- Qto module has now various methods to do bulk object quantification and quantity populating
- IFC drawings now roundtrip as a Blender camera object
- Mesh evaluation when updating geometries is now faster thanks to disabling boolean calculations. Thanks s-leger!
- You can now select all products that are part of a group
- Old annotation system now creates IFC elements again. Text and misc animations now work with the new WIP drawing system.
- Users can now regenerate the linework or annotation layers in the new WIP drawing system.
- BCF imports now autodetect the BCF version. Thanks TestPrab!
- 2D representations are now reimplemented in the new WIP drawing system.
- OCC is now no longer necessary, resulting in less conflicts with other addons and a significantly smaller filesize.
- Assigning a representation to a type product now syncs the mapped representations of all product type instances
- Project and version data for BCF XML v3 is now supported in the library. Thanks TestPrab!
- New support for API listeners for parametric modifications when authoring native IFCs.
- The search UI is only shown if an IFC is present.
- New UI to add type instances.
- Adding a new type instance now snaps it to the storey you're working on
- Typed dumb walls now inherit wall thicknesses from the type material
- You can now generate walls from sketching
- New wall join tool with support for T-junction joints, butt joints, and mitre joints
- You can now unjoin walls
- You can now join walls in bulk
- Stroke generated walls now auto detect joints where possible
- You can now generate walls from the cursor position, perpendicular to walls in the current storey
- Improved handling of non-manifold elements with openings. Thanks aothms!
- Polygons coplanarity is ensured when updating geometry. Thanks s-leger!
- New wall align tool with support for center, interior, and exterior alignment
- New formwork calculation tool to generate formwork meshes
- Dumb walls now auto calculate length, width, height, and simple volumes
- Dumb walls now auto generate wall axis upon updating
- 2D curve geometry can now be created again. Thanks s-leger!
- Copying objects in Blender now auto-copy them in IFC too. Thanks theoryshaw and s-leger!
- Layer set usages now inherit the layer set from the typed product.
- Total layer set thickness is now shown in the UI
- BCF XML v3 now supports all asspects of BCF XML v3 except for the new documents system in the library. Thanks TestPrab!
- Dumb walls now auto update thickness if the layer thickness changes.
- New datepicker UI in the visualiation interface. Thanks htlcnn!
- New wall tool with hotkeys for rapid wall creation.
- New wall flipping feature, with support for aligned walls.
- Super barebones UI to show space boundaries for energy analysis.
- Point lights (IfcLightSourcePositional) are now supported and can be exported. Thanks Ilkin!
- New wall split feature.
- MVDs now reflect the design transfer view by default.
- IFC header metadata can now be edited.
- API listeners can now be removed. Thanks s-leger!
- IfcOpenShell API now uses standardised Pythonic setting names
- Raster underlays are now supported in the new WIP drawing system.
- New walls are now selected when created.
- Project data directory is now customisable and actually works.
- Dumb slabs are now parametric and inherit thicknesses from their type materials
- Changing wall types now auto updates the thickness
- Updating any attribute (duration, start, or finish now calculates the other attributes)
- Parametric engines are now loaded on startup
- Experimental usecase serialisation feature in preparation for version control and logging
- Dumb slabs now update thicknesses based on layer thicknesses and type assignment if changed
- Dumb slabs now roundtrip the Blender solidify modifier
- New feature to recalculate schedule metadata including early start and finish dates, late start and finish dates, total float, and critical paths.
- Schedule metadata is now calculated using calendar dates
- Dumb walls and slabs are now always exported as parametric solids instead of meshes

Fixes:

- Fix rotation check in geolocation MicroMVD validation
- Fix bug where people and organisation Id data was not recorded in IFC2X3. Thanks SigmaDimensions!
- Fix bug where syncing upon export was just broken
- Fix bug where extrusion direction was incorrectly detected for some mesh to solid conversions
- Fix bug where partial imports broke when whitelisting only spatial elements
- Fix bug where presentation layers couldn't be added
- Fix bug where dropdowns didn't refresh when you started a new file
- Fix bug where adding a new material didn't make it available for assignment to objects
- Fix bug where editing pset templates just broke
- Fix bug where saving is done twice in authoring mode. Thanks theoryshaw!
- Fix bug where box representations could be duplicated when adding new bodies and ensure that styles are synced. Thanks theoryshaw!
- Fix bug where edit mode syncing didn't work if you edited many objects at once
- Fix bug where you couldn't assign objects to a freshly created layer
- Fix bug where import mesh cleaning would inadvertently mark meshes as edited
- Fix bug where syncing was not maintained across file saves
- Fix bug where you shouldn't be able to reassign classes of non-rooted elements
- Fix bug where deletion syncing may fail on freshly created objects
- Fix bug where a new Blender file will remember old pset templates and libraries.
- Fix crash when pressing undo after assigning an IFC class to an object.
- Fix bug where UI didn't update when a type name was changed. Thanks theoryshaw!
- Fix bug where migrating an IFC version may explode the filesize.
- Fix bug where activities not in WBSes wouldn't import from P6 XML.
- Fix bug where empty material slots caused errors
- Fix bug where edit pset usecase didn't import the right module. Thanks brunopostle!
- Fix bug where related openings weren't deleted if you deleted a product.
- Fix bugs related to grid name syncing, axis delete and copy, and grid deletion
- Fix bug where objects might be unlinked from non IFC collections. Thanks s-leger!
- Fix bug where the logic behind detecting swept disk geometry was faulty. Thanks s-leger!
- Fix bug where assigning types and synchronising geometry was unstable.
- Fix crash when switching representations for type products
- Fix bug where IFC2X3 files did not correctly generate 2D representations
- Fix bug where you were unable to remove a representation
- Fix bug where type instance cubes were missing a face.
- Fix bug where active object edits would not be synced
- Fix bug where certain objects couldn't be deleted. Thanks theoryshaw!
- Fix bug where objects with the same name failed to be synchronised
- Fix bug where switching drawings didn't work when in a local view.
- Fix bug where drawings couldn't have a slash in their name
