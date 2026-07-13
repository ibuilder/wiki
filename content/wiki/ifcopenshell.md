---
title: "IfcOpenShell"
url: "/ifcopenshell/"
aliases: ["/IfcOpenShell/"]
categories: ["BIM Collaboration Format (BCF)", "IfcOpenShell", "Industry Foundation Classes (IFC)", "Software"]
lastmod: "2025-08-03T23:04:20Z"
---

<aside class="software-infobox">
<img src="/media/ifcopenshell-logo.png" alt="">
<dl>
<dt>Website</dt><dd>http://www.ifcopenshell.org/</dd>
<dt>Source</dt><dd><a href="https://github.com/IfcOpenShell/IfcOpenShell">github</a></dd>
<dt>License</dt><dd><a href="https://github.com/IfcOpenShell/IfcOpenShell">LGPL-3.0 &amp; GPL-3.0</a></dd>
<dt>Issues</dt><dd><a href="https://github.com/IfcOpenShell/IfcOpenShell/issues">Report a bug</a></dd>
<dt>Community</dt><dd><a href="https://sourceforge.net/p/ifcopenshell/discussion/">Forum</a></dd>
<dt>Maturity</dt><dd>Mature</dd>
<dt>Support</dt><dd><a href="https://opencollective.com/opensourcebim">OpenSourceBIM</a></dd>
</dl>
</aside>


