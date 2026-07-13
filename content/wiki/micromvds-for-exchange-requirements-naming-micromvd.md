---
title: "Naming MicroMVD"
url: "/micromvds-for-exchange-requirements-naming-micromvd/"
parent: "/micromvds-for-exchange-requirements/"
aliases: ["/MicroMVDs_for_exchange_requirements/Naming_MicroMVD/", "/Naming_MicroMVD/"]
categories: ["BIMTester", "MicroMVD", "Model View Definitions (MVD)"]
lastmod: "2022-07-28T11:22:31Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to ensure classification system standards are correctly applied.

Warning: this MicroMVD is only in a draft form. It is not ready for use.

<pre>
Feature: Naming

For BIM elements to integrate into existing workflows
As any stakeholder required to identify element information
Particular element attributes and properties must comply with a naming scheme

Scenario: Receiving a file
 * The IFC file &quot;{file}&quot; must be provided
 * IFC data must use the {schema} schema

Scenario: Specific property values must follow a pattern
 * The elements defined by &#x27;{query}&#x27; are referred to as {element_group_name}
 * The element {guid} is exempt from the group {element_group_name} because {reason}
 * All {element_group_name} elements have a {attribute} property matching the pattern {pattern}
 * All {element_group_name} elements have a {attribute} property taken from the list in {csv_file}

Scenario: Particular elements have property values that must follow a pattern
 * The element {guid} has a {attribute} property matching the pattern {pattern}
 * The element {guid} has a {attribute} property taken from the list in {csv_file}
</pre>

You can fill out the variables using the guide below.

| Variable | Example | Description |
| --- | --- | --- |
| <code>{file}</code> | project.ifc | The filename or path to any IFC file. |
| <code>{schema}</code> | IFC4 | The schema version. At the moment, these are likely to be either IFC4 or IFC2X3. |
| <code>{guid}</code> | 28q3AgmxP5cepIweO5Of$o | This is a 22 character GlobalId for a particular IFC element. |
