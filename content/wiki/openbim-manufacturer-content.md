---
title: "OpenBIM Manufacturer Content"
url: "/openbim-manufacturer-content/"
aliases: ["/OpenBIM_Manufacturer_Content/"]
categories: ["Industry Foundation Classes (IFC)"]
lastmod: "2020-12-09T16:03:20Z"
---

> **Stub:** This article needs expansion.


## Introduction
[OpenBIM](/openbim/) is all about making access to data and interoperability easy and lossless. Manufacturer content, such as you can find online at sites like [BIMobject](https://www.bimobject.com), typically offer files to designers authored in proprietary formats specifically for an intended software platform. A better solution would be the exclusive use of [Open Formats](https://en.wikipedia.org/wiki/Open_format). 

## Selecting a file format
Each file format has different strengths and weaknesses. This articles focuses on interoperability and use of open formats.

There are several advantages in using [Industry Foundation Classes (IFC)](/ifc-industry-foundation-classes/) as a format for manufacturer content.
- There is some ability to store some parametric geometry
- IFC is an a widely supported open file format
- All the information contained in an IFC file is available to the owner of the file

There are also some disadvantages to using IFC
- Each geometric object can only have one material
- Parametric controls are limited

There is a [File format comparison](/file-format-comparison/) useful for selecting relevant file formats.

## Storing object data
[BuildingSMART International](/buildingsmart-international/) has developed the [BuildingSMART Data Dictionary (bSDD)](/bsdd-buildingsmart-data-dictionary/) as a multi lingual standardized description framework for object data.

## Example
The following section (and this whole page) is to document an ongoing project and will be updated as the project progresses. Contact Duncan Lithgow if you have some input you think is relevant (or just edit this page).

A manufacturer will often think of asking a consultant they have worked with on projects to make some content they can share with other consultants. Typically this will then be offered in the format of the consultant company, often this will be the dominant software platform for that type of content in that region.

## File Formats
In this example the client has asked for Revit Families of their zip screen / sun screen. As a supporter of cross platform solutions, and to support the client in widening the market for their product, one would want to make the digital asset available to multiple software platforms. In this case the targets are:
- Autodesk [Revit](/autodesk-revit/)
- Trimble [SketchUp](/SketchUp/)
- Graphisoft [ArchiCAD](/archicad/)
- McNeil [Rhinoceros 3D](/rhinoceros-3d/)

## Manufacturer Data
**Revit Family**
The manufacturer has some data they want stored in the native Revit Family RFA file. To standardize this is should be stores according to [bSDD](/bsdd-buildingsmart-data-dictionary/) conventions. For example the [bSDD data for an electric motor](http://bsdd.buildingsmart.org/#concept/details/3_kLW3eI10Xem4Z9zSCTzp) can be used to structure information about efficiency class, voltage, model and much more.
