---
title: "Grids MicroMVD"
url: "/micromvds-for-exchange-requirements-grids-micromvd/"
parent: "/micromvds-for-exchange-requirements/"
aliases: ["/Grids_MicroMVD/", "/MicroMVDs_for_exchange_requirements/Grids_MicroMVD/"]
categories: []
lastmod: "2022-07-28T11:22:31Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure IFC data includes grids.

<pre>
Feature: Grids

In order to locate objects
For all model coordinators and recipients of the final built environment
Grids must be present

Scenario: Ensure that grids are present
 * There are grids
 * A &quot;{shape}&quot; grid with the name &quot;{name}&quot; exists with the correct number of axes
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{shape}</code> | rectangular | The shape of the grid, chosen from "rectangular", "radial", "triangular", or "irregular". |
| <code>{name}</code> | A | The name of a grid, typically "A" or "B" |
