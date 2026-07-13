---
title: "BCF - BIM Collaboration Format"
url: "/bcf-bim-collaboration-format/"
aliases: ["/BCF_-_BIM_Collaboration_Format/", "/BIM_Collaboration_Format_(BCF)/"]
categories: ["BIM Collaboration Format (BCF)", "buildingSMART International"]
lastmod: "2022-07-28T12:42:49Z"
---

> **Stub:** This article needs expansion.


{{< wiki-image src="/media/building-collaboration-format-icon.png" alt="Script \"Logo of the BIM Collaboration Format." mode="thumb" align="right" >}}

The BIM Collaboration Format (BCF) is a technology by [buildingSMART International](/buildingsmart-international/) to allow different BIM applications to communicate model-based issues with each other. Examples of issues may be model coordination problems, RFIs, or model clashes. As an open format, it allows many users to identify model problems in a variety of tools, bypassing proprietary formats and workflows. BCF specifies the metadata to be stored with each issue, as well as the rules on how the metadata may be edited and transferred. It is similar to a standardisation on how "bugtrackers" work in the software industry. The official terminology used for a model issue in BCF is called a "topic". A collection of BCF topics are stored in a BCF project.

BCF is may be used together with [Industry Foundation Classes (IFC)](/ifc-industry-foundation-classes/) models that have been previously shared among project collaborators. However, although BCF contains metadata to aid in linking to aspects of an IFC model, BCF may be used with any model, including proprietary ones. Each BCF topic may include camera viewpoints of the relevant model problem, to allow the user to investigate the issue. It is also possible to use BCF without any 3D model at all, simply sharing topics with only image snapshots.

The current stable version of BCF is version 2.1. A future version 3 is currently being drafted.

The official BCF standard is hosted on these pages:

- [BIM Collaboration Format (BCF) homepage](https://www.buildingsmart.org/standards/bsi-standards/bim-collaboration-format-bcf/)
- [BCF-XML specification for developers](https://github.com/BuildingSMART/BCF-XML)
- [BCF-API specification for developers](https://github.com/BuildingSMART/BCF-API)

BCF information may be transferred to other users in two ways. The BCF-XML specification allows users to transfer files with the <code>.bcf</code> extension to import and export a BCF project from different software. The BCF-API specification instead allows users software to connect directly to a BCF server to retrieve and update data in the BCF project.

## Implementations
Free Software with support for BIM Collaboration Format includes [Bcfier](/bcfier/), [OpenProject](/openproject/), [BIMData](/BIMData/), [Bonsai](/bonsai/) and the [BCF-Plugin-FreeCAD](/freecad-bcf-plugin-freecad/) to [FreeCAD](/freecad/). For developers, [IfcOpenShell](/ifcopenshell/) contains [bcf-python](/ifcopenshell/#bcf-python), intended to supersede [bcfplugin](/bcfplugin/), which was originally a fork of the FreeCAD BCF implementation with FreeCAD's GUI code removed. There is also a variety of commercial products with multi user server integration, some of them with free limited versions.

## BCF Specification
The BCF specification is relatively straightforward. A brief summary is provided here. The top level data container is known as the BCF project, with a UUID and a project name attribute.

The BCF project contains zero or more topics. Each topic represents a model issue. A topic will have a UUID, a title, description, priority, stage, labels (similar to tags), creation date / author, due date, and assigned to. If modified, it may contain the modification date and author.

A topic may also contain viewpoints, comments, related files, related links, and a "BIM snippet". Viewpoints store camera angles and visibility settings of element, including 3D annotations in the view. Comments represent a flat sequence of comments by different authors. Related files are similar to the concept of a file attachment, but usually refer to which 3D models are relevant to the topic. A "BIM snippet" is intended to hold a small excerpt of arbitrary data, such as a JSON file. No specification is made on how to interpret this data.

## BCF-XML
The BCF-XML specification describes how to transfer BCF project data by storing it in a file with the extension <code>.bcf</code>. This file is a zipped folder containing XML files and other related or attached files, like screenshot images.

## BCF-API
The BCF-API specification describes how to transfer BCF project data by making REST HTTP calls to a central server. The BCF-API specification only describes client behaviour, and does not describe how the server implementation works. However, it does cover user authorisation.

## Software Libraries
- The [xBIM Tookit (eXtensible Building Information Modelling)](https://github.com/xBimTeam/XbimBCF) is a CDDL licensed library (standalone) for Serializing/Deserializing BCF files 

## See also
- OSArch forum discussion: [Adding the ability to the BCF Libraries to connect with the API](https://community.osarch.org/discussion/485/adding-the-ability-to-the-bcf-libraries-to-connect-with-the-api)
- [BIM Collaboration Format (BCF)](/categories/bim-collaboration-format-bcf/)

## External Resources
- [BIM Collaboration Format](https://en.wikipedia.org/wiki/BIM_Collaboration_Format) on Wikipedia
