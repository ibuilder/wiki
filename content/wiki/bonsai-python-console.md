---
title: "Using the Python console with Bonsai"
url: "/bonsai-python-console/"
aliases: ["/BlenderBIM_Add-on/Using_the_Python_console_with_BlenderBIM_Add-on/", "/Using_the_Python_console_with_BlenderBIM_Add-on/", "/blenderbim-add-on-using-the-python-console-with-blenderbim-add-on/", "/bonsai-using-the-python-console-with-bonsai/"]
categories: ["Blender", "Bonsai"]
lastmod: "2024-10-29T09:49:04Z"
---

Bonsai comes with my useful Python libraries to interrogate BIM data, in addition to the math and geometry libraries that Blender comes with. A short list of these additional libraries is provided:

- **ifcopenshell** - used for querying, writing, and manipulating IFC data and files
- **bcfplugin** - used for querying, writing, and manipulating BCF data and files
- **fcl** - used for writing custom logic for clash detection
- **OCC** - used or directly accessing the [Open CASCADE](/open-cascade/) geometry kernel for low-level geometric analysis
- **svgwrite** - used for writing SVG for construction documentation
- **ifcdiff** - used for comparing IFC files for changes
- **ifccsv** - used for exporting and importing BIM data with CSV
- **ifcclash** - a frontend of FCL, allowing you to trigger clash sets for collision detection

{{< wiki-image src="/media/blender-python-console.png" alt="How to switch to Blender Python console mode" mode="thumb" caption="How to switch to Blender Python console mode" align="right" width="300" >}}

{{< wiki-image src="/media/blender-python-ifcopenshell.png" alt="Running IfcOpenShell commands in the Blender console" mode="thumb" caption="Running IfcOpenShell commands in the Blender console" align="right" width="300" >}}

You can launch an interactive Python shell letting you query BIM data in real-time. To do so:

1. [Install Bonsai](https://bonsaibim.org/download.html) and ensure it is enabled
1. Switch to the Blender Python console mode.
1. There is no step 3.

You can now type in <code>import ifcopenshell</code> and it'll work! Have fun!

{{< wiki-image src="/media/blender-text-editor.png" alt="How to switch to Blender's built in text editor" mode="thumb" caption="How to switch to Blender's built in text editor" align="right" width="300" >}}

Alternatively, you can write a full script from a text file and run it. Instead of switching to the Python console mode, just switch to the Blender text editor mode, and press the <code>Run Script</code> button in the top right once you've written or loaded a script. You can also press <code>Alt P</code> as a short cut, but your mouse cursor must be over your code when you press the hotkey.

The Blender text editor has basic line numbers, syntax highlighting, and line wrapping abilities. The output will be to the system console (not to mistake with Blender Python Console). On Mac and Windows, the console may not be visible. 
To make it visible on Windows, go click on <code>Window &gt; Toggle System Console</code>. 
On Mac you need to start Blender from terminal with <code>&quot;/Applications/Blender.app/Contents/MacOS/Blender&quot; -con</code> (path can be different depending on your Blender installation).

If you'd like to access the currently loaded or imported IFC file, there is no need to re-open the file with IfcOpenShell. Instead, you can access it as so:


```python
import bonsai.tool as tool
ifc = tool.Ifc.get()
```
