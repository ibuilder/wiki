---
title: "Bonsai Quantity Takeoff"
url: "/bonsai-quantity-takeoff/"
aliases: ["/BlenderBIM_Add-on/Bonsai_QuantityTakeoff/", "/blenderbim-add-on-bonsai-quantitytakeoff/"]
categories: []
lastmod: "2025-01-05T09:16:36Z"
---

## Quantity Take-off (QTO)
With Bonsai it is possible to perform Quantity take-off with the operator located under the "Costing and Scheduling" tab (as of the December 2024 version). By clicking on the "Perform Quantity Take-off" button it is possible to perform the quantity dimension calculation and assign these values to the standard Quantity Set defined by the schema for that specific class.

By default, it is possible to choose between these two "ruleset":

- IFC4 Base Quantities - IfcOpenShell

- IFC4 Base Quantities - Blender

In simple words, the main difference between these two rulesets is that the first one uses the IfcOpenShell geometry processor and the second one uses Blender (TODO: explain this concept better).

These two rulesets are enough for the majority of use case but sometimes a user may want to modify or add new rulesets in order to perform custom calculations.

At the moment it is not possible to simply add a new ruleset without modifying the code, but modify the code is not so difficult to add a new one and this is a perfect example for the Free Software Foundation "red shoes example" (don't you know it? https://u.fsf.org/shoetool)

First of all you need to find where are the folders containing the files that Bosai actually uses. If you are not sure where they are located you can look at the installation scripts located into this folder:

/src/bonsai/scripts/installation/

In Linux, the folder is at:  

"$HOME/.config/blender/4.3/extensions/.local/lib/python3.11/site-packages"

In Windows the folder is at:  

"C:\Users\username\AppData\Roaming\Blender Foundation\Blender\4.3\extensions\.local\lib\python3.11\site-packages"

Pay attention that, since this actually modifies the files that allows Bonsai to work, it's always a good advice to make a backup.

There are the three files that are interesting:

1. ifc5d folder > *.json file

{{< wiki-image src="/media/bonsai-quantity-takeoff-patht-to-file.png" alt="patht to file" mode="frameless" align="center" width="720" >}}

In this folder there are the .json files that map all the classes and properties with the calculating functions. So for example let's open "IFC4QtoBaseQuantitiesBlender.json":

The first four lines contain infos about the ruleset (Name, Description) and the type of the "calculator" (Blender in this case).

{{< wiki-image src="/media/jsonfile.png" alt="json file" mode="frameless" align="center" width="1000" >}}

The other lines map the object property standard class with the blender calculating function. If there is a <code>Null</code> instead of the calculating function name, it means that there is no mapping and the calculation is not performed.

For example, "IfcActuator": {Qto_ActuatorBaseQuantities": {"GrossWeight": null}} will not perform but "IfcWall": {"Qto_WallBaseQuantities": {"GrossVolume": "get_gross_volume"}} will.

{{< wiki-image src="/media/ifc-wall.png" alt="IfcWall calculation" mode="frameless" align="center" width="600" >}}

In this case, this means that, for every IfcWall object, there will be created a new Quantity Set called "Qto_WallBaseQuantities", with the "GrossVolume" property and the function "get_gross_volume" will be used to calculate the (gross) volume.

So, where are these functions? Because this ruleset uses the Blender calculator, the calculating functions are stored here:

2. /bonsai/bim/module/qto/calculator.py

{{< wiki-image src="/media/calculator.png" alt="calculator py" mode="frameless" align="center" width="800" >}}

This file contains the calculating functions so, for example, if you open it you will find the "get_gross_volume" function and you can see what the function actually does in order to perform the calculation:

{{< wiki-image src="/media/get-gross-volume.png" alt="get_gross_volume_function" mode="frameless" align="center" width="450" >}}

3. /ifc5d/qto.py

{{< wiki-image src="/media/qto.png" alt="qto.py path" mode="frameless" align="center" width="720" >}}

In this file there is the RULE_SET variable definition that is a list of all the available rulesets. It needs to correspond with the .json file name located in the folder.

{{< wiki-image src="/media/ruleset.png" alt="rule_set function" mode="frameless" align="center" width="640" >}}

This file also contains the correct definition of the calculating function so, if we add new calculating functions, it is necessary to also add new lines there.

## Step-by-step to create a new ruleset
Let's play a little with creating a new ruleset. In this example we create a new calculator to perform the rebar weight calculation automatically, multiplying the gross volume times a constant value.

**1**. Copy/paste an existing .json file in the ifc5d folder (for simplicity let's copy "IFC4QtoBaseQuantitiesBlender.json") and rename it as you want (like "IFC4QtoBaseQuantitiesBlenderRebar.json")

**2**. Add the same file name string into the "/ifc5d/qto.py" RULE_SET variable so it should be like this:

RULE_SET = Literal["IFC4QtoBaseQuantities", "IFC4QtoBaseQuantitiesBlender", "**IFC4QtoBaseQuantitiesBlenderRebar**"] 

If you now run Blender, you will already see the new ruleset under the "Costing and Scheduling" tab, but of course right now it does the same things as the Blender one.

**3**. Open the "IFC4QtoBaseQuantitiesBlenderRebar.json" file with a text editor to do some customization.

**4**. Change "name" in the second line into something like "My Ruleset - Rebar" and "description" to "This ruleset quantifies rebar weight starting from the object gross volume". Let's keep the blender calculation and focus on the mapping.

**5**. Keep only **IfcBeam** and **IfcSlab** objects and delete the others since, for calculation purposes, beams and slabs have different rebar weight/concrete volume ratio. After the modification, the file should look like this:

    {
        "name": "My Ruleset - Rebar",
        "description": "This ruleset quantifies rebar weight starting from the object gross volume",
        "calculators": {
            "Blender": {
                "IfcBeam": {
                    "Qto_BeamRebarQuantities": {
                        "RebarWeight": "get_rebar_beam_weight"
                    }
                },
                "IfcSlab": {
                    "Qto_SlabRebarQuantities": {
                        "RebarWeight": "get_rebar_slab_weight"
                    }
               }
            }
        }
    }


**6**. Open the file: "/bonsai/bim/module/qto/calculator.py", notice that we haven't yet defined the new calculating functions "get_rebar_beam_weight" and "get_rebar_slab_weight", add new ones by copy/paste an existing one and modify them like:

    def get_rebar_beam_weight(o: bpy.types.Object) -> float:
        constant_beam_rebar = 250
        return constant_beam_rebar * get_gross_volume(o)

    def get_rebar_slab_weight(o: bpy.types.Object) -> float:
        constant_slab_rebar = 100
        return constant_slab_rebar * get_gross_volume(o)

**7**. Define the new functions in the "/ifc5d/qto.py" file in order to correctly add the new calculating function by adding the following lines under #IfcMassMeasure section under Blender class

{{< wiki-image src="/media/massmeasure.png" alt="add new functions" mode="frameless" align="center" width="720" >}}

    # Rebar
    "get_rebar_beam_weight": Function("IfcMassMeasure", "Beam Rebar Weight", ""),
    "get_rebar_slab_weight": Function("IfcMassMeasure", "Slab Rebar Weight", ""),

*Et voilà*, now it should be possible to perform the Quantity Take-off method with a custom defined ruleset.
