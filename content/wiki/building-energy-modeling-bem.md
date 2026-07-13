---
title: "Building Energy Modeling (BEM)"
url: "/building-energy-modeling-bem/"
aliases: ["/Building_Energy_Modeling_(BEM)/", "/Energy_Modeling/"]
categories: ["Autodesk Revit", "Building Energy Modeling (BEM)"]
lastmod: "2022-11-16T14:21:10Z"
---

> **Stub:** This article needs expansion.

## Introduction
There is currently 2 BIM format related to energy modeling : [gbXML](https://www.gbxml.org/) and IFC ([using IfcRelSpaceBoundary2ndLevel](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_1/FINAL/HTML/link/ifcrelspaceboundary2ndlevel.htm))
Most energy analysis software reads gbXML. Some read IFC. Generating geometry for gbXML and IfcRelSpaceBoundary is quite similar. Information contained in both format is different. There are significant challenges (in 2022) with IFC and space boundaries, [BuildingSMART International](/buildingsmart-international/) is working to improve the situation by improving the Information Delivery Manual (IDM) for Building Energy Modelling (BEM). The current status (in 2022) can be seen in a video from bS Virtual Summit Spring 2021 in the presentation [BR5 - Jeffrey Ouellette - Building Energy Modelling (BEM)](https://vimeo.com/539127482).

See the [Building Energy Modeling (BEM)](/categories/building-energy-modeling-bem/) category for more general info and tools!

Note to editors: Add a gbXML vs IFC features comparison

## Energy modeling workflow (/!\Work in progress/!\)
## Modeling the building
Building need to be modeled with all data relevant to energy analysis :
- Building geometry : Walls, Slabs, Doors, Windows, Spaces etc…
- Energy data : Thermal transmittance, wall layers, thermal conductivity, solar transmittance, light transmittance etc…
Overmodelled building often lead to error and/or uselessly complex computation. A energy model should be simple and contain only energy relevant information.

## Bonsai
Bonsai allows you to create, modify an IFC targeting energy analysis. You can either:
- Rework an IFC coming from another authoring tool. This is probably the most efficient workflow currently. It allows you to enhance your model and fixes common known issues incoming from popular authoring software.
- Create a model from scratch. You might want to take a look at topologic and related projects for more automation.

## Energy specific geometry
An algorithm need to generate energy specific [space boundaries](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_1/FINAL/HTML/link/ifcrelspaceboundary2ndlevel.htm)
## Export to common energy exchange formats
Software need provide an Ifc or gbXML.

### Revit
#### Configuration
TODO
#### Known issues
> **Warning:** lastly tested with Revit 2021. revit-ifc 21.2.1
IFC 2x3 and 4 : 
- export boundaries at middle of the wall instead of interior face.
- roof boundaries are oversplitted if they host an element (eg. skylight / hole for lift top)
- type B boundaries are not exported
IFC4 :
- CorrespondingBoundary attribute is not filled
- ParentBoundary attribute is not filled

### ArchiCAD
#### Configuration
By default ArchiCAD use IFC4 reference view MVD which do not contain IfcMaterialLayerSet(Usage). So layered wall will not contain thickness of each layer. Use a custom IFC translator using parametric 

#### Known issues
> **Warning:** lastly tested with ArchiCAD 24
IFC 2x3 and 4 :
- window and door boundaries are not coplanar with their host
- There is no hole for window and door boundaries in their host
- type B boundaries are not exported
IFC4 :
- CorrespondingBoundary attribute is not filled
- ParentBoundary attribute is not filled

## Adaptation to local standards
Both IFC and gbXML are not directly usable for local standards as each country have it's own specification. [Add an exemple]

A tool for adjusting an .ifc file to local regulations is [BIMxBEM](/bimxbem/) which currently has a configuration to support Swiss standards for energy modeling. Contact the developer and you can start making a new localization.

## Scientific article or conference paper on energy modeling
| Full text  
available ? | publication  
year | Title | Short resume |
| --- | --- | --- | --- |
| Yes | 2020 | [IFC to Building Energy Performance Simulation: A systematic review of the main adopted tools and approaches](https://www.researchgate.net/publication/345983333_IFC_to_Building_Energy_Performance_Simulation_A_systematic_review_of_the_main_adopted_tools_and_approaches) |  |
| Yes | 2020 | [IFC-Based BIM-to-BEM Model Transformation](https://www.researchgate.net/publication/341025570_IFC-Based_BIM-to-BEM_Model_Transformation) |  |
| Yes | 2017 | [Automatic generation of second-level space boundary topology from IFCgeometry inputs](https://discovery.ucl.ac.uk/id/eprint/1546334/1/CBIP_revised.pdf) | Polyhedron algorithm |
| Yes | 2017 | [Template based code generation of Modelica building energy simulation models](https://www.researchgate.net/publication/318218730_Template_based_code_generation_of_Modelica_building_energy_simulation_models) | City to [Modelica](/Modelica/) |
| Yes | 2016 | [BIM based whole-building energy analysis towards an improved interoperability](https://www.ofcoursecme.nl/?mdocs-file=3201) | IFC to gbXML |
| Yes | 2016 | [BIM enabled building energy modelling: development and verification of a GBXML to IDF conversion method](https://repository.lboro.ac.uk/articles/BIM_enabled_building_energy_modelling_development_and_verification_of_a_GBXML_to_IDF_conversion_method/9437450) | gbXML to idf to design4energy |
| Yes | 2016 | [Model View Definition for Advanced Building Energy Performance Simulation](https://www.researchgate.net/publication/308614558_Model_View_Definition_for_Advanced_Building_Energy_Performance_Simulation) | Energy MVD |
| Yes | 2016 | [Research & Development Roadmap for BuildingEnergy Modeling](https://www.energy.gov/sites/prod/files/2016/02/f29/DOE-BTO-BEM-Roadmap-DRAFT-2-1-2016.pdf) |  |
| Yes | 2015 | [Service-Oriented Architecture For DataExchange Between A Building InformationModel And A Building Energy](https://www.researchgate.net/publication/279198228_Service-Oriented_Architecture_For_Data_Exchange_Between_A_Building_Information_Model_And_A_Building_Energy_Model) |  |
| Yes | 2015 | [Link between BIM and energy simulation](https://www.researchgate.net/publication/300634003_Link_between_BIM_and_energy_simulation) | IFC to Space Bondary Tool to IDF to energy+  
gbXML to IDF to energy+ |
| Yes | 2015 | [INTEROPERABILITY OF BUILDING ENERGY MODELING (BEM) WITH BUILDING INFORMATION MODELING (BIM)](https://www.researchgate.net/publication/282814185_INTEROPERABILITY_OF_BUILDING_ENERGY_MODELING_BEM_WITH_BUILDING_INFORMATION_MODELING_BIM) |  |
| Yes | 2014 | [Translating Building Information Modeling to Building EnergyModeling Using Model View Definition](https://www.researchgate.net/publication/266951250_Translating_Building_Information_Modeling_to_Building_Energy_Modeling_Using_Model_View_Definition) | [Revit](/autodesk-revit/) to [Modelica](/Modelica/) |
| Yes | 2013 | [Transforming BIM to BEM: Generation ofBuilding Geometry for the NASA AmesSustainability Base BIM](https://simulationresearch.lbl.gov/sites/all/files/lbnl-6033e.pdf) | Ifc to BEM using Space Boundary Tool |
| Yes | 2013 | [Interfacing BIM with Building Thermal and Daylighting Modeling](https://www.researchgate.net/publication/262009985_Interfacing_BIM_with_Building_Thermal_and_Daylighting_Modeling) | [Revit](/autodesk-revit/) to [Modelica](/Modelica/) |
| Yes | 2013 | [A Thermal Simulation Tool for Building and Its Interoperabilitythrough the Building Information Modeling (BIM) Platform](https://www.mdpi.com/2075-5309/3/2/380/pdf) | State on softwares in 2013 |
| Yes | 2011 | [ThermalOpt: A Methodology forAutomated BIM-BasedMultidisciplinary ThermalSimulation for Use in OptimizationEnvironments](https://www.researchgate.net/publication/257778673_ThermalOpt_A_methodology_for_automated_BIM-based_multidisciplinary_thermal_simulation_for_use_in_optimization_environments) | Ifc to thermal simulation |
| Yes | 2008 | [IFC BIM-Based Methodology for Semi-Automated Building EnergyPerformance Simulation](https://eetd.lbl.gov/sites/all/files/publications/919e.pdf) | Ifc to energy+ |
| No | 2015 | [A process to divide curved walls in IFC-BIM intosegmented straight walls for building energyanalysis](https://www.researchgate.net/publication/282533267_A_process_to_divide_curved_walls_in_IFC-BIM_into_segmented_straight_walls_for_building_energy_analysis) | Curved wall segmentation |
| No | 2017 | [Building Information Modelling for analysis of energy efficientindustrial buildings – A case study](https://www.sciencedirect.com/science/article/abs/pii/S1364032116002173) | [Revit](/autodesk-revit/) to gbXML to sketchup to idf to energy+ |
| No | 2013 | [An algorithm to generate space boundaries for building energysimulation](https://www.researchgate.net/publication/259633402_An_Algorithm_to_generate_space_boundaries_for_building_energy_simulation) | Graph algorithm |
| No | 2016 | [Automation of CAD models to BEM models for performance basedgoal-oriented design methods](https://www.sciencedirect.com/science/article/abs/pii/S0360132316304140) |  |
| No | 2016 | [A framework to integrate object-oriented physical modelling with building information modelling for building thermal simulation](https://www.researchgate.net/publication/271824420_A_framework_to_integrate_object-oriented_physical_modelling_with_building_information_modelling_for_building_thermal_simulation) |  |
| No | 2007 | [A comparative study of the IFC and gbXML informational infrastructures for data exchange in computational design support environments](https://www.researchgate.net/publication/285494452_A_comparative_study_of_the_IFC_and_gbXML_informational_infrastructures_for_data_exchange_in_computational_design_support_environments) | [Revit](/autodesk-revit/) to [Modelica](/Modelica/) |
| No | 2016 | [BIM IFC information mapping to building energy analysis (BEA) model with manually extended material information](https://www.researchgate.net/publication/303179536_BIM_IFC_information_mapping_to_building_energy_analysis_BEA_model_with_manually_extended_material_information) |  |
| Yes | 2019 | [A combined scientometric and conventional literature review to grasp the entire BIM knowledge and its integration with energy simulation](https://www.researchgate.net/publication/329954730_A_combined_scientometric_and_conventional_literature_review_to_grasp_the_entire_BIM_knowledge_and_its_integration_with_energy_simulation) |  |
| Yes | 2021 | [Automatic IFC data enrichment with space geometries for Building Energy Performance Simulations](https://www.conftool.pro/bs2021/index.php/30888_Lilis_Georgios_Nektarios.pdf?page=downloadPaper&filename=30888_Lilis_Georgios_Nektarios.pdf&form_id=30888) |  |
| Yes | 2021 | [Automatic generation of second level space boundary geometry from IFC models](https://www.conftool.pro/bs2021/index.php/30156_Fichter_Eric.pdf?page=downloadPaper&filename=30156_Fichter_Eric.pdf&form_id=30156) |  |
| Yes | 2019 | [A Workflow for Automated Building Energy Performance Model Generation Using BIM Data](https://www.researchgate.net/profile/Georgios-Lilis/publication/335676583_A_Workflow_for_Automated_Building_Energy_Performance_Model_Generation_Using_BIM_Data/links/5d73518d92851cacdb271141/A-Workflow-for-Automated-Building-Energy-Performance-Model-Generation-Using-BIM-Data.pdf) |  |
| Yes | 2019 | [An IFC data preparation workflow for building energy performance simulation](https://www.researchgate.net/profile/Georgios-Lilis/publication/334448038_An_IFC_data_preparation_workflow_for_building_energy_performance_simulation/links/5d2a0f84299bf1547cb48c6c/An-IFC-data-preparation-workflow-for-building-energy-performance-simulation.pdf) |  |
## See also
- There is a discussion tag on our forum for [Building Energy Modeling (BEM)](https://community.osarch.org/discussions/tagged/Building_Energy_Modeling_BEM)

## External Resources
- [Information Delivery Manual (IDM)Development for Building Information Modelling (BIM) and Building Energy Modelling (BEM) Workflows](https://app.box.com/s/1lo25g724749mbqjhgixy2nqdarq33uw)
- [Discussion topic on buildingSmart forum](https://forums.buildingsmart.org/t/about-the-bim-bem-idm-development-category/4172)
