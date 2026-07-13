---
title: "Revit IFC classifications"
url: "/revit-setup-for-openbim-revit-ifc-classifications/"
aliases: ["/Revit_IFC_classifications/", "/Revit_classifications/", "/Revit_setup_for_OpenBIM/Revit_IFC_classifications/"]
categories: ["Autodesk Revit"]
lastmod: "2022-01-31T10:39:01Z"
---

You will be required to modify classification settings. The classification settings dialog can be found in the <code>File &gt; Export &gt; IFC &gt; Modify Setup &gt; Property Sets &gt; Classification Settings ...</code> location.

{{< wiki-image src="/media/revit-classifications-settings.png" alt="Revit-classifications-settings.png" mode="inline" >}}

The details of the classification system that you are using will be entered into the fields of this settings window. An example is shown.

{{< wiki-image src="/media/revit-classifications-settings2.png" alt="Revit-classifications-settings2.png" mode="inline" >}}

These values will vary depending on which classification system you are using. A list of standard values are provided in the [IFC classifications](/ifc-industry-foundation-classes-ifc-classifications/) page. The value of <code>Classification field name</code> will vary depending on whether you use the plug-in or not to manage your classifications.

## Classification without any plug-ins
This portion of the guide applies if you are not using any plug-ins to classify objects.

The <code>Classification field name</code> must have <code>ClassificationCode</code> set as a value.

You must create a new type parameter assigned to the object called <code>ClassificationCode</code>. Classifications are composed of two parts: a classification code, and a name of that particular classification item.  For example, in <em>Uniclass</em>, a code might be <code>SS_30_10_30_25</code>, and its corresponding name is <code>Heavy steel roof framing systems</code>.  This must be entered into the <code>ClassificationCode</code> as follows: <code>SS_30_10_30_25:Heavy steel roof framing systems</code>. The <code>:</code> symbol separates between the code and the name.

If your classification system does not have names but only has codes, then you may omit the <code>:</code> symbol and the name portion, and just enter <code>SS_30_10_30_25</code>, but this is discouraged. If your code contains the <code>:</code> symbol itself, you must specify a name portion.

## Autodesk Classification manager for Revit
This portion of the guide applies if you are using the [Autodesk Classification Manager for Revit](http://www.biminteroperabilitytools.com/classificationmanager.php). Even if you are using this plug-in, it does not mean your IFC export will contain classification data correctly.

The plug-in stores its classification codes in various parameter names scattered throughout different objects. You must include all of the relevant parameter names that the plug-in creates into a comma separated list in the <code>Classification field name</code> input field. An example is shown below:

<pre>Classification.Facility.Number,Classification.Space.Number,Classification.Uniclass.Pr.Number,Classification.Uniclass.EF.Number,Classification.Uniclass.Ss.Number</pre>

## Using multiple classification systems
The instructions so far allow you to only specify a single classification system.

To use another classification system, you must add another type parameter called <code>ClassificationCode(2)</code> to the relevant families. However, the text value of this field has special requirements. It must follow the formatting <code>[SystemName]Code:Name</code>. For example, you might fill this out with <code>[Uniclass 2015]SS_30_10_30_25:Heavy steel roof framing systems</code>.

It is not currently possible to fill out other information such as the edition, edition date, etc for subsequent classification systems.

You may add even more classification systems, such as <code>ClassificationCode(3)</code>, <code>ClassificationCode(4)</code> and so on.
