---
title: "Bonsai Adding labels linked to properties and quantities"
url: "/bonsai-adding-labels-linked-to-properties-and-quantities/"
aliases: ["/Adding_labels_linked_to_properties_and_quantities/", "/BlenderBIM_Add-on_Adding_labels_linked_to_properties_and_quantities/", "/blenderbim-add-on-adding-labels-linked-to-properties-and-quantities/"]
categories: ["Blender", "Bonsai"]
lastmod: "2024-08-17T21:47:11Z"
---

## Displaying data
Each element in a BIM model usually contains a lot of data. The data can obviously be accessed by using a dedicated BIM viewer or read directly by a machine, however, very often a simple graphical way is still necessary. Bonsai uses a system of variables which can be linked to object properties or quantities and which then get dynamically replaced with the actual linked value on 2D view export.

The most common uses of this feature include: 
- room tags
- door/window tags
- fire ratings
- staircase labels
- element composition tags etc.

There is currently no way to see the actual value in the main Blender UI window.

## Adding a text with a variable
When working with BIM objects in Blender, it's often necessary to display specific properties of an object as a label. Bonsai provides a powerful system for linking labels to object properties using variables. This section will guide you through the process of creating and using these linked labels.

For a text object to show a property value of an element, three conditions are necessary:
- The text object has to be linked to the element
- A variable name has to be declared in the text object and it must be linked to a property of the element
- The variable name must be included in the text object (in double curly brackets)

To add a variable text object:
1. Create a new text with Add>Text and manually link it to an object
1. Exit the edit mode, go to Object Data Properties > Text Paper space and pick an object in the Related Element field
1. To declare a variable, go to Object Data Properties > Text Paper space, click on "Add variable" and fill in the variable name
1. The variable must be linked to an object property by filling in the Property Key field

### Basic Syntax
To link a label to an object property, use the following syntax in your text object:

<code>{{property.Name}}</code>

Where <code>property</code> is the type of property you're referencing, and <code>Name</code> is the specific property name.

### Common Property Types
Here are some common property types you can use:

#### Type Properties
- <code>{{type.Name}}</code>
    - This references properties related to the object's type
    - Example: For a door, <code>{{type.Name}}</code> might display "3680R" (the door type)

#### Attributes
Attributes are referenced simply by name:
- <code>{{PredefinedType}}</code> - Predefined properties in the IFC schema
- <code>{{GlobalId}}</code> - Unique identifier of the object
- <code>{{Name}}</code> - Name of the object
- <code>{{Description}}</code> - Description of the object
- <code>{{ObjectType}}</code> - Object type
- <code>{{Tag}}</code> - Tag property of the object

#### Pset Properties
Properties are referenced by name, prefixed with Pset_Name:
- <code>{{Pset_Name.PropertyName}}</code>
- Example: <code>{{Pset_SpaceCommon.NetPlannedArea}}</code>

#### Quantity Properties
Quantities are referenced by name, prefixed with Qto_Name:
- <code>{{Qto_Name.QuantityName}}</code>
- Example: <code>{{Qto_SpaceBaseQuantities.NetFloorArea}}</code>

#### Material Properties
Make sure to assign the material in 'IFC Object Material':
- Material Name: <code>{{material.Name}}</code>
- Material Layer Set Name: <code>{{material.LayerSetName}}</code>
- Material Name (alternative): <code>{{material.item.Material.Name}}</code>
- Material Layers Name: <code>{{material.MaterialLayers.Name}}</code>

Alternative ways to reference material properties:
- <code>{{material.item.Name}}</code>
- <code>{{&quot;material&quot;.&quot;item&quot;.&quot;Name&quot;}}</code>
- <code>{{r&quot;material&quot;.&quot;item&quot;.&quot;Name&quot;}}</code>
- <code>{{mat.i.Name}}</code>

#### Custom Properties
Custom properties (for example in parametric objects) are referenced by name:
- Example: <code>{{Width}}</code>

### Advanced Usage
You can use the double backtick command to run custom evaluations:

- Get the material name assigned to the 1st material layer:
<code>``{{material.item.Material.Name}}[0]``</code>

- Display the total layer thickness rounded to 2 decimal points:
<code>``round(sum({{mat.i.LayerThickness}}),2)``</code>

- Check if an object has a specific status:
<code>``{{r&quot;Pset_.*Common&quot;.&quot;Status&quot;}}[0]`` = EXISTING (for example)</code>
<code>``{{r&quot;Pset_.*Common&quot;.&quot;Status&quot;}}[0][:2]`` = EX (for example)</code>

- Convert a quantity to a different unit:
<code>``int({{Qto_SpaceBaseQuantities.NetFloorArea}})`` SF = 350 SF (for example)</code>

Remember to link your text object to the BIM object and declare the variable name in the text object, linking it to a property of the element. The variable name must be included in the text object using double curly brackets <code>{{like this}}</code>.

By using these syntaxes and techniques, you can create dynamic labels that update automatically based on the properties of your BIM objects in Blender.


{{< wiki-image src="/media/bonsai-ifc-space-tag.jpg" alt="An example of a tagged Ifc Element" mode="frame" caption="An example of a tagged Ifc Element" align="center" width="600" >}}

## Labeling multiple objects
A semi-automatic way to do this whole process is to select objects to be tagged and use the "N" panel > Bonsai > Annotation > Text - this creates a text object for every selected element and links it automatically. (Important: The texts are placed relative to the active Drawing camera, the command will fail if there is no drawing camera present!) Then select one of the created texts, add the desired variables and formatting, select the other texts again and use Object Data Properties > Text Paper space > Propagate Text Data to apply the same variables and formatting on all selected.

{{< wiki-video src="/media/bonsai-auto-tag-02.mp4" poster="/media/bonsai-auto-tag-02.png" title="Adding multiple labels with Bonsai (click on the image and open original file to see the animation)" caption="Adding multiple labels with Bonsai (click on the image and open original file to see the animation)" align="center" width="600" >}}


{{< wiki-image src="/media/bonsai-tagged-ifc-spaces-export.svg" alt="The resulting 2D svg export with interpreted variables" mode="frame" caption="The resulting 2D svg export with interpreted variables" align="center" width="600" >}}
Note that the default style of IfcSpace after export is no fill and no border, which makes it invisible and harder to select with the default Inkscape settings.

## Calculations inside labels
The exporter interpreting the variable also evaluates python functions included in the Property key field. This enables for example simple calculations like rounding - <code>round({{BaseQuantities.GrossFloorArea}},1)</code>, unit conversion, etc.
