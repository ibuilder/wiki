---
title: "IFC sequence concepts"
url: "/ifc-industry-foundation-classes-ifc-concepts-ifc-sequence-concepts/"
aliases: ["/IFC_-_Industry_Foundation_Classes/IFC_concepts/IFC_sequence_concepts/", "/Industry_Foundation_Classes_(IFC)/IFC_concepts/IFC_sequence_concepts/"]
categories: ["Industry Foundation Classes (IFC)"]
lastmod: "2022-07-28T10:21:42Z"
---

Processes are individual events or tasks. Processes may have different meanings when used in different scenarios. When processes are used in construction, they represent construction tasks which have associated sequence relationships, may transform inputs into outputs, and have relationships to costs, products, and resources. When processes are used in facility management, they represent maintenance tasks, including to-do lists and recurring patterns.

The primary classes related to this concept are:

- IfcWorkCalendar
- IfcWorkControl
- IfcWorkPlan
- IfcWorkSchedule
- IfcRelSequence
- IfcTask
- IfcTaskTime
- IfcLagTime
- IfcTaskType

Bits that are currently skipped for further analysis:

- IfcTask: Quantities of resources consumed by the task are dealt with by defining the IfcElementQuantity for the resource and not at the instance of IfcTask.
- IfcTask: Constraints may be applied to a task to indicate fixed task duration, fixed start or fixed finish, where IfcMetric.ReferencePath is set to the corresponding attribute on the IfcTaskTime entity.

## A project has plans related to construction and facility management
{{< wiki-image src="/media/ifc-concept-sequence-workplan.png" alt="Ifc-concept-sequence-workplan.png" mode="inline" >}}

Work plans group work schedules, typically to distinguish between schedules for construction management purposes and schedules used for facility management purposes.

Note: the purpose attribute seems to have some similarities, but since it is so loosely defined, we don't really know what to make of it. Also note that the docs for IfcWorkPlan seem to suggest that a work plan being declared to the project actually means that a work plan is about constructing the project. With some imaginative interpretation, this could mean that a work plan could be assigned to something else entirely, not with a declares, but instead with a IfcRelAssignsToControl relationship, and therefore only indirectly be assigned to the IfcProject. However, no evidence is found of a usecase of this.

Source: IfcWorkPlan, IfcWorkControl

## A project may have work calendars
{{< wiki-image src="/media/ifc-concept-sequence-workcalendar.png" alt="Ifc-concept-sequence-workcalendar.png" mode="inline" >}}

A work calendar is a definition of working time and holiday times. Later on, this calendar can be used to describe when things are available or when tasks are allowed to take place. A typical calendar might be a 5-day working week, when you work on Monday to Friday and take Saturday and Sunday off.

Note: we are unsure whether or not it is more appropriate to store calendars at the project level or at the work plan level (described in another concept with caveats of its own) or both. For now, our implementation stores calendars at the project level.

Source: IfcWorkSchedule

## A project has schedules related to construction and facility management
{{< wiki-image src="/media/ifc-concept-sequence-workschedule.png" alt="Ifc-concept-sequence-workschedule.png" mode="inline" >}}

A work schedule is used to group together tasks to achieve a goal.

Note: we are unsure what is the purpose of directly assigning work schedules to the project. It makes more sense to group it within an IfcWorkPlan, which acts as a distinguishing factor between work schedules used for sequencing, compared to facility management, or other currently unknown purposes (perhaps, safety routine checks?). We think this relationship should be removed. The docs for IfcWorkControl also state that you should only relate it to the project as a fallback if no better context may be provided.

Source: IfcWorkSchedule, IfcWorkControl

## A project may contain tasks
{{< wiki-image src="/media/ifc-concept-sequence-task-project.png" alt="Ifc-concept-sequence-task-project.png" mode="inline" >}}

When a task has no parent, it is defined globally as a task in your project.

Note: we are unsure what is the purpose of this. Tasks seem to make sense within the context of a work schedule, not elsewhere. We think this relationship should be removed.

Source: IfcTask, IfcWorkSchedule

## A work plan contains calendars
{{< wiki-image src="/media/ifc-concept-sequence-workcalendar-plan.png" alt="Ifc-concept-sequence-workcalendar-plan.png" mode="inline" >}}

A calendar within a work plan implies that the calendar is related to the work plan, and may be used later on to describe availability for other concepts within the work plan, such as tasks or resources.

Note: there is only a single sentence describing this relationship in the source, and it uses a nests relationship which is different from all other work plan relationships, so we are suspicious about this concept and do not currently support it.

Source: IfcConstructionResource

## A work plan contains schedules
{{< wiki-image src="/media/ifc-concept-sequence-workschedule-workplan.png" alt="Ifc-concept-sequence-workschedule-workplan.png" mode="inline" >}}

