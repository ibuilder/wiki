---
title: "Regard3D+Blender+FreeCAD workflow"
url: "/regard3d-blender-freecad-workflow/"
aliases: ["/Regard3D%2BBlender%2BFreeCAD_wiki_page/", "/Regard3D%2BBlender%2BFreeCAD_workflow/"]
categories: ["FreeCAD"]
lastmod: "2021-10-31T12:25:20Z"
---

[Forum's discussion](https://community.osarch.org/discussion/474/floss-workflow-with-regard3d-blender-freecad#latest).

This wiki present a [FLOSS](/floss/) workflow for an architecture job (documentation and registration of an existing house renovation), that involve the use of Regard3D, Blender and FreeCAD for Geometry Scanning, BIM modeling and CAD documentation.
This workflow is fully multi-platform (the three programs run on Windows, Mac, Linux).

{{< wiki-image src="/media/floss-summary-workflow.png" alt="FLOSS SummaryWorkflow.png" mode="inline" width="700" >}}

## Tools
As a basic requirement for this tutorial, it is necessary to have a medium level of knowledge about the tools used in this workflow. This tutorial is about the workflow, not about each tool.


[Regard3D](http://www.regard3d.org/)

[Blender](/blender/) (v2.8)

[Point Cloud Visualiser](/point-cloud-visualizer/)

[FreeCAD](/freecad/) (v0.19)

## Geometry scanning
The idea is to gather geometry data of an existing building for further 3D modeling process. For this purpose, we will use open source photogrammetry software.

##### Creation of data set of photos
1. Recommendation: Camera's metadata must include focus lens (you can add that information manually later). 
1. Shoot several photos of the building with a camera or smartphone. In general it is good to take more than 60-80 images from different angles. Look for info about photogrammetry good practices.

##### Point cloud generation with Regard3D.
1. For this step it is used Regard3D, but there are other photogrammetry programs that can be used. Refers to [Software Directory](/aec-free-software-directory/) for more options.
1. Import image set. 
1. Generate point clouds of the model (see [tutorial](https://www.regard3d.org/index.php/documentation/tutorial) ).
1. Export point cloud file (*.ply). You can save several point clouds files to cover all facades of the building.
1. Mesh generation (Optional). Also, you can generate mesh surfaces with the point clouds. But, for this case I found efficient enough to work only with the point clouds. 


{{< wiki-image src="/media/regard3d.png" alt="Regard3d.png" mode="inline" align="none" width="700" >}}

## 3D Mesh modeling
Volumetric mesh reconstruction with Blender + point cloud visualizer (0.9.3v).
Using Blender you can visualise the point cloud and generate a volumetric mesh to get the general dimensions and shapes of the building. However, this step is optional, because you can directly import the point clouds into FreeCAD. Anyway, the point cloud visualiser has more manipulation options than FreeCAD.

##### Importing the point clouds
1. Install [Point Cloud Visualiser](https://blendermarket.com/products/pcv) add-on (0.9.3v is free). Here [more documentation](https://jakubuhlik.com/docs/pcv/docs.html). But these are basic steps to load and work in Blender:
1. In blender create a empty object.
1. Import a point cloud file in the empty object, using PCV.
1. Edit the point cloud position and scale it, if it is necessary (use Enable Edit Mode, in the PCV panel).
1. Export the edited point cloud in the empty object, to save the edition (use Export PLY in the PCV panel). 
1. When you open the blender file, select the empty object and load the last exported PLY file, to display the edited point cloud, with the right position and scale..


{{< wiki-image src="/media/blender-pcv.png" alt="Blender PCV.png" mode="inline" align="none" width="500" >}}

{{< wiki-image src="/media/blender-pointcloud.png" alt="Blender pointcloud.png" mode="inline" align="none" width="700" >}}

##### Geometry modeling
1. Model the main volumes with Blender, using the points as reference. 
1. Option 1) Once you have the 3D model complete, you could convert the Blender meshes into BIM models using [Bonsai](https://bonsaibim.org/).
    - Install Bonsai
    - Set the meshes as BIM objects
    - Export the model as IFC file

1. Option 2) Once you finish with the 3D modeling, export the model as a simple mesh file (OBJ, STL...).

 
{{< wiki-image src="/media/blenderpointcloud.png" alt="Blenderpointcloud.png" mode="inline" align="none" width="700" >}}

## BIM modeling
Develop a BIM model with FreeCAD (using as reference the mesh or the IFC file from Blender).
Once you got a good mesh volume of the building geometry, export a stl file or IFC file to FreeCAD to recreate the main walls, windows, doors and aditional architecture details of the building with the [Arch Workbench](https://wiki.freecadweb.org/Arch_Module). at the end of this workflow the idea is to save a FreeCAD file with only 3D models. You can have a look to a FreeCAD file example [here](https://wiki.osarch.org/images/f/f2/Dormitorios01_02.FCStd).

##### Importing the files to FreeCAD
1. Opt 1) Import a mesh file.
    - If the result of the previous step was a simple mesh file, you can import with [Mesh Design workbench](https://wiki.freecadweb.org/Mesh_Workbench).
    - Fix position and scale of the mesh with [Mesh Scale](https://wiki.freecadweb.org/Mesh_Scale) tool.
1. Opt 2) Import a IFC file.
    - If the result of the previous step was a IFC file, FreeCAD can import IFC2x3 or IFC4 based files. See [Arch IFC](https://wiki.freecadweb.org/Arch_IFC). 
    - Check the FreeCAD Preference for additional options of [IFC import/export](https://wiki.freecadweb.org/Import_Export_Preferences) feature.

##### BIM modeling
1. Based on the mesh/IFC, generate or complete the BIM model using the [Arch Workbench](https://wiki.freecadweb.org/Arch_Module) or eventually, [BIM Workbench](https://wiki.freecadweb.org/BIM_Workbench).
1. For each building, place the 3D model components (walls, structures, and other arch elements) into an [Arch Building Part](https://wiki.freecadweb.org/Arch_BuildingPart). 
1. For each Arch Building Part, create [Arch Section Planes](https://wiki.freecadweb.org/Arch_SectionPlane) (for elevations, plans, sections, etc).
1. For each Arch Section Planes, create [Draft Shape2DView](https://wiki.freecadweb.org/Draft_Shape2DView) objects. You can edit the labels of these Shape2DView to refer view names.
    - Open [Draft Workbench](https://wiki.freecadweb.org/Draft_Module). 
    - Create all the Shape2DView projections, considering the necessary 2D views for the CAD documentation.
    - Arrange the Shape2DView projections in the 3D scene. Once you are done, you should not move these projections anymore.
1. Save and close this file. This file will contain the 3D geometries and the plain Shape2DView projections for future references.


{{< wiki-image src="/media/freecad-mesh.png" alt="Freecad mesh.png" mode="inline" align="none" width="700" >}}
{{< wiki-image src="/media/freecad-bim.png" alt="FreeCAD BIM.png" mode="inline" align="none" width="700" >}}
{{< wiki-image src="/media/freecad-3-g2-b1k-qv-k2.png" alt="Freecad 3G2B1kQvK2.png" mode="inline" align="none" width="700" >}}
{{< wiki-image src="/media/freecad-bim2.png" alt="Freecad BIM2.png" mode="inline" align="none" width="700" >}}

## 2D CAD documentation
This step is for generating PDF files for printing, with 2D CAD documentation (sections, elevations, etc) with FreeCAD. The idea is to work with these 2D drawings in a new and independent FreeCAD file (independent from the 3D models file) that is very light and can be shared easily. The workflow involves the use of [Draft workbench](https://wiki.freecadweb.org/Draft_Module) and [TechDraw workbench](https://wiki.freecadweb.org/TechDraw_Module).

I share the 2D Freecad file as example of CAD documentation made with FreeCAD. You need FreeCAD +0.19 to open the file. Also, there is a bug with the TechDraw pages when you open the file (the drawing layout is a mess). Don't worry. Just click on Turn View Frames On/Off command in TechDraw Workbench and it will fix it. [Link to the 2D FreeCAD file.](https://community.osarch.org/uploads/editor/9w/0qj3m2zvdwbx.zip)

##### 2D drawing with Draft workbench
1. Create a new FC file.
1. Import the Shape2DView objects from the FreeCAD file with the 3D models, using [Arch Reference](https://wiki.freecadweb.org/Arch_Reference).
1. As alternative, you can import the Shape2DView objects using [App:Link](https://wiki.freecadweb.org/Std_LinkMake) option.
1. Open [Draft workbench](https://wiki.freecadweb.org/Draft_Module).
1. Arrange the Shape2DView objects in the 3D space.
1. Draw annotations, dimensions, symbols, lines, etc. with Draft workbench tools.
1. Create a set of layers for Shape2DView objects, Dimensions, symbols, etc with [Draft Layer](https://wiki.freecadweb.org/Draft_Layer).
1. Place each group of 2D elements into the respective layer.
1. Save the file.

{{< wiki-image src="/media/freecad-jueqo-dg3k8.png" alt="Freecad JueqoDg3k8.png" mode="inline" align="none" width="700" >}}

##### Page layout with TechDraw workbench
This workflow is just a suggestion. You can develop one for your own. But the purpose is to generate drawings with different line widths and styles, to enrich the sheet presentation. 

[TechDraw Preference](https://wiki.freecadweb.org/TechDraw_Preferences) allows to setup many preferences and styles.

1. Open [TechDraw workbench](https://wiki.freecadweb.org/TechDraw_Module)
1. Create a [new TD Page](https://wiki.freecadweb.org/TechDraw_PageDefault) (define format and scale).
1. Select a Shape2DView object or a group of them, from the Combo View panel.
1. Press [TechDraw Insert View](https://wiki.freecadweb.org/TechDraw_View) (TDIV) command to insert them in the TD page.
1. Select Draft objects (lines, symbols), from the Combo View panel.
1. Press TDIV command to insert them in the TD Page.
1. On the TD page, place the TDIV of draft objects on top of the first TDIV.   
1. With several TDIV for each group of objects, you can assign different properties (line width). 
    - Also, you can select specific lines of these TDIV and change their appearance with [TechDraw DecorativeLine](https://wiki.freecadweb.org/TechDraw_DecorateLine).
1. Select the Draft Layer of dimensions, in the Combo View panel. 
    - Press [TD Draft View](https://wiki.freecadweb.org/TechDraw_DraftView) and setup its properties.  
    - Place on top of the rest of TDIV. 
1. For lines with style, select their Draft Layer. Press TD DraftView and setup the properties:  
    - Data/ Line Style = 5,2,0,5,2 (or something similar, different numbers will produce different patterns). 
    - Data/ Override Style = true 
1. Create a [TD ClipGroup](https://wiki.freecadweb.org/TechDraw_ClipGroup) and place all the views inside. 
1. You can create more TD pages if you want. If you need many pages, split the project in several FreeCAD files.

    - Recommended links between TechDraw Views and 2D objects**

|  |  |  |  |
| --- | --- | --- | --- |
| use TD InsertView | for Shape2DView | Plans, Sections | Allow to apply hatches on plans and sections areas. |
| use TD InsertView | for Draft lines | simple lines and symbols | Allow to work with different line widths. |
| use TD DraftView | for Draft Layers | Dimensions, Texts, lines | Allow to apply line styles and other properties on group of draft objects |
| use TD DraftView | for Draft objects | simple lines and symbols | Allow to apply line styles and other properties on individual objects |
Here you can find more examples of [Page layouts with TechDraw WB](/freecad-page-layouts-with-techdraw-wb/).

##### Export PDF files
1. Once the TD page is ready, you can move or share this FC file, and export PDF files of the drawing sheets.
    - Select the TD page to export. 
    - Press Menu File - Export PDF.


{{< wiki-image src="/media/freecad-techdraw-house-renovation-drawing.png" alt="2DDrawingFC01.png" mode="inline" align="none" width="700" >}}


{{< wiki-image src="/media/freecad-techdraw-house-renovation-drawing-detail.png" alt="2DDrawingFC02.png" mode="inline" align="none" width="700" >}}
