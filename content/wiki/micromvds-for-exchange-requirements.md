---
title: "MicroMVDs for exchange requirements"
url: "/micromvds-for-exchange-requirements/"
aliases: ["/MicroMVDs_for_exchange_requirements/", "/Using_MicroMVDs_for_exchange_requirements/"]
categories: ["BIMTester", "Bonsai", "MicroMVD", "Model View Definitions (MVD)"]
lastmod: "2022-07-28T11:31:00Z"
---

To guarantee correct BIM data, data exchange requirements need to be specified and audited. **A MicroMVD is a collection of sentences that describe auditing requirements, written in plain language understood by both technical and non-technical stakeholders. These sentences are organised into categories, and can be processed by a computer to automatically check whether or not the requirements are satisfied.**

This approach builds on the concept in software development called [unit testing](https://en.wikipedia.org/wiki/Unit_testing), specifically [behavior driven development](https://en.wikipedia.org/wiki/Behavior-driven_development). Describing the requirement in simple to understand (but still machine readable) [gherkin format](https://en.wikipedia.org/wiki/Cucumber_(software)) makes the intentions clear to designers and makes writing unit tests simple.

[BIMTester](/bimtester/) has implemented use of MicroMVDs for auditing model quality from IFC files. [BIMTester](/bimtester/) is integrated into [Bonsai](/bonsai/)

Here is an example of a simple MicroMVD, which checks that an IFC4 file is provided.

<pre>
Feature: Project setup

In order to view the BIM data
As any interested stakeholder
We need an IFC file

Scenario: Receiving a file
 * IFC data must use the &quot;IFC4&quot; schema
</pre>

This MicroMVD is stored in a simple text file with the <code>.feature</code> file extension. The file name is arbitrary, but may be used to describe what it is auditing. These simple text files can be edited in any text editor, such as [Vim](https://www.vim.org/), Apple TextEdit, or Microsoft Notepad. No proprietary software is required: anybody can read and write MicroMVDs.

These <code>*.feature</code> files, each containing sentences like the above can be processed by a computer. In the example above, a MicroMVD auditing program will check that a particular IFC file uses the <code>IFC4</code> schema. The MicroMVD auditing program can then generate a report, which can be used by stakeholers to track whether or not a project is satisfying its requirements.

Unlike other auditing solutions like Solibri or SimpleBIM, MicroMVDs are non-proprietary, do not expire, are free, much lighter, are easy to change and develop, and are cross-platform.

## List of MicroMVDs
Although you are free to write your own MicroMVD specific to your project, a series of MicroMVDs have been published online that address common problems. You can copy and paste these templates into your own <code>*.feature</code> files, and modify it to suite your project.

## Subpages
{{< subpages >}}

All MicroMVD can be found in [MicroMVD](/categories/micromvd/)

## Auditing BIM data with Bonsai and MicroMVDs
{{< wiki-image src="/media/bimtester.png" alt="The BIMTester Quality Auditing panel in Bonsai" mode="thumb" caption="The BIMTester Quality Auditing panel in Bonsai" align="right" width="300" >}}

{{< wiki-image src="/media/bimtester-report.png" alt="An example audit report from BIMTester" mode="thumb" caption="An example audit report from BIMTester" align="right" width="300" >}}

To begin auditing BIM data, you will need an IFC file. Let's imagine you have a file called <code>file.ifc</code>.

You will then need to specify your exchange requirements. Follow the steps below:

1. Create a new text file called <code>audit.feature</code>
1. Copy a MicroMVD template (e.g. [Project setup MicroMVD](/micromvds-for-exchange-requirements-project-setup-micromvd/)) into your <code>audit.feature</code> file.
1. Modify the template based on your project. For example, you may change the sentence <code> * IFC data must use the &quot;{schema}&quot; schema</code> to read <code> * IFC data must use the &quot;IFC4&quot; schema</code>.

Now that you have specified your exchange requirements, you can audit it using a program. One free and open source option is [BIMTester](https://bonsaibim.org/download.html), which comes with [Bonsai](/bonsai/), or can be [run standalone](https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.6.0/src/ifcbimtester). Here's an example of how to audit it:

1. Launch Blender with [Bonsai](/bonsai/) installed.
1. Open up the *BIMTester* panel in the *Scene Properties*.
1. Navigate to your <code>file.ifc</code> file in the *IFC File* property. This is the IFC that will be audited.
1. Navigate to your <code>audit.feature</code> file in the *Feature / IDS* property. This is your audit requirements file.
1. Press the <code>Execute BIMTester</code> button.
1. Your audit report results will pop up in your browser.

The *Custom Steps* is for advanced users who have built their own custom requirements. This requires coding knowledge.

## Modifying a MicroMVD
MicroMVDs are designed to be modified to be specific to your project. You are free to delete lines that don't apply to your project, or add additional lines if you need to audit more things in your project. You can have a single <code>.feature</code> or multiple files for each IFC, depending on how you want to organise your project. Once you have tailored it to your project, it is encouraged to include it in your project contract, so that all stakeholders are crystal clear on exactly what the data exchange requirements are, and how it will be audited.

If you know how to code, you can also define your own sentences. Read more in [Developing custom MicroMVDs](/developing-custom-micromvds/).
