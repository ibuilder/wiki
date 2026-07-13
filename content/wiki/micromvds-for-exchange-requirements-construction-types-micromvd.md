---
title: "Construction types MicroMVD"
url: "/micromvds-for-exchange-requirements-construction-types-micromvd/"
aliases: ["/Construction_types_MicroMVD/", "/MicroMVDs_for_exchange_requirements/Construction_types_MicroMVD/"]
categories: []
lastmod: "2022-07-28T11:22:29Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure IFC elements are categorised by construction type.

<pre>
Feature: Construction types

In order to quickly determine typical construction types of elements
For procurement and coordination of subcontractors during construction and fabrication
Each element should be assigned to a relevant typical construction type

Scenario: Receiving a file
 * The IFC file &quot;{file}&quot; must be provided
 * IFC data must use the {schema} schema

Scenario: All elements need to have a construction type assigned
 * Construction type names must be unique
 * The following construction types are approved:
   | IFC Element Type | Name   |
   | {ifc_class}      | {name} |
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{file}</code> | project.ifc | The filename or path to any IFC file. |
| <code>{schema}</code> | IFC4 | The schema version. At the moment, these are likely to be either IFC4 or IFC2X3. |
| <code>{guid}</code> | 28q3AgmxP5cepIweO5Of$o | This is a 22 character GlobalId for a particular IFC element. |
| <code>{ifc_class}</code> | IfcWallType | This case insensitive text value must correspond to the full name of an IFC class. This must be an IfcElementType class. |
| <code>{name}</code> | CON01 | Any valid label that is used to tag or annotate construction types on drawings or schedules. |
