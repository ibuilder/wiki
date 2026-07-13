---
title: "Quantity take-off MicroMVD"
url: "/micromvds-for-exchange-requirements-quantity-take-off-micromvd/"
aliases: ["/MicroMVDs_for_exchange_requirements/Quantity_take-off_MicroMVD/", "/Quantity_take-off_MicroMVD/"]
categories: ["BIMTester", "Bonsai", "MicroMVD", "Model View Definitions (MVD)"]
lastmod: "2022-07-28T11:22:32Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure that data is present for basic dimensional quantity take-off.

- Concrete material: "Concrete" in IfcMaterial.Category
- Concrete construction method: Pset_ConcreteElementGeneral.ConstructionMethod
- Strength class: Pset_ConcreteElementGeneral.StrengthClass
- Compressive strength: IfcMaterial.Pset_MaterialConcrete.CompressiveStrength
- Wall load bearing: Pset_WallCommon.LoadBearing – True/False
- Wall acousting rating: Pset_WallCommonAcousticRating – Rw / Rw + Ctr 
- Wall fire rating: Pset_WallCommon.FireRating -/-/-

<pre>
Feature: Quantity take-off

In order to cost elements
For cost planners
All elements need to have dimensional and cost-significant metadata assigned

Scenario: All walls must have cost-significant metadata
 * All walls must have a LoadBearing property
 * All walls must have an AcousticRating property
 * All walls must have a FireRating property

Scenario: All concrete elements are identifiable and contain data
 * All concrete elements must be assigned to a concrete material
 * All concrete elements must have their construction method assigned with one of the following values:
   | Value   |
   | In-situ |
   | Precast |
   | {value} |
 * All concrete elements must have their strength class assigned with one of the following values:
   | Value   |
   | N       |
   | S       |
   | {value} |
 * All concrete materials must have their compressive strength assigned with one of the following values:
   | Value     |
   | 20000000  |
   | 25000000  |
   | 32000000  |
   | 40000000  |
   | 50000000  |
   | 65000000  |
   | 80000000  |
   | 100000000 |
   | {value}   |

Scenario: All blockwork walls are identifiable and contain data
 * All blockwork walls must be assigned to a block material
 * All blockwork layers must have a thickness assigned with one of the following values:
   | Value |
   | 0.09  |
   | 0.19  |
   | 0.39  |
 * All blockwork walls must have a core filled property assigned with one of the following values:
   | Value       |
   | None        |
   | 1.2m        |
   | Full height |
 * All blockwork walls must have a load bearing property
 * All blockwork walls must have a HasReinforcement property determining if they contain reinforcement
 * All blockwork walls must have a HasStiffeners property determining if they contain stiffeners

Scenario: All brick walls are identifiable and contain data
 * All brick walls must be assigned to a brick material
 * All brick walls must have a finish assigned with one of the following values:
   | Value  |
   | Render |
   | Paint  |
   | None   |

Scenario: All partition walls are identifiable and contain data
 * All partition walls must be assigned to a partition material
 * All plasterboard layers must be assigned to a plasterboard material
 * All plasterboard materials must have an ImpactResistant property
 * All plasterboard materials must have a MoistureResistant property
 * All plasterboard materials must have a FireResistant property

Scenario: All steel elements are identifiable and contain data
 * All steel elements must be assigned to a steel material
 * All steel elements must have a coating assigned with one of the following values:
   | Architectural  |
   | Fire resistant |
   | None           |
 * All steel elements must have a grade assigned with one of the following values:
   | 250 |
   | 300 |
   | 350 |
   | 400 |
   | 450 |

Scenario: All walls must have dimensional quantities
 * All in-situ concrete walls must have a Length, Height, NetVolume, and GrossSideArea quantity
 * All precast concrete walls must have a Length, Width, Height, and GrossSideArea quantity
 * All blockwork walls must have a Length, Width, Height, and GrossSideArea quantity
 * All partition walls must have a Length, Width, Height, and GrossSideArea quantity
 * All other walls must have a Length, Width, Height, and GrossSideArea quantity

Scenario: All slabs must have dimensional quantities
* All in-situ concrete slabs must have a Width, Length, Depth, Perimeter, GrossArea, and GrossVolume quantity
* All precast concrete slabs must have a Width, Length, Depth, Perimeter, GrossArea, and GrossVolume quantity
* All other slabs must have a GrossArea quantity

Scenario: All columns must have dimensional quantities
* All concrete columns must have a Length, OuterSurfaceArea, and GrossVolume quantity
* All steel columns must have a Length, OuterSurfaceArea, GrossVolume, and GrossWeight quantity
* All other columns must have a Length, OuterSurfaceArea, GrossVolume, and GrossWeight quantity

Scenario: All beams must have dimensional quantities
* All concrete beams must have a Length and GrossVolume quantity
* All steel beams must have a Length, OuterSurfaceArea, GrossVolume, and GrossWeight quantity
* All other beams must have a Length and GrossVolume quantity

Scenario: All foundations must have dimensional quantities
* All footings must have a Length, Width, Height, GrossSurfaceArea, and GrossVolume quantity
* All piles must have a Length, OuterSurfaceArea, GrossVolume, and GrossWeight quantity

Scenario: All other elements must have dimensional quantities
* All railings must have a Length quantity
* All openings must have a Width, Height, Depth, Area, and Volume quantity
* All stair flights must have a Length and GrossVolume quantity
* All structural members must have a Length, OuterSurfaceArea, GrossVolume, and GrossWeight quantity
* All reinforcement bars must have a Length and Weight quantity
* All reinforcement mesh must have a Length, Width, and Weight quantity
* All curtain wall panels must have a GrossArea quantity
* All windows must have an Area quantity
* All duct segments must have a Length, OuterSurfaceArea, and GrossWeight quantity
* All pipe segments must have a Length, OuterSurfaceArea, and GrossWeight quantity
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{file}</code> | project.ifc | The filename or path to any IFC file. |
| <code>{schema}</code> | IFC4 | The schema version. At the moment, these are likely to be either IFC4 or IFC2X3. |
