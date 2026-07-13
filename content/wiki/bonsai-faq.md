---
title: "Bonsai FAQ"
url: "/bonsai-faq/"
parent: "/bonsai/"
aliases: ["/BlenderBIM_Add-on/BlenderBIM_Add-on_FAQ/", "/BlenderBIM_Add-on_FAQ/", "/blenderbim-add-on-blenderbim-add-on-faq/"]
categories: ["Bonsai", "Software"]
lastmod: "2024-04-16T14:27:11Z"
---

This page contains FAQ's mainly gathered and referred to [Forum](https://community.osarch.org/)
## Bonsai
### Version of Blender to use ?
Which version of Blender is safest to use with Bonsai?

a Latest stable Blender until otherwise stated on the downloads page

### No update after export ? [Forum Link](https://community.osarch.org/discussion/465/blenderbim-nothing-gets-updated-after-first-export)
*Bonsai 0.0.210221 / Blender 2.91.2 / macOS Big Sur 11.2.1*

When I create a random mesh and assign the IFC class, I can export it correctly to IFC.

However, everytime I start editing the mesh in Blender and repeat the export, the IFC file keeps the first geometry. 

Am I missing a step? Do you need to reassign class or remove and regenerate the representation first?

**a Currently manual regeneration**

by [Dion](https://community.osarch.org/profile/Moult)
Right now, you need to regenerate the representation. In the Mesh properties, there is a button called "Update Mesh Representation". For easy access, you can use the "Shift E" shortcut in the viewport and either mouse/keyboard shortcut to the "Update Mesh Representation" command.

In the master branch, there is now a mode to auto update every time you update it in Blender, so that you do not need to explicitly tell it to regenerate the representation.

The reason for this behaviour is:

1. There have been quite a lot of usecases where people want to edit the objects but not edit the IFC file, such as if they are prototyping or experimenting with an option, or simply tweaking the geometry for a particular specific purpose that should not be fed back into the IFC. This makes editing the IFC an explicit operation.
1. Users need to understand that Blender by default manipulates meshes out of the box. Sometimes, editing meshes in IFC is what you want. Sometimes not. Sometimes you want to maintain the parametric shape. Sometimes you want to convert parametric shapes into meshes, and sometimes the other way around. Making these conversions explicit is something that Bonsai is doing to ensure that the full capabilities of IFC are not lost on the user. In most BIM apps, users don't get a say in this, and things are translated mostly in a hardcoded, magic way. This is the opposite of how I believe Bonsai should work - users should have a choice between heuristic magic, and fine-grained custom manual control.

The UX is still far from polished - as you've discovered, it was not obvious to you as a user how these workflows occur. In fact, there are still no gizmos to edit parametric shapes visually in 3D, only via entering properties, which is quite poor UX. There is also currently no way to convert from mesh to parametric (the function exists, but no UX for it - so we will bring it back in the next release perhaps), although you can convert from parametric to mesh. There is also no UX to edit heavily nested parametric IFC geometry (e.g. nested CSG booleans with different type of solids). However, the code now supports all of these things at a fundamental programmatic level - so we can start moving away from the guts and into the UX.

Hope it helps describe the current state of the software. Things are changing fast, though

### How to validate IFC file for issues ?
{{< wiki-image src="/media/ifc-validation.png" alt="IFC Validation.png" mode="thumb" >}}

IFC file validation is available from *Quality and Coordination* tab -> *Debug* section (check the screenshot).

You can either open project in Bonsai or just select it only for debug.

After validation is finished (it can take some time on large projects) you'll be able to check the results in Blender System Console. 

On Windows and Unix it can be opened in Blender from *Window -> Toggle System Console*. 

On Mac to see the system console Blender should be started from the terminal with <code>-con</code> argument: 

<code>&quot;/Applications/Blender.app/Contents/MacOS/Blender&quot; -con</code>.

## IFC
## Handling Multi Part objects in IFC
Q: How do you handle ifc classification for multi part objects, for example, a desk made up of 5 parts would have an empty at the top level of the hierarchy named Desk. In ifc, this hierarchy is not preserved and the only way I've seen to get the entire desk to export as ifc is to classify each of the five components as an ifc desk, which is neither logical nor helpful. If my hierarchy named Desk and every collection instance linked to it can be exported either as one compound object each named Desk, or a multipart object with the hierarchy preserved and the top level of the hierarchy named Desk, that would be most helpful. This seems to me like a good candidate for the sort of automation python tends to be good at, which would be nice to have as part of the export process.

A: The correct technique is to use IFC aggregations. You can find the ability to create aggregations from the scene properties. It effectively creates a collection instance, and lets you retain the class hierarchy underneath it.

### Collection instances [Forum Link](https://community.osarch.org/discussion/345/random-blenderbim-questions-troubleshooting)
I've come to find collection instances to be really handy in organizing my work, so that for repetitive objects or groups of objects, I only need to edit the main object and the changes get propagated to all the instances. However collections instances don't show up when the file is exported to ifc. How can collection instances be made to appear in ifc exports without making the instances real, while also preserving object hierarchies?

**a Use Aggregates**

The correct technique is to use IFC aggregations. You can find the ability to create aggregations from the scene properties. It effectively creates a collection instance, and lets you retain the class hierarchy underneath it. [Dion](https://community.osarch.org/profile/Moult)

{{< wiki-image src="/media/at2-fixme.png" alt="At2 Fixme" mode="inline" >}}There is a page started on [IFC aggregates](/ifc-industry-foundation-classes-ifc-aggregates/), which needs improving.

## Must an IFC file contain Geometry ? [Forum Link](https://community.osarch.org/discussion/comment/5567#Comment_5567)
a No

More elaborate answers [here](https://community.osarch.org/discussion/comment/5567#Comment_5567), by [Dion](https://community.osarch.org/profile/Moult)

## Bonsai Search for class or property ?
- How Do I select all IfcDoor or IfcWindow etc?
- How Do I select all object with "Beton" in the object name?
    - How Do I select all object with "Beton" in the type?

a [From forum](https://community.osarch.org/discussion/comment/5761#Comment_5761) 

The search panel gives you what you're after.

{{< wiki-image src="/media/bonsai-search-class.png" alt="Search for an IFC class or property in Bonsai" mode="inline" >}}

To find those of the type "Beton", go to an object of a type you want to select, then in the object properties this button will select all of that type:

{{< wiki-image src="/media/bonsai-ifc-class-panel.png" alt="IFC class panel in Bonsai" mode="inline" >}}

 
## Mesh Optimization Tips to remember while working with Bonsai
{{< wiki-image src="/media/bonsai-mesh-statistics.jpg" alt="Mesh statistics in Bonsai" mode="thumb" align="right" >}}
{{< wiki-image src="/media/bonsai-optimised-mesh-statistics.jpg" alt="Optimised mesh statistics in Bonsai" mode="thumb" align="right" >}}

Paraphrased from [comment by Dion Moult](https://community.osarch.org/discussion/comment/5513/#Comment_5513) on the OSArch forum.

- Most geometry (used for BIM projects) are not detailed meshes, but simple parametric shapes. Detailed meshes are not optimised for BIM. Typically, you'd want to treat your BIM model the same way you'd deal with creating assets for game - keep the polycount low, and make it generated (i.e. parametric) in standardised scenarios (e.g. profiles). If you do want to include high poly geometric assets, such as for archviz, keep that as a separate file, and have BIM include the low poly proxy, and reference the high poly asset via an external file. The process for this referencing is not (yet) standardised, but there are a few approaches used in the past. To give an idea, a table would be 3000 polygons.

- Compare that to an object in a BIM model which had over 61,000 polygons. This in itself takes 17 seconds for IfcOpenShell to process, per object. This single mesh (which was not reused - thus leading to further inefficiency) was the primary cause for the "forever to import" issue. If you exclude it during import, using a blacklist filter query of .IfcFurniture[Name*="insert object name here"], then the file imports in just under 3 minutes. Not great, but at least it isn't forever.

- Having too many objects is a problem. 13,000 objects does not make sense for a small scale project. There are bookshelves, where a single row of books accounts for about 180 objects. This does not make sense - even in regular 3D modeling, you wouldn't have 180 objects for a single row of books. In BIM, you should model objects based on how they are installed on site. In this case, the books should not even be in the model, but if you wanted it to, then it should be merged into the bookshelf - an entire bookshelf with all of its books should be one object. Of the 13,000 objects, 9,888 are books (edit: there are more, actually). Fixing the 9,888 books on my computer drops the import time from the already improved 3 minutes, down to 70 seconds, to give an idea of the desired behaviour.

- No mesh reuse. If you use the same chair 24 times, you should use the same mesh. Instead, the meshes are all duplicated, not linked. So use linked duplicates instead.


{{< wiki-image src="/media/at2-tip.png" alt="At2 Tip.png" mode="thumb" align="left" >}} 
- A quick way to check quality of geometry is looking at Statistics. 
  Statistics are enabled from the 'Viewport Overlays menu'. 
  Stats will show in top left part of screen.

[Link to community post](https://community.osarch.org/discussion/607/blender-boolean-problem#latest)


 
## IFC Styles vs IFC Materials
[Explained in details on OSArch](https://community.osarch.org/discussion/comment/13744/#Comment_13744).

TLDR: Ifc Materials is what object is actually made of, Ifc Styles - what it looks like. Basically Ifc Styles is like Blender materials.


 
## Ifc Contexts
[Explained in details on OSArch](https://community.osarch.org/discussion/comment/15044/#Comment_15044)
