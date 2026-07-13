---
title: "IFC - Industry Foundation Classes"
url: "/ifc-industry-foundation-classes/"
aliases: ["/IFC_-_Industry_Foundation_Classes/", "/Industry_Foundation_Classes_(IFC)/"]
categories: ["buildingSMART International", "File formats", "Industry Foundation Classes (IFC)"]
lastmod: "2023-02-14T21:48:26Z"
---

{{< wiki-image src="/media/freecad-ifc-viewer.png" alt="An IFC file being viewed in FreeCAD" mode="thumb" caption="An IFC file being viewed in FreeCAD" align="right" >}}

IFC (Industry Foundation Classes), is an [Open Data](/aec-open-data-directory/) schema and set of formats used to store [OpenBIM](/openbim/) data. It is developed and maintained by [BuildingSMART International](/buildingsmart-international/). IFC data can digitally describe many concepts, including:

- Physical objects in our built environment (walls, slabs, columns, pipes)
- 2D and 3D geometry that represents objects or annotate objects
- A diverse set of properties and attributes spanning many domains
- Materials attributes and display colours
- Construction planning, resource allocation, and scheduling
- Quantification of elements
- Roles and responsibilities of organisations and individuals
- Design strategies and legal constraints
- Analytical models for structural analysis, energy analysis, and light analysis

The majority of BIM programs can read and write IFC data. However, the quality of vendor support for IFC data varies significantly between software. There are a lot of myths about IFC - so [BuildingSMART International](/buildingsmart-international/) made a video series to address this: [IFC Myth Busters](https://www.buildingsmart.org/resources/myth-busters/leon-van-berlo/)
<div style="float: right; margin: 30px;">{{< youtube "https://www.youtube.com/watch?v=kMpzrUJY7LU" >}}</div>

## Subpages


## IFC versions
There are currently three commonly supported versions of IFC: IFC2X3, IFC4 and more recently IFC4x3. 

- IFC2x3 (typically as Coordination View 2.0 or "CV 2.0") is typically what many BIM authors are used to using to export and exchange models. IFC2X3 has been an ISO standard since 2005.

- IFC4 has been very slowly implemented in BIM authoring software despite being an ISO standard since 2013. IFC4x contains many new features compared to IFC2X3, such as improved geometry representations, geolocation support, and more element categories. 

- IFC4x3 became an ISO standard in March 2022 and extends IFC4 to be better suited for linear infrastructure (Roads, Railways, Bridges, Earthworks, Geotechnics, Ports & Waterways)

Officially released [documentation is available from buildingSMART international](https://standards.buildingsmart.org/IFC/RELEASE/).

For IFC 4x3 it is also possible for you to improve the documentation by visiting the [automatically generated version](http://ifc43-docs.standards.buildingsmart.org/).

## IFC formats
IFC data is most commonly found in a plain text file format with the file extension <code>.ifc</code>. A common misconception is that IFC is only a intermediate file format. Instead, IFC is a schema, with a full file being only one of many possible ways to store or transfer OpenBIM data. It is possible to transfer portions of OpenBIM data, or full models, using a variety of serialisations. Other serialisations include:

- <code>.ifc</code> IFC-SPF format, a commonly used plain text format based on STEP
- <code>.ifczip</code> IfcZIP format, where a single <code>.ifc</code> file is compressed into a ZIP package
- <code>.ifcxml</code> IfcXML format, a plain text format
- <code>.json</code> JSON format, a plain text format
- <code>.hdf</code> HDF5 format, a binary format
- <code>.sqlite</code> SQLite format, a binary format

In reality, currently only <code>.ifc</code> and <code>.ifczip</code> sees common usage.

## IFC classes
In IFC, a single concept is known as an *IFC class*. There are hundreds of IFC classes. Examples of IFC classes are <code>IfcWall</code>, <code>IfcBuilding</code>, and <code>IfcTask</code>. Classes can have attributes, for instance, the <code>IfcWall</code> can have a <code>Name</code> attribute. Classes can also have relationships to other classes, for example an <code>IfcWall</code> can be related to an <code>IfcBuilding</code> by being spatially contained within the <code>IfcBuilding</code>.

{{< wiki-image src="/media/ifc-wall.png" alt="An example hierarchy of IFC classes" mode="thumb" caption="An example hierarchy of IFC classes" align="right" >}}

Classes can inherit from other classes, building up a hierarchy of classes. If a class inherits from another class, it inherits all of its attributes and relationships. For example, the <code>IfcProduct</code> class has a <code>Representation</code> attribute, which can store 3D geometry that represents that class. Because the <code>IfcWall</code> class inherits from the <code>IfcProduct</code> class, it also has a <code>Representation</code> attribute to store 3D geometry. However, the <code>IfcPerson</code> class does *not* inherit from the <code>IfcProduct</code> class, and so it does *not* have a <code>Representation</code> attribute.

See also the sub page specific to [IFC_classes](/ifc-industry-foundation-classes-ifc-classes/)

## See also
- Our [AEC Open Data directory](/aec-open-data-directory/) has links to sample IFC files
- Our [Autodesk Revit](/categories/autodesk-revit/) links to pages on using IFC in [Autodesk Revit](/autodesk-revit/)
- Our [Graphisoft Archicad](/categories/graphisoft-archicad/) links to pages on using IFC in [ArchiCAD](/archicad/)
- [XbimXplorer](/xbimxplorer/) is a Windows-only viewer capable of loading IFC2x3 and IFC4 models based on the [xbim toolkit](https://docs.xbim.net/index.html) project
- [IFC Pipeline](https://view.ifcopenshell.org/) is an open source self-hosted IFC processing and visualization pipeline powered by [IfcOpenShell](/ifcopenshell/)
- [Online3DViewer](https://3dviewer.net/index.html) is a free and open source (MIT license) web solution to visualize and explore 3D models right in your browser.
- There is an [IFC Merge git project](https://github.com/brunopostle/ifcmerge) which uses git to [store and manage IFC data in git](https://community.osarch.org/discussion/comment/12598/#Comment_12598) making incremental changes and revision management possible (project proposal 2022)
- Our friends at [Bonsai](/bonsai/) have a site to help you [choose the correct IFC Class](https://bonsaibim.org/search-ifc-class.html) for your physical objects.

## External Resources
- [BuildingSMART International](/buildingsmart-international/) Denmark have written an [IFC Export Guide for Revit and ArchiCAD](https://anvisninger.molio.dk/Gratis-vaerktojer/buildingSMART/IFC_Export_Guide_EN)
- [BuildingSMART International](/buildingsmart-international/) International Modeling Support Group have written an [IFC 2x Edition 3 Model Implementation Guide](https://standards.buildingsmart.org/documents/Implementation/IFC2x_Model_Implementation_Guide_V2-0b.pdf) (PDF file)
- [Industry Foundation Classes – A standardized data model for the vendor-neutral exchange of digital building models](https://publications.cms.bgu.tum.de/books/bim_2018/06_IFC_07.pdf) (PDF file)
- [IFC Myth Busters](https://www.buildingsmart.org/resources/myth-busters/leon-van-berlo/)
- Open Source online IFC viewer: https://alliance-batiment.ciqo.eu/
