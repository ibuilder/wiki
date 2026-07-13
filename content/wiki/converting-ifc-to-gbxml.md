---
title: "Converting IFC to gbXML"
url: "/converting-ifc-to-gbxml/"
aliases: ["/Converting_IFC_to_gbXML/"]
categories: []
lastmod: "2025-05-06T14:04:00Z"
---

//* Note to Editors: Just putting resources here to reference when eventually creating this page:*//

The [IFC to gbXML converter](https://github.com/brunopostle/IFC-to-gbXML-converter) tool (python scripts) supports IFC2x3 and IFC4 in SI units.

- [OSArch Forum post](https://community.osarch.org/discussion/comment/18046#Comment_18046) on IFC to gbXML conversion.

## [Converting IFC to gbXML/Required data in IFC file for Conversion](/converting-ifc-to-gbxml-required-data-in-ifc-file-for-conversion/)
- Each Site **should** have location attributes, ie. *RefLatitude*, *RefLongitude*, *RefElevation* and *SiteAddress*. *RefLatitude* **must** be correct.
- Each *Building* **should** have a *BuildingAddress*.
- *Spatial Elements* **must** be structured correctly, ie. a *Space* **must** be contained within a *Building Storey*, which **must** be contained within a *Building*, which **must** be contained within a *Site*.
- Each *Space* **should** have *Qto_SpaceBaseQuantities/NetFloorArea* and *Qto_SpaceBaseQuantities/NetVolume* quantities.
- Each *Space* **must** be bounded by *2nd Level Space Boundary* relationships.
- Each *Space Boundary* **must** have a *Related Building Element*, planar *Connection Geometry*, and an *Internal Or External Boundary* attribute.
- Each *Window* and *Door* (or its Type) **must** have a U-value property in *Pset_WindowCommon/ThermalTransmittance* or *Pset_DoorCommon/ThermalTransmittance*.
- Each *Window* and *Door* (or its Type) **should** have a transmittance property in *Pset_WindowCommon/GlazingAreaFraction* or *Pset_DoorCommon/GlazingAreaFraction*.
- Each *Building Element* (or its Type) with a solid construction **must** have a U-value property (eg. *Pset_WallCommon/ThermalTransmittance*) **or** be constructed from a *Material Layer Set* with full thermal properties.
- Each *Material Layer* in a *Material Layer Set* construction **must** have a *Thickness* attribute, and each *Material* in a *Material Layer* **must** have an R-value property in *Pset_MaterialEnergy/ThermalConductivityTemperatureDerivative*.
- For metric projects, units for U-Values **must** be W/m²·K, and R-values **must** be m²·K/W. For imperial projects (ie. where the LENGTHUNIT is feet or inches), U-value units **must** be Btu/h·ft²·F, and R-values **must** be h·ft²·F/Btu.

## See Also
- [OpenStudio](/openstudio/)
- [Building Energy Modeling (BEM)](/building-energy-modeling-bem/)
