---
title: "COBie MicroMVD"
url: "/micromvds-for-exchange-requirements-cobie-micromvd/"
aliases: ["/COBie_MicroMVD/", "/MicroMVDs_for_exchange_requirements/COBie_MicroMVD/"]
categories: ["BIMTester", "MicroMVD", "Model View Definitions (MVD)"]
lastmod: "2022-07-28T11:22:28Z"
---

The following [MicroMVD](/micromvds-for-exchange-requirements/) vocabulary can be used to check against the successfully exchange of [COBie - Construction Operations Building Information Exchange](/cobie-construction-operations-building-information-exchange/) data.

Note that the vocabulary is not currently exhaustive.

| Test definition | Justification |
| --- | --- |
| <code>Given the IFC file &quot;{file}&quot;</code> | An IFC-SPF file is the expected format for COBie data |
| <code>Then the file should be an {schema} file</code> | COBie data must conform to a client-nominated schema. |
| <code>Then the element {id} is an {ifc_class}</code> | COBie data must only apply to maintainable assets. By default, the COBie standard states that an asset is maintainable when it belongs to a particular IFC class. A client may also provide a list of IFC classes that define a maintainable asset to override the default list. Correct IFC classification forms the basis of all maintainable asset categorisation. |
| <code>Then all {ifc_class} elements have a name matching the pattern &quot;{pattern}&quot;</code> | Although COBie does not mandate a naming scheme, COBie elements are identified by their name, and so a consistent naming pattern will be established with the client and will be audited. |
| <code>Then all {ifc_class} elements have an? {property_path} property</code> | A large variety of COBie data is stored in property sets. |
| <code>Then all {ifc_class} elements have an? {property_path} property</code> | A large variety of COBie data is stored in property sets. |
| <code>Then all {ifc_class} elements have an? {attribute} attribute</code> | Some COBie data, such as Description is stored in element attributes. |
| <code>Then there is a site named &quot;{name}&quot;</code> | COBie data groups assets into facilities and sites. |
| <code>Then there is a building named &quot;{name}&quot;</code> | COBie data groups assets into facilities and sites. |
