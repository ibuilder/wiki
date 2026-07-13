---
title: "Bonsai"
url: "/bonsai/"
aliases: ["/BlenderBIM_Add-on/", "/blenderbim-add-on/"]
categories: ["Blender", "Blender Add-on", "Bonsai"]
lastmod: "2025-05-06T13:41:30Z"
---

<aside class="software-infobox">
<img src="/media/bonsai-logo.png" alt="">
<dl>
<dt>Website</dt><dd><a href="https://bonsaibim.org/">bonsaibim.org</a></dd>
<dt>Source</dt><dd><a href="https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/bonsai">source</a></dd>
<dt>License</dt><dd><a href="https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.8.0/src/bonsai/COPYING">GPL-3.0-or-later</a></dd>
<dt>Issues</dt><dd><a href="https://github.com/IfcOpenShell/IfcOpenShell/issues">report bugs</a></dd>
<dt>Community</dt><dd><a href="https://bonsaibim.org/community.html">community</a></dd>
<dt>Maturity</dt><dd>Functional</dd>
<dt>Support</dt><dd><a href="/donation-directory/#bonsai">donate</a></dd>
</dl>
</aside>

## Description
Bonsai is an add-on to [Blender](/blender/) and part of our [Blender add-ons](/categories/blender-add-on/) directory. It provides functions related to [OpenBIM](/openbim/) reading, writing, and analysis through a user interface to IfcOpenShell.

Bonsai is alpha software, expect things to change and break. It is not ready for regular production work if you're not willing to expend a lot of pain and effort. Please read the [Bonsai Roadmap](/bonsai-roadmap/) to understand progress on the software.

You can find ways to offer financial support in the [Donation Directory](/donation-directory/).

## Subpages
{{< subpages >}}

