---
title: "Modeling Plenum Spaces"
url: "/openstudio-openstudio-sketchup-plug-in-modeling-plenum-spaces/"
aliases: ["/OpenStudio/OpenStudio_SketchUp_Plug-in/Modeling_Plenum_Spaces/"]
categories: ["OpenStudio SketchUp Plug-in"]
lastmod: "2025-04-24T15:37:17Z"
---

Based off of this [UnmetHours post](https://unmethours.com/question/182/modeling-plenums-in-openstudio/)[^1].

## Tips
- Always entirely delete any mistakes
- If adjusting spaces or zones, make sure lines recognize adjacent ones, otherwise surfaces that don't recognize each other might be left in the model - i.e. not having complementary outside boundary conditions.

**Suggested Workflow**:
1. Create geometry in SU, intersect surfaces, match surfaces, and visually check outside boundary conditions.
1. Create thermal zones either manually in SU, using the SU user script, or manually in OS.
1. Move to OS and run without HVAC by setting ideal air loads on to test the geometry. This can be done manually for all zones or by writing a measure to do it if your model has a lot of zones.
1. Use the measure "Add Output Diagnostics" with "DisplayAllWarnings" selected - this will give additional details in the ERR file to troubleshoot any severe errors.
1. If there are geometry-related errrors, use the "Search Surfaces" feature in SU to find those mentioned in the ERR file and fix.
1. In extreme cases, manually delete OS objects from the OSM file, but this should be avoided because it can cause additional errors.

## Notes


[^1]: Unmet Hours. (2015). Unmethours.com. https://unmethours.com/question/182/modeling-plenums-in-openstudio/
