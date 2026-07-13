---
title: "Start coding for Blender"
url: "/start-coding-for-blender/"
aliases: ["/Start_coding_for_Blender/"]
categories: ["Blender", "Bonsai"]
lastmod: "2021-10-16T09:08:11Z"
---

[Blender](/blender/) core is coded in C. Some part like Cycles are coded in C++. Python is widely used for extending Blender functionalities with scripts and addons.

(For Bonsai specific code see [Bonsai code examples](/bonsai-code-examples/))
## C/C++
Blender foundation made a video to present code structure :

[Dive Into The Code (peertube)](https://video.blender.org/videos/watch/1501943c-1f16-4c4c-ad72-19c2e299796d)

{{< youtube "https://youtu.be/tCdx7gzp0Ac" >}}
## python
## Introduction
Good introduction to python use in Blender from Curtis Holt :

{{< youtube "https://youtu.be/XqX5wh4YeRw" >}}


Useful resource on creating custom UI with Python in Blender:

https://blender.stackexchange.com/questions/57306/how-to-create-a-custom-ui


The Scripting for Artists tutorial series by Sybren Stuvel is another useful resource for learning to script with Python in Blender:

[Scripting for Artists](https://www.youtube.com/watch?v=opZy2OJp8co&list=PLa1F2ddGya_8acrgoQr1fTeIuQtkSd6BW)


Ditto the series by Darkfall:

[Tutorial Series by Darkfall](https://www.youtube.com/watch?v=cyt0O7saU4Q&list=PLFtLHTf5bnym_wk4DcYIMq1DkjqB7kDb-)


To learn more checkout the [Blender Python API documentation](https://docs.blender.org/api/current/index.html) especially Quickstart part.

## Creating custom add-ons
Creating a custom add-on is no magic. If you need help getting started, the [Create your first Blender add-on](/create-your-first-blender-add-on/) tutorial will help you.

## Tips and Tricks
### From Blender Python API doc
Blender Python API documentation has a special [Tips and Tricks](https://docs.blender.org/api/current/info_tips_and_tricks.html) chapter including external editor usage, inserting a python interpreter etc…

### bpy stubs for auto-completion
Main known project which provide stubs for auto-completion is [fake-bpy-module](https://github.com/nutti/fake-bpy-module). It also provide type hints for python >= 3.7 which should allow to perform type checking (eg. mypy).
