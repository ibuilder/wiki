---
title: "OpenStudio Application"
url: "/openstudio-openstudio-application/"
aliases: ["/OpenStudio/OpenStudio_Application/"]
categories: ["OpenStudio"]
lastmod: "2025-05-04T03:38:01Z"
---

OpenStudio Application is a software that is part of the OpenStudio ecosystem of tools designed for building energy modeling. The OpenStudio Application is now independently supported and maintained with open source contributions by The OpenStudio Coalition and members of the software community at the GitHub repository https://github.com/openstudiocoalition/OpenStudioApplication. The NREL OpenStudio Application repository no longer accepts new issues or pull requests. Please submit new issues or enhancement requests in the new OpenStudio Coalition repository at https://github.com/openstudiocoalition/OpenStudioApplication/issues.

[1] To understand why the graphical user interfaces are being separated from the SDK, please refer to [A Shift in BTO’s BEM Strategy: A New Future for the OpenStudio Application](https://www.openstudio.net/new-future-for-openstudio-application)*.

For more information about the [OpenStudio Coalition](/openstudio-openstudio-coalition/), including tutorials and documentation for the OpenStudio Application and [OpenStudio SketchUp Plug-in](/openstudio-openstudio-sketchup-plug-in/), please visit https://openstudiocoalition.org/.

## Overview
The OpenStudio Application is a fully featured graphical interface to OpenStudio models including envelope, loads, schedules, geometry, HVAC, and OpenStudio Measures. The OpenStudio Application is open source software and is free to use. The OpenStudio Application is built on top of the [OpenStudio SDK](https://github.com/NREL/OpenStudio).

- [Introduction to OpenStudio Application](/openstudio-openstudio-application-introduction-to-openstudio-application/)

## FloorspaceJS
The FloorspaceJS is a widget for creating 2D for building energy models. NREL [contracted the development](https://github.com/NREL/floorspace.js/issues/348#issuecomment-454983387) of the tool to get it to its current state, but there is very little activity on the tool at the moment. Developers can leverage this open-source software module to produce building energy modeling UI's which include geometry creation. FloorspaceJS is meant to cover simple building geometry use cases only. More complex building geometry is best developed in a full featured CAD tool and exported to gbXML or other formats for building energy modeling. FloorspaceJS is implemented in JavaScript with minimal dependencies, allowing it to be integrated into a wide range of applications, including the OpenStudio Application.

[Documents](https://nrel.github.io/floorspace.js/docs) for FloorspaceJS and the [latest development version](https://nrel.github.io/floorspace.js/) can be found on the [GitHub repository](https://github.com/NREL/floorspace.js). The latest development version can be run in a web browser (preferably Google Chrome).

See article on [OpenStudio Application Geometry](/openstudio-openstudio-application-geometry/) for more information.

## Downloading the OpenStudio Application
The OpenStudio Application can be downloaded for Mac, Linux, and Windows by logging in at https://openstudiocoalition.org/app/.

## Miscellaneous Guides by OpenStudio Section
- {{< wiki-image src="/media/on-location-tab.png" alt="On location tab.png" mode="inline" >}} Site
- {{< wiki-image src="/media/on-schedules-tab.png" alt="On schedules tab.png" mode="inline" >}} Schedules
- {{< wiki-image src="/media/on-constructions-tab.png" alt="On constructions tab.png" mode="inline" >}} [Constructions](/openstudio-openstudio-application-constructions/)
- {{< wiki-image src="/media/on-loads-tab.png" alt="On loads tab.png" mode="inline" >}} Loads
- {{< wiki-image src="/media/on-space-types-tab.png" alt="On space types tab.png" mode="inline" >}} Space Types
- {{< wiki-image src="/media/on-geometry-tab.png" alt="On geometry tab.png" mode="inline" >}} [Geometry](/openstudio-openstudio-application-geometry/)
- {{< wiki-image src="/media/on-building-tab.png" alt="On building tab.png" mode="inline" >}} Facility
- {{< wiki-image src="/media/on-spaces-tab.png" alt="On spaces tab.png" mode="inline" >}} Spaces
- {{< wiki-image src="/media/on-thermal-zone-tab.png" alt="On thermal zone tab.png" mode="inline" >}} Thermal Zones
- {{< wiki-image src="/media/on-hvac-tab.png" alt="On hvac tab.png" mode="inline" >}} HVAC Zones
- {{< wiki-image src="/media/on-var-tab.png" alt="On var tab.png" mode="inline" >}} Output Variables
- {{< wiki-image src="/media/on-sim-settings-tab.png" alt="On sim settings tab.png" mode="inline" >}} Simulation Settings
- {{< wiki-image src="/media/on-scripts-tab.png" alt="On scripts tab.png" mode="inline" >}} [Measures](/openstudio-openstudio-application-measures/)
- {{< wiki-image src="/media/on-run-tab.png" alt="On run tab.png" mode="inline" >}} Run Simulation
- {{< wiki-image src="/media/on-results-tab.png" alt="On results tab.png" mode="inline" >}} Results Summary

## Subpages
