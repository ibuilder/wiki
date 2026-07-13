---
title: "Scalable Vector Graphics (SVG)"
url: "/scalable-vector-graphics-svg/"
aliases: ["/Scalable_Vector_Graphics_(SVG)/"]
categories: ["File formats"]
lastmod: "2022-06-03T19:11:49Z"
---

> **Stub:** This article needs expansion.


{{< wiki-image src="/media/svg-logo.png" alt="1200px-SVG logo.svg.png" mode="inline" width="64" >}}

SVG is an image format developed by the [World Wide Web Consortium (W3C)](https://da.wikipedia.org/wiki/World_Wide_Web_Consortium) for vector graphics. SVG uses an XML format and is easy to generate on the fly and edit in many programs. [Inkscape](/inkscape/) and [Krita](/krita/) are leading examples of vector graphics editors using the SVG format, but many other programs can export to SVG.

## Advantages and Disadvantages
Pros of SVG:
- Supported everywhere!
- Easy to read, easy to write, and a variety of data types to play with (paths, primitives, groups, defs...)
- Classes (like layers, but more flexible, which is both good and bad) with styles at run-time
- Can be turned interactive, with HTML, CSS, and Javascript (animation, hyperlinking, style combo changes, LOD zoom in/out, drag/drop - annoying tag obscuring your drawing? Just flick it away! Real-time updates from RSS or API - no more outdated drawings at site! Etc...)
- Can add properties and metadata relating it back to model space. And not just classes, but serious metadata - could include IFC-XML inside SVG using their "metadata" element.

Cons of SVG:
- CAD programs don't typically treat it as a CAD format. Modification is usually done in artsy programs like [Inkscape](/inkscape/) which aren't designed for drafting.
- Only one paper space. No absolute units. You can have embedded SVGs (which mean multiple SVGs), but everything has to be bound within a single document at the end of the day, there isn't a native concept of "pages".
- 2D only. Unless you include IFC-XML.

## See also
- [Getting started with 2D CAD drafting](/getting-started-with-2d-cad-drafting/)
- SVG is listed in the [AEC Open Data Standards Directory](/aec-open-data-standards-directory/)
- Discussion on documentation formats on the OSArch discussion forum [What is best for documentation when svg, dxf, dwg?](https://community.osarch.org/discussion/170/what-is-best-for-documentation-when-svg-dxf-dwg)

## External Resources
- [SVG article on Wikipedia](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics)
- [World Wide Web Consortium's page on the SVG format](https://www.w3.org/Graphics/SVG/)
- [Understanding SVG Coordinate Systems and Transformations](https://www.sarasoueidan.com/blog/svg-coordinate-systems/)
