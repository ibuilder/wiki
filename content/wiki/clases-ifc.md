---
title: "Clases IFC"
url: "/clases-ifc/"
aliases: ["/Clases_IFC/"]
categories: ["Industry Foundation Classes (IFC)"]
lastmod: "2021-01-12T01:23:16Z"
---

Cuando hablamos acerca de conceptos BIM, nos referimos a objetos como muros, puertas y ventanas. Algunas veces nos referimos a elementos "no-objetos" como edificios, materiales y anotaciones. También nos referimos a otros conceptos como coordenadas, propiedades y geometría. Cada elemento, objeto, concepto o sustantivo a los que nos referimos son "Clases" en IFC, y a partir de éstos es que proviene el nombre "[Industry Foundation Classes](/ifc-industry-foundation-classes-clases-fundamentales-de-la-industria/)". El uso del término "clase" en vez de "elemento" o "concepto" proviene de la industria de desarrollo de software.

Todos los datos digitales en IFC pertenecen a una clase IFC. Las clases IFC pueden ser agrupadas en dos grandes categorías: *rooted* (enraizadas) y *non-rooted* (desenraizadas). Las clases *Rooted* heredan atributos de una clase IFC llamada <code>IfcRoot</code>, mientras las *non-rooted* no heredan nada. Esta clase <code>IfcRoot</code> es especial porque provee los siguientes cuatro atributos:

| Atributo | Requerido | Descripción |
| --- | --- | --- |
| <code>GlobalId</code> | Si | Identificador único del objeto, generado por la computadora. Es usualmente creado automáticamente por la herramienta BIM utilizada. |
| <code>OwnerHistory</code> |  | Este atributo especial puede almacenar nombres, fechas, organizaciones, proveedores de software y detalles del contacto de personas que son responsables del objeto. Usualmente es creado automáticamente por la herramienta BIM utilizada. |
| <code>Name</code> |  | Contiene un texto corto, el nombre del objeto. |
| <code>Description</code> |  | Una descripción del objeto. |
Todas las clases *rooted* son semánticamente significantes para los usuarios finales, y creadas específicamente para un proyecto o biblioteca. Algunos ejemplos son <code>IfcProject</code>, <code>IfcBuilding</code>, y <code>IfcWall</code>. Normalmente son registradas en la documentación, o nombradas específicamente en cronogramas del proyecto. Estos objetos son generalmente útiles para los usuarios finales, y por esta razón pueden ser rastreados con un <code>GlobalId</code> y nombrados con un <code>Name</code>.

En contraste, las clases *non-rooted* no tienen la capacidad de poseer un <code>GlobalId</code> ni un <code>Name</code>, y son utilizadas para almacenar datos no específicos del proyecto como coordenadas XYZ, valores de colores RGB, vectores, etc. Un ejemplo es <code>IfcCartesianPoint</code>. Son necesarias desde una perspectiva técnica, son usualmente generadas automáticamente por la herramienta BIM utilizada y pueden ser ignoradas por los usuarios finales. Sin embargo es importante saber que existen, ya que los usuarios avanzados pueden encontrarlas al intentar optimizar los datos [OpenBIM](/openbim/).

Las clases son a menudo descriptas como lo que heredan. Por ejemplo, las clases *rooted* pueden ser descriptas como clases que heredan atributos de <code>IfcRoot</code>, o subclases de <code>IfcRoot</code>.
Si una clase se desprende de otra clase, o es una subclase de otra clase, hereda las mismas características de esta clase, como la capacidad de poseer ciertos atributos, propiedades o relaciones asignadas a ella. Las subclases en realidad no heredan los valores de los atributos en sí, sino sólo la capacidad de tener ese atributo.

## Subclases de <code>IfcRoot</code>
Las clases *Rooted* pueden ser despiezadas en los siguientes tres tipos de clases:

| Clase IFC | Descripción |
| --- | --- |
| <code>IfcObjectDefinition</code> | Estas subclases describen objetos o cosas que están relacionadas con la industria AEC. Esto incluye muros, personas y tareas. Se pueden entender como los "sustantivos" de IFC. |
| <code>IfcPropertyDefinition</code> | Estas subclases describen propiedades de objetos y cosas. No son por sí mismas un objeto sino una propiedad o cantidad, como resistencia al fuego, uso energético o volumen. |
| <code>IfcRelationship</code> | Estas subclases describen relaciones entre los objetos, entre propiedades o entre objetos y propiedades. La relación puede ser de objetos que contienen a otros objetos, que se conectan con objetos, que tienen "inputs" y "outputs" en el sistema, o que son asignados a una propiedad o cantidad. |
## Subclases de <code>IfcObjectDefinition</code>
Si bien hay muchas subclases IFC, hay sólo algunas relevantes para autores BIM, y es útil tener un resumen de ellas. Debajo de estas pocas hay muchas subclases que profundizan en el detalle, pero conocer estas amplias categorizaciones ayuda a comprender los datos IFC. La siguiente tabla no está completa.