## Features
- [Featured projects](/bonsai-featured-projects/)
- Import <code>.ifc</code>, <code>.ifczip</code>, and <code>.ifcxml</code> formats
- Export <code>.ifc</code>, <code>.ifczip</code>, and <code>.ifcjson</code> formats
- Checking IFC data against an [Information Delivery Manual](https://technical.buildingsmart.org/standards/information-delivery-manual/) with [MicroMVDs](/micromvds-for-exchange-requirements/)
- Provide an interface to manage IFC data, including:
    - Assigning IFC classes
    - Assigning attributes to IFC elements
    - Assigning properties and property sets to IFC elements
    - Assigning quantities and quantity sets to IFC elements
    - Calculating quantities of IFC geometry
- [Clash detection](/bonsai-clash-detection/)

## Benefits
Bonsai is your free, open source, NativeIFC AECO toolkit.
- “**Your**” because it belongs to you, the users. Bonsai is not owned by a company.
- “**Free**”, in two ways: you don’t have to pay, as in “free beer”, and free as in freedom/liberty. Bonsai will always be free because everybody is allowed to distribute Bonsai free of charge. Bonsai ensures your freedom by using a GNU license which provides the four freedoms:
    - The freedom to use our software for any purpose.
    - The freedom to learn how our software is built.
    - The freedom to change our software to suit your needs.
    - The freedom to share our software with others, so we can all work together easier. If ten people each share one improvement, then everyone in the industry gets ten improvements.
- “**Open source**” allows and encourages building communities around software projects. Users are in control of their tools.
- “**NativeIFC**” because it is not translating geometry to and from an internal schema. The native language of Bonsai is the IFC schema. Changes you make are changes to IFC data. 
- “**AECO**” indicates that Bonsai is designed to be used by architects, engineers, construction, and operations teams; everybody in our industry.
- “**Toolbox**” because it is a collection of specialised tools for users to solve their problems.

Bonsai will transform the industry in three ways: through academia, as part of an AECO workflow, and as a forerunner of new AECO tools.

### Academia
A few universities in Europe have already incorporated Bonsai into their curriculum and students are already starting to use Bonsai as part of their thesis work. 

As Bonsai becomes entrenched in academia, the new generation of AECO professionals will be familiar with IFC and with Bonsai. When these people join the workforce, they will use Bonsai to solve problems. Their supervisors will have no objection to this, because Bonsai doesn’t cost the company any money.

There are three benefits of Bonsai for academia: it is free, it makes it easier to teach IFC, and it is open source.

#### Free
Bonsai is free. With Bonsai on their computer, students don’t have to go to the university computer centre to work on a licensed copy of proprietary software.

#### Easier to teach IFC
Bonsai makes it easier to teach IFC. The structure and terminology used in Bonsai matches what is in the IFC specification. A professor can teach a lesson based on the IFC specification and then give a practical assignment on the same topic to be completed using Bonsai.

#### Open source
Bonsai is open source. An open source application makes research easier and makes Bonsai a suitable platform for a thesis. 

### Part of the AECO workflow
There are three benefits of having Bonsai as part of the AECO workflow: It is an alternative to paid software, it works together with paid software, and it improves quality.

#### Alternative to paid software
Bonsai can be an alternative to paid AECO software. The long-term objective of Bonsai project is to provide a free, open source alternative to paid software in the AECO workflow; an alternative that provides features equal to or better than what is available from paid software. It may take a few years to achieve this objective, but we are on track. 

Some users may choose to continue to use paid software, just as many choose to use Microsoft Office, rather than the free open source alternatives available. What is important is that users will have a choice. 

There is a rapidly growing number of utilities that are NativeIFC. These utilities, things like IFC checkers and IFC viewers, are useful tools, but they operate on the peripheral of AECO workflows. Bonsai is game-changing because it aims to provide a NativeIFC alternative to the core applications in AECO workflows.

#### Works together with paid software
Bonsai can work together with paid AECO software. You will rarely find an architect who uses both Revit and ArchiCAD on the same project; although sometimes the architect uses ArchiCAD and other members of the design team use Revit. 

There are a few large projects on which the architect uses both Revit and Bonsai. There are also a few large projects on which the architect uses both ArchiCAD and Bonsai. There are also a few small projects on which the architect uses Bonsai instead of Revit or ArchiCAD. 

Bonsai has many features to address user needs on large projects using Revit or ArchiCAD.
- Bonsai can be used to analyse and debug an IFC file created by Revit or ArchiCAD. You can export IFC data into your favourite spreadsheet, use spreadsheet tools to analyse the data, modify the data in the spreadsheet, and then update the IFC file with the corrected data from the spreadsheet.
- Bonsai includes a patch utility that allows you to apply recipes to fix commonly occurring problems in IFC files. For example, many BIM authoring software packages do not handle geolocation properly and this can be fixed using the patch utility.

#### Improves quality
Bonsai will improve the quality of all AECO software. With the availability of Bonsai as a free, open source option for the industry, software vendors will have to provide better value to justify their price tag. Over time, as Bonsai continuously improves, paid software will also have to continuously improve. The big winners are the AECO community because software improves quickly and they are no longer locked in and held hostage by vendor-controlled models. We don’t measure the success of Bonsai using market share; we measure success by the quality of tools available to the AECO industry and the impact this has on the built environment. 

### Forerunner of new AECO tools
Bonsai is the first of a new generation of applications based on NativeIFC for the AECO industry. Bonsai will be a forerunner of new applications in three ways: it inspires imitators, it is an enabling platform, and it is a new category of tools.

#### Inspire imitators
Bonsai will inspire imitators. Before Bonsai, the only NativeIFC applications were utilities and viewers. Nobody had attempted to create a comprehensive IFC authoring tool that was NativeIFC. In this sense, Bonsai is a trailblazer. Inspired by the example of Bonsai, software developers can say, “If Bonsai can create an authoring application based on NativeIFC, why can’t I?” 

Often, it is the companies who follow closely behind the trailblazer who make the biggest impact. For example, a computer user interface using a desktop, windows, and mouse was first developed at Xerox’s Palo Alto research centre, but it was Microsoft and Apple who brought them to the mainstream. 

Who knows, maybe some company will grab hold of the NativeIFC approach and build a suite of world-class applications that ends up dominating the market. That would be great. There will always be Bonsai as a free, open source alternative. 

Even though Bonsai is currently in its early stages, its potential has already been recognised. It won the buildingSMART 2020 technology award. It was given a MegaGrant by Epic Games. And in 2021, Google sponsored two people to work on it as part of their “Summer of Code” initiative.

#### Enabling platform
Bonsai can be an enabling platform for new AECO applications. Bonsai is much, much more than a new software application for the AECO industry. Bonsai is also an enabling platform for an entire ecosystem of new NativeIFC software applications. To explain this, we need to look under the hood.

{{< wiki-image src="/media/under-the-hood.png" alt="Under the hood" mode="thumb" caption="Under the hood" >}}

Everything starts with the user. The User Interface allows the user to interact with Bonsai. The user experience, display, menu items, and input fields, come from a combination of existing Blender features and the new additional features of Bonsai. 

Under the hood, there are dozens of world-class 3D computer graphics features provided by the developers of Blender combined with dozens of AECO features provided by the developers of Bonsai. Both the developers of Blender and the developers of Bonsai regularly add new features. Typically, each feature is written as a separate software module, also called an application program. Some of the functionality of Bonsai is available without using Blender. 

A user can write a script to access the features directly, without a Blender user interface. This can be useful when you want to automate a series of tasks. 

There are dozens of application programs. Sometimes, these application programs need to read or write data. Reading and writing of data are done through an application programming interface or API. The API allows each application program to interact with a software called IfcOpenShell. 

The user never interacts directly with IfcOpenShell, only application programs interact directly with IfcOpenShell. IfcOpenShell provides a simple way for application programs of Bonsai to read and write NativeIFC data. The developers of Bonsai don’t have to worry about the complexity of IFC. IfcOpenShell hides all this complexity from the developers. 

Bonsai is built on top of the IfcOpenShell platform. IfcOpenShell is free open source software that allows any developer, not just the developers of Bonsai, to easily read and write NativeIFC data. 

IfcOpenShell has been around for a decade and already works as an enabling platform for many types of utilities and other software applications. Some of these may be free, while others may be paid software, but all of them will work together seamlessly because they all use NativeIFC. 

FreeCAD and Bonsai are software applications using the IfcOpenShell platform. They are both free and open source. There are also many paid software applications using the IfcOpenShell platform. IfcOpenShell is not the only free open source platform available to work with NativeIFC. 

A developer may also choose to build their application on top of the xBIM platform or the IFC.js platform. Applications built on any of these platforms will work together seamlessly because they are all based on NativeIFC.

#### New category of tools
Bonsai can be a catalyst for a new category of software tools. There is some really cool stuff being added to Blender and Bonsai will be able to take advantage of this. For example, Blender is already being used for virtual reality and augmented reality. It will be easy to fully integrate this with Bonsai. 

There is an emerging need for digital tools, tailored to the AECO industry, that simplify communications, coordination, and collaboration between stakeholders, including clients and facility managers. Fortunately, buildingSMART anticipated this need and developed a BIM Collaboration Format, or BCF, for issue management. Tools using the BCF specification allow smart issue tracking and smart issue exchange between stakeholders. The BCF specification supports both a workflow using a file exchange and a workflow using an API in a client-server environment. Bonsai is one of the first applications to support the new BCF API, ready for others to build upon. Just as IFCopenshell, xBIM and IFC.js are platforms for new NativeIFC applications, the BCF API is a platform for new applications that focus on smart collaboration between AECO stakeholders.

### Conclusion
Bonsai provides many benefits to the AECO industry. Bonsai will transform the AECO industry.

## Learn More
Bonsai website has a tutorial to export your first model.

- [How to install Bonsai](https://docs.bonsaibim.org/quickstart/installation.html)
- [Bonsai beginners tutorial: my first BIM project](https://docs.bonsaibim.org/quickstart/introduction_to_bim.html)

You can then read these articles to learn to use the add-on in more detail.
- [Bonsai installation](/bonsai-installation/)
- [Bonsai setting up a BIM project](/bonsai-setting-up-a-bim-project/)
- [Bonsai importing geospatial data](/bonsai-importing-geospatial-data/)
- [Bonsai for building and exporting an IFC model](/bonsai-for-building-and-exporting-an-ifc-model/)
- [Bonsai adding information to IFC](/bonsai-adding-information-to-ifc/)
- [Bonsai exporting 2D documentation](/bonsai-exporting-2d-documentation/)
- [Adding labels linked to properties and quantities](/bonsai-adding-labels-linked-to-properties-and-quantities/)
- [A simple step-by-step example of a project with Bonsai](/a-simple-step-by-step-example-of-a-project-with-bonsai/)
- [Bonsai and COBie](/bonsai-and-cobie/)
- [Bonsai Costing](/bonsai-costing/)
- [5D Bonsai: a tool for quantity surveyors or cost engineers](https://community.osarch.org/discussion/160/5d-blenderbim-a-tool-for-quantity-surveyors-or-cost-engineers)

We are collecting tips, tricks and best practices for using Bonsai on this page:

- [Bonsai FAQ](/bonsai-faq/) — questions collected from the [community forum](https://community.osarch.org/)

## Advanced usage
- [Bonsai code examples](/bonsai-code-examples/)

## External Resources
- [Bonsai documentation](https://docs.bonsaibim.org/)
- [IFC Architect](https://www.youtube.com/channel/UCnl3Zvy78lNfGIYLBxAu5-g/videos) YouTube channel with many video tutorials about Bonsai (formerly called BlenderBIM).
- [Petru Conduraru](https://community.osarch.org/profile/condur) of the BIMVoice [Youtube Channel](https://www.youtube.com/channel/UCPKI_VFw_UHYwEB3WeP69Sw) and [Podcast](https://bimvoice.com/) has some introductory videos and a [playlist](https://www.youtube.com/c/BIMvoice/search) focusing on Bonsai.
- "[A Modular Toolkit for Developing openBIM Data Pipelines](https://vimeo.com/479924151)" presentation to [BuildingSMART International](/buildingsmart-international/), 20 minute video. The project won the 2020 Technology Award. The toolkit includes [Bonsai](/bonsai/) and its components IFC Diff, IFC Clash, BIM Tester, IFC Patch, IFC CSV, and IFC COBie.
- In [this](https://twitter.com/theoryshaw/status/1448024088631549955) Twitter thread [Ryan Schultz](https://community.osarch.org/profile/theoryshaw) from [OpeningDesign](http://openingdesign.com/) provides a series of quick, off-the-cuff Bonsai tutorials. They are centered around the development and evolution of The Stead: an open source modular/panelized home.
- Some examples of [generating 2D drawing directly from IFC](https://github.com/IfcOpenShell/IfcOpenShell/issues/1153)
- [IFC-101-course:](https://github.com/myoualid/ifc-101-course) A video-series on IFC and Bonsai
- [Search YouTube for Bonsai tutorials](https://www.youtube.com/results?search_query=bonsai+ifc)
- [Bonsai/Video Tutorials](/bonsai-video-tutorials/)
