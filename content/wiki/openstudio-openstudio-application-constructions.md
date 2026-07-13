---
title: "Constructions"
url: "/openstudio-openstudio-application-constructions/"
aliases: ["/OpenStudio/OpenStudio_Application/Constructions/"]
categories: ["OpenStudio Application"]
lastmod: "2025-04-25T18:15:31Z"
---

This page will contain links to or direct inclusion of tutorials and guides related to the constructions tab of the [OpenStudio Application](/openstudio-openstudio-application/).

## Creating Glazing Construction from Scratch
In order to create a glazing type (with specific aluminum framing, double glazing, coating, gas fill, etc.) with specific SHGC's, R-values from scratch, OpenStudio Application allows users to create *some* fenestration materials and constructions[^1]. However, not every [EnergyPlus](/energyplus/) option is available through the OS App.

The most basic is the Simple Glazing System Window Material (requires rated U, SHGC & VT) - look up the "Materials" sub-tab under the "Constructions" tab:

{{< wiki-image src="/media/os-application-simple-glazing-system-window-material.png" alt="OSApplication Simple Glazing System Window Material.png" mode="inline" width="1000" >}}

It is also possible to upload Lawrence Berkeley National Laboratory (LBNL) Window Data for a specific fenestration product. See EnergyPlus Input-Output reference document section or *5.4 Getting Data from WINDOW Program*. These two data types may be supported fully in the OS App, but it is mapped to the [SDK](/openstudio-openstudio-sdk/) behind the scenes: 

 OS:Construction:WindowDataFile,
   {90d22889-50da-4091-8355-fa2ff516e4e6}, !- Handle   Construction Window Data
   File 1;                                 !- Name

This file type could be saved in .osm format and then copy-pasted into your .osm file before reopening. See also OpenStudio Coalition User docs page *[Window Property Frame and Divider](https://openstudiocoalition.org/tutorials/tutorial_windowproperty_frameanddivider/)* and OS SDK documentation on *[WindowPropertyFrameAndDivider Class Reference](https://s3.amazonaws.com/openstudio-sdk-documentation/cpp/OpenStudio-3.9.0-doc/model/html/classopenstudio_1_1model_1_1_window_property_frame_and_divider.html)*.

## Modeling Thermal Bridges
This topic is based on the [this UnmetHours post](https://unmethours.com/question/101240/what-is-the-best-way-to-model-linear-thermal-bridges-in-energyplus/), and is related to few topics - [EnergyPlus](/energyplus/) and [OpenStudio Measures](/openstudio-openstudio-application-measures/)[^2].

The *Thermal Bridging and Derating* ([TBD](https://github.com/rd2/tbd)) measure can automate the modification of U-values for walls that include thermal bridging.

This guide is a stub and should be expanded.

#### Related UnmetHours Posts
The following posts should be looked at as well:
- [What is the best way to model linear thermal bridges in EnergyPlus?](https://unmethours.com/question/101240/what-is-the-best-way-to-model-linear-thermal-bridges-in-energyplus/)
- [Introduction of Thermal Bridging and Derating Measure and Other Related Software](https://unmethours.com/question/49632/on-major-thermal-bridging-and-derating-of-surface-constructions/)
- [State of Practice for Thermal Bridges](https://unmethours.com/question/66355/state-of-practice-for-thermal-bridges/#66381)
- [90.1 2022 Requirements for Linear Thermal Bridges](https://unmethours.com/question/97085/901-2022-requirements-for-linear-thermal-bridges/)

## Notes


[^1]: Unmet Hours. (2025). Unmethours.com. https://unmethours.com/question/101556/creating-glazing-construction-from-scratch/

‌
[^2]: Unmet Hours. (2025). Unmethours.com. https://unmethours.com/question/101240/what-is-the-best-way-to-model-linear-thermal-bridges-in-energyplus/