A work schedule is used to group together tasks to achieve a goal. That goal is related to the work plan that it is part of. Typically, a work plan will contain multiple schedules. Each schedule may be planned, actual, or a baseline.

Source: IfcWorkPlan

## A work plan may contain tasks
{{< wiki-image src="/media/ifc-concept-sequence-workplan-task.png" alt="Ifc-concept-sequence-workplan-task.png" mode="inline" >}}

A work plan may contain tasks, which imply that the tasks are relevant to that work plan.

Note: although this is possible, we don't really see the point of it. It makes more sense for tasks to be related to work schedules, not work plans. We think this relationship should be removed.

Source: IfcWorkPlan

## A work plan may contain resources
{{< wiki-image src="/media/ifc-concept-sequence-workplan-resource.png" alt="Ifc-concept-sequence-workplan-resource.png" mode="inline" >}}

A work plan may contain resources, which imply that the resources are relevant to that work plan. These should only be top level resources, such as subcontract or crew resources. Later on, sub resources, such as labour, equipment, or material, may then be related to tasks or calendars in a separate concept.

Source: IfcWorkPlan, IfcConstructionResource

## A work calendar determines when a task can occur
{{< wiki-image src="/media/ifc-concept-sequence-task-calendar.png" alt="Ifc-concept-sequence-task-calendar.png" mode="inline" >}}

If a task is assigned a calendar, its duration may be specified in terms of working days (which IFC calls work time), instead of calendar / elapsed days. In this example, if the calendar is a 5 day working week, the task takes 10 working days, which is equivalent to 2 weeks of actual elapsed time.

Source: IfcWorkCalendar, IfcWorkSchedule

## A work calendar describes when a resource is available
{{< wiki-image src="/media/ifc-concept-resource-availability.png" alt="Ifc-concept-resource-availability.png" mode="inline" >}}

A resource is only available on certain dates and not others.

Source: IfcWorkCalendar

## A work calendar can be inherited through child tasks, procedures, and events
{{< wiki-image src="/media/ifc-concept-sequence-task-calendar-inheritance.png" alt="Ifc-concept-sequence-task-calendar-inheritance.png" mode="inline" >}}

If a task does not have a calendar assigned to it, it inherits the calendar from its parent task. This inheritance makes it easy to assign default calendars to a top level task in a work schedule and only override as necessary in more specific child tasks.

This same inheritance applies to procedures and events.

Note: it is assumed, but no evidence found, that hierarchical resources have this same inheritance behaviour. In other words, it is assumed that if a resource does not have a calendar assigned to it, it inherits the calendar from its parent resource.

Source: IfcWorkSchedule

## A calendar may override the availability of an inherited calendar
{{< wiki-image src="/media/ifc-concept-sequence-task-calendar-inheritance-override.png" alt="Ifc-concept-sequence-task-calendar-inheritance-override.png" mode="inline" >}}

A calendar may be a child of a parent calendar. The exception times of the child calendar will first inherit, and then override the availability of its parent calendar. A calendar is only allowed to have one parent calendar.

It is currently ambiguous as to how the working times of a child calendar interacts with its parent calendar. We currently assume that if a working time is present in a child calendar, it also overrides the availability of its parent calendar.

For example: a parent calendar has a working time of Monday to Friday. The child calendar has a working time of Saturday, and an exception time of Monday. The final availability of the child calendar is therefore Tuesday to Saturday.

Source: IfcWorkCalendar

## A work schedule may be planned
{{< wiki-image src="/media/ifc-concept-sequence-workschedule-planned.png" alt="Ifc-concept-sequence-workschedule-planned.png" mode="inline" >}}

In construction scheduling, a work schedule can represent your current plan of tasks, prior to the start of construction. A planned schedule typically has scheduled start, finish, and durations for its tasks. A planned schedule must not have any actual starts, actual finishes, or actual duration data. Similarly, a planned schedule must not have any lag times which are marked as "measured" lag times.

Note: the definition that distinguishing planned from actual is assumed. It is not clear in the docs. Also, the fact that we need to read the docs for IfcConstructionResource to figure this out isn't very nice.

Source: IfcConstructionResource, IfcLagTime

## A work schedule may represent actual dates when the tasks are underway or complete
{{< wiki-image src="/media/ifc-concept-sequence-workschedule-actual.png" alt="Ifc-concept-sequence-workschedule-actual.png" mode="inline" >}}

A work schedule may be labeled as an actual schedule, if it contains actual start / end dates of tasks, and actual durations of tasks. Similarly, a actual schedule may have lag times which are marked as "measured" lag times.

