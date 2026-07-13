---
title: "Bonsai Costing"
url: "/bonsai-costing/"
aliases: ["/BlenderBIM_Add-on/BlenderBIM_Costing/", "/BlenderBIM_Costing/", "/blenderbim-add-on-blenderbim-costing/"]
categories: ["Blender", "Bonsai Costing", "Bonsai"]
lastmod: "2025-04-14T06:07:03Z"
---

## W.I.P. Demonstrations
## Live Session 1 15/05/2021
### Main Topics
1. How to convert IFC2x3 to IFC4
1. Discovering the Scheduling Tools
1. Discovering the Costing Tools
1. Discovering the Quantity Take Off Tools
### Video Demo
<div><youtube width="600" height="340">https://www.youtube.com/embed/lTUsC6OE01k</youtube></div>

### Sample Files
## Project Setup and Costing Tools
## Project setup
- Option 1: Native authoring of IFC in Bonsai 


{{< wiki-image src="/media/create-project-2.png" alt="Create New Project" mode="frame" caption="Create New Project" align="center" width="200" >}}

1. You can find the command in Blender-Bonsai under File --> New IFC Project and Choose which unit, template, or from the wizard panel
1. Make sure to use IFC4 or IFC4x3, otherwise convert your IFC2x3 file to IFC4 or IFC4x3

- Option 2: Open an existing .ifc file

{{< wiki-image src="/media/open-project-2.png" alt="Open an Existing IFC Project" mode="frame" caption="Open an Existing IFC Project" align="center" width="200" >}}

1. Go to File --> Open IFC Project
1. Navigate to your .ifc file and click Load Project or

1. Open Recent IFC Project from the drop-down menu

## Create a Cost Schedule
*Entity Definition* of [IfcCostSchedule](https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD1/HTML/schema/ifcsharedmgmtelements/lexical/ifccostschedule.htm)   

*An IfcCostSchedule brings together instances of IfcCostItem either for the purpose of identifying purely cost information as in an estimate for constructions costs or for including cost information within another presentation form such as a work order.*

Cost Schedules can be added under the Blender Scene Properties > Cost and Scheduling > Cost Panel.

Clicking "+ Add Cost Schedule" will add as many schedules as required.

{{< wiki-image src="/media/wiki-costing-001.png" alt="Create a New IfcCostSchedule" mode="frame" caption="Create a New IfcCostSchedule" align="center" width="200" >}}

Assign Name and Type, as described below in Editing attributes

### Edit Cost Schedule attributes
Before populating our Cost Schedules with cost items, it is best to give further information about the Cost Schedules.
This is done by editing the Cost Schedules attributes, by clicking on the "Grease Pencil"

{{< wiki-image src="/media/edit-cost-schedule-properties.png" alt="Edit Cost Schedule Properties" mode="frame" caption="Edit Cost Schedule Properties" align="center" width="200" >}}

A Cost Schedule has the following attributes you can edit:
- Name, 
- Description, 
- ObjectType,
- Identification, 
- PredefinedType,
- Status (PLANNED, APPROVED,AGREED,ISSUED,STARTED), 
- Submitted On, 
- Update Date,

Note: 
- The Cost Schedule's Predefined Type can either be chosen from the dropdown list, or set as "USERDEFINED". If the latter is set as "USERDEFINED", then the attribute Object Type should denote the particular type that further defines the object.
- If "SCHEDULEOFRATES" is selected its format does not use quantities, more on this in the dedicated paragraph  

### Create a Schedule of Rates
The purpose of the Schedule of Rates is to provide a Cost Schedule limited to the Cost Value of a Cost Item without quantities  

The same Cost Value can be assigned to a Cost Item in a, for instance, Bill of Quantities, creating a link between the two Cost Schedules.


{{< wiki-video src="/media/create-sor.mp4" poster="/media/create-sor.png" title="Create Cost Schedule of Rates" caption="Create Cost Schedule of Rates" align="center" width="200" >}}

Editing of a Cost Item in the Schedule of Rates follows the same process used in other Cost Schedules.

{{< wiki-video src="/media/create-sor-cost-item.mp4" poster="/media/create-sor-cost-item.png" title="Create Cost Item in a Schedule of Rates" caption="Create Cost Item in a Schedule of Rates" align="center" width="200" >}}

## Create Cost Items
*Entity Definition* of  [IfcCostItem](https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD1/HTML/link/ifccostitem.htm)  

*An IfcCostItem describes a cost or financial value together with descriptive information that describes its context in a form that enables it to be used within a cost schedule. An IfcCostItem can be used to represent the cost of goods and services, the execution of works by a process, lifecycle cost and more.*

Click on the Folder Tree to Enable Editing Cost Items

{{< wiki-image src="/media/edit-cost-schedule.png" alt="Open a Cost Schedule for Editing" mode="frame" caption="Open a Cost Schedule for Editing" align="center" width="200" >}}

