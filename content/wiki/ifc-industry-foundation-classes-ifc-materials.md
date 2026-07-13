---
title: "IFC materials"
url: "/ifc-industry-foundation-classes-ifc-materials/"
parent: "/ifc-industry-foundation-classes/"
aliases: ["/IFC_-_Industry_Foundation_Classes/IFC_materials/", "/IFC_materials/", "/Industry_Foundation_Classes_(IFC)/IFC_materials/"]
categories: ["Industry Foundation Classes (IFC)"]
lastmod: "2023-03-11T15:42:08Z"
---

IFC can store information about real life materials, and objects can be assigned to materials. Materials may contain attributes like a name and description, and contain physical properties. Some of these properties are part of the IFC standard, such as concrete strength, thermal properties, or mechanical properties, or it may be a custom property defined by the user.

A material may be assigned directly to an object. However, for more complex materials, it is possible to combine multiple materials into a composite material. This composite material is known as a material "set" in IFC, and may then be assigned to an object. There are three distinct types of composite material sets.

- Material layer set (each material within this represents a single layer)
- Material constituent set (each material within this represents a single constituent)
- Material profile set (each material within this represents a single profile)

When a material set is defined, it is sometimes necessary to describe which parts of the geometry a portions of the material set applies to. For example, when an object has a material layer set, we need to describe the thickness of each material layer. When we describe a material set assignment parametrically, this is known as a material set usage. There are two types of parametric usages that can be defined in IFC:

- Material layer set usage
- Material profile set usage

A material may also have a visual style associated with it, such as a colour. When viewing an IFC model, the colour of an object may represent its material.

However, it is also possible for IFC objects to be assigned a visual style or colour that is not associated with a material. This is a common cause for confusion, as users may think a colour represents a material. It is made more confusing by the fact that a visual style may have a name. This name is not the same as a material name, but some BIM software may not make the distinction between them.

A visual style may be used to represent non-material information. One common usecase is when a style correlates with a discipline. For example, all hydraulic objects may be coloured blue, and all mechanical objects may be coloured green. The concept of visual styles is a separate concept to materials, and will not be described further here.

## Single Material
The simplest possible material definition is a single material by itself. For example, a [stirrup](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_1/FINAL/HTML/link/reinforcing-stirrup.htm) or a pipe might have their material assigned this way. A few attributes are stored with each material.

| Attribute | Required | Description |
| --- | --- | --- |
| <code>Name</code> | Recommended | This can store the name of the material. If a material is given a unique label or tag that is referenced in documentation annotation or schedules, this is where it should be stored. It is usually a short, coded name. |
| <code>Description</code> | Recommended | This allows you to write a sentence or so to describe the material in human terms. |
| <code>Category</code> | Recommended | Sometimes, it is important to broadly categorise materials to isolate them for costing or procurement purposes. There is no strict requirement on what categories are allowed, but it is highly recommended to use the value "Concrete", "Steel" or blank. |
It is possible for a single material to have [IFC properties](/ifc-attributes-and-properties/) assigned to it. The following sets are defined by the buildingSMART standard, and should be available in your BIM authoring application. If you wish to store a property that is not part of the standard, you may be define your own property set.

| Property Set | Description |
| --- | --- |
| <code>Pset_MaterialCombustion</code> | Used to store chemical properties of combustible materials. |
| <code>Pset_MaterialCommon</code> | Generic material properties. |
| <code>Pset_MaterialEnergy</code> | A set of extended material properties for energy calculation purposes. |
| <code>Pset_MaterialFuel</code> | A set of extended material properties of fuel energy typically used within the context of building services and flow distribution systems. |
| <code>Pset_MaterialHygroscopic</code> | A set of hygroscopic properties of materials. |
| <code>Pset_MaterialMechanical</code> | Useful for describing mechanical properties, usually relevant to structural analysis. |
| <code>Pset_MaterialOptical</code> | A set of optical properties of materials. |
| <code>Pset_MaterialThermal</code> | A set of thermal material properties. |
| <code>Pset_MaterialWater</code> | A set of extended material properties for of water typically used within the context of building services and flow distribution systems. |
{{< wiki-image src="/media/typical-ifc-material.svg" alt="TypicalIfcMaterial.svg" mode="inline" >}}

## Material Constituent Set
A constituent set is made up of individual material constituents. The constituent set itself may be assigned a couple attributes.

| Attribute | Required | Description |
| --- | --- | --- |
| <code>Name</code> | Recommended | This can store the name of the material constituent set. If a material is given a unique label or tag that is referenced in documentation annotation or schedules, this is where it should be stored. It is usually a short, coded name. |
| <code>Description</code> | Recommended | This allows you to write a sentence or so to describe the material in human terms. |
Each individual material constituent within the set is a single material, as described above, but may include additional attributes to describe the nature of the constituent.