Note: the definition that distinguishes planned from actual is assumed. It is not clear in the docs. Also, the fact that we need to read the docs for IfcConstructionResource to figure this out isn't very nice.

Source: IfcConstructionResource, IfcLagTime

## Work schedules may be duplicated and compared as a baseline
{{< wiki-image src="/media/ifc-concept-sequence-workschedule-baseline.png" alt="Ifc-concept-sequence-workschedule-baseline.png" mode="inline" >}}

A work schedule may be duplicated. The old copy of the work schedule is known as a baseline. You can have multiple baseline work schedules. A baseline schedule can be used to compare between old plans and current plans. This baseline comparison can be used as a benchmark to measure your progress or changes in executing or planning a project.

Note: this usecase is not very clearly described in the docs, and mostly hinted at in the IfcConstructionResource page. However, it is common practice to duplicate and create baselines, and so based on this knowledge, we have attemped to describe this concept the best we can.

Source: IfcConstructionResource

## A work schedule may nest other work schedules
{{< wiki-image src="/media/ifc-concept-sequence-subschedule.png" alt="Ifc-concept-sequence-subschedule.png" mode="inline" >}}

Uh. A schedule has subschedules. This is possible, but we have no idea what the usecase is. Nor we do know what it implies for derived dates, calendar inheritance, or cost derivation. We don't currently support this relationship.

Note: there is also an ambiguous note about how work schedules can include other work schedules as sub-items using aggregation instead of nesting. We take a prudent stance that this sentence is just misleading and should be ignored.

Source: IfcWorkSchedule

## A work schedule may contain resources
{{< wiki-image src="/media/ifc-concept-sequence-workschedule-resource.png" alt="Ifc-concept-sequence-workschedule-resource.png" mode="inline" >}}

A work schedule may define the resources that it uses.

Note: this concept is not fully understood, and why it is important to link resources to a work schedule as opposed to simply the tasks within it, or to a work plan.

Source: IfcWorkSchedule, IfcConstructionResource

## A work schedule may contain tasks
{{< wiki-image src="/media/ifc-concept-sequence-task.png" alt="Ifc-concept-sequence-task.png" mode="inline" >}}

In construction scheduling, a work schedule is a collection of tasks that must be completed over a specific timeline in order to reach the final deliverable for the project, such as constructing and commissioning a building.

Source: IfcWorkSchedule

## A work schedule may contain documents
{{< wiki-image src="/media/ifc-concept-sequence-workschedule-document.png" alt="Ifc-concept-sequence-workschedule-document.png" mode="inline" >}}

A work schedule may contain associated documents, such as gantt chart diagrams, related bid documents, safety and risk registers, and reports.

Source: IfcWorkSchedule

## A task may contain subtasks
{{< wiki-image src="/media/ifc-concept-sequence-subtask.png" alt="Ifc-concept-sequence-subtask.png" mode="inline" >}}

In construction scheduling, a task may contain subtasks. This hierarchy of tasks forms the Work Breakdown Structure (WBS).

Source: IfcTask

## A task may be assigned a task time, to determine duration and scheduling times
{{< wiki-image src="/media/ifc-concept-sequence-task-time.png" alt="Ifc-concept-sequence-task-time.png" mode="inline" >}}

A task may have its duration described most simply in terms of elapsed time. In this case, the task takes 7 days.

Source: IfcTaskTime

## A child of a recurring task occurs every time its parent task recurs
{{< wiki-image src="/media/ifc-concept-sequence-task-time-recurring.png" alt="Ifc-concept-sequence-task-time-recurring.png" mode="inline" >}}

Typically in facility management, a parent task would define a recurring time interval at which a maintenance job would need to be performed. Its subtasks, or child tasks, would then typically form the punch list of tasks to be performed in sequence for the parent maintenance job.

Source: IfcTask

## A task may have sequential relationships to other tasks
{{< wiki-image src="/media/ifc-concept-sequence-sequence.png" alt="Ifc-concept-sequence-sequence.png" mode="inline" >}}

In this scenario, a predecessor task (setting up formwork) has a finish to start relationship to a successor task (pouring concrete) with a lag time of 1 elapsed day between them.

Note: When lag times are expressed as absolute duration in working days (i.e. not elapsed days), there is an ambiguity as to whether the predecessor or successor task calendar should be applied. Based off testing in existing scheduling software, it seems as though both calendars are applied, and the one resulting in the worse value (i.e. the longest lag time) is chosen.

Source: IfcTask, IfcRelSequence, IfcProcess

## A task may have a lag time expressed as a ratio
{{< wiki-image src="/media/ifc-concept-sequence-sequence-ratio.png" alt="Ifc-concept-sequence-sequence-ratio.png" mode="inline" >}}

