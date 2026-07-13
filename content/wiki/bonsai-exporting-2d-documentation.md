---
title: "Bonsai exporting 2D documentation"
url: "/bonsai-exporting-2d-documentation/"
parent: "/bonsai/"
aliases: ["/BlenderBIM_Add-on/BlenderBIM_Add-on_exporting_2D_documentation/", "/BlenderBIM_Add-on_exporting_2D_documentation/", "/BlenderBIM_Add-on_pages_Exporting_2D_documentation/", "/Exporting_2D_documentation_with_BlenderBIM_Add-on/", "/blenderbim-add-on-blenderbim-add-on-exporting-2d-documentation/"]
categories: ["Blender", "Bonsai"]
lastmod: "2024-11-07T23:31:35Z"
---

## 2D Construction Documentation
Although still in early [alpha](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha) development, Bonsai provides the capability to publish a complete traditional 2D construction documentation of your model. The result is currently a combination of vector and raster data, compiled into [SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) sheet files. (the projected geometry is rendered as a raster image, the cut geometry and any 2D annotations are kept as vectors)

There is one fundamental difference to the way traditional software handles 2D documentation. The 2D vector output from Bonsai is not a finished fixed vector image, but as per definition of SVG a set of 2D geometry with applied CSS styling. That means, that in theory we can output one set of drawings and only by changing the applied CSS we can control the [LOD](/level-of-detail/).

The SVG sheet file is compiled from a SVG sheet template and one or more views exported from Blender, interpreting any variables included in the template and/or view.

The resulting SVG sheets can be easily converted into pdf files for presentation or dxf for collaboration. Examples of available converters:
- [Inkscape](/inkscape/)
- [Batik](http://xmlgraphics.apache.org/batik/)

## Setting up a view
A view is basically an orthographic camera, which you can place manually, or by using the "Add Drawing" button in Output Properties > SVG Drawings. This command creates the necessary camera with a default name, centered on origin. The newly created camera is automatically activated and you can rename it by double clicking its name. 

You can also activate any camera used as a view by selecting it from the list and using the "Activate View" command.

## Selecting geometry to be cut
The raster image is rendered directly from your Blender model. The vector section is however not performed on the Blender geometry, but on an external [IFC](/Introduction_to_IFC/) file. 

[How to export an IFC file from Blender.](/bonsai-for-building-and-exporting-an-ifc-model/)

The ifc file on which the vector cut will be performed has to be chosen under Output Properties > SVG Drawings > Add IFC File and selecting one or more IFC files.
{{< wiki-image src="/media/bonsai-ifc-file-selection-01.jpg" alt="Selecting an IFC file for a section cut" mode="frame" caption="Selecting an IFC file for a section cut" align="center" >}}

## Defining drawing appearance
As mentioned earlier, the resulting SVG file gets its final appearance from the style sheet, defined in the [Project data directory](/bonsai-setting-up-a-bim-project/). The CSS controls the appearance using classes, which means that by assigning an arbitrary class, any group of objects can be assigned a specific appearance. Some of the classes are defined as an example in the <code>PROJECT_DATA_DIRECTORY⁄styles⁄default.CSS</code>, defining the appearance of the annotation elements added through UI (see below) and some basic material hatches.
The symbols and hatches referenced by the CSS file are standard SVG files stored in <code>PROJECT_DATA_DIRECTORY⁄templates⁄</code>

The predefined material classes are assigned automatically to all objects, based on the name of their Blender material. As an example, when no material is defined, the section hatch in SVG is the default black. By assigning a material named named <code>brick</code> (case sensitive!) to an object, its resulting hatch in SVG changes in two parallel diagonal lines. Note that it is's blender material name if your object's material is IfcMaterial. If it's not IfcMaterial (for example if it's IfcMaterialLayerSet) then <code>brick</code> should be IfcMaterialLayerSet's name.

More material patterns are available in [`bonsai/bim/data/assets/patterns.svg`](https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.8.0/src/bonsai/bonsai/bim/data/assets/patterns.svg). These include <code>crosshatch1</code>, <code>crosshatch2</code>, <code>crosshatch3</code>, <code>sand</code>, and <code>grass</code>. You can also define your own patterns in a similar manner.
{{< wiki-image src="/media/svg-brick-hatch-pattern.jpg" alt="Left: object without material, Right: object with Blender material named \"brick\"." mode="frame" caption="Left: object without material, Right: object with Blender material named \"brick\"." align="center" >}}

