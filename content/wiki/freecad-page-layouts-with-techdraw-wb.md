---
title: "Page layouts with TechDraw WB"
url: "/freecad-page-layouts-with-techdraw-wb/"
parent: "/freecad/"
aliases: ["/FreeCAD/Page_layouts_with_TechDraw_WB/", "/Page_layouts_with_TechDraw_WB/"]
categories: ["FreeCAD"]
lastmod: "2023-11-05T15:00:50Z"
---

## FreeCAD Page Layouts with TechDraw WB
This is a list with examples of FreeCAD files that includes Page Layouts made with TechDraw Workbench for Architecture projects. You can download these files for studying to replicate or to develop your own workflow.
[TechDraw WB](https://wiki.freecadweb.org/TechDraw_Workbench) is a module of FreeCAD originally for mechanical design drawings. There are some features for Architecture, but TechDraw has little control on them. This is the reason why it is necessary to document workflows that allow to elaborate drawings for a more complex technical documentation, commonly used in areas of AEC industry. In the future, FreeCAD developers will improve and optimize these workflows in new FreeCAD versions.

### FreeCAD files
| Project | Description |
| --- | --- |
| {{< wiki-image src="/media/freecad-tech-draw-wb.png" alt="Freecad TechDrawWB.png" mode="inline" width="300" >}} | {{< wiki-image src="/media/FC_Bathroom.fcstd" alt="FC Bathroom.fcstd" mode="thumb" >}}  
FreeCAD file with a 3D model of bathroom and 3 possible layouts made with TechDraw WB |
| {{< wiki-image src="/media/freecad-techdraw-house-renovation-drawing.png" alt="2DDrawingFC01.png" mode="inline" width="300" >}} | {{< wiki-image src="/media/FreeCAD_House_RenovationBlueprints.fcstd" alt="FreeCAD House RenovationBlueprints.fcstd" mode="thumb" >}}  
FreeCAD file with layouts of a [house renovation](https://wiki.osarch.org/index.php?title=Regard3D%2BBlender%2BFreeCAD_workflow) made with TechDraw WB |
| {{< wiki-image src="/media/fc-furniture-compound.png" alt="FC FurnitureCompound.png" mode="inline" width="300" >}} | {{< wiki-image src="/media/FurnitureCompound.fcstd" alt="FurnitureCompound.fcstd" mode="thumb" >}}  
FreeCAD file with a 3D object (furniture) linked to a 2D projection. You can turn on/off the 3D model and keep visible the 2D projection in the tridimensional space or in the TechDraw page. This workflow uses [App Link objects](https://wiki.freecadweb.org/Std_LinkMake). See [below](/freecad-page-layouts-with-techdraw-wb/#import-furniture-with-2d-drawing) a description of this workflow. |
| {{< wiki-image src="/media/freecad-d-label.png" alt="Freecad dLabel.png" mode="inline" width="300" >}} | {{< wiki-image src="/media/Dlabel_for_Shape2d.fcstd" alt="Dlabel for Shape2d.fcstd" mode="thumb" >}}  
FreeCAD file with a window object 2D projection, linked to a Draft label.  If you change the information or model of the window 3D object, the label in the 2D projection will update automatically. |
| {{< wiki-image src="/media/freecad-dlabel.png" alt="FreecadDlabel.png" mode="inline" width="300" >}} | {{< wiki-image src="/media/Dlabel_on_Shape2d_V2.fcstd" alt="Dlabel on Shape2d V2.fcstd" mode="thumb" >}}  
New version of a FreeCAD file with a window object 2D projection, linked to a Draft label.  If you change the information or model of the window 3D object, the label in the 2D projection will update automatically. |
### Workflow tips
#### Yorik's workflow.
1. Model your building using BIM or any other FreeCAD tools
1. Use Building parts for your levels (not mandatory, but they carry an automatic, built-in section plane)
1. Place Section planes where you want sections and elevations (and plans if you didn't use Building parts)
1. Create Shape 2D views from your Building parts and section planes
1. Create other Shape 2D views for views that cut through your model, and set them in Cut Faces mode. That way, you can give a different aspect to viewed and cut geometrty
1. Annotate these views with texts, dimensions, symbols, hatches...
1. Put everything related to one view (Shape 2D views, annotations,...) into one same group or Building part
1. On a TechDraw page, create a TechDraw view from that group or Building part.
More information in [Yorik's website](https://yorik.uncreated.net/blog/2021-020-freecad-september).

#### Link table for TechDraw layout.
    - Recommended links between TechDraw Views and 2D objects**

|  |  |  |  |
| --- | --- | --- | --- |
| use [TD InsertView](https://wiki.freecadweb.org/TechDraw_View) | for [Shape2DView](https://wiki.freecadweb.org/Draft_Shape2DView) | Plans, Sections | Allow to apply hatches on plans and sections areas. |
| use TD InsertView | for Draft lines | Simple lines and symbols | Allow to work with different line widths. |
| use [TD DraftView](https://wiki.freecadweb.org/TechDraw_DraftView) | for [Draft Layers](https://wiki.freecadweb.org/Draft_Layer) | Dimensions, texts, lines | Allow to apply line styles and other properties on group of draft objects |
| use TD DraftView | for Draft objects | Simple lines and symbols | Allow to apply line styles and other properties on individual objects |
| use [TD ArchView](https://wiki.freecadweb.org/TechDraw_ArchView) | for [Arch SectionPlane](https://wiki.freecadweb.org/Arch_SectionPlane) | Sections, dimensions, Lines and symbols | Allow to apply line widths and other properties on cut lines. |
More information in [this wiki section.](/regard3d-blender-freecad-workflow/#2d-cad-documentation)

#### Import furniture with 2D drawing
This workflow uses [App Link objects](https://wiki.freecadweb.org/Std_LinkMake).
1. Create a file with a piece of furniture.
1. Make a 2D view from the top using Shape 2D View and put it all in a Link Group.
1. Link the furniture to the main file where you are doing the project.
1. In this example I created 6 elements of the furniture using the Element Count option.
1. Then select all the 2D drawings of each element and create sub-links.
1. Create a 2D layer and put all the sub-links into it.
1. This enables us to show the 2D drawing and 3D model at different times, which is very practical later on in combination with Working Plane View to create 2D plans.
1. When one of the elements is moved, the 2D drawing is moved together with it.
1. Insert a TD DraftView in a TechDraw page. You can move the sub-links object to arrange the furniture layout. If you include a couple of lines as "mayor frame" in the layer, the TD_DraftView will keep the same position in the TD page.

The original idea and more information [in this forum](https://forum.freecadweb.org/viewtopic.php?p=496267#p496267).

### See also
- [Workflow Directory](/aeco-workflow-examples/) with more FreeCAD projects.
- [List of famous building models](/freecad-architecture-3d-models-created-in-freecad/) made with FreeCAD.

### External references
- [TechDraw workbench page](https://wiki.freecadweb.org/TechDraw_Workbench) in the FreeCAD wiki.
- [Basic TechDraw Tutorial](https://wiki.freecadweb.org/Basic_TechDraw_Tutorial) in the FreeCAD wiki.
