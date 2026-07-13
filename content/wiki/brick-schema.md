---
title: "Brick Schema"
url: "/brick-schema/"
aliases: ["/Brick_Schema/"]
categories: ["Building Energy Modeling (BEM)"]
lastmod: "2022-03-13T20:19:13Z"
---

> **Stub:** This article needs expansion.


The Brick Schema is an open-source effort to standardize semantic descriptions of the physical, logical and virtual assets in buildings and the relationships between them. The Brick schema is defined using the [Resource Description Framework](https://en.wikipedia.org/wiki/Resource_Description_Framework), a building block for the Semantic Web and Linked Open Data. Brick defines a graph of the entities in building, and the relationships between them. 

Brick is often used to describe the equipment and sensors of a building, and is most common in the Building Automation and Controls field, as well as in [Building Energy Modeling (BEM)](/building-energy-modeling-bem/), but can be used for many applications in the built environment.    

## Example
## History and current status
Brick was originally developed through a collaboration between researchers from seven different universities and research labs, and was presented at [BuildSys 2016](https://dl.acm.org/doi/10.1145/2993422.2993577). Brick is now managed through a non-profit consortium, which includes many of the original research universities as well as industrial members. Brick is open-source and released under the [BSD](/bsd/) license. 

Brick 1.1 was released in 2019, and Brick 1.2 was released in 2021. The next version of Brick, 1.3, will be released in early 2022. Brick 1.3 will include support for linking Brick models to realtime sensor networks such as [BACnet](/BACnet/), which will support digital twin use cases. 
 
## Brick compared to IFC
Although there is some overlap between the two, Brick is largely complementary to [IFC](/ifc-industry-foundation-classes/) and in particular to the [IFC classes](/ifc-industry-foundation-classes-ifc-classes/). Brick contains a more detailed set of equipment and sensor types. Brick does not define its own geometric types, and spatial information is largely limited to topologic relationships such as 'contains', and spatial classifications, such as 'Classroom', 'Building', 'Parking Structure', etc.   

However, because Brick is based on RDF, Brick models can use other RDF schemas to include geographical and geometric information. For example, a model using Brick can use the [GeoSPARQL](https://www.ogc.org/standards/geosparql) standard to provide GIS coordinates for objects in the Brick graph. 

An IFC file can link to a Brick model using an IfcLibraryReference. For example, in the IFC model, an air handler unit in the model can use an IfcLibraryReference to include the identifier for that same AHU in the Brick model. Applications can use that link to combine information from both the IFC and the Brick model. 

## External Resources
- [Brick Schema and Consortium homepage](https://brickschema.org/)
- [Brick Schema on Github](https://github.com/brickschema/brick)