## Adding annotation
There are currently two ways to add annotation. First, Bonsai plug-in recognizes a number of appropriately named objects on view export and interprets them as 2D annotation and second, it also recognizes the annotation added by the [MeasureIt-ARCH](/measureit-arch/) plug-in. (currently only in the latest git master branch, see [MeasureIt_ARCH readme](https://github.com/kevancress/MeasureIt_ARCH/commit/831fe4a20f585d0f75b9f4c9e5a6893c3f4a5933) for more information on how to make it work with Bonsai) 

Currently recognized objects with their respective necessary names are:


- Curve - IfcAnnotation/Dimension.Number - as a dimension
- Curve - IfcAnnotation/Equal.Number - as a dimension with the letters EQ instead of its value
- Curve - IfcAnnotation/Leader.Number - as a label with a leader arrow symbol
- Curve - IfcAnnotation/Stair.Number - as a staircase arrow symbol
- Curve - IfcAnnotation/Section Level - as a section elevation dimension with an arrow symbol
- Curve - IfcAnnotation/Plan Level - as plan elevation dimension with a crosshair symbol
- Mesh - IfcAnnotation/Hidden.Number - as a dashed curve
- Text - IfcAnnotation/Text.Number - as a text field
- Curve - IfcAnnotation/Fall - indicate slope on a ramp, for example

The plug-in provides commands to create the correctly named dummy object in the Sidebar ("N" panel) > Bonsai > Annotation.
{{< wiki-image src="/media/bonsai-annotation-01.jpg" alt="Dummy annotation objects" mode="frame" caption="Dummy annotation objects" align="center" >}}

## Dimensions
- Override a dimension
    - Set the Description attribute of that dimension. This means that that dimension needs to be separate from other dimensions.
    - Add BBIM_Dimension pset and enable "DescriptionOnly". Otherwise the description is shown in addition, instead of replacing the dimension.

- Show ticks on dimension strings in Blender viewport {{< wiki-image src="/media/dimension.png" alt="Dimension.png" mode="inline" >}}
    - EPset_Annotation.Classes = oblique
        - {{< wiki-image src="/media/ticks.png" alt="Ticks.png" mode="inline" >}}

## Intelligent Tagging of Objects
Go [here](/bonsai-adding-labels-linked-to-properties-and-quantities/) for adding labels, like wall/window tags, that are intelligently linked to the object's data.

{{< wiki-image src="/media/bulk-tag-location.png" alt="Bulk tag location.png" mode="thumb" >}}

To tag objects:
- select Annotation Tool choose annotation type
- select objects to tag
- use "Bulk Tag"


If you moved the tagged objects or changed them (for example stair is wider now) you can readjust tags by selection annotations and using "Readjust" in Annotation Tool.

Currently there are 2 ways of tagging:
1. Text tagging - will create IfcAnnotation of type Text at the center of the object then you can refer to the tagged object properties in the text. [More](/bonsai-adding-labels-linked-to-properties-and-quantities/#adding-a-text-with-a-variable).
1. Stair Arrow tagging - will create stair arrow by the stair X axis going until the last stair step. [Example](https://i.imgur.com/xFHtY73.png).

## Drawing Styles and Filters
If you select the camera object of the drawing, and go to EPset_Drawing property you can set the following property values

- Metadata:
    - For example add property you'd like to be exported to SVG class.  Examples
        - <code>Pset_WallCommon.Status</code>
        - <code>r&quot;Pset_.*Common&quot;</code>
            - Will attach a class like the following to the SVG object <code>rPsetCommon-StatusEXISTINGDEMOLISHid68585</code>
                - Example of how a css regular expression to style the svg <code>[class*=&quot;PsetCommon-StatusEXISTINGDEMOLISH&quot;] { fill: url(#demolish); stroke: red; stroke-dasharray: 2, 1; }</code>
    *NOTE: currently attaching metadata is not supported for 2d representations and it's not possible to create custom style for them. See [example](https://community.osarch.org/discussion/comment/16117/#Comment_16117), [related issue to track progress](https://github.com/IfcOpenShell/IfcOpenShell/issues/3330)*
- Include and Exclude
    - In the Include and Exclude property you can indicate what to include/exclude from the drawing.  A few examples.
        - Exclude:
            - <code>IfcElement , /Pset_.*Common/.Status=DEMOLISH</code>
            - <code>IfcElement , /Pset_.*Common/.Status=NEW</code>
            - <code>IfcElement , EPset_Status.Status=DEMOLISH</code>
        - Include:
            - <code>IfcElement , /Pset_.*Common/.Status=DEMOLISH</code> only show demo.
            - <code>IfcElement , /Pset_.*Common/.Status=NEW</code> only show new.
- Paths to...
    - Stylesheet:
        - defaults to: <code>drawings/assets/default.css</code>
    - Markers:
        - defaults to: <code>drawings/assets/markers.svg</code>
    - Symbols:
        - defaults to: <code>drawings/assets/symbols.svg</code>
    - Patterns:
        - defaults to: <code>drawings/assets/patterns.svg</code>
    - ShadingStyles:
        - defaults to: <code>drawings/assets/shading_styles.json</code>

- Dimension Rounding
    - MetricPrecision:
    - ImperialPrecision:
        - Example: <code>1/2</code> rounds to the nearest 1/2"
- JoinCriteria
    - If no JoinCriteria is given, it defaults to unjoin the following things <code>[&quot;class&quot;, &quot;material.Name&quot;, &#x27;r&quot;Pset.*Common&quot;.&quot;Status&quot;&#x27;]</code>. If you want to unjoin just <code>material.Name</code>, for example, set JoinCriteria value to: <code>material.Name</code>

## Text Styling
- Background for Ifc Text annotations in SVG
To add fill background of Ifc Text annotation with white color you can add "fill-bg" class to EPset_Annotation.
{{< wiki-image src="/media/text-fill-bg-class-tag.png" alt="Top: in Blender setup, Bottom: the result in svg" mode="frame" caption="Top: in Blender setup, Bottom: the result in svg" align="center" >}}


## Exporting a view
To export a view, select the proper camera, go to Object Data Properties > Diagrams and Documentation > Cut section. On running the "Cut section" command a SVG file is generated in the Diagrams folder in your [Data Directory.](/bonsai-setting-up-a-bim-project/#project-data-directory)
The contents of the generated SVG file depend on the options you check in the Diagrams and Documentation section:
- Should Recut - a vector image is generated by intersecting a plane parallel to the camera plane in camera origin with geometry of the ifc files selected in Output Properties > Documentation.
- Should Render - a raster image is generated by rendering the current Blender model with the current camera
- Should Extract - metadata from the IFC file, such as material or property data (such as in smart annotations), are re-extracted
{{< wiki-image src="/media/bonsai-view-export-options-01.jpg" alt="View export options" mode="frame" caption="View export options" align="center" >}}

## Creating schedules and adding them to a sheet
video: https://matrix.to/#/!WKUQKbTubvxEQJxrIY:matrix.org/$ESx7ajDMO8ZBQahCuD63p0UXn38TCz7cfK4ipq0bgcw?via=matrix.org

Using IFCCSV
[Bonsai IFCCSV](/bonsai-ifccsv/)

## Background SVG
Background SVG's: https://github.com/IfcOpenShell/IfcOpenShell/issues/3002#issuecomment-1518668495

## Copying Annotation from one drawing to another
https://github.com/IfcOpenShell/IfcOpenShell/issues/2966#issuecomment-1606914228

## Settings in Blender Preferences - Add-ons
- SVG to PDF Command: 
    - Windows Examples: 
        - <code> [[[[&quot;inkscape.exe&quot;, &quot;svg&quot;, &quot;-o&quot;, &quot;pdf&quot;]]]] </code>
            - If you want to set the DPI <code> [[[[&quot;inkscape.exe&quot;, &quot;svg&quot;, &quot;-o&quot;, &quot;pdf&quot;, &quot;--export-dpi=300&quot;]]]] </code>  
- SVG Command: 
    - Windows Examples: 
        - <code> [[[[&quot;C:/Program Files/Google/Chrome/Application/chrome.exe&quot;,  &quot;path&quot;]]]] </code>
        - <code> [[[[&quot;C:/Program Files/Inkscape/bin/inkscape.exe&quot;,  &quot;path&quot;]]]] </code>

## See also
- [Getting started with 2D CAD drafting](/getting-started-with-2d-cad-drafting/)

## Updating from older Drawing System
https://github.com/IfcOpenShell/IfcOpenShell/issues/2978#issuecomment-1510374693

## External Resources
- [Support making construction drawing generation like, really, really awesome](https://www.bountysource.com/issues/95048565-make-construction-drawing-generation-like-really-really-awesome)

Tutorial & Examples
- [Creating drawings - Bonsai 200912 Technical WIP Demo - September 12, 2020](https://peertube.social/videos/watch/cb5ec2ca-5469-477a-8fd7-db357ba4c289)
- [IFC OpenBIM SVG construction documentation - 200620 Bonsai Technical WIP Demo - June 23, 2020](https://peertube.social/videos/watch/021a6574-b175-4c43-b83d-6a133c54a199)
- [Housing alteration design documentation with Bonsai](https://community.osarch.org/discussion/199/demonstration-of-blenderbim-add-on-used-to-produce-house-alteration-drawings)
- [The Revit office building as pure IFC documentation](https://community.osarch.org/discussion/comment/693/#Comment_693)
- [Examples of floor plans derived from IFC](https://community.osarch.org/discussion/comment/4419/#Comment_4419)
