---
title: "Prj"
url: "/prj/"
aliases: ["/Prj/"]
categories: ["Blender", "Blender Add-on"]
lastmod: "2022-08-16T10:10:43Z"
---

<aside class="software-infobox">
<img src="/media/grey1x4.png" alt="">
<dl>
<dt>Website</dt><dd><a href="https://gitlab.com/marzof/prj">gitlab.com/marzof/prj</a></dd>
<dt>Source</dt><dd><a href="https://gitlab.com/marzof/prj">Repo on gitlab</a></dd>
<dt>License</dt><dd><a href="https://gitlab.com/marzof/prj/-/blob/main/LICENSE">GNU GPLv2</a></dd>
<dt>Issues</dt><dd><a href="https://gitlab.com/marzof/prj/-/issues">Issue page on gitlab</a></dd>
<dt>Community</dt><dd>&quot;&quot;</dd>
<dt>Maturity</dt><dd>Promising</dd>
<dt>Support</dt><dd>&quot;&quot;</dd>
</dl>
</aside>


*prj* is a [Blender_Add-on](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html) for generating semantic technical drawings from 3d model. Its main purpose is to help architects and designer to make building and interior drawings automatically. *prj* generates linked data-rich SVG drawings.
It has particular strengths:

- Drawings are in the open file format [Scalable Vector Graphics (SVG)](/scalable-vector-graphics-svg/). SVG is a non-binary and non-proprietary format that can be viewed by a simple browser on any device. Interactivity can be implemented in SVG files and their styles can be handled by [web standard CSS](https://en.wikipedia.org/wiki/CSS). Editing is easy and graphically powerful using free software like [Inkscape](/inkscape/) and [Krita](/krita/).

- Drawings are linked. Every 3D object is represented in a single dedicated SVG file and all those files are linked (as <use> element) to the main drawing. That allows to keep files size small and to limit redrawing to changed objects only.

- Drawings are data-rich. Every object stores information about it directly inside the SVG. Hence text searches are possible over single and multiple drawings.

*prj* is also able to produce drawings in the less free [DXF](/drawing-exchange-format-dxf/) or [DWG](/drawing-dwg/) file formats.

*prj* uses [Blender Line Art](https://docs.blender.org/manual/en/latest/scene_layout/object/properties/line_art.html) feature and SVG grease pencil exporter.

## Why use prj?
*prj* isn't trying to be a simple drawing tool. Its main aim is to be a tool to manage projects information by generating data-rich drawings (a kind of BIM drawing tool).

This is why it generates drawings in SVG format with a linked structure: this way every object in the drawing can return informations about it (product id, size, weight, physical properties, cost, typology, family belonging, etc…) and allow user to get, for example, bill of quantities or interactive drawing you can query.

For these reasons it's recommended to complete the drawing process (composing, styling with css, adding annotations and dimensions) using an SVG editor (like the open source [Inkscape](/inkscape/)). There are plans for prj SVG exports to store many other types of data in the future (such as quantities).

### prj vs bonsai 2d drawing
Main difference between prj and Bonsai 2D_documentation:

- Bonsai focuses on creating 2D documentation based on an IFC project
- prj exports Blender objects regardless of being part of an ifc project

As of July 2022 have tested prj (v0.0.9d) exported svg files imported to [qcad professional](/qcad/) . This seems to work fine.

## See also
- [Inkscape](/inkscape/)
- [Blender](/blender/)
- [Krita](/krita/)
- - [Scalable Vector Graphics (SVG)](/scalable-vector-graphics-svg/)
- The [prj tag](https://community.osarch.org/discussions/tagged/prj) on the OSArch forum

## External Resources
- [*Getting started*](https://gitlab.com/marzof/prj#getting-started) guide
- [*Tips and tricks*](https://gitlab.com/marzof/prj/-/wikis/Tips-and-tricks)