[IfcOpenShell](/ifcopenshell/) is an open source (LGPL 3) software library that helps developers work with the [industry foundation classes](http://www.buildingsmart-tech.org/specifications/ifc-overview)  (IFC) file format. The IFC file format can be used to describe building and construction data. The format is commonly used for [building information modelling](https://en.wikipedia.org/wiki/Building_information_modeling) (BIM), for example, mechanical loading analysis, and thermal and energy efficiency studies.

IfcOpenShell is primarily a collection of C++ libraries, however, as it has [Python](/Python/) bindings, it can be integrated with programs like [FreeCAD](/freecad/) and [Blender](/blender/). It has support for Windows, Mac, and Linux. IfcOpenShell can be used as C++ developer libraries, through Python modules, via a number of Unix-style command line applications, or via graphical interfaces. The core libraries have support for IFC2X3, IFC4, IFC4.3, as well as custom IFC schemas defined by the user. Supported serialisations include IFC-SPF, IFC-JSON, IFC-XML, and IFC-HDF5.

IfcOpenShell supports geometry processing using the [Open CASCADE](/open-cascade/) geometry kernel. IFC geometry may be uniformly triangulated regardless of their original definition.

IfcOpenShell is also unique in its extensive Python API, which includes hundreds of functions for common IFC manipulation operations. This API supports many aspects of IFC not usually supported in other tools, including cascading geometric coordinate changes, subgraph purging, appending elements, and extensive support for 4D and 5D BIM operations like cost formulas, critical path analysis, and calendar-based scheduling propagation. It is also unique in its support for HDF5 caching, voxel analysis for dealing with less than precise BIM geometry, and semantic SVG-based drawing generation.

## Tools
In addition to a developer library, IfcOpenshell can be used through multiple command line tools which can be used independently or together :
## [bcf-python](https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.6.0/src/bcf)
A simple Python implementation of [BIM Collaboration Format (BCF)](/bcf-bim-collaboration-format/). The data model is described in data.py. Manipulation of BCF-XML is available via bcfxml.py and manipulation of BCF-API is available via bcfapi.py. See also [BIM Collaboration Format (BCF)](/categories/bim-collaboration-format-bcf/). 

## [IfcConvert](http://ifcopenshell.org/ifcconvert)
A command line tool to convert IFC to different format including :
| .obj | WaveFront OBJ | (a .mtl file is also created) |
| --- | --- | --- |
| .dae | Collada | Digital Assets Exchange |
| .glb | glTF | Binary glTF v2.0 |
| .stp | STEP | Standard for the Exchange of Product Data |
| .igs | IGES | Initial Graphics Exchange Specification |
| .xml | XML | Property definitions and decomposition tree |
| .svg | SVG | Scalable Vector Graphics (2D floor plan) |
| .ifc | IFC-SPF | Industry Foundation Classes |
You can pass multiple options. Type <code>IfcConvert --help</code> to learn more (considering it is installed on your system).

## [IfcGeomServer](https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.6.0/src/ifcgeomserver)
A command-line tool which allow to process geometry in a crash safe manner using a child process with dynamic linking.

## [IfcOpenShell-python](http://ifcopenshell.org/python)
A python API to manipulate IFC. See [IfcOpenShell code examples](/ifcopenshell-code-examples/). Comes with many utility functions for geolocation, data extraction, IFC query filtering, and more.

## IFC Clash
IFC Clash detection using the flexible collision library.

## IFC2CA
Conversion of IFC files into input files for Code_Aster structural simulation software.

## IFC COBie
Conversion of IFC-SPF data into SpreadsheetML format for the COBie MVD. Includes error logging of invalid data and support for open format alternatives like CSV and ODS.
See also: [Bonsai and COBie](/bonsai-and-cobie/)

## IFC CSV
Import and export support of IFC data to and from CSV files using a custom IFC query language.
See also: [Bonsai IFCCSV](/bonsai-ifccsv/)

## IFC Diff
Compares two IFC files with settings to check geometry or particular data relationships. Produces a parseable diff in JSON.

## IFC Patch
Provides a standard interface for users to easily apply predetermined "recipes" to manipulate IFC data without needing to have any technical knowledge. See forum topic for a example how to run it. https://community.osarch.org/discussion/10/ifcpatch-tool-now-available#latest

## IFC Sverchok
Provides an extension to the Blender Sverchok add-on for visual programming nodes for IFC within the Blender environment.

## BIMTester
Provides a way to specify BIM exchange requirements using natural human language and audit IFC files to check if they comply with the requirements.

## [IfcBlender](http://ifcopenshell.org/ifcblender)
Replaced by [Bonsai](/bonsai/).

## [IfcMax](http://ifcopenshell.org/ifcmax)
This plugin seems to not be developed anymore. It was an Ifc importer for 3ds Max.

## Softwares powered by ifcopenshell
The following lists of projects, academia, and industry organisations is incomplete. People who use IfcOpenShell are not required to advertise that they do so and IfcOpenShell is a community effort that does not collect or have a list of customers like private companies.

## FOSS projects
- [BIMxBEM](/bimxbem/) : import IfcRelSpaceBoundary, IfcSpace and related building elements geometry and data
- [Bonsai](/bonsai/) : ifcopenshell-python - import/export, multi-core geometry processing and more (Winner of 2020 buildingSMART Awards in Technology)
- [FreeCAD](/freecad/) : ifcopenshell-python - import/export Parametric 3D modeler allowing you to easily modify your design. 
- [georeference-ifc](https://github.com/stijngoedertier/georeference-ifc) Add geoferencing to IFC models
- [ifc-pipeline](/ifc-pipeline/) : IfcConvert / ifcopenshell - python
- [IFC Toolbox](https://youshengcode.github.io/IfcToolbox.Doc/#/) No-code IFC editing uses IfcOpenShell for model conversions.
- [IFCGref](https://github.com/tudelft3d/ifcgref/) Visualisation of georeferenced models
- [IfcLCA](https://github.com/IfcLCA/IfcLCA) Lifecycle analysis from IFC data
- [IFC Suite](https://ifcsuite.inex.fr/) Online simple IFC editing
- [BIMServer](https://github.com/opensourceBIM/BIMserver) enables you to store and manage the information of a construction (or other building related) project. 
- BIMSurfer
- [OpenProject](https://www.openproject.org/) An open source commercial CDE that uses IfcOpenShell for model processing.
- [opensource.construction Model Checker](https://modelcheck.opensource.construction/) A set of standardised tests to check model quality including IDS.
- [Speckle](https://modelcheck.opensource.construction/) a platform for model collaboration across any tool
- [xeokit-sdk](https://xeokit.io/) An open source 3D graphics SDK from xeolabs for BIM and AEC. Built to view huge models in the browser. Used by industry leaders.

## Proprietary projects
- [Areo](http://areo.io/) SMART Facilities Management
- [Augin.app](https://augin.app/en/) Publish and view AEC content in augmented reality in the environment on a 1:1 scale.
- [BIMData.io](https://bimdata.io/) Provides an integrated viewer capable of loading several tens of thousands of objects. 
- [Bimforce](https://bimforce.com/en/homepage/) for IFC drawing generation
- [Cove.Tool](https://www.cove.tools/) to integrate into Blender for sustainability analysis
- [KeyFrame](https://scai.group/) to help process IFC models for their viewer
- [Modulize](https://modulize.io/) - Uses IfcOpenShell "quite a lot"
- [Regola](https://regola.io/) - Used for model checking
- [RengaSoftware](https://rengabim.com/) - used in [various operations](https://github.com/IfcOpenShell/IfcOpenShell/issues/1028#issuecomment-776085665) internally
- [Spectar](https://www.spectar.io/) - Used for IFC conversions
- [StreamBIM](https://streambim.com/) (previously known as Rendra.io) (Winner of 2020 buildingSMART Awards in Construction via Project Celsius)
- [Tridify](https://tridify.com/) (Epic Megagrants recipient) Stream large & complex BIMs from the Cloud. A BIM Communication Service for all stakeholders with communication to issue management software.
- [TriDyme](https://www.tridyme.com/) TriDyme helps construction's companies to develop their own cloud-based (online) applications.
- [Wittym](https://wittym.com/) Wittym centralises digital twin data and simply connects experts with non-experts on a web platform. IfcOpenShell is used in the web platform to organize IFC in databases.
- [IfcPropertyRenamer](https://github.com/louistrue/PythonForIFC/tree/main/IfcPropertyRenamer) A GUI to bulk rename properties
- [IFC Werkzeug](https://ifcdev.baseapps.net/viewer) A web app to view and edit data about IFCs
- [Sortdesk IFC Viewer](https://viewer.sortdesk.com?utm_source=OSArch&utm_medium=listing&utm_campaign=product_promotion&utm_content=ifcopenshell_page) Used to view IFC files and validate them against IDS specs (using <code>ifctester</code>)

## Academia
IfcOpenShell is also used in university courses around the world.

- École Polytechnique Fédérale de Lausanne (EPFL Switzerland)
- Fachhochschule Nordwestschweiz FHNW (University of Applied Sciences and Arts Northwestern Switzerland)
- Federal University of Viçosa in Brazil
- MSc-education of Architecture, Civil Engineering and Construction & Robotics tracks at RWTH Aachen University in Germany
- Technical University of Denmark
- TU Eindhoven in the Netherlands
- Parametric Design with Visual Programming in BIM by the Online Zigurat Global Institute for Technology
- [BIMfag](https://bimfag.no/) Courses for BIM technicians in Norway
- Tallinn University of Technology in Estonia
- [Masterclass Building Intelligence](https://ideamechelen.be/masterclass-building-intelligence) Thomas More Mechelen in Belgium
- Universität der Künste Berlin
- [University of Maribor](https://fgpa.um.si), Slovenia, Faculty of Civil Engineering, Transportation Engineering and Architecture
- University of South Australia

It has also been a primary contributor in a number of research papers.

- [IfcOpenShell results on Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=ifcopenshell&btnG=)
- [Bonsai results on Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=blenderbim&btnG=)

## Industry
IfcOpenShell is known to be used in various companies and organisations. Size is roughly based on employee numbers: tiny (1-10), small (<100), medium (<1000), large.

| Name | Country | Company Size | Sector |
| --- | --- | --- | --- |
| Acciona | Spain | Large | Development |
| AF Gruppen Norge AS | Norway | Large | Example |
| Ai.K Data Labs | India | Tiny | Example |
| BAUPUNKTNULL AG | Switzerland | ? | Example |
| BCCV | Morocco | Tiny | Example |
| bda2bim | France | Tiny | Example |
| bimdo | Switzerland | Tiny | Consultancy |
| Bouygues Construction | Australia | Large | Example |
| Brasfield & Gorrie | USA | Large | General Contractor |
| BUCC BV | Netherlands | Tiny | Engineering |
| Bylor | UK | Large | Construction |
| Euskal Trenbide Sarea | Spain | Medium | Operations |
| Freyssinet | Australia | Large | Engineering |
| Géo²Concept | France | Small | Engineering |
| Geosurv | Australia | Small | Engineering |
| John Holland | Australia | Large | Construction |
| Ingenieursbureau 3BM | Netherlands | Example | Example |
| Kier Group | UK | Large | Construction |
| Laing O'Rourke | Australia | Large | Construction |
| LAB Entreprenør AS | Norway | Medium | Example |
| Lendlease | Australia | Large | Construction |
| Norconsult Norge AS | Norway | Large | Example |
| OpeningDesign | USA | Tiny | Design |
| Rambøll | Denmark | Large | Engineering |
| RB Rail AS | Rail Baltica | Estonia, Latvia and Lithuania | Medium | Operations |
| SBB | Switzerland | Large | Example |
| Société des Grands Projets | France | Medium | Example |
| Spectar | USA | Small | Example |
| Tietoa Finland Oy | Finland | Small | Example |
| TMR (Queensland Department of Transport and Main Roads) | Australia | Large | Operations |
| Transport for NSW | Australia | Large | Operations |
| WSP | Australia | Large | Engineering |
## Installation
IfcOpenShell may be packaged in different Linux repositories, ready to install and use; or it can be packaged together with some programs that use it, for example, [FreeCAD](/freecad/).

In other cases you may get one of the stand-alone, pre-compiled distributions, or you may download and compile the source code yourself.

To learn more about installing IfcOpenShell, visit the page in the FreeCAD wiki: [IfcOpenShell](https://wiki.freecadweb.org/IfcOpenShell).

## See also
- Visit the [IfcOpenShell Category](/categories/ifcopenshell/) on this website.

## External Resources
- Visit the IfcOpenShell Academy: http://academy.ifcopenshell.org/category/ifcopenshell/
- Visit the IfcOpenShell forum: https://sourceforge.net/p/ifcopenshell/discussion/
- learn with Jupyter Notebook coding examples from:
https://github.com/jakob-beetz/IfcOpenShellScriptingTutorial (by Jakob Beetz)

https://github.com/bimfag/intro-python-bim (by Sigve Martin Pettersen and Hans Martin Eikerol)

https://github.com/jakob-beetz/ifcopenshell-notebooks (by Jakob Beetz)

- Tutorial and code examples:

https://github.com/stefkeB/ifcopenshell_examples (by Stefan Boeykens)
