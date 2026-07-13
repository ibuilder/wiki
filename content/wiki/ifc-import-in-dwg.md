---
title: "IFC import in DWG"
url: "/ifc-import-in-dwg/"
aliases: ["/IFC_import_in_DWG/"]
categories: ["Drawing (DWG)", "Industry Foundation Classes (IFC)"]
lastmod: "2021-12-16T07:17:48Z"
---

IFC can be used in several [DWG](/drawing-dwg/) based software products to transfer design data. It will contain only data for 3D modelspace use. Paperspace information like annotations and dimensions are best transferred additionally as separate DWGs. Development of DWG-based IFC is mostly based on the work of the Open Design Alliance (ODA). This is a non-profit technology consortium that provides software solutions as platform for engineering applications. Which is main domain for DWG use.

The results of importing IFC may vary per ifc file and per software. 3d objects become either Solids, Meshes or 'software specific entities'. For use in practice the speed of the conversion is a very important aspect to have workable solutions. Preferably this is done in the background. Like updating models of other disciplines as underlay for design in progress. 

These days a couple of software vendors are working hard to improve their capabilities for handling IFC2x3 and IFC4. BricsCAD, Ares commander and GstarCAD are upcoming names in the DWG ecosystem. Of course, the Autodesk AutoCAD verticals have an import function as well. 

----

**BricsCAD BIM**

BricsCAD BIM supports IFC2x3 and IFC4 for import and export. It is certified for IFC 2X3 coordination view 2.0. The IFC standard includes both parametric and non-parametric shapes, material definitions, metadata in the BIM file, and property sets (PSets).

Fast and reliable Import and Export

IFC will be turned mainly into Solids (ACIS) with a variety of metadata

IMPORT OPTIONS
EXPORT OPTIONS
EXPORT BASE QUANTITIES
IMPORT PARAMETRIC COMPONENTS

{{< wiki-image src="/media/example-bim-import-brics-cad.jpg" alt="Example BIM import BricsCAD.jpg" mode="thumb" align="center" width="600" >}} 

A short demo of importing and organizing IFC rebar is demonstrated in this video

{{< youtube "e4RFG80Imoo" >}}

**Ares Commander**


The BIM Navigator palette enables you to import and view one or multiple BIM files. Supported formats include IFC (versions 2X3, 4 and 4×2), as well as RVT ([Revit](/autodesk-revit/) versions 2011 through 2020). You can further use the filters to show/hide only the objects you need, combining criteria such as the discipline, category, floor, class, or other BIM properties.

Fast and reliable Import and Export

IFC will become "BIM entities" in the software

BIMDEBUG options:
RVT support

-BIMMOVE,
 
-IMPORT OPTIONS

-NO IFC EXPORT

-FILTERS
etc.

{{< wiki-image src="/media/example-bim-import-ares-commander.jpg" alt="Example BIM import ARES commander.jpg" mode="thumb" align="center" width="600" >}} 


**Gstar CAD**

IFC module is still heavily in Beta mode. 
GstarCAD 2020 should be able to handle IFC2x3 and IFC4
Results may differ, conversion is fast.
The 3D perspective system variable doesn't work in GstarCAD

Example BIM import GstarCAD

{{< wiki-image src="/media/example-bim-import-gstar-cad.jpg" alt="Example BIM import GstarCAD.jpg" mode="thumb" align="center" width="600" >}}


**AutoCAD Architecure & AutoCAD Civil3D** 

- AutoCAD verticals have the same API or 'IFC engine' under the hood
- Very very slow import and export function, to the point of being unworkable
- IFC2x3, from version 2020 it should be able to handle IFC4 support (No increase in speed ?!)
- Hierarchy comes in over several DWG files XREFs, a clumsy way


Import process is slow coding to AutoCAD
{{< wiki-video src="/media/autocad-ifc-import.mp4" poster="/media/autocad-ifc-import.png" title="AutoCAD ifc import" align="center" width="600" >}} 

{{< wiki-image src="/media/example-bim-import-autocad.jpg" alt="Example BIM import AutoCAD.jpg" mode="thumb" align="center" width="600" >}} 
{{< wiki-image src="/media/example-bim-import-autocad-architecture.jpg" alt="Example BIM import AutoCAD Architecture.jpg" mode="thumb" align="center" width="600" >}}


written by Hans Lammerts

Resources:

https://www.opendesign.com/products/ifc-sdk

https://knowledge.autodesk.com/support/autocad-architecture/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/AutoCAD-Architecture/files/GUID-39E247EA-AF9E-4BF4-8821-040A405F3778-htm.html.
