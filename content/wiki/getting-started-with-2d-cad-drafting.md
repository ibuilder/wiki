---
title: "Getting started with 2D CAD drafting"
url: "/getting-started-with-2d-cad-drafting/"
aliases: ["/Getting_started_with_2D_CAD_drafting/"]
categories: ["Drawing (DWG)", "Drawing Exchange Format (DXF)"]
lastmod: "2024-04-19T20:24:38Z"
---

Computer Aided Drafting (CAD) in 2D is an important part of many design workflows, some would say legacy workflows. It is a digital extensions of hand made technical drawings.

## The problem
The field of 2D CAD within the AEC industry is currently dominated by [AutoCAD](/autocad/), and in particular, the proprietary [DWG](/drawing-dwg/) file format. Heavy reliance on AutoCAD, along with the tight control that parent company Autodesk exerts over the proprietary DWG file format, both stifles innovation and perpetuates proprietary software in our industry. In contrast [open formats](/aec-open-data-standards-directory/) support users freedom.

To make the switch away from proprietary software and file formats, there are two key ways in which you can make a difference in the industry. The first is by requesting and producing the open [DXF](/drawing-exchange-format-dxf/) format instead of the proprietary DWG format. The second is by switching from AutoCAD to another software entirely.

## Switch from DWG to DXF
[Drawing Exchange Format (DXF)](/drawing-exchange-format-dxf/) is an open format that provides many similar features to [Drawing (DWG)](/drawing-dwg/). In general, DXF is much more widely supported and has much better cross-platform support. It is extremely easy to switch. Almost all CAD software has the ability to read and write DXF, so it is simply a manner of making it a habit to use one instead of the other. It is also usually a good idea to specify DXF as a digital deliverable in contracts. Most BIM projects currently specify IFC as an OpenBIM format, but neglect to also specify DXF as an open format.

If a DWG file is provided, and it is not possible to ask for the provider to provide a DXF instead, you have a few options. The first is to open the DWG with QCAD or [LibreCAD](/librecad/), and then convert it to a DXF yourself. Of the two, QCAD's support for DWG far surpasses [LibreCAD](/librecad/), but unfortunately relies on [Open Design Alliance (ODA)](/open-design-alliance-oda/). 

