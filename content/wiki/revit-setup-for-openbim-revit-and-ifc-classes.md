---
title: "Revit and IFC classes"
url: "/revit-setup-for-openbim-revit-and-ifc-classes/"
aliases: ["/Revit_and_IFC_classes/", "/Revit_setup_for_OpenBIM/Revit_and_IFC_classes/"]
categories: ["Autodesk Revit", "Industry Foundation Classes (IFC)"]
lastmod: "2022-01-31T10:37:53Z"
---

It is possible to control which [IFC classes](/ifc-industry-foundation-classes-ifc-classes/) map to which Revit objects when exporting and importing to some degree. Prior to reading this, it is important to first read the resources provided in [Revit setup](/revit-setup-for-openbim/).

To set IFC classes and predefined types in Revit, it requires intimate knowledge of all of the IFC class names, which ones can be used (i.e. which ones are not abstract), and all of the predefined types possible. Revit does not provide any interface or drop downs or lists that aid selection. Therefore, if you make a spelling mistake, or accidentally type extra characters, the export will also be incorrect. It may be useful to use the [Bonsai IFC class search website](https://bonsaibim.org/search-ifc-class.html) to discover which IFC classes should be used.

## Export
Revit follows a series of convoluted rules to determine what IFC class an object is exported as. If one rule cannot be satisfied, it moves on to the next rule until it finds a suitable IFC class. Strap on your seat belts, because this is going to do your head in.

Note that the rules described on this page are a simplification. The Revit IFC export code is far more nuanced, but it would take prohibitively long to describe all of the edge cases.

## Rule 1: Hardcoded IFC export classes
Revit has a series of hardcoded IFC export classes depending on the type of Revit object. It is not possible to override the rules described in this table in any way, and users are required to remodel the object using another method if they wish to get correct OpenBIM output. The table below describes the *internal* type of Revit object, and how it is exported. If you are unsure what this *internal* type is, this can be checked in the [Revit API documentation](https://www.revitapidocs.com/2020/) (note: this requires some programming background knowledge to understand). If your object is not part of the table below, proceed to rule 2.

| Revit Category | IFC Class | Notes |
| --- | --- | --- |
| <code>Area Scheme</code> | <code>IfcGroup</code> |  |
| <code>Assembly Instance</code> |  |  |
| <code>Beam System</code> | <code>IfcElementAssembly</code> |  |
| <code>Ceiling</code> | <code>IfcCovering</code> |  |
| <code>Ceiling and Floor</code> |  |  |
| <code>Wall Foundation</code> |  |  |
| <code>Curve Element</code> |  |  |
| <code>Curtain System</code> | <code>IfcCurtainWall</code> or <code>IfcRoof</code> | If drawn as a wall, it turns into <code>IfcCurtainWall</code>. If drawn as a roof, it turns into <code>IfcRoof</code>. |
| <code>Duct Insulation</code> | <code>IfcCovering.INSULATION</code> |  |
| <code>Duct Lining</code> | <code>IfcCovering.WRAPPING</code> |  |
| <code>Electrical System</code> |  |  |
| <code>Fabric Area</code> |  |  |
| <code>Fabric Sheet</code> |  |  |
| <code>Face Wall</code> |  |  |
| <code>Filled Region</code> |  |  |
| <code>Grid</code> |  |  |
| <code>Group</code> |  |  |
| <code>Hosted Sweep</code> |  |  |
| <code>Part</code> |  |  |
| <code>Pipe Insulation</code> | <code>IfcCovering.INSULATION</code> |  |
| <code>Railing</code> | <code>IfcRailing</code> |  |
| <code>Ramp</code> | <code>IfcRamp</code> |  |
| <code>Rebar</code> | <code>IfcReinforcingBar</code> |  |
| <code>Rebar Coupler</code> |  |  |
| <code>Roof Base</code> |  |  |
| <code>Spatial Element</code> |  |  |
| <code>Stairs</code> |  |  |
| <code>Text Note</code> |  |  |
| <code>Topography Surface</code> |  |  |
| <code>Truss</code> |  |  |
| <code>Wall</code> | <code>IfcWall</code> or <code>IfcWallStandardCase</code> or <code>IfcFooting</code> | A wall in IFC4 is always an <code>IfcWall</code> unless it is a system family and has its function set to <code>Retaining</code> or <code>Foundation</code>. If so, you have the option of overriding it to be an <code>IfcFooting</code>. |
| <code>Wall Sweep</code> | <code>IfcBuildingElementProxy</code> |  |
| <code>Zone</code> |  |  |
## Rule 2: Check for a manually overridden parameter that exists in the family itself
In the next rules, we will talk about overriding parameters. Typically these are defined in your project, but if you have this parameter defined not as a project parameter but as a family parameter, then this will take precedence and the value set in the family will determine what it is exported as.

This can lead to very troublesome fixes, where you have set the IfcExportAs parameter throughout your project, but the exporter will still ignore it and follow your family parameters overrides, which cannot be scheduled. This involves a very painful process where you need to go through each family and press "Edit Family" and fix them one by one.

If you do not have any parameters in your family definition, please keep reading.

## Rule 3: Check for a manually overridden instance parameter
The IFC export class can be overridden on a per instance basis. To do this, parameters need to be created and assigned to instances. A shared parameter file with these parameters is provided in the [Revit setup](/revit-setup-for-openbim/) page. If none of these parameters are present, proceed to rule 3.

When the IFC class is overridden at an instance level, this additionally overrides the IFC type object that the IFC element is assigned to. For example, if your Revit category is <code>Structural Columns</code>, but override a column instance to be an <code>IfcWall</code>, Revit will also automatically create a corresponding <code>IfcWallType</code> with the column type information. It is not possible to control the IFC class of the corresponding IFC type object. To determine the corresponding type, Revit will attempt to simply append the word "Type" to the end of the element class name.

When a predefined type is defined, it should be noted that it will set the predefined type on the corresponding IFC type object, not the IFC object itself. For example, if you set a predefined type of <code>PLUMBINGWALL</code>, that value will get assigned to the <code>IfcWallType</code>, not the <code>IfcWall</code>. This means that if you have two instances with two different predefined types belonging to one Revit family and same Revit type, Revit will still create two IFC type objects in IFC. It is not possible to control this, and will likely lead to broken type and element relationships in schedules, as well as unnecessarily duplicated information.

| Parameter Name | Parameter Type | Notes |
| --- | --- | --- |
| <code>IfcExportAs</code> | Instance | This may be filled out in two ways, either just the desired IFC export class (e.g. <code>IfcWall</code>) or the IFC export class and the predefined type joined with the dot symbol (e.g. <code>IfcWall.PLUMBINGWALL</code>). This text is case insensitive, but it is recommended for neatness to follow the conventions in the IFC documentation, where the classes use CapsCase and the predefined type uses ALLCAPS. |
| <code>IfcType</code> | Instance | **Note: this is deprecated and should not be used.** Despite being deprecated, Autodesk still ships this in their shared parameters file, and so we have chosen to document its usage here. This may be filled out with the desired predefined type (e.g. <code>PLUMBINGWALL</code>). This text is case insensitive, but it is recommended for neatness to use ALLCAPS as per the IFC documentation. If a predefined type is specified both in the <code>IfcType</code> parameter as well as in the <code>IfcExportAs</code> parameter (via joining with the dot symbol), then the <code>IfcType</code> takes priority. Therefore, it is advised to generally not use the dot notation, and keep the two values separated. |
| <code>IfcExportType</code> | Instance | **Note: this should be used instead of <code>IfcType</code>.** This may be filled out with the desired predefined type (e.g. <code>PLUMBINGWALL</code>). This text is case insensitive, but it is recommended for neatness to use ALLCAPS as per the IFC documentation. If a predefined type is specified in all three possible parameters, i.e. the <code>IfcExportType</code> parameter, the <code>IfcType</code> parameter as well as in the <code>IfcExportAs</code> parameter (via joining with the dot symbol), then the <code>IfcExportType</code> takes priority over the other two. Therefore, it is advised to generally not use the dot notation, and keep the two values separated. It also advised to avoid <code>IfcType</code> completely to prevent user confusion. |
## Rule 4: Check for a manually overridden type parameter
You can also override by Revit type. Note that the parameters below only work if you are using a recent version of the exporter, so please update as recommended in the [Revit setup](/revit-setup-for-openbim/), as some out of the box exporters have a bug which prevent these parameters from working. If none of these parameters exist, proceed to rule 4.

If the project is based on IFC2X3, it is advisable to override by type, as IFC2X3 contains more granular IFC classes for element types, especially in regards to MEP disciplines.

Similar to how manually overriding instance parameters will cause a corresponding IFC type object to be generated, manually overriding type parameters will also change all instances. For example, if a type is overridden to be an <code>IfcWallType</code>, all instances will turn into <code>IfcWall</code>. For this reason it is generally advised to override by type prior to overriding by instance.

| Parameter Name | Parameter Type | Notes |
| --- | --- | --- |
| <code>IfcExportAs[Type]</code> | Type | See rules for manually overridden instance parameters in Rule 2. |
| <code>IfcType[Type]</code> | Type | See rules for manually overridden instance parameters in Rule 2. |
| <code>IfcExportType[Type]</code> | Type | See rules for manually overridden instance parameters in Rule 2. |
## Rule 5: Check if it is part of a furniture group
If the element is contained within a Revit group that is to be exported as an <code>IfcFurniture</code>, it is always exported into an <code>IfcSystemFurnitureElement</code>. If this is not the case, proceed to rule 5.

## Rule 6: Check IFC class mappings table
Revit offers a mapping table from Revit category (and subcategory) to IFC class and IFC Predefined Type. You can manually access this by going to <code>File &gt; Export &gt; Options &gt; IFC Options</code>. You can save and load these settings. After this rule is applied, proceed to rule 6.

Out of the box, there are many shortcomings to the IFC class mappings table. OSArch provides an improved default set of IFC class mappings in the [Revit setup](/revit-setup-for-openbim/) page, and describes what the improvements are.

## Rule 7: Set blank predefined types to UNDEFINED
If the predefined type cannot be determined after the rules so far, it is set to <code>UNDEFINED</code>.

If after all these rules, the IFC class is still unknown, or is an <code>IfcBuildingElementProxy</code> or <code>IfcBuildingELementProxyType</code>, then proceed to rule 7.

## Rule 8: Check for particular hardcoded structural types
This rule only applies if the IFC class is still undetermined, or if it has determined the class to be an <code>IfcBuildingElementProxy</code> or <code>IfcBuildingELementProxyType</code>. This means that even if you wanted the object to be a <code>IfcBuildingElementProxy</code> or <code>IfcBuildingELementProxyType</code>, there is still a chance that Revit will ignore the instruction and override it at the last moment. This only applies to structural type families, where certain types will export as a particular type.

| Revit Category | IFC Class |
| --- | --- |
| <code>Structural Beam</code> | <code>IfcBeam</code> |
| <code>Structural Brace</code> | <code>IfcMember</code> |
| <code>Structural Footing</code> | <code>IfcFooting</code> |
| <code>Structural Column</code> | <code>IfcColumn</code> |
## Import
TODO
