---
title: "BIMxBEM"
url: "/bimxbem/"
aliases: ["/BIMxBEM/"]
categories: ["Building Energy Modeling (BEM)", "Software"]
lastmod: "2022-08-04T16:13:45Z"
---

> **Stub:** This article needs expansion.

<aside class="software-infobox">
<img src="/media/icon-freecad.png" alt="">
<dl>
<dt>Website</dt><dd><a href="https://github.com/ENAC-CNPA/BIMxBEM">github.com/ENAC-CNPA/BIMxBEM</a></dd>
<dt>License</dt><dd>LGPL-3.0-only</dd>
<dt>Maturity</dt><dd>Unknown</dd>
</dl>
</aside>

A tool which analyzes [IFC](/ifc-industry-foundation-classes/) data to feed local standards compliant energy related data to [energy simulation](/building-energy-modeling-bem/) software.

BIMxBEM is a [FreeCAD](/freecad/) Workbench with the following feature:

- Read existing IfcRelSpaceBoundary2ndlevel produced by any authoring tool.
- Complete missing information (not filled by authoring tool or missing in older schema eg. 2x3).
- Adapt boundaries according local (Switzerland) standard for energy analysis.
- Translate gathered information in simpler xml format to be used by energy analysis software.
- Supported schema versions: 2x3, 4, 4.1
- Supported file formats: .ifc & .ifcXML


- Website: https://github.com/ENAC-CNPA/BIMxBEM
- License: LGPL-3.0-only
- Source: https://github.com/ENAC-CNPA/BIMxBEM
