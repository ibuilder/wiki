---
title: "Bonsai IFCCSV"
url: "/bonsai-ifccsv/"
aliases: ["/BlenderBIM_Add-on/BlenderBIM_IFCCSV/", "/BlenderBIM_IFCCSV/", "/blenderbim-add-on-blenderbim-ifccsv/"]
categories: ["Bonsai"]
lastmod: "2024-05-10T18:13:26Z"
---

> **Stub:** This article needs expansion.


The IFC CSV feature of [IfcOpenShell](/ifcopenshell/) is implemented in [Bonsai](/bonsai/).

{{< wiki-image src="/media/name.png" alt="IFC CSV panel in Bonsai" mode="thumb" caption="IFC CSV panel in Bonsai" >}}


You can either query an external IFC model by loading it via file picker or load the currently active IFC file by ticking off the <code>Load from Memory</code> check box. 

You can either use the pipette to select objects currently selected in the 3D view or using the [Facet Based Selector Syntax](https://docs.ifcopenshell.org/ifcopenshell-python/selector_syntax.html) specify which IFC classes will be queried.  For example, specify IFC classes manually like <code>IfcWall</code> or <code>IfcSlab</code> or you can use a comma <code>,</code> to select more than one class, like so: <code>IfcWindow, IfcSpace</code>.

You can save your query as a <code>.json</code> template or load an existing template. Here's an simple example. 

{{< wiki-image src="/media/bonsai-ifccsv-image.png" alt="Example.png" mode="inline" align="left" >}}

Finally, you can save the output to CSV with the <code>Export IFC to CSV</code> button. One usecase of IFC CSV is to quickly bulk edit many values in an IFC file. So after exporting to CSV, you can edit some properties and load them into your model again with the <code>Import CSV to IFC</code> button.

Examples of how to fill out the CSV attribute field are shown in the table below.

| Description | IFC CSV Query | Example output |
| --- | --- | --- |
| Attributes |  |  |
| Name of element | Name | MyWall |
| Name of IFC type | type.Name | WAL300 |
| Predefined type on element level | PredefinedType | ELEMENTEDWALL |
| Predefined type on type level | type.PredefinedType | SOLIDWALL |
| Property and Quantity Sets |  |  |
| A dictionary of a property set, its   
properties with non-null values and   
an id | Pset_WallCommon | {'IsExternal': True, 'id': 16041} |
| Value of a single property | Pset_WallCommon.IsExternal | TRUE |
| Quantity set property value. Output is a   
number (int or float). | Qto_WallBaseQuantities.Length | 7, 10.66 |
| Materials |  |  |
| Name of a single material name,   
material constituent set name,   
material profile set name.   
Note that names of material layer   
sets will not show here. | material.Name OR mat.Name | Concrete, WoodenWindow, SteelColumn |
| Name of material items. This can be  
name of a single material, material   
layers, constituents or profiles | material.item.Name OR mat.i.Name | Concrete,['SteelProfile'],  
['BrickLayer', 'InsulationLayer'],    
['WoodenFrame', '3-layer window pane'] |
| Name of the first material item. | material.item.Name.0 | Concrete, SteelProfile,   
BrickLayer, WoodenFrame |
| Name of the material used in the   
material item, eg. a material used   
on a material layer. | material.item.Material.Name | ['Steel'], ['Brick', 'GlassWool'],   
['Pine', '3-4-3-4-3 pane'] |
| Thickness of a material layer. In   
case of a single material, output   
will be empty. In case of a constituent   
set or a profile set output will be [None]. | material.item.LayerThickness | [0.3, 0.2], [3000.0], [None, None] |
| Property value (eg. mass density) of each   
material in a material set. Will be [None] if   
material doesn't have the property. Output is   
a list. | material.item.Material.  
Pset_MaterialCommon.MassDensity | [15.0, 30.0], [30.0],   
[2000.0, None], [None, None] |
| Property value (eg. mass density) of a material.   
Output is a number (int or float). | material.Pset_MaterialCommon.MassDensity | 20, 2000 |
| Name of a material layer set. | material.LayerSetName | LayeredBrickWall |
| Names of material layers in a layer set. The same   
as 'material.item.Name' but this query outputs   
only for material layer sets. | material.MaterialLayers.Name | ['BrickLayer', 'InsulationLayer'] |
| Thickness of material layers in a layer set. The same   
as 'material.item.LayerThickness' but this query outputs   
only for material layer sets. | material.MaterialLayers.LayerThickness | [0.3, 0.2] |
| Name of the material used in the   
material layer. The same as 'material.item.Material.Name'   
but this query outputs only for material layer sets. | material.MaterialLayers.Material.Name | ['Brick', 'GlassWool'] |
| Names of material constituents in a constituent set. The same   
as 'material.item.Name' but this query outputs   
only for material constituent sets. | material.MaterialConstituents.Name | ['WoodenFrame', '3-layer window pane'] |
| Name of the material used in the material constituent. The same   
as 'material.item.Material.Name' but this query outputs only   
for material constituent sets. | material.MaterialConstituents.Material.Name | ['Pine', '3-4-3-4-3 pane'] |
| Names of material profiles in a profile set. The same   
as 'material.item.Name' but this query outputs   
only for material profile sets. | material.MaterialProfiles.Name | ['SteelProfile'] |
| Name of the material used in the material profile.  
The same as 'material.item.Material.Name' but this query   
outputs only for material profile sets. | material.MaterialProfiles.Material.Name | ['Steel'] |
| Property value (eg. mass density) of each profile in a   
material profile set. Output is a list. The same as   
'material.item.Material.Pset_MaterialCommon.MassDensity'   
but this query outputs only for material profile sets. | material.MaterialProfiles.Material.  
Pset_MaterialCommon.MassDensity | [20.0], [2400, 3000.0] |
| Property value of the first profile in a material profile set.   
Output is a number. | material.MaterialProfiles.Material.  
Pset_MaterialCommon.MassDensity.0 | 20, 2400 |
