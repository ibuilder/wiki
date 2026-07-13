---
title: "IfcPlusPlus"
url: "/ifcplusplus/"
aliases: ["/IfcPlusPlus/"]
categories: []
lastmod: "2022-08-05T04:37:43Z"
---

<aside class="software-infobox">
<img src="/media/ifcplusplus-logo.png" alt="">
<dl>
<dt>Website</dt><dd><a href="https://ifcquery.com/">ifc++</a></dd>
<dt>Source</dt><dd><a href="https://github.com/ifcquery/ifcplusplus">github</a></dd>
<dt>License</dt><dd>&quot;MIT&quot;</dd>
<dt>Issues</dt><dd><a href="https://github.com/ifcquery/ifcplusplus/issues">github</a></dd>
<dt>Maturity</dt><dd>Mature</dd>
</dl>
</aside>

[IFC++](/ifcplusplus/) or [IfcPlusPlus](/ifcplusplus/) is a C++ open source (MIT license) library from the [IfcQuery](/ifcplusplus/) project for reading, writing, and viewing [IFC](/ifc-industry-foundation-classes/) files.

The IFC++ library can be used for general purpose, and it also includes a sample IFC visualization application. This viewer is based on Qt 5 and OpenSceneGraph (OSG), and can load big IFC files very fast, and thus can be used to compare the performance of other free IFC viewers, like [Blender](/blender/) and [FreeCAD](/freecad/), which internally use the [IfcOpenShell](/ifcopenshell/) library.

## Installation
The IFC++ distribution is provided as source code, so to use the library and the sample viewer, the code must be compiled.

To learn more about installing IFC++, visit the page in the FreeCAD wiki: [IfcPlusPlus](https://wiki.freecadweb.org/IfcPlusPlus).

## Viewers
- The IFC++ distribution includes a sample viewer in source code that uses the IFC++ library, and that is compiled together with it.

- A second viewer exists with the generic name of "**IfcQuery**", that uses pre-compiled IFC++, Qt, and OSG libraries, and is only available for Windows. This viewer is more complete than the sample viewer included with the source code of IFC++, but is not open source. It is free for use and available by downloading the *SimpleViewerExampleQt.zip* package from [ifcquery.com](http://www.ifcquery.com/), and running *SimpleViewerExampleQt.exe*. This viewer is self-contained, everything that it requires to run is included in the *.zip* archive.

*Note:* in common usage, the names "IfcQuery", "IFC++", and "IfcPlusPlus" may be used interchangeably to refer to the same thing, the C++ library or more specifically the IFC viewer.
