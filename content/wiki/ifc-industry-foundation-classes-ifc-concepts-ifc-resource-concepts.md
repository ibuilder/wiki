---
title: "IFC resource concepts"
url: "/ifc-industry-foundation-classes-ifc-concepts-ifc-resource-concepts/"
parent: "/ifc-industry-foundation-classes-ifc-concepts/"
aliases: ["/IFC_-_Industry_Foundation_Classes/IFC_concepts/IFC_resource_concepts/", "/Industry_Foundation_Classes_(IFC)/IFC_concepts/IFC_resource_concepts/"]
categories: ["Industry Foundation Classes (IFC)"]
lastmod: "2022-07-28T10:21:42Z"
---

Resources represent things which can be consumed in a process which have an associated cost or scheduling impact.

## A role manages a resource
{{< wiki-image src="/media/ifc-concept-resource-manager.png" alt="Ifc-concept-resource-manager.png" mode="inline" >}}

An organisation, person, or role is responsible for managing, allocating, delegating, and scheduling usage of a resource.

## A role consumes a resource
{{< wiki-image src="/media/ifc-concept-resource-consumer.png" alt="Ifc-concept-resource-consumer.png" mode="inline" >}}

An organisation, person, or role is performing some form of work that consumes a resource.

## Resource availability restrictions
{{< wiki-image src="/media/ifc-concept-resource-availability.png" alt="Ifc-concept-resource-availability.png" mode="inline" >}}

A resource is only available on certain dates and not others.

## A resource is an asset
{{< wiki-image src="/media/ifc-concept-resource-asset.png" alt="Ifc-concept-resource-asset.png" mode="inline" >}}

A resource is an asset. Although not shown, the asset may then be owned by an organisation as described in [IFC group concepts](/IFC_group_concepts/).

## A resource is consumed by a task
{{< wiki-image src="/media/ifc-concept-resource-task.png" alt="Ifc-concept-resource-task.png" mode="inline" >}}

A resource is consumed by a task.

## A resource may be consumed by a particular quantity during execution of a task
{{< wiki-image src="/media/ifc-concept-resource-task-consumption.png" alt="Ifc-concept-resource-task-consumption.png" mode="inline" >}}

10m3 of concrete is consumed by a task.
