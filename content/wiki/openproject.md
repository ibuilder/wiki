---
title: "OpenProject"
url: "/openproject/"
aliases: ["/OpenProject/"]
categories: ["Autodesk Revit", "BIM Collaboration Format (BCF)", "Industry Foundation Classes (IFC)", "Revit extensions"]
lastmod: "2021-06-17T08:14:13Z"
---

<aside class="software-infobox">
<img src="/media/icon-open-project-64x64.png" alt="">
<dl>
<dt>Website</dt><dd><a href="https://www.openproject.org">openproject.org</a></dd>
<dt>Source</dt><dd><a href="https://github.com/opf/openproject">github</a></dd>
<dt>License</dt><dd><a href="https://github.com/opf/openproject/blob/dev/docs/COPYRIGHT.rdoc">GPL3</a></dd>
<dt>Issues</dt><dd><a href="https://docs.openproject.org/development/report-a-bug/">report bugs</a></dd>
<dt>Community</dt><dd><a href="https://community.openproject.org/projects/openproject/forums">Forum</a> <a href="https://twitter.com/openproject">Twitter</a> <a href="https://www.linkedin.com/company/openproject-gmbh/">LinkedIn</a></dd>
<dt>Maturity</dt><dd>?</dd>
</dl>
</aside>


OpenProject is the leading open source project management software. Support your project management process along the entire project life cycle: From project initiation to closure. Includes support for browser based IFC viewing and issue tracking using [BCF](/bim-collaboration-format/)<https://www.openproject.org/openproject-bim-10-5/>

With the [Community Edition](https://www.openproject.org/download-and-installation/) you can host OpenProject yourself on-premises for free. With the [hosted Cloud Edition](https://start.openproject.com/go/bim) you can try a 14 day trial period and play around with it.

## IFC
The [IFC](/ifc-industry-foundation-classes/) viewer is built with [xeokit](/xeokit/). This allows browsing and discussing IFC models for everyone with a browser and Internet connection.

The IFC files get converted to [xeokit](/xeokit/)'s file formats for fast browsing on the web.

## BCF
OpenProject supports [BIM Collaboration Format (BCF)](/bcf-bim-collaboration-format/) XML 2.1 import and export of static files. For multi user environments some endpoints for the REST based BCF-API are already available and are used from within the web front end. Implementing missing endpoints are on the near development roadmap.

## Revit Add-in (GPL-3.0)
The [OpenProject Revit Add-in](https://github.com/opf/openproject-revit-add-in) is currently under development. It is a fork of the [BCFier](https://github.com/teocomi/BCFier) code. It updates the support for BCF 2.1 and to latest Revit version. However, the goal is to facilitate almost real time collaboration. So the the Add-in loads OpenProject in a small web browser and is able to communicate with Revit underneath. This way users can enjoy all the features of OpenProject while still in the context of Revit. (If you are a Revit Add-in developer and looking for job, let us know)

## Resources
- [OpenProject on Github](https://github.com/opf/openproject)
- [Blog](https://www.openproject.org/blog/#bim)