FreeCAD 0.19 linux version (appimage) [can import DWG files based on LibreDWG library](https://yorik.uncreated.net/blog/2021-004-freecad-november-december), and eventually export with this format too. To install this library on Windows version see this [FreeCAD documentation](https://wiki.freecadweb.org/FreeCAD_and_DWG_Import).

Another CAD program using the LibreDWG library is [SolveSpace](/solvespace/). It can import DWG files up to some extend (even saved as AutoCAD 2013) and export them as DXF (2007), PDF or SVG. 

If it is not possible to submit DXFs for a project, for example if a client specifically request only DWGs and you are unable to convince them otherwise (though there may be little technical reason for them to do so), QCAD may be used to save DWGs. [LibreCAD](/librecad/) is unable to create DWGs, at the moment.

If you have a lot to convert, or if the conversion is unsatisfactory, or if you use neither LibreCAD or QCAD (such as if you are using Blender or programmatically generating DXFs), as a fallback option you may use the proprietary [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter), or the proprietary [ODA Online Converter](https://www.opendesign.com/oda_online_converter). Although this is proprietary software, it is mentioned on the OSArch wiki because the [Open Design Alliance (ODA)](/open-design-alliance-oda/) has debatably helped improve access the open data standards in the AEC industry due to their work in reverse engineering the DWG file format, and the ODA library is also used in QCAD under the hood, and it is cross-platform.

A comparison table is provided to help people learn the difference between the two formats. See also the more general [File format comparison](/file-format-comparison/)

| Feature | DWG | DXF |
| --- | --- | --- |
| The majority of basic drafting, including lines, text, dimensions, hatching, colours, and layers | Supported | Supported |
| Easy to use cross-platform and across all CAD tools | Not supported. DWG is inconvenient to use with free software as well as cross-platform. Users are usually required to use proprietary software to use DWG. | Supported |
| Storage in ASCII for open data parsing | Not supported | Supported |
| Storage in binary for efficient file sizes | Supported | Supported (Note: A common misconception is that DXF is only ASCII. DXF actually has an ASCII and a Binary variant) |
| 3D lines and points, common in survey drawings | Supported | Supported (Note: A common misconception is that DXF does not support 3D. This is not true) |
## Converting from PDF to DXF
In many cases, if the files were created corrected, 2D drafting sheets can be found inside a PDF format file. For these cases you can convert these files to DXF files, suitable for further edition with CAD software. [Inkscape](/inkscape/) 1.0 has options to open and save both PDF and DXF files.
To work as converter, [Inkscape](/inkscape/) can open a PDF file and with the function "Save a copy" you will have the option of Save as type: Desktop Cutting Plotter (AutoCAD DXF R12 and R14) format. It is important to notice that the original PDF must be a vector drawing (no bitmap). Also, [Inkscape](/inkscape/) 1.0 can open files with AutoCAD DXF R13 extension.
Note: R14 support splines (curves), but R12 only support straight lines. It is recommended to check [this post](http://cutlings.wasbo.net/svg-to-dxf-in-inkscape-v1-0/) for more information.

As an option you can use [Scribus](https://www.scribus.net/) to open a PDF file to be exported as SVG file. Then you can open the SVG file to save it as DXF format with Inkscape. On the other hand, you can follow [this tutorial using Inkscape and pstoedit](https://thinkmoult.com/how-to-bulk-convert-pdf-to-dxf-or-dwg.html).

## Switching to free/libre software
While there are very advanced free/libre 3D geometry applications, there are very few 2D applications with high quality drafting capabilities.
 
The most advanced with paper setups, scaling and printing tools:

- [QCAD](/qcad/) Community Edition is the most feature rich libre/free software for 2D CAD. It is multi platform and supports a typical 2D CAD workflow.
- [QCAD](/qcad/) Professional is the paid version of QCAD with a few more functions. Buy QCADE professional supports the development of QCAD Community Edition.
- [LibreCAD](/librecad/) is a free/libre 2D CAD software. It is a fork from QCAD v2 and has seen gradual development.

There are many tools with vector drawing functionality but not really specific to 2D drafting.

- [CAD Sketcher](/cad-sketcher/) CAD Sketcher is a constraint-based sketcher addon created for Blender 
- [FreeCAD](/freecad/) has three workbenches useful for 2D drafting, [Sketcher](https://wiki.freecadweb.org/Sketcher_Workbench), [Draft](https://wiki.freecadweb.org/Draft_Module) & [Techdraw](https://wiki.freecadweb.org/TechDraw_Module). TechDraw is the most advanced and sees most development.
- [SolveSpace](/solvespace/) can import DWG files up to some extend (even saved as AutoCAD 2013). It has some basic 2D drawing tools to do some edition. Finally it can export the files as DXF (2007), PDF or SVG.
- [ZCAD](https://github.com/zamtmn/zcad) is a small 2D CAD program that can open, edit, save DXF2000 files and has a few edition tools. ZCAD is in beta development.
- [LX-Viewer](http://lx-viewer.sourceforge.net/) (Linux Drawing Viewer) is a program that will allow you to open, view, print DXF files. But it cannot edit files.
- [Inkscape](/inkscape/) & [Krita](/krita/) have been used by some for drafting. You can use Inkscape as PDF/DXF converter, for editing drawings and presentation improvement. And then, export a final PDF/DXF file.
- [Libre Office Draw](https://www.libreoffice.org/) can open DXF files version 2004 or earlier, but it cannot make complex editions. It exports PDF/SVG format (no [DXF](/drawing-exchange-format-dxf/)/[DWG](/drawing-dwg/) support).
- [CadZinho](https://github.com/zecruel/CadZinho) is a very new 2D CAD project. You can open DXF files.

## See also
- [Scalable Vector Graphics (SVG)](/scalable-vector-graphics-svg/)
