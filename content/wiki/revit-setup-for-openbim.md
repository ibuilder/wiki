---
title: "Revit setup for OpenBIM"
url: "/revit-setup-for-openbim/"
aliases: ["/Revit_setup/", "/Revit_setup_for_OpenBIM/"]
categories: ["Autodesk Revit"]
lastmod: "2025-05-07T06:57:05Z"
---

> **Warning:** this page has not been audited for accuracy for Revit versions above 2018

## Subpages
{{< subpages >}}

[Autodesk Revit](/autodesk-revit/) does not come with strong official support for [Industry Foundation Classes (IFC)](/ifc-industry-foundation-classes/). This guidebook relies on [Revit](/autodesk-revit/) users using the [revit-ifc](https://github.com/Autodesk/revit-ifc) open-source Revit IFC plug-in. Although the plug-in comes bundled with Revit, the bundled version is usually outdated and contains bugs that prevent basic functionality from working (such as the ability to assign IFC type parameters using the official shared parameters file, [bug report](https://github.com/Autodesk/revit-ifc/issues/217)). It is therefore a requirement for productive output to update to the latest version using the download links below.

- [Download revit-ifc 2019](https://apps.autodesk.com/RVT/en/Detail/Index?id=1763588736399554049)
- [Download revit-ifc 2020](https://apps.autodesk.com/RVT/en/Detail/Index?id=8986482933300179260)
- [Download revit-ifc 2021](https://apps.autodesk.com/RVT/en/Detail/Index?id=7265544480016320144)
There can be a delay between a new version being ready and appearing on apps.autodesk.com, the executables are first published in the [revit-ifc github](https://github.com/Autodesk/revit-ifc/releases)

## Setting up IFC class mappings
Revit comes with a mappings file to map Revit family categories to IFC classes. OSArch has provided its own version of this file with the following improvements:

- Out of the box, Revit won't export grids to IFC. This fixes that, exporting grids appropriately to <code>IfcGrid</code>
- Instead of being excluded from export, <code>Structural Connections</code> are now exported as <code>IfcMechanicalFastener</code> or <code>IfcFastener</code> as relevant.
- <code>Topography</code> is exported as <code>IfcSite</code>, to allow for IFC2X3 geolocation to occur.
- Structural holes are exported as <code>IfcOpeningElement</code> instead of being omitted.
- Structural members are exported as <code>IfcMember</code> instead of <code>IfcBuildingElementProxy</code>, except for <code>Joist</code> objects, which are exported as <code>IfcBeam</code>.
- Wall sweep walls are exported as <code>IfcWall</code> instead of <code>IfcBuildingElementProxy</code>.

You can download it here:

- [Revit and IFC class mapping](https://raw.githubusercontent.com/Moult/revit-ifc/osarch/Install/Program%20Files%20to%20Install/exportlayers-ifc-osarch.txt)

It is important to ensure that class mapping are valid. Revit will not stop you from specifying invalid class mappings, such as mapping certain objects to be exported as <code>IfcSite</code> or <code>IfcGrid</code>. This will end up creating invalid IFC files which can cause problems in other software.

See also: [IFC classes](/ifc-industry-foundation-classes-ifc-classes/)

## Setting up shared parameters
Simply installing the plug-in does not guarantee the quality of IFC exports and imports. Many parameters need to be manually created and export settings need to be manually written. To aid this procedure a shared parameters file is provided. This is similar to the shared parameters provided by Autodesk, with some additions to overcome shortcomings in the Autodesk version, in particular for geolocation and type vs instance parameter name clashes. Many of these parameters will be used throughout the guidebook.

Whenever one of these shared parameters are used, they <strong>must</strong> belong to the <code>IFC Parameters</code> group, as shown below.

{{< wiki-image src="/media/revit-setup-group.png" alt="An example of IFC parameters in Revit" mode="inline" >}}

OSArch has prepared a Revit shared parameters files, shown below. They are based off the official Autodesk shared parameters, but contains a few improvements:

- IFC2X3 geolocation parameters are added
- The deprecated parameter <code>IfcSiteGUID</code> has been removed, as the built-in parameter should be used instead.

You can download them here:

- [Shared parameters for instances](https://raw.githubusercontent.com/Moult/revit-ifc/osarch/Install/Program%20Files%20to%20Install/IFC%20Shared%20Parameters-RevitIFCBuiltIn_ALL.txt)
- [Shared parameters for types](https://raw.githubusercontent.com/Moult/revit-ifc/osarch/Install/Program%20Files%20to%20Install/IFC%20Shared%20Parameters-RevitIFCBuiltIn-Type_ALL.txt)

## Setting up property set mappings
The Revit IFC exporter also requires the user to define property sets to be exported. By default, the definition is empty. A template is provided below.

{{< wiki-image src="/media/revit-setup-psets.png" alt="Setting up psets in Revit" mode="inline" >}}

A starting template for Revit user defined psets can be found here: {{< wiki-image src="/media/Revit-psets.txt" alt="Revit-psets.txt" mode="inline" >}}.

The syntax of defining custom property sets is also explained in this video: https://www.youtube.com/watch?v=SswHKtcM3mI

## Parameter expression
Revit allow you to use parameter expression to replace a parameter value on export. See [revit-ifc source forge wiki](https://sourceforge.net/p/ifcexporter/wiki/Notes%20on%20parameter%20expression/).

For example, to map Revit native <code>Description</code> to <code>IfcRoot.Description</code> you can add an <code>IfcDescription[Type]</code> type parameter and enter value <code>{$this(&quot;Description&quot;)}</code>.

## Revit and IFC <code>GlobalId</code> attributes
IFC <code>GlobalId</code> values do not exist in a default Revit project file. To create and see the GlobalId select the checkbox shown below select the <code>Store the IFC GUID in an element parameter after export</code> option in <code>File &gt; Export &gt; IFC &gt; Modify Setup &gt; Advanced</code> window, as shown below. It is highly recommended that this option is always enabled.

{{< wiki-image src="/media/revit-settings-ifcglobalid.png" alt="Revit-settings-ifcglobalid.PNG" mode="inline" >}}

After your export is complete, you can now see a new parameter called <code>IfcGUID</code> for your objects as shown below. Despite the inconsistent naming, this is actually the IFC <code>GlobalId</code>. This property can now be overridden, copied, or searched for. If the text is deleted, it will be rewritten on your next export. Revit will always rewrite the original <code>GlobalId</code>, with whatever id is written inside Revit. There is no way to automatically regenerate a fresh ID for an existing Revit object, so if it is overwritten is can only be retrieved by finding it manually in the IFC file.

{{< wiki-image src="/media/revit-params-ifcglobalid.png" alt="Revit-params-ifcglobalid.png" mode="inline" >}}

It is possible to determine the IFC <code>GlobalId</code> without the overhead of exporting a full IFC file, since it is predetermined. Every Revit element has a <code>UniqueId</code> parameter, which is a hexademical string formatted in groups of <code>8-4-4-4-12-8</code>. This string contains 8 more hexadecimal characters at the end compared to the standard UUID formatting. These 8 trailing hexadecimal characters store the Revit <code>ElementId</code>. The remaining standard UUID formatted string is called the Revit <code>EpisodeId</code>, which provides true uniqueness, as the Revit <code>ElementId</code> has no guarantee of uniqueness.

<pre>
ElementId = 130315 (Decimal) or 1fd0b (Hex)
           &lt; ........... EpisodeId .......... &gt;-&lt;ElmtId&gt;
UniqueId = 60f91daf-3dd7-4283-a86d-24137b73f3da-0001fd0b
</pre>

This <code>UniqueId</code> can be converted into an IFC GUID by XOR-ing the last 8 characters of the <code>EpisodeId</code> and the 8 character <code>ElementId</code>. This provides an IFC GUID in standard UUID format. Revit calls this standard UUID format the "DWF GUID" for historical reasons, but it contains the same data as the IFC GUID. It may then be compressed to the 22-character IFC base64 <code>GlobalId</code> attribute.

Example Python code of this procedure is shown below.


```python
unique_id = UniqueId.replace('-', '')
dwf_guid = unique_id[0:-16] + hex(int(unique_id[-16:-8], 16) ^ int(unique_id[-8:], 16))[2:]
# 60f91daf3dd74283a86d24137b720ed1
ifc_guid = ifcopenshell.guid.compress(dwf_guid)
# 1W_HslFTT2WwXj91DxSWxH
```

Althought it will fail for some elements. Using RevitAPI you can use a function like :

```python
from Autodesk.Revit.DB import ExportUtils, Element

def generate_ifc_guid(element: Element):
    dwf_guid = ExportUtils.GetExportId(doc, element.Id).ToString().replace("-", "")[:32]
    return ifcopenshell.guid.compress(dwf_guid)
```


## See also
- [OpenBIM](/openbim/)
- [Autodesk Revit](/autodesk-revit/)
- [Software Comparison & IFC](/ifc-industry-foundation-classes-software-comparison/)

## External References
- buildingSMART Denmark have written an [IFC Export Guide for Revit and ArchiCAD](https://anvisninger.molio.dk/Gratis-vaerktojer/buildingSMART/IFC_Export_Guide_EN)
