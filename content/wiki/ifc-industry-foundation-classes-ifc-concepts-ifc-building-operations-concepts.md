---
title: "IFC building operations concepts"
url: "/ifc-industry-foundation-classes-ifc-concepts-ifc-building-operations-concepts/"
parent: "/ifc-industry-foundation-classes-ifc-concepts/"
aliases: ["/IFC_-_Industry_Foundation_Classes/IFC_concepts/IFC_building_operations_concepts/", "/Industry_Foundation_Classes_(IFC)/IFC_concepts/IFC_building_operations_concepts/"]
categories: []
lastmod: "2022-07-28T10:21:41Z"
---

The primary classes related to this concept are:

- IfcWorkCalendar
- IfcWorkControl
- IfcWorkPlan
- IfcWorkSchedule
- IfcRelSequence
- IfcTask
- IfcTaskTime
- IfcTaskType
- IfcEvent
- IfcProcedure
- IfcEventType
- IfcProcedureType

## A procedure may be defined by a typical procedure type
{{< wiki-image src="/media/ifc-concept-sequence-procedure-type.png" alt="Ifc-concept-sequence-procedure-type.png" mode="inline" >}}

Typically in smart buildings or in process diagrams that describe complex maintenance or emergency procedures, procedure types may be used to describe typical procedures that may occur. Example typical procedures may be "close" for an actuator or "evacuate building". These typical procedures types may then relate to individual procedure instances to describe the capabilities of individual products in a smart building, or relate to tasks to describe complex processes in more detail.

Source: IfcProcedure, IfcProcedureType

## An event may be defined by a typical event type
{{< wiki-image src="/media/ifc-concept-sequence-event-type.png" alt="Ifc-concept-sequence-event-type.png" mode="inline" >}}

Typically in smart buildings or in process diagrams that describe complex maintenance or emergency procedures, event types may be used to describe typical events that may occur. Example typical events may be "motion sensed" or "fire detected". These typical event types may then relate to individual event instances. The individual event instances are then responsible for triggering procedures, as described later in this document.

Source: IfcEvent, IfcEventType

## A product type may be able to perform procedures
{{< wiki-image src="/media/ifc-concept-sequence-procedure.png" alt="Ifc-concept-sequence-procedure.png" mode="inline" >}}

Products which have capabilities can describe the procedures they are capable of. These procedures may later on be linked to events to program smart building capabilities and reactions to their surroundings.

Source: IfcProcedure

## A product may inherit procedures from its type
{{< wiki-image src="/media/ifc-concept-sequence-procedure-product-type.png" alt="Ifc-concept-sequence-procedure-product-type.png" mode="inline" >}}

If a type has procedures, then all of its product instances also inherit all of its procedures.

Source: IfcProcedure

## A product type may have events that can trigger procedures
{{< wiki-image src="/media/ifc-concept-sequence-event-product-type.png" alt="Ifc-concept-sequence-event-product-type.png" mode="inline" >}}

Product types may have events which trigger procedures. This is typically used in building operations and smart buildings.

Source: IfcEvent

## A product may inherit events from its type
{{< wiki-image src="/media/ifc-concept-sequence-event-product.png" alt="Ifc-concept-sequence-event-product.png" mode="inline" >}}

Products may also have events which trigger procedures. This is typically used in building operations and smart buildings. If a product type has an event type, it must inherit the event and its related procedures as well.

Source: IfcEvent

## An event may be constrained to only trigger at certain times
{{< wiki-image src="/media/ifc-concept-sequence-event-calendar.png" alt="Ifc-concept-sequence-event-calendar.png" mode="inline" >}}

A calendar may constrain when an event can occur. In this example, the motion sensor will only start monitoring for motion events during night hours. These night hours are defined by the calendar.

Source: IfcEvent

## A procedure may be constrained to only be performed at certain types
{{< wiki-image src="/media/ifc-concept-sequence-procedure-calendar.png" alt="Ifc-concept-sequence-procedure-calendar.png" mode="inline" >}}

A calendar may constrain when a procedure can be performed. In this example, the alarm may only be reset during the night. These night hours are defined by the calendar.

Source: IfcProcedure

## Warning or cautionary advice may be provided when tasks are to be performed
{{< wiki-image src="/media/ifc-concept-sequence-procedure-advice.png" alt="Ifc-concept-sequence-procedure-advice.png" mode="inline" >}}

If an IfcProcedure has its appropriate PredefinedType set to an "ADVICE_*", then it may be attached to another process to describe warnings, caution, or additional information to be aware of when performing that task. This is typical in building maintenance works.

Source: IfcProcedure

## A task may contain procedures and events
{{< wiki-image src="/media/ifc-concept-sequence-task-nest-procedure-event.png" alt="Ifc-concept-sequence-task-nest-procedure-event.png" mode="inline" >}}

A task may be broken down into procedures and events, if it is better described as a process diagram instead of a punch list (which would be a list of subtasks). When an event is nested in a task, it means that the event only may occur during the task time period.

Source: IfcProcedure, IfcEvent

## A procedure may be broken down into more procedures and events
{{< wiki-image src="/media/ifc-concept-sequence-procedure-nest.png" alt="Ifc-concept-sequence-procedure-nest.png" mode="inline" >}}

If a procedure is particularly complex, it may be further broken down in more detail by nesting more procedures and events within it. Note that although it is possible to break down IfcProcedures into more detail, it is not allowed to break down IfcEvents into sub events.

Source: IfcProcedure, IfcEvent

## Events and procedures may have a sequence
{{< wiki-image src="/media/ifc-concept-sequence-event-procedure-sequence.png" alt="Ifc-concept-sequence-event-procedure-sequence.png" mode="inline" >}}

Events and procedures may be sequenced in a particular order. If an event occurs before a procedure, this implies that the procedure will occur in response to an event. If an event occurs after a procedure, this implies that completing a procedure will trigger an event. Unlike tasks which have durations, there is no such thing as lag time nor sequence types in this context.

Source: IfcProcedure, IfcEvent
