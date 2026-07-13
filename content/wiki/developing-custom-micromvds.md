---
title: "Developing custom MicroMVDs"
url: "/developing-custom-micromvds/"
aliases: ["/Developing_custom_MicroMVDs/"]
categories: []
lastmod: "2020-08-10T02:14:01Z"
---

## Authoring a custom MicroMVD
If you wish to write your own custom MicroMVD, some basic technical knowledge is required. The first is how to structure a MicroMVD. Each MicroMVD must follow the generic format shown below:

<pre>Feature: Name of the exchange requirement

In order to achieve a business goal
As a particular user or stakeholder
We need to satisfy specific technical requirements

Scenario: Check a particular technical requirement
 * Some data must be in a certain way
 * Some other data must be in another way

Scenario: Check another particular technical requirement
 * Some data must be in a certain way
 * Some other data must be in another way
</pre>

A feature file always starts by defining the name of the <code>Feature</code>. Below the feature name is an three sentence paragraph which describes the value this MicroMVD delivers to the project. This paragraph is optional, but encouraged to help align both technical and non-technical project participants.

The individual audits are then categorised into one or more <code>Scenario</code> blocks. Each scenario has a name that focuses on a particular technical requirement of the exchange requirement, and contains one or more test sentences. Each sentence checks data related to the scenario. The feature name and scenario names can be anything, but must be prefixed by <code>Feature: </code> and <code>Scenario: </code> respectively. The test sentences within each <code>Scenario</code> block must match a pattern defined in the MicroMVD for the project.

These MicroMVDs are templates to be used as a starting point for projects to describe exchange requirements. It is encouraged to modify it to project requirements, delete irrelevant tests, and add new tests as required.

## Packaging test suites for recipients
The author of the test suite will provide a folder named <code>features/</code>. The contents of this folder will contain:

<pre>features/test-suite-A.feature # This is a test suite
features/test-suite-B.feature # This is another test suite, you can have multiple
features/environment.py # This defines the test environment
features/template.html # This is the HTML report template
features/steps/steps.py # The defines the test sentences
</pre>

These files constitute the full test system, and must be shared in full to all recipients and all authors. This ensures full transparency of exchange requirements.

The <code>steps.py</code> file requires basic programming knowledge to understand and modify, and is generally only modified by the test author.  Recipients are free to inspect it to gain a better understanding of what constitutes test compliance.

The <code>environment.py</code> file contains the environment settings to run the tests, using the [Behave](https://github.com/behave/behave) system. An intermediate knowledge of <em>Behave</em> and <em>Python</em> is required to modify this file. For most recipients, this file must be left alone.

The <code>template.html</code> file contains a HTML report template. It is plain HTML code with [Mustache](https://mustache.github.io/) for the templating language. A basic knowledge of HTML and Mustache is required to modify this file, which is self-explanatory.

## Receiving and running test suites
A recipient will receive a <code>features/</code> directory. They are not required to modify the files in any way.

The cross-platform, free software [BIMTester](https://bonsaibim.org/download.html) tool is capable of running the test suite and generating reports. The BIMTester tool expects the <code>features/</code> directory to be in the current working directory.

Recipients are encouraged to run the tests and generate reports at their convenience. The test author may optionally provide an automated platform which runs tests and generate downloadable reports, as well as track progress on test results.

## Maintaining test suites
The test suite will be working document that will grow throughout the project lifecycle to ensure that data quality regressions are not made, and that the level of information which has been audited is clearly documented.

The test author will advise all recipients whenever new tests are being introduced or new test sentences are being defined.
