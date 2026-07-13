---
title: "Bonsai installation"
url: "/bonsai-installation/"
parent: "/bonsai/"
aliases: ["/BlenderBIM_Add-on/BlenderBIM_Add-on_installation/", "/BlenderBIM_Add-on_installation/", "/How_to_install_the_BlenderBIM_Add-on/", "/blenderbim-add-on-blenderbim-add-on-installation/"]
categories: ["Bonsai"]
lastmod: "2022-07-27T14:01:02Z"
---

[Bonsai](/bonsai/) is an extension to the popular free and open-source 3D authoring package [Blender](/blender/). Bonsai and Blender both work on **Linux**, **macOS**, and **Windows**.

## Installation
1. Install [Blender](https://www.blender.org/download/). If you don't have administrator rights on Windows, you can [download a portable ZIP](https://www.blender.org/download/Blender2.83/blender-2.83.0-windows64.zip/) instead.
1. Download [Bonsai](https://bonsaibim.org/download.html). You do not need to unzip the file you download.
1. Launch Blender, and access the <code>Edit -&gt; Preferences</code> window.
1. Select the <code>Add-ons</code> tab, and press <code>Install...</code> on the top right.
1. Navigate to Bonsai <code>.zip</code> file, and press <code>Install Add-on</code>.
1. You should now see <code>Import-Export: Bonsai</code> available in your add-ons list. Enable the add-on by pressing the checkbox beside it.

All done! If you check your <code>Scene properties</code> panel on the bottom right of the Blender interface, you will see a panel related to *Building Information Modeling*.

## Upgrading
Download the latest version of Bonsai from the website, and uninstall any current Bonsai before installing the latest version.

If you are upgrading to a new version of Blender, just install Bonsai as if it were a fresh installation.

## Uninstallation
Find Bonsai entry in the <code>Edit &gt; Preferences &gt; Add-ons</code> window, and press the <code>Remove</code> button.

{{< wiki-image src="/media/uninstall-bonsai.png" alt="Uninstall-bonsai.png" mode="inline" >}}

## Known issues
- Ubuntu Blender package 2.82.a+dfsg-1 for Ubuntu 20.04 seems to package Blender without <code>numpy</code>. You are required to install <code>numpy</code> separately.
- Clash detection relies on <code>fcl</code>, which is not currently available nor packaged for Mac. You are required to install it yourself. If you do, let us know, so we can share it with others.
- There is a conflict with LuxCoreRender 2.4 for Linux. As temporary workarround copy /home/xxx/.config/blender/2.8x/scripts/addons/BlendLuxCore/bin/libtbb.so.2 to /home/xxx/.config/blender/2.8x/scripts/addons/bonsai/libs/libtbb.so.2

## Using the bleeding-edge version
If you're a developer, or just really keen, it is possible to run the latest bleeding edge version of Bonsai without having to wait for an official release, since Bonsai is coded in Python and doesn't require any compilation. First, install the latest official release, and then download the latest source code. If you don't know how to use the "Git" system, you can [manually download the latest code](https://github.com/IfcOpenShell/IfcOpenShell/archive/v0.6.0.zip). If you know how to use Git, you can also stay up to date like so:

 $ git clone https://github.com/IfcOpenShell/IfcOpenShell.git
 $ cd IfcOpenShell
 $ git checkout v0.6.0

Current Bonsai source is located in the <code>src/bonsai/</code> directory. Follow the [official development installation guide](https://docs.bonsaibim.org/guides/development/installation.html) for a live development environment or packaged build. The location of the Blender extension folder depends on how Blender was installed.

 /path/to/blender/2.83/scripts/addons/

Otherwise, if you installed Blender using an installation package, the add-ons folder depends on which operating system you use. On Linux:

 ~/.config/blender/2.83/scripts/addons/

On Mac:

 /Users/{YOUR_USER}/Library/Application Support/Blender/2.83/

On Windows:

 C:\Users\{YOUR_USER}\AppData\Roaming\Blender Foundation\2.83\scripts\addons

Restart Blender for the changes to take effect. In Edit > Preferences > Add-ons you will see that the version number of Bonsai has changed to 0.0.999999, which represents an un-versioned Bonsai.

Although Bonsai itself is pure Python, it does have quite a few dependencies. These are installed in the <code>libs/</code> folder of Bonsai. On rare occasions, it is possible that one of these dependencies have been updated to a later version. In this case, simply replacing Bonsai files will not be sufficient, and you may experience and error in enabling the add-on or running particular features.

If you are a developer, you can watch for changes in the [Makefile](https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.6.0/src/ifcblenderexport/Makefile), and run the appropriate command to build your own add-on version depending on your platform:

 $ make dist PLATFORM=linux
 $ make dist PLATFORM=macos
 $ make dist PLATFORM=win

If you are not a developer, it is advised to wait for the next official release. Whenever a release comes out, it is advised to also uninstall Bonsai, and install the official release, before returning to the bleeding-edge version.