| Clase IFC | Descripción |
| --- | --- |
| <code>IfcContext</code> | Esta categoría especial contiene el punto inicial de los datos IFC, describiendo tanto a un proyecto como a una biblioteca. Sólo posee dos subclases: <code>IfcProject</code> y <code>IfcProjectLibrary</code>. Revisa [proyectos y contextos IFC](/ifc-projects-and-contexts/) para más información. |
| <code>IfcElement</code> | Esta clase contiene los clásicos elementos de construcción físicos como losas, columnas, vigas, carpitenrías, cañerías, cables, ductos y demás. Algunas subclases de <code>IfcElement</code> son <code>IfcColumn</code>, <code>IfcBeam</code> y <code>IfcFurniture</code>. Pueden tener una geometría asociada. |
| <code>IfcSpatialElement</code> | Estas clases describen conceptos espaciales, como sitios, edificios, puentes, pisos y espacios. Estas clases <code>IfcSpatialElement</code> pueden contener elementos <code>IfcElement</code>, como una losa contenida en  
un piso del edificio. Algunos ejemplos de subclases de <code>IfcSpatialElement</code> son <code>IfcSite</code>, <code>IfcBuilding</code> y <code>IfcSpace</code>. |
| <code>IfcElementType</code> | Estas clases describen tipos constructivos. Un tipo constructivo puede ser asignado a un <code>IfcElement</code>, igual que un particular <code>IfcWall</code> debe tener un particular tipo constructivo de dos capas de might have a particular construction type of 2 layers of plasterboard on a metal frame. Example subclasses of <code>IfcElementType</code> include <code>IfcWallType</code>, <code>IfcDoorType</code>, and <code>IfcWindowType</code>. |
| <code>IfcStructuralActivity</code>, <code>IfcStructuralItem</code> | These are useful for structural analysis. They hold data to describe an anaytical model, including members, nodes, connections, loads, and forces, as well as the results from the calculations. Example subclasses include <code>IfcStructuralCurveMember</code>, <code>IfcStructuralPointConnection</code>, and <code>IfcStructuralPointReaction</code>. |
| <code>IfcActor</code>, <code>IfcControl</code>, <code>IfcProcess</code>, <code>IfcResource</code> | These are useful for scheduling information, describing responsibility, tasks, resources, and timelines for construction sequencing or project planning. Example subclasses include <code>IfcTask</code>, <code>IfcConstructionMaterialResource</code>, and <code>IfcWorkSchedule</code>. |
## Subclasses of <code>IfcPropertyDefinition</code>
The following non-exhaustive table describes common subclasses used to describe properties, which can later be assigned to objects.

| IFC Class | Description |
| --- | --- |
| <code>IfcPropertySet</code> | These classes help store properties of other classes, such as <code>IfcElement</code>. For instance, it may store a fire rating associated with an <code>IfcWall</code>. Some properties names and values are standardised within IFC, but end-users can also create their own properties. See [IFC attributes and properties](/ifc-attributes-and-properties/) for more information. |
| <code>IfcQuantitySet</code> | This is similar to <code>IfcPropertySet</code> but focuses on calculated quantities (lengths, areas, volumes, weights, etc). Some quantity names and values are standardised within IFC, but end-users can also create their own quantities. See [IFC attributes and properties](/ifc-attributes-and-properties/) for more information. |
| <code>IfcPropertyTemplateDefinition</code> | If you don't want to actually to store the value of a proprety but instead want to describe a template of what properties exist, which are required, and what data is valid for the purposes of exchange requirements or company standards, then this template subclass allows you to do so. |
| <code>IfcPreDefinedPropertySet</code> | For some reason, some properties to do with door and window linings are given a special status in the IFC schema and have their own category. This will likely disappear in the future and merge into <code>IfcPropertySet</code>. |
## Subclasses of <code>IfcRelationship</code>
Although there are many IFC subclasses, there are only a handful relevant to different BIM authors, and it is useful to provide a summary of them. Underneath these handful are many subclasses which go into more detail, but knowing these these broad categorisations exist help with an understanding of IFC data. The following table is not exhaustive.

