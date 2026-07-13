---
title: "Speckle"
url: "/speckle/"
aliases: ["/Speckle/"]
categories: []
lastmod: "2022-10-17T18:36:36Z"
---

> **Stub:** This article needs expansion.

{{< wiki-image src="/media/icon-speckle-64.png" alt="Icon speckle 64.png" mode="inline" >}}

[Speckle](https://speckle.systems/)

Speckle is an open source[^1] cloud-based data platform for AEC. It provides a method of liberating data from one platform to another in a quick, manageable, and efficient way. It works with [Blender](/blender/), ThreeJS and [Dynamo](/dynamo/) as well as with proprietary solutions like [Revit](/autodesk-revit/)/Dynamo, GSA, Unreal, Rhino/Grasshopper and Excel. A project connecting speckle with [FreeCAD](/freecad/) has been [started](https://github.com/yorikvanhavre/WebTools/blob/master/Speckle.py).

Speckle allows you to transfer data and geometry through a network. It defines a common geometry language.

## Use case example
Architect which works in Rhino want to send his geometry to Civil Engineer which is working on Blender
1. Architect creates a stream and send it to a remote database (Speckle Server) using Rhino or Grasshopper Speckle plugin
1. Civil Engineer retrieves the stream from Speckle Server using Blender Speckle plugin
1. HVAC engineer which is stuck on Revit join. He connect to Speckle Server and retrieves the stream using Revit Speckle plugin.
Engineers are now happy to be able to work with a model from a software which currently do not have native export to IFC.

## Notes
- Notable features : 
    - You can transfer geometry and data with ease and in short time.
    - It works with common AEC softwares. Easy to communicate a model.
    - git (git like ?) model versioning.
- Known limitations :
    - Data-structure is not normalized. IFC schema could be used but this feature need to be developed.
    - You cannot work on same objects (eg. security engineer cannot fill in fire protection data in an architect's wall). Although merge feature might allow this in future.

## Testing Speckle
You can test Speckle on their server [Speckle Hestia](https://hestia.speckle.works). Follow [get started](https://speckle.systems/docs/essentials/start) instructions on their website.

## Definitions/parts
**speckle kit**

«it's basically a schema and its implementations to and from a given set of software apps».[^2]

Documentation is available in high level version[^3] and more technical one [^4]

**speckle-server[^5]**

This is the Speckle Server 2.0. It consists of two distinct parts:
- The server application itself, which is a nodejs app exposing a GraphQL API.
- The frontend application, which is a static vuejs app.

**PySpeckle[^6]**

A Python Speckle Client. It powers SpeckleBlender.

**SpeckleBlender[^7]**

Speckle add-on for Blender. License: MIT

## Resources
- Website: https://speckle.systems/
- Documentation: https://speckle.systems/docs/essentials/start
- Forum: https://discourse.speckle.works/

## References


[^1]: [https://speckle.systems/blog/opensource-aec-speckle ''Open Source in AEC & Speckle'']
[^2]: [https://community.osarch.org/discussion/comment/3845/#Comment_3845 OSArch discussion]
[^3]: [https://speckle.systems/blog/schemas-revisited/ Dimitrie Stefanescu, ''Schemas & Standards: The BYO Approach'', Speckle blog]
[^4]: [https://speckle.systems/docs/developers/object-models/ ''Schemas & Object Models (.NET)'', Speckle wiki documentation]
[^5]: [https://github.com/specklesystems/speckle-server speckle-server repository]
[^6]: [https://github.com/speckleworks/PySpeckle PySpeckle repository]
[^7]: [https://github.com/speckleworks/SpeckleBlender SpeckleBlender repository]