| Attribute | Required | Description |
| --- | --- | --- |
| <code>Name</code> | Recommended | This is the name of an individual material constituent within the set, such as "Cement" |
| <code>Description</code> |  | This allows you to write a sentence or so to describe the material in human terms. |
| <code>Fraction</code> |  | This optional attribute may store the percentage of volume or weight that this constituent represents. |
| <code>Category</code> |  | This is the purpose of the constituent or the role it plays within the material set. |
There are two typical usages of a material constituent set. The first typical usage is where a material is made up of a mixture of constituents, like how concrete is made up of sand, cement, aggregate, etc. Each constituent is mixed together, but represents a "fraction" of the whole material constituent set.

The second typical usage is where a single object is simply made up of different materials in an arbitrary structure. For example, a single window element can be made up of an aluminium frame and a glazed panel. In this case, geometry may be modeled that represents the frame, which is assigned to one constituent, and more geometry may be modeled to represent the panel, which is assigned to another constituent.

Although in this example geometry is modeled for each constituent, this is optional. It is acceptable to have a constituent set without needing to explicitly model each constituent geometrically.

{{< wiki-image src="/media/typical-ifc-material-constituent-set.png" alt="TypicalIfcMaterialConstituentSet.png" mode="inline" >}}

## Material Layer Set
A layer set is made up of individual material layers. The layer set itself may be assigned a couple attributes.

| Attribute | Required | Description |
| --- | --- | --- |
| <code>Name</code> | Recommended | This can store the name of the material layer set. If a material is given a unique label or tag that is referenced in documentation annotation or schedules, this is where it should be stored. It is usually a short, coded name. |
| <code>Description</code> | Recommended | This allows you to write a sentence or so to describe the material in human terms. |
Each individual material layer within the set is a single material, as described above, but may include additional attributes to describe the nature of the layer.

| Attribute | Required | Description |
| --- | --- | --- |
| <code>Name</code> | Recommended | This is the name of an individual material layer within the set, such as "Brick" |
| <code>Description</code> |  | This allows you to write a sentence or so to describe the material in human terms. |
| <code>LayerThickness</code> | Yes | The thickness of the material layer. The meaning of "thickness" depends on its usage, but is typically a length using the unit settings of the project, like "0.15m". It may be set to zero for thin materials, such as a membrane. |
| <code>IsVentilated</code> |  | If this is set to true, it means the layer is an air gap, if set to false, it is a solid material. |
| <code>Category</code> |  | This is the purpose of the layer or the role it plays within the material set. It is an arbitrary value, but these values are recommended by buildingSMART: "LoadBearing", "Insulation", or "Finish". |
| <code>Priority</code> |  | This is a number that determines how layers overlap at a junction or corner in a building. A layer with a higher priority will displace or protrude into the layer of a lower priority. |
A typical usage for material layer set is a wall which is often made of multiple layers, creating a "sandwich" of layers. Example layers in a single wall element may be an outer plasterboard lining, an insulation layer, an air gap, or a steel framing layer.

{{< wiki-image src="/media/typical-ifc-material-layer-set.png" alt="TypicalIfcMaterialLayerSet.png" mode="inline" >}}

## Material Layer Set Usage
TODO

## Material Profile Set
{{< wiki-image src="/media/profileset.svg" alt="An example of a material profile set with multiple profiles" mode="thumb" caption="An example of a material profile set with multiple profiles" align="right" >}}

A profile set is made up of individual material profiles. A profile is a shape or outline of a typical cross section which is extruded along an axis. Typically, this is used for structural analysis, where a material profile helps define its mechanical properties.

Typically, only a single profile would be defined in a profile set. This profile would also typically be parameterised, such as a circular proflie, rectangular profile, or I-shaped profile. This would then be used for a duct, pipe, or a beam.

It is also possible, though less common, to define multiple profiles in a profile set. This results in a composite profile, which is useful for describing complex shapes.

{{< wiki-image src="/media/typical-ifc-material-profile-set.svg" alt="TypicalIfcMaterialProfileSet.svg" mode="inline" >}}

## Material Profile Set Usage
TODO

## Assignment example
Following diagram shows how materials are related to their object. Any child of IfcObjectDefinition as IfcWall, IfcDuct etc… can get a material assigned this way :
{{< wiki-image src="/media/ifc-materials-thumbnail.png" alt="IfcMaterials thumbnail.png" mode="thumb" align="center" link="https://wiki.osarch.org/images/8/84/IfcMaterials.svg" >}}
