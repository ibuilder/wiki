---
title: "Low carbon construction"
url: "/low-carbon-construction/"
aliases: ["/Low_carbon_construction/"]
categories: []
lastmod: "2023-07-11T13:25:14Z"
---

> **Stub:** This article needs expansion.

... but I'm working on it [User:Duncan](/User:Duncan/)

Low Carbon Construction describes an approach to architecture, engineering & construction (AEC) which focuses on lowering a projects [carbon footprint](https://en.wikipedia.org/wiki/Carbon_footprint). A simple description cited on Wikipedia is the following:

*LCA studies the environmental aspects and potential impacts throughout a product's life cycle (i.e., cradle-to-grave) from raw materials acquisition through production, use and disposal. The general categories of environmental impacts needing consideration include resource use, human health, and ecological consequences.*

Building's LCA stages according to EN 15978:

{{< wiki-image src="/media/buildings-lca-stages-according-to-en-15978.jpg" alt="Buildings-LCA-stages-according-to-EN-15978.jpg" mode="inline" >}}

This page lists Free/Libre & Open Source Software relevant for reducing the carbon impact of the AEC sector.

Design & analysis itself is out-of-scope, but is an essential aspect of securing the low carbon impact of a project.

Useful design software is Blender (with relevant add-ons) & FreeCAD. Two dimensional drafting software like LibreCAD & QCAD CE are perhaps less useful as they cannot provide the basis for extracting material, areas & quantities for any analysis.

Analysis software is a huge category where FLOSS is very strong. Ladybug Tools is perhaps the most powerful as it brings many other tools together. Ladybug Tools is essentially an interface for several industry standard validated engines. It is divided into modules which support the following and more:

- Daylighting and thermodynamic modeling (see Radiance)
- Energy models (see EnergyPlus/OpenStudio)
- Standard EnergyPlus Weather files (.EPW)
- Solar radiation studies
- Sunlight-hours modeling
- Computational fluid dynamics modelling of air & thermal flows (see OpenFOAM)
- District energy simulation (see URBANopt)
- Electrical infrastructure simulation (see OpenDSS)
- Renewables optimization (see REopt)
- Heat island modelling (see UWG)

There are integrations with design software such as [Ladybug-Blender](https://github.com/ladybug-tools/ladybug-blender/) written in Python. There is some integration of [Ladybug-FreeCAD](https://wiki.freecad.org/index.php?title=Ladybug).

    1. list of tools. Ladybird tool can be integrated directly inside FLOSS tools [Sverchok](/sverchok/) (inside [Blender](/blender/)) and commercial software like [Dynamo](/dynamo/) (inside [Revit](/autodesk-revit/)) and [Grasshopper](/Grasshopper/) (inside [Rhino](/rhinoceros-3d/)).