| IFC Class | Description |
| --- | --- |
| <code>IfcRelAssigns</code> | This relationship is used when a particular object supplies a resource or fulfills a task for another object. It is commonly used for resource management and construction sequencing, determining processes, resources, and actions performed by people. Example subclasses include <code>IfcRelAssignsToResource</code>, <code>IfcRelAssignsToProcess</code>, and <code>IfcRelAssignsToProduct</code>. |
| <code>IfcRelAssociates</code> | This relationship is used when a particular object has a source of information associated with it, such as an external document, classification system like Uniclass, project library, or material definition. This is commonly used for facility management. Example subclasses include <code>IfcRelAssociatesDocument</code>, <code>IfcRelAssociatesClassification</code>, and <code>IfcRelAssociatesMaterial</code>. |
| <code>IfcRelConnects</code> | This relationship is used when a particular object is joined physically or virtually to another object. This is usually used in analytical models, such as structural analysis where members and nodes connect to each other, MEP systems analysis where ports join together, or environmental analysis, where spaces have boundaries and are covered by particular material layers. Example subclasses include <code>IfcRelConnectsStructuralMember</code>, <code>IfcRelConnectsPorts</code>, and <code>IfcRelSpaceBoundary</code>. |
| <code>IfcRelDecomposes</code> | This relationship is used when a particular object (physical or virtual) is built up of smaller object parts. Smaller parts may be simple aggregated into a larger whole, or projecting from a object, or embed itself within another object. Example subclasses include <code>IfcRelAggregates</code>, <code>IfcRelProjectsElement</code>, and <code>IfcRelVoidsElement</code>. |
| <code>IfcRelDefines</code> | This relationship is used when a particular object can be defined by a common set of definitions, such as properties, manufacturer / construction types, or a template of definitions. This relationship is very commonly used, specifically to define properties (both buildingSMART standard properties, and custom user properties) to objects, and define construction types. Example subclasses include <code>IfcRelDefinesByProperties</code>, <code>IfcRelDefinesByType</code>, and <code>IfcRelDefinesByTemplate</code>. |
## A summary of non-rooted elements
There are far too many *non-rooted* elements to list in totality, however a curated selection as shown below give a indication of the types of data that are stored in an IFC file, which can be reused by *rooted* elements.

| IFC Class | Description |
| --- | --- |
| <code>IfcMaterial</code> | A material may be named, and then have further *non-rooted* classes assigned to it, such has simple RGB colours, textures, and material properties for environmental simulations. |
| <code>IfcCartesianPoint</code> | As you might expect, IFC can store 2 or 3 dimensional Cartesian coordinates. This is one of the building blocks of many other *non-rooted* classes, such as the ability to locate an object in space, or build up geometric representations. |
| <code>IfcFacetedBrep</code> | A huge variety of geometric forms may be described in IFC. One commonly known format is a faceted BREP, or series of polygons that describe the surface of an object. |
| <code>IfcPerson</code> | Information about people and organisations can be recorded, which is especially useful as some countries have legislation that requires this to be stored. |
| <code>IfcPropertySingleValue</code> | This commonly used class can define a single property in terms of a property name and its associated value. In addition, there are other classes that allow more complex properties in tabular or calculated form to be stored. |
| <code>IfcObjective</code> | This little-known class can store design intentions, strategies, and objectives to be then associated with objects or portions of the BIM model. |
| <code>IfcRegularTimeSeries</code> | When scheduling, events may occur at predictable time intervals, which may be stored. |
## List of IFC classes
There are multiple versions of IFC in use in the industry, and each version has hundreds of IFC classes. This makes it impractical to describe them in their entirety in a separate community wiki. However, there are some resources available for those who do want a list:

- [Official IFC4.2 specification list of all classes](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/inheritance-general-usage-all%20entities.htm)
- [Official IFC4.2 specification list of all object types](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/inheritance-general-usage-object%20types.htm)
- [IFC4.2 classes and property sets in spreadsheet format](/media/Ifc-4.2.0.0.ods)
- [Bonsai free online IFC4.2 class search tool for built elements](https://bonsaibim.org/search-ifc-class.html)
- [Official IFC2x3 TC1 specification list of all classes](https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/inheritance_index.htm)
- [IFC2x3 TC1 classes in spreadsheet format](/media/Ifc-2.3.0.1.ods)
