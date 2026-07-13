---
title: "Levels MicroMVD"
url: "/micromvds-for-exchange-requirements-levels-micromvd/"
aliases: ["/Levels_MicroMVD/", "/MicroMVDs_for_exchange_requirements/Levels_MicroMVD/"]
categories: []
lastmod: "2022-07-28T11:22:31Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure IFC data includes grids.

<pre>
Feature: Levels

In order to locate objects
For all model coordinators, costers, schedulers, and recipients of the final built environment
Levels must be present

Scenario: Ensure that levels are present
 * The building with name &quot;{name}&quot; contains storeys
 * A datum storey must not exist
 * All building &quot;{name}&quot; storeys specify an elevation for the SSL
 * All building &quot;{name}&quot; storeys specify an elevation for the FFL
 * All building &quot;{name}&quot; storeys specify an elevation or Z position.
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{name}</code> | 123FOO | The name of the building |
