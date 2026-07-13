---
title: "Construction sequencing MicroMVD"
url: "/micromvds-for-exchange-requirements-construction-sequencing-micromvd/"
aliases: ["/Construction_sequencing_MicroMVD/", "/MicroMVDs_for_exchange_requirements/Construction_sequencing_MicroMVD/"]
categories: []
lastmod: "2022-07-28T11:22:29Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used for construction sequencing data.

<pre>
Feature: Construction sequencing

In order to analyse construction sequencing schedules
For construction sequencers and site managers
Specific model metadata and structure is required

Scenario: All piles are identifiable and contain data
 * All piles must be assigned to a concrete or steel material
 * All piles must have their type assigned with one of the following values:
   | Value  |
   | BORED  |
   | DRIVEN |

Scenario: All multistorey elements are divided per storey
 * All walls are limited to the height of their current storey.
 * All columns are limited to the height of their current storey.
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{guid}</code> | 28q3AgmxP5cepIweO5Of$o | This is a 22 character GlobalId for a particular IFC element. |
