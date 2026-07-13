---
title: "Building Envelope Specification"
url: "/openstudio-openstudio-application-building-envelope-specification/"
parent: "/openstudio-openstudio-application/"
aliases: ["/OpenStudio/OpenStudio_Application/Building_Envelope_Specification/"]
categories: ["OpenStudio Application"]
lastmod: "2025-04-22T18:30:08Z"
---

The process of defining the envelope of a building for a building energy model consists a few core steps[^1]:
1. Weather
1. Building Envelope Geometry
1. Surfaces
1. Constructions
1. Sub-surfaces

## Envelope Geometry and Building Spaces
There are several ways that building and space geometry can be built and brought into OpenStudio.
1. [OpenStudio Plug-in in SketchUp](/openstudio-openstudio-sketchup-plug-in/) can be used for generating detailed models that cannot be built only within 2D models.
1. Any computer aided drafting (CAD) program that can export geometry to the Green Building Extensible Markup Language (gbXML) format can be used as well, as OpenStudio can import gbXML files.
1. OpenStudio includes a [built-in JS floor plan space editor](/OpenStudio/OpenStudio_Application/FloorspaceJS/) that can be used to develop 2D floor plans of the building. Note that the JS floor plan space editor can be used to create modify plans built in the JS editor, but cannot be used to modify imported gbXML files.
1. The OpenStudio API can also be used to procedurally create geometry for OpenStudio models.

OpenStudio Coalition recommends that more complex building geometry is best developed in a full featured CAD tool and exported to gbXML, as FloorspaceJS best covers simple building geometry use cases only[^2].

### Spaces
The geometry of an OpenStudio model at its base comprises three-dimensional volumes called spaces. These spaces correlate closely with rooms, and their corresponding internal loads, schedules, and other energy load related information. OpenStudio supports the create of space templates, called an OpenStudio Space Type. It is possible to assign one space type to each space. Note that the concept of spaces is not currently supported by [EnergyPlus](/energyplus/), and is an OpenStudio specific object.

OpenStudio spaces can be assigned to thermal zones. Each thermal zone can contain one or more spaces. As thermal zones are composed of spaces, the geometry of a thermal zone is defined by spaces. Thermal zones are supported and defined by EnergyPlus. *Building Energy Modeling with OpenStudio* recommends that spaces be created only as small as required to define the different activities and uses within a building, while also supporting appropriate thermal zoning.

#### Advice Drawing Geometry
It is recommended for most accurate model creation to:
1. Draw exterior walls on outside face of exterior walls.
1. Draw interior wall aligned with center of walls inside building.

### Surfaces
The volumes of spaces are defined by surfaces. Surfaces are infinitely thin, two-dimensional polygons that separate the inside of a space from the outside. In addition to having edges associated with the polygons, surfaces also have directionality (which side of the face is up and which side is down). The normal vector of a surface (calculated by right-hand rule) should always point out of space. 

Each surface can be classified as either a wall, floor or roof/ceiling. An additional parameter of a surface also specifies the outside boundary condition applied to a surface. The different types of boundary conditions are:
- Outdoor Surface
- Ground Surface
- Interior Surface
- Adiabatic Surface

Note, that the default behavior of the OS SketchUp Plug-in is to draw the surfaces of space reversed. This can cause negative volume errors[^3]. It is possible to manually reverse faces, and also a script exists to reverse the order of surfaces (assuming you have an array of those surfaces):

surface.setVertices(OpenStudio::reverse(surface.vertices))

### Constructions
Each surface has an associated construction. The construction is composed of layers of materials. Materials must be assigned properties associated with heat transfer characteristics. Wall assemblies, such as metal stud with insulation, must be modeled with the properties of the entire assembly. EnergyPlus will treat the assembly as a uniform surface for heat transfer calculations. OpenStudio comes packaged with common materials and assemblies. Further materials and assemblies can be found in the [Building Component Library](/openstudio-building-component-library/).

## Notes


[^1]: Brackney, L., Benne, K., Macumber, D., & Parker, A. (2018). Building Envelope Specification. In Building Energy Modeling with OpenStudio (pp. 13–58). essay, Springer International Publishing AG.
[^2]: The OpenStudio Coalition. (2025). FloorspaceJS - OpenStudio Coalition User Docs. Openstudiocoalition.org; The OpenStudio Coalition. https://openstudiocoalition.org/reference/geometry_editor/
[^3]: Unmet Hours. (2023). Unmethours.com. https://unmethours.com/question/92975/how-to-fix-negative-zone-volume/
