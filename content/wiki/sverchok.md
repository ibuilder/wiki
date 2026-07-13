---
title: "Sverchok"
url: "/sverchok/"
aliases: ["/Sverchok/"]
categories: ["Blender Add-on", "Sverchok"]
lastmod: "2022-07-28T12:56:32Z"
---

> **Stub:** This article needs expansion.


<aside class="software-infobox">
<img src="/media/sverchok.png" alt="">
<dl>
<dt>Website</dt><dd><a href="https://nortikin.github.io/sverchok/">github</a></dd>
<dt>Source</dt><dd><a href="https://github.com/nortikin/sverchok/">github</a></dd>
<dt>License</dt><dd><a href="https://github.com/nortikin/sverchok/blob/master/LICENSE">GPLv3-only</a></dd>
<dt>Issues</dt><dd><a href="https://github.com/nortikin/sverchok/issues">issues</a></dd>
<dt>Community</dt><dd><a href="https://github.com/nortikin/sverchok/discussions">discussions</a> <a href="https://discord.gg/pjHHhjJz8Z">discord</a></dd>
<dt>Maturity</dt><dd>Mature</dd>
<dt>Support</dt><dd><a href="/donation-directory/#sverchok">donate</a></dd>
</dl>
</aside>


## Description
<div style="float: right; margin: 30px;">{{< youtube "https://www.youtube.com/watch?v=mHNeH8H2wZI" >}}</div>
Sverchok is a [Blender add-on](/categories/blender-add-on/). Sverchok is a parametric tool for architects and designers for [Blender](/blender/) and [FreeCAD](/freecad/). You can use it to program objects' model geometry without knowing any programming languages. Sverchok has been inspired by Grasshopper from [Rhino 3D](/rhinoceros-3d/) and it uses a similar node-based visual programming principle. Developers are working to bring these feature to free/libre software.

Sverchok has nodes that interact with other [free/libre software](/free-software/) projects:
- [Some nodes depend on FreeCAD libraries](http://nikitron.cc.ua/sverch/html/search.html?q=freecad&check_keywords=yes&area=default)
- [Some nodes depend on Ladybug Tools libraries](http://nikitron.cc.ua/sverch/html/nodes/ladybug/ladybug_index.html)

There is currently development on letting [Blender handle solids via Sverchok and FreeCAD](https://github.com/nortikin/sverchok/pull/3377).

## Wiki Tutorials
- [Blender Topo Mesh2Contours](/blender-topo-mesh2contours/) - Exporting dxf contours from Blender topo mesh
- [Blender Topo Mesh2XYZ](/blender-topo-mesh2xyz/) - Exporting csv with xyz values from Blender topo mesh for import into Revit or Archicad
- [Blender 2D dxf to ifc](/blender-2d-dxf-to-ifc/) - Generating ifc objects from labeled 2D drawing for collision checks

## External Tutorials
- Read the full [Sverchok documentation](http://nikitron.cc.ua/sverch/html/main.html) and start with the [introduction to Sverchok](http://nikitron.cc.ua/sverch/html/induction.html#)
- [Getting started with Sverchok for 3D modeling](https://www.blender3darchitect.com/modeling-for-architecture/getting-started-with-sverchok-for-3d-modeling/) with Blender 2.8 from blender3darchitect.com
- [Sverchok Nodes – Quick Start](https://blender-addons.org/sverchok-nodes-quick-start/) with Blender from blender-addons.org
- [Resources list on Sverchok github](https://github.com/nortikin/sverchok/wiki/Resources)
- [Code Plastic - Learning Sverchok](http://www.codeplastic.com/learning-sverchok-ebook/) Book for learning Sverchok -Parametric and computational design tool for Blender 2.79
- [Classical Grasshopper algorithms with Sverchok](https://www.victorcalixto.xyz/tutorials/sverchok/sverchok) great way to switch from Rhino/Grasshopper

## See also
- [Ladybug Tools](/ladybug-tools/) has similar programming nodes
- [FreeCAD](/freecad/) has begun working with Sverchok
- Sverchok is designed for [Blender](/blender/)
- Sverchok includes nodes for working with [Topologic](/topologic/)
- Sverchok includes re-implementations of [Ladybug Tools](/ladybug-tools/) nodes

{{< wiki-image src="/media/ladybug-nodes-for-ray-intersection-in-sverchok.png" alt="Ladybug nodes for Ray intersection in Sverchok.png" mode="inline" width="480" >}}
