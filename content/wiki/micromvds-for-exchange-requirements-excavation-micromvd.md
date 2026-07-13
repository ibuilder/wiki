---
title: "Excavation MicroMVD"
url: "/micromvds-for-exchange-requirements-excavation-micromvd/"
aliases: ["/Excavation_MicroMVD/", "/MicroMVDs_for_exchange_requirements/Excavation_MicroMVD/"]
categories: []
lastmod: "2022-07-28T11:22:30Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure that the model captures data relevant to bulk excavation works during construction.

<pre>
Feature: Excavation

In order to evaluate costs and construction sequencing of excavation work
For cost planners and construction planners
Excavation volumes must be present in 3D with relevant metadata

Scenario: Bore hole log data must be digital
 * Bore hole log data must be in &quot;{format}&quot; format

Scenario: Bulk excavation volumes must be present
 * At least one excavation volume is present.
 * Excavation volumes must be uniquely named from the following list:
  | Name   |
  | {name} |
 * All excavation volumes must be assigned to a material, named from the following list of possible materials:
  | Name            |
  | {material_name} |
 * All excavation volume materials must be broken down into its constituents
 * All excavation volume materials must store the material density
 * All excavation volume materials must store the bulking factor as a property called BulkingFactor in a custom property set called uMVD_MaterialExcavation
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{format}</code> | csv | A digital format to extract bore hole data from |
