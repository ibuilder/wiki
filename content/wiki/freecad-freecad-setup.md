---
title: "FreeCAD setup"
url: "/freecad-freecad-setup/"
aliases: ["/FreeCAD/FreeCAD_setup/", "/FreeCAD_setup/"]
categories: ["FreeCAD", "Software"]
lastmod: "2022-07-26T14:14:21Z"
---

[FreeCAD](https://www.freecadweb.org) is an open-source multi-purpose, generic, feature-based parametric modeling application. It runs on Windows, Mac and Unixes/Linux. On Linux it is generally found inside your package manager, on other platforms, or if you want a more bleeding-edge version of what your Linux distribution offers, your best choice is to grab the latest release from the [FreeCAD github releases page](https://github.com/FreeCAD/FreeCAD/releases).

FreeCAD features a specific [BIM workbench](https://wiki.freecadweb.org/BIM_Workbench) that can be installed from menu **Tools->Addon Manager** once FreeCAD is installed. The BIM workbench is still a work-in-progress (in the open-source world nothing is never really "finished"), but already allows you to do a full BIM workflow and all the operations that are commonly done with other BIM applications, such as modelling, managing BIM properties of objects, producing 2D documents, and working with IFC files.

To be able to import/export IFC files, an additional component named [IfcOpenShell](http://www.ifcopenshell.org/) must also be installed. The best way to obtain it is by grabbing an automatic build from the [IfcOpenBot](https://github.com/IfcOpenBot/IfcOpenShell/commits/v0.6.0) repository. Look for further instructions on the [FreeCAD wiki](https://wiki.freecadweb.org/Arch_IFC).

When switching to the BIM workbench for the first time, a welcome dialog will show, giving you hints as what to do next. Basically it involves setting up a couple of preference options, such as you preferred working unit (which you can change anytime while working or even work with mixed units), and a couple of default values such as colors and the default work plane grid.

The BIM workbench also features an in-game tutorial found in menu **Help->BIM tutorial**, which will walk you through the whole process of setting FreeCAD up and building a simple model, up to producing 2D drawings and exporting IFC files.

There are many resources to help you learn FreeCAD and doing BIM modeling with it. Start with the [BIM workbench documentation](https://wiki.freecadweb.org/BIM_Workbench), or have a look at the [tutorials section](https://wiki.freecadweb.org/Tutorials) on the FreeCAD wiki, or the [BIM with FreeCAD](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU) video series on youtube.

Also check [FreeCAD setting up a model for IFC export](/freecad-freecad-setting-up-a-model-for-ifc-export/) on this wiki.