To add a Cost Item click on "+ Add Summary Cost"

{{< wiki-image src="/media/create-cost-item.png" alt="Add Summary Cost" mode="frame" caption="Add Summary Cost" align="center" width="300" >}}

Refering to the figure below, and the attached template, a basic cost item structure would look like this:

{{< wiki-image src="/media/edit-cost-item-01.png" alt="Cost Item entities" mode="frame" caption="Cost Item entities" align="center" width="300" >}}

Attributes are editable directly from the panel (in the green frame) by double-clicking on them
- ID : the Identification value of the Cost Item, typically according to a Cost Breakdown Structure (CBS) or similar
- Name : the name assigned to the Cost Item or a short description of its scope

Other attributes can be edited by selecting the "Edit" icon and clicking on the "pencil" as indicated below

{{< wiki-image src="/media/edit-cost-item-02.png" alt="Cost Item Edit Menu" mode="frame" caption="Cost Item Edit Menu" align="center" width="300" >}}

Items editable activating the Edit icon:

1. Cost Item parenting hierarchy
1. Sorting order
1. Quantity
1. Value
1. Edit attributes

The parent items, or Summary Cost Items, should contain calculations of overall quantities and/or overall costs, whilst the related nested items would contain the specific quantites and costs of assigned Building Elements, Processes, or Resources.

In the image below parent Item S.01 contains the `SUM` of the child items 1.1 and 1.2 below

{{< wiki-image src="/media/edit-cost-item-03.png" alt="Cost Item Hierarchy" mode="frame" caption="Cost Item Hierarchy" align="center" width="300" >}}

Cost items can be further nested like in the image below where the top item contains cost items 1.1 and 1.2, and a summary cost item 1.3 which itself contains cost items 1.3.1, and 1.3.2

{{< wiki-image src="/media/edit-cost-item-04.png" alt="Cost Items Nested Structure" mode="frame" caption="Cost Items Nested Structure" align="center" width="300" >}}

### Add Cost Item Values
1. Manually
To manually add a value to a cost item, select the item, then "Edit", and click on the "disc" icon


{{< wiki-image src="/media/cost-edit.png" alt="edit cost item" mode="frameless" align="center" width="800" >}}

now some options become available at the bottom of the panel

in this example (1) select "Fixed" from the drop-down menu, (2) enter the desired value, (3) click on "Add Value", and (4) close the cost item edit

{{< wiki-image src="/media/cost-edit-2.png" alt="Edit cost value" mode="frameless" align="center" width="800" >}}

The cost item has a value that is multiplied times the "quantity" to calculate its "Total Cost"

If the cost item represents a "Summary", or a parent of nested child cost items, the procedure is as follows: (1) Select "Sum" from the drop-down menu, (2) click on "Add Value", (3) close the cost item edit:

{{< wiki-image src="/media/cost-edit-3.png" alt="add a sum value to a cost item" mode="frameless" align="center" width="800" >}}

1. From a Schedule of Rates

- open the panel "Cost Item Rates"
- select the Schedule of rates from the drop-down menu
- select the rate
- click on the icon to link the rate to the one in the main Cost Schedule

### Add Cost Item Quantities
There are different ways to add a Cost Item Quantity

1. by manually enter it: (1) select the Cost Item, (2) "Edit", (3) click on the "switch" icon

{{< wiki-image src="/media/quantity-edit.png" alt="edit quantity" mode="frameless" align="center" width="800" >}}

then click on the "pencil" to edit it

{{< wiki-image src="/media/quantity-edit2.png" alt="quantity edit 2" mode="frameless" align="center" width="800" >}}

Once the panel below is available (1) enter the quantity in the box (in this case it shows CountValue, if a different unit is used, like volume or area, it may not look the same), (2) click on the tick icon to close it

{{< wiki-image src="/media/quantity-edit3.png" alt="edit quantity step 3" mode="frameless" align="center" width="800" >}}

### Assign Building Elements to Cost Items
This session goes through the process of:

1. perform take-off quantity of elements in the project
1. check values in Quantity Sets automatically assigned to the elements
1. assign quantity values to the cost items in a cost schedule

### Derive Quantities from linked Building Element Quantities
Insert Content Here

### Calculate Cost Item Totals
1. Component Values and how to use them
1. Calculating overall cost based on nested cost items

## Useful Tools
### Copying Unit Costs between cost items
Insert Content Here

### Quantity Take off Tools
1. Derive Heights, Areas, Volumes
    1. Manual quantities
    1. Automatic quantities
    1. Derive formwork areas

## Creating Project Libraries
## Deriving Cost items from Processes
## Deriving Costs items from Resources
## Creating Schedule of Rates based on Processes, Resources and Products
## Sample Files
- .ifc template for costing
