---
title: "IFC Patch Recipes"
url: "/bonsai-ifc-patch-recipes/"
parent: "/bonsai/"
aliases: ["/BlenderBIM_Add-on/IFC_Patch_Recipes/", "/blenderbim-add-on-ifc-patch-recipes/"]
categories: []
lastmod: "2023-05-09T14:47:32Z"
---

Ifc Patch can be found in the Scene Properties Tab,
Under the IFC Quality Control Drop down menu

Code for IFC Patch Recipes in located [here](https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.7.0/src/ifcpatch/ifcpatch/recipes).

For Windows use <code>\</code>, for Mac and GNU/Linux use <code>/</code> in the path


## MergeProject
An example, for Windows:

{{< wiki-image src="/media/merge-project3.png" alt="MergeProject3.png" mode="inline" >}}

## OffsetObjectPlacements
The arguments for OffsetObjectPlacements are a list of numbers. If you specify 3 numbers [X,Y,Z], the coordinates will be offset by X, Y, Z. If you specify 4 numbers [X,Y,Z,Az], it will be offset by X, Y, Z and rotated along the Z axis by Az. If you specify 6 numbers [X,Y,Z,Ax,Ay,Az] it will translate along all three axes and also rotate along all three axes. [-source](https://community.osarch.org/discussion/comment/12408/#Comment_12408)

## RecycleNonRootedElements
Consolidates redundant non-rooted entities, like the following example, down to one entity.

<code>#45=IFCOWNERHISTORY(#9,#8,.READWRITE.,.MODIFIED.,1629040293,#9,#8,1629040293);</code>
<code>#52=IFCOWNERHISTORY(#9,#8,.READWRITE.,.MODIFIED.,1629040293,#9,#8,1629040293);</code>

{{< wiki-image src="/media/recycle-non-rooted-elements.png" alt="RecycleNonRootedElements.png" mode="inline" >}}
