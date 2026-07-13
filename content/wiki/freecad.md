---
title: "FreeCAD"
url: "/freecad/"
aliases: ["/FreeCAD/"]
categories: ["FreeCAD"]
lastmod: "2023-11-05T14:53:15Z"
---

<aside class="software-infobox">
<img src="/media/icon-freecad.png" alt="">
<dl>
<dt>Website</dt><dd><a href="https://www.freecadweb.org">freecadweb.org</a></dd>
<dt>Source</dt><dd><a href="https://github.com/FreeCAD/FreeCAD">Github</a></dd>
<dt>License</dt><dd><a href="https://github.com/FreeCAD/FreeCAD/blob/master/LICENSE">LGPLv2-only</a></dd>
<dt>Issues</dt><dd><a href="https://tracker.freecadweb.org/my_view_page.php">report bugs</a></dd>
<dt>Community</dt><dd><a href="https://forum.freecadweb.org/">Forum</a> <a href="https://fosstodon.org/@FreeCAD">Mastodon</a> <a href="https://twitter.com/FreeCADNews">Twitter</a> <a href="https://discord.gg/NpMefpXWFT">Discord</a> <a href="https://blog.freecad.org/">FreeCAD News Blog</a></dd>
<dt>Maturity</dt><dd>Functional</dd>
<dt>Support</dt><dd><a href="/donation-directory/#freecad">donate</a></dd>
</dl>
</aside>

This is the front page of a series of pages about FreeCAD
## Subpages
{{< subpages >}}

## Introduction
FreeCAD is an open-source, extensible, parametric 2D and 3D modeler primarily designed for mechanical engineering but which can be used in many different fields like machining, CNC routing, 3D printing, static and thermal finite element analysis, and of course, architecture and construction. Parametric modeling allows you to modify your design by going back into your model history and changing its parameters.

FreeCAD uses the [Open CASCADE](/open-cascade/) modelling kernel for the creation of 2D and 3D shapes, and is divided into "workbenches" that provide tools for specific domains.
- Part and PartDesign Workbenches provide tools for the creation of generic 3D models.
- [Sketcher Workbench](https://wiki.freecadweb.org/Sketcher_Workbench) provides tools to create mathematically constrained 2D sketches that can be used for extrusion in Part and PartDesign.
- [Draft Workbench](https://wiki.freecadweb.org/Draft_Module) provides tools to create parametric 2D objects in a plane.
- [Arch Workbench](https://wiki.freecadweb.org/Arch_Module) builds on top of Draft, to create parametric 3D solids used in architecture, like walls, pillars, rebars, windows, doors, and roofs.
- [TechDraw Workbench](https://wiki.freecadweb.org/TechDraw_Module) provides tools to create 2D projections of arbitrary 3D bodies in order to create technical drawings and documentation that can be exported as [PDF](https://en.wikipedia.org/wiki/PDF).
- [Reinforcement workbench](https://wiki.freecadweb.org/Reinforcement_Workbench) is an external workbench that provides tools for Reinforcement Generation and Detailing. This workbench provides an interface and presets for the creation of common rebar types. 

The base program can be extended by [custom macros](/custom_macros/) and workbenches programmed in Python, which allows defining new parametric objects as well as more complex tools for working with the model.
- The [BIM Workbench](https://wiki.freecadweb.org/BIM_Workbench) builds on top of Draft and Arch, and provides even more tools for building modelling.
- The Reinforcement Workbench extends the rebar tools of the Arch workbench to create even more complex rebar patterns.

There are also tools for computational fluid dynamics based on [OpenFOAM](/openfoam/) [CfdOF](https://github.com/jaheyns/CfdOF) and a lees active fork [Cfd](https://github.com/qingfengxia/Cfd).

There is also development of integration with nodes for visual programming with [Sverchok](/sverchok/), [Dynamo](https://dynamobim.org/) (using [DynFreeCAD](/dynfreecad/)) and [PyFlow](/pyflow/).

The FreeCAD project is under constant development, and it has a community of users and developers who discuss and help each other in the [FreeCAD forum](https://forum.freecadweb.org).

## See also
- [Featured projects](/freecad-architecture-3d-models-created-in-freecad/)
- [Bonsai](/bonsai/)
- [Sweet Home 3d](/sweet-home-3d/)
- [Regard3D+Blender+FreeCAD workflow](/regard3d-blender-freecad-workflow/)
- The [OSArch Discussion forum](https://community.osarch.org) has lots of [discussions about FreeCAD](https://community.osarch.org/search?Search=freecad). You can improve this wiki by turning some of them into pages in this series.

## External resources
- [FreeCAD Blog](https://blog.freecad.org/)
- [Youtube BIM Workbench tutorial playlist](https://www.youtube.com/playlist?list=PLcr32YYn5HL11neg4Mxxm35ZNkZnyITZw) in Portuguese (turn on subtitles) by HR Compacta ([more playlists](https://www.youtube.com/c/HRCompacta/playlists)). It's possible also to buy more advanced video courses.
- [Youtube BIM Workbench tutorial](https://www.youtube.com/watch?v=rkWOFQ2fGZQ&list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU) by [Yorik Van Havre](/yorik-van-havre/)
- [FreeCAD BIM development news](https://yorik.uncreated.net/blog/freecad) is a blog by [Yorik Van Havre](/yorik-van-havre/), one of the main developers of FreeCAD and author of the Draft, Arch, and BIM workbenches, detailing the progress of the BIM tools in FreeCAD
- [Youtube playlist: Blender & Freecad Arch Workflow](https://www.youtube.com/watch?v=xOIdc6nTMT4&list=PLDd21g-eSHwn41rhRP-hidQhErgXoXZQ1) (Blender 2.7 & FreeCAD 0.17)
- [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide) from 2020
- Main website: https://www.freecadweb.org
- Documentation wiki: https://wiki.freecadweb.org
- Community forum: https://forum.freecadweb.org
- The [BIM Workbench](https://wiki.freecadweb.org/BIM_Workbench)
- [Architectural modelling with FreeCAD](https://wiki.freecadweb.org/Arch_Module) from the FreeCAD wiki
- About [OpenCasCade Technology](https://en.wikipedia.org/wiki/Open_Cascade_Technology)
- FreeCAD user Thomas-Neemann has a [YouTube channel](https://www.youtube.com/channel/UCVcztV5hHKE8J03GgKekj_g/videos) showing FreeCAD for [point clouds](https://www.youtube.com/watch?v=3uJ5vhYb6gU), [steel](https://www.youtube.com/watch?v=kHZx5WwquvA) & [wood frame](https://www.youtube.com/watch?v=i1hPNeygr3k) buildings
- [Architecture designs, concepts and demonstrations](https://forum.freecad.org/viewtopic.php?f=36&t=61546&sid=4b9fba49ebbed683f0cb1464d2884b7a) is the Thomas-Neemann's thread in FreeCAD official forum with videos and demonstrations of FreeCAD being used for Architecture projects.