A lag time between two tasks may be expressed as a ratio instead of an absolute duration. If taken as a ratio, the lag duration is determined by the ratio multiplied by the scheduled duration of the predecessor task. So in this scenario, assuming the P10D of the predecessor task is elapsed time, the lag time will be P5D.

Note: In the case of a lag time specified as an absolute duration, the worse of two possible calendars is chosen. In the case of a ratio, the duration of the predecessor task is explicitly nominated. Therefore, we also assume that the calendar of the predecessor task is the only calendar that applies in this scenario.

Source: IfcLagTime

## Tasks can construct or install objects
{{< wiki-image src="/media/ifc-concept-resource-task-construction.png" alt="Ifc-concept-resource-task-construction.png" mode="inline" >}}

A task may be linked to a product. When the task is set as being a construction task, this means that the task results in this wall being constructed.

Source: IfcProcess

## Tasks may consume resources
{{< wiki-image src="/media/ifc-concept-resource-task.png" alt="Ifc-concept-resource-task.png" mode="inline" >}}

A task consumes resources.

Source: IfcTask, IfcProcess, IfcConstructionResource

## A task request may result in a project order being created
{{< wiki-image src="/media/ifc-concept-sequence-task-projectorder.png" alt="Ifc-concept-sequence-task-projectorder.png" mode="inline" >}}

A request of work, maintenance, purchasing, or other types of requests may be represented as an IfcTask typically to a helpdesk or building maintenance company. This may then result in a project order being created.

Note: the wording behind this concept is ambiguous in the documentation, and the usecase of a helpdesk is not fully elaborated. Therefore this description should be treated with suspicion.

Source: IfcTask

## A task may move a product from one location to another
{{< wiki-image src="/media/ifc-concept-sequence-task-move.png" alt="Ifc-concept-sequence-task-move.png" mode="inline" >}}

A task may involve moving products from one location to another. A typical example would be a jump form moving between floors of a building. The product is duplicated at each possible location that it may be at different points of time.

Source: IfcTask

## A task, event, or procedure may contain properties
{{< wiki-image src="/media/ifc-concept-sequence-task-pset.png" alt="Ifc-concept-sequence-task-pset.png" mode="inline" >}}

A task, event, or procedure may contain properties. Typically this is used for risk assessment. For logistic tasks, it may also contain properties for packing instructions.

Source: IfcTask

## A task may be assigned a classification reference
{{< wiki-image src="/media/ifc-concept-sequence-task-classification.png" alt="Ifc-concept-sequence-task-classification.png" mode="inline" >}}

If tasks are based on an external classification system, such Omniclass, which guides the hierarchy of the work breakdown structure, the task may be assigned to a classification reference.

Source: IfcTask

## A project task may be based off a typical task type or template from a library of tasks
{{< wiki-image src="/media/ifc-concept-sequence-task-type.png" alt="Ifc-concept-sequence-task-type.png" mode="inline" >}}

Whereas an IfcTask represents an actual task within a project's work schedule, it may be derived from a task template, also called a task type. Task types are not project specific and may typically be shared within a library of tasks to aid planners in creating schedules.

Source: IfcTask, IfcTaskType

## A task type can nest a task type
{{< wiki-image src="/media/ifc-concept-sequence-task-type-nest-task-type.png" alt="Ifc-concept-sequence-task-type-nest-task-type.png" mode="inline" >}}

Note: It is currently ambiguous as to what this means.

Source: IfcTaskType

## A task type can nest a task
{{< wiki-image src="/media/ifc-concept-sequence-task-type-nest-task.png" alt="Ifc-concept-sequence-task-type-nest-task.png" mode="inline" >}}

Note: It is currently ambiguous as to what this means.

Source: IfcTaskType

## A task type can nest a task, that is also typed
{{< wiki-image src="/media/ifc-concept-sequence-task-type-nest-task-with-type.png" alt="Ifc-concept-sequence-task-type-nest-task-with-type.png" mode="inline" >}}

Note: it is currently ambiguous as to what this means.

Source: IfcTaskType, IfcRelDefinesByObject

## When a task type is used in a project, its child tasks are linked to the project tasks
{{< wiki-image src="/media/ifc-concept-sequence-task-type-definesbyobject.png" alt="Ifc-concept-sequence-task-type-definesbyobject.png" mode="inline" >}}

When a task type with subtasks is used in a project, it creates corresponding task instances in your task tree. To correlate these task instances back to the task type, an object relationship is created.

Note: usecases and workflows of this is still currently ambiguous. Also, there is a discrepancy where the documentation in IfcTaskType describes a nesting relationship, whereas the IfcRelDefinesByObject documentation describes an aggregation relationship.

Source: IfcTaskType, IfcRelDefinesByObject
