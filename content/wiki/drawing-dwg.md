---
title: "Drawing (DWG)"
url: "/drawing-dwg/"
aliases: ["/Drawing_(DWG)/"]
categories: ["Drawing (DWG)", "Drawing Exchange Format (DXF)", "File formats"]
lastmod: "2026-06-27T10:46:49Z"
---

> **Stub:** This article needs expansion.

The Drawing (DWG) file format developed by [Autodesk](https://en.wikipedia.org/wiki/Autodesk) is a proprietary file format and the native file format for a number of proprietary CAD systems, originally developed for [AutoCAD](/autocad/) . The [Drawing Exchange Format (DXF)](/drawing-exchange-format-dxf/) is usually a better alternative for free software as it has better support for virtually the same content.

Wikipedia has a good article about [the DWG format and it's history](https://en.wikipedia.org/wiki/.dwg).

## DWG in FOSS Software
There have been several efforts at making a free software library for reading/writing DWG files
- [libdxfrw](/libdxfrw/) which is the default DXF/DWG library for [LibreCAD](/librecad/) (versions 2 & 3)
- [LibreDWG](/libredwg/) which is more advanced but in beta state
- [ACadSharp](/ACadSharp/) ([ACadSharp](https://github.com/DomCR/ACadSharp)) allows to read or create CAD files using .Net and also extract or modify existing content in the files.
- [acadrust](/acadrust/) ([acadrust](https://docs.rs/acadrust/latest/acadrust/)) is pure Rust library for reading and writing CAD files in DXF and DWG formats.

You can read about the struggles of supporting DWG in free software in the [libregraphicsworld](http://libregraphicsworld.org) article [LibreDWG revived, starts getting regular releases](http://libregraphicsworld.org/blog/entry/libredwg-revived-starts-getting-regular-releases)

## Free software known to have some support for DWG
- [FreeCAD](/freecad/) uses [LibreDWG](/libredwg/) from version 0.19 for Linux builds and Conda Windows builds. Otherwise check the [FreeCAD documentation](https://wiki.freecadweb.org/FreeCAD_and_DWG_Import) or ask in our forum.
- [GauchoCAD](https://github.com/tercoide/GauchoCAD) uses [LibreDWG](/libredwg/) but is currently alpha software with no released packages
- [LibreCAD](/librecad/) has basic DWG support using the [libdxfrw](/libdxfrw/) library
- [Open CAD Studio](/Open_CAD_Studio/) ([Open CAD Studio](https://github.com/HakanSeven12/OpenCADStudio)) OCS is a CAD application for 2D drafting and 3D modeling, built with Rust. Reads and writes DWG and DXF files natively.
- [SolveSpace](/solvespace/) can import DXF and DWG and export 2D sketches and 3D wireframes as DXF using the [libdxfrw](/libdxfrw/) library. Moving to [LibreDWG](/libredwg/) is under discussion.
- [QCAD](/qcad/) has a commercial version which adds DWG support using the non-free ODA Teigha Library.
- [ZCAD](/zcad/) is a simple CAD program, written in Lazarus / FPC. It can open and save DXF2000 files. They are actively working on DWG support with the [LibreDWG](/libredwg/) library.

## Current status of LibreDWG
Generally LibreDWG is stable for the most common entities and objects for DWG and DXF, plus hundreds more. It can write DWG r2000 already, plus all DXF versions. DWG write support for 2004-2018 is about 80% done. See also [LibreDWG discussion list](https://lists.gnu.org/archive/html/libredwg/2020-12/threads.html) and [LibreDWG news](https://savannah.gnu.org/news/?group=libredwg)

Please test and [report bugs](https://github.com/LibreDWG/libredwg/issues).

There is currently focus on gambas bindings (that's the free GNU VBA variant) for GauchoCAD and C++ bindings for SolveSpace. Perl and python bindings are ready but unused.

**Current limitations:**
- Not feature parity with [Open Design Alliance (ODA)](/open-design-alliance-oda/)
- Many basic dynamic blocks and parametrics are done but it's still a work in progress.
- DWG write support for 2004-2018 is about 80% done, still some bugs.
- Creating 3dsolids from scratch, writing acis data is also not yet good enough.
- The objects and fields are all done, but it's undocumented and unstable.
- lisp bindings, like for guile would be nice, but low priority (no one has asked for it)

## See also
- [Libdxfrw](/libdxfrw/) is the DXF / DWG library used by [LibreCAD](/librecad/)
- [Drawing Exchange Format (DXF)](/drawing-exchange-format-dxf/)
- [Open Design Alliance (ODA)](/open-design-alliance-oda/)
- [FreeCAD](/freecad/)
- [GambasCAD](/GambasCAD/)
- [Getting started with 2D CAD drafting](/getting-started-with-2d-cad-drafting/)

## External Resources
- The [Open Design Alliance](https://www.opendesign.com) has a freely available proprietary [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) for converting between different versions of .dwg and .dxf
- The ODA has [published a DWG specification](https://www.opendesign.com/files/guestdownloads/OpenDesign_Specification_for_.dwg_files.pdf)
- [DWG at Wikipedia](https://en.wikipedia.org/wiki/.dwg) gives background on the way Autodesk has pursued anyone trying to achieve compatibility.
