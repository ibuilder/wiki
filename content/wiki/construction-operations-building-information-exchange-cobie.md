---
title: "Construction Operations Building Information Exchange (COBie)"
url: "/construction-operations-building-information-exchange-cobie/"
aliases: ["/Construction_Operations_Building_Information_Exchange_(COBie)/"]
categories: ["buildingSMART International", "File formats", "Industry Foundation Classes (IFC)"]
lastmod: "2025-04-03T23:48:13Z"
---

> **Stub:** This article needs expansion.


COBie is a [Model View Definition](/mvd-model-view-definitions/) of IFC for the purposes of computer aided facility management. It describes the exchange requirements of what data needs to be present in an IFC file. The official specifications are found in three documents:

- [National BIM Standard v3 Section 4.2](https://www.nibs.org/files/pdfs/nbimsv3/NBIMS-US_V3_4.2_COBie.pdf) - Describes the intentions and formats of COBie data exchange, workflows and how it benefits the facility management process, and what properties must be present in the IFC file
- [Annex A](https://www.nibs.org/files/pdfs/nbimsv3/NBIMS-US_V3_4.2_COBie_Annex_A.pdf) - Defines which IFC Classes are considered maintainable assets, as well as data mappings from IFC-SPF/IFCXML to SpreadsheetML, and SpreadsheetML to COBieLite
- [Annex B](https://www.nibs.org/files/pdfs/nbimsv3/NBIMS-US_V3_4.2_COBie_Annex_B.pdf) - A list of references and definitions

The buildingSMART Alliance also has a [COBie MVD](http://docs.buildingsmartalliance.org/MVD_COBIE/) on their website which includes an mvdXML. This is a duplicate of the definition by the National BIM Standard organisation. buildingSMART had previously also distributed other COBie MVD documents as a PDF on their website, but this was incorrectly distributed and does not constitute the COBie standard (Note: confirmed by Bill East, author of COBie in 9 October 2019).

## COBie definition of a maintainable asset
COBie defines what is and isn't a maintainable asset by providing a list of IFC classes. The full list is available in the specification, but is often hard to decipher for those new to IFC. For convenience, a full list is provided in the [COBie definition of a maintainable asset](/cobie-definition-of-a-maintainable-asset/) page, including descriptions and predefined types.

## COBie data formats
The specification also outlines multiple ways to present COBie data:

| Format | Notes |
| --- | --- |
| IFC-SPF (.ifc) | Often, an IFC-SPF is produced which contains all of the data relevant for the Coordination View / Reference View MVD, and then is subsequently filtered for COBie-specific data. Most BIM authoring tools require specific workarounds or extra steps in their workflow to extract this IFC-SPF output. |
| IFCXML (.ifcxml) | No tool is currently known to be capable of producing a fully COBie compliant IFCXML file. |
| SpreadsheetML (.xls) | This is a proprietary XML specification tied to Microsoft Excel 2003. This spreadsheet form of COBie was originally designed for [three purposes](https://www.wbdg.org/resources/construction-operations-building-information-exchange-cobie):  
- If a user wants to view COBie data and are incapable to view it in its IFC-SPF data and lack the technical expertise  
- If project stakeholder lacks the funds to invest in IFC-based COBie data  
- If the project scope is small, and a spreadsheet is sufficient to capture the data  
Despite this original intention, the COBie spreadsheet format is currently the most popular format. |
| COBieLite (.xml) | Similar to how COBie IFC-SPF and IFCXML may be converted into SpreadsheetML format via a specified mapping, there is a specified mapping from SpreadsheetML to COBieLite in Appendix A. There is less data loss in this mapping, but there is still a difference in the data. |
## Complications with IFC-SPF
TODO

## Complications with SpreadsheetML
The COBie specification states that there is no difference between the three formats. However, this is not accurate. The specification describes a mapping from the IFC-SPF format to the spreadsheet format. This mapping is a "many-to-one" mapping, describing a series of ways to process potentially multiple data points into a single cell in the spreadsheet. Therefore it is possible to convert from IFC-SPF or IFC-XML into SpreadsheetML, but not vice versa. The mapping is also prone to ambiguity due to its usage of natural language.

For BIM authoring tools that provide both an IFC-SPF and SpreadsheetML output, it should be assumed that the mapping is not correctly followed. Only two tools are currently known that implement the mappings correctly: [Bonsai](/bonsai/) and the [BIMServer COBie Plugins](https://github.com/opensourceBIM/COBie-plugins) (Note: this is in theory, both have not been independently audited).

Another common concern is that SpreadsheetML is tied to a proprietary format, which may not be acceptable for some users. [Bonsai](/bonsai/) is capable of providing the same data in CSV and ODS formats as an alternative to SpreadsheetML.

## Common deviations from the COBie specification
COBie users are expected to review the COBie specifications and determine if there are modifications to be made. Modifications include a review of the definition of a maintainable asset, as well as what properties are expected to be stored, and at what project stage these are to be stored.

The COBie specification was originally written as an IFC2X3 MVD. In IFC4, some definitions have yet to be reviewed in the specification. Therefore, there are some portions of the COBie specification which are unlikely to apply in IFC4. We have outlined some common deviations below.

| IFC Class | Predefined Type | Notes |
| --- | --- | --- |
| IfcCovering | * MOLDING  
- SKIRTINGBOARD  
- INSULATION  
- WRAPPING  
- COPING |  |
## Resources
- Bill East, the original author of COBie, has some good [Cobie related articles on LinkedIn](https://www.linkedin.com/in/williameast/detail/recent-activity/posts/)
