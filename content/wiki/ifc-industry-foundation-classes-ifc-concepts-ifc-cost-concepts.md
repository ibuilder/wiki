---
title: "IFC cost concepts"
url: "/ifc-industry-foundation-classes-ifc-concepts-ifc-cost-concepts/"
parent: "/ifc-industry-foundation-classes-ifc-concepts/"
aliases: ["/IFC_-_Industry_Foundation_Classes/IFC_concepts/IFC_cost_concepts/", "/Industry_Foundation_Classes_(IFC)/IFC_concepts/IFC_cost_concepts/"]
categories: []
lastmod: "2022-07-28T10:21:41Z"
---

The primary classes related to this concept are:

- IfcCostSchedule
- IfcCostItem
- IfcCostValue

## A cost schedule can exist
{{< wiki-image src="/media/ifc-concept-cost-costschedule.png" alt="Ifc-concept-cost-costschedule.png" mode="inline" >}}

A cost schedule is a collection of cost items, used for a specified purpose. Typical purposes are cost plans and tenders.

Note: there is no explicit documentation which explains how a cost schedule is related back to the project or context. Therefore, in the absence of documentation, we are assuming that we declare it to the project as shown. However, this is only an assumption. There are explicit arguments against this assumption, such as that a cost schedule must be tied back to a project order. However, this evidence is not considered strong enough as it is never mentioned in the cost schedule documentation page itself.

Source: IfcProjectOrder

## A cost schedule can be part of a project order
{{< wiki-image src="/media/ifc-concept-cost-projectorder.png" alt="Ifc-concept-cost-projectorder.png" mode="inline" >}}

Project orders, such as work orders, change orders, or in particular purchase orders, may include a cost schedule. For example, a cost schedule may be used to provide an estimate of costs for a work order.

Source: IfcCostSchedule, IfcProjectOrder

## A cost schedule may have approval requests
{{< wiki-image src="/media/ifc-concept-cost-costschedule-approval.png" alt="Ifc-concept-cost-costschedule-approval.png" mode="inline" >}}

A cost schedule may have an approval associated with it, to determine whether it is approved or not.

Source: IfcCostSchedule

## A cost schedule may have a series of approvals
{{< wiki-image src="/media/ifc-concept-cost-costschedule-approval-rel.png" alt="Ifc-concept-cost-costschedule-approval-rel.png" mode="inline" >}}

An approval that relates to a cost schedule may itself be broken down into sub approvals. This implies that the sub approvals (RelatedApprovals) must first be approved before the parent approval (RelatingApproval) may be approved.

Source: IfcCostSchedule

## A cost schedule may have actors associated with it
{{< wiki-image src="/media/ifc-concept-cost-costschedule-actor.png" alt="Ifc-concept-cost-costschedule-actor.png" mode="inline" >}}

A cost schedule may describe the people who authored it, who are stakeholders, recipients, or clients.

Source: IfcCostSchedule

## A cost schedule may contain cost items
{{< wiki-image src="/media/ifc-concept-cost-costschedule-costitem.png" alt="Ifc-concept-cost-costschedule-costitem.png" mode="inline" >}}

Cost schedules can contain a single summary cost item. An IfcCostItem describes a cost or financial value together with descriptive information that describes its context in a form that enables it to be used within a cost schedule. An IfcCostItem can be used to represent the cost of goods and services, the execution of works by a process, lifecycle cost and more. This summary cost item may then be broken down further into more cost items, but only one summary cost item is allowed.

Source: IfcCostSchedule

## A cost item may be assigned a classification reference
{{< wiki-image src="/media/ifc-concept-cost-costitem-classification.png" alt="Ifc-concept-cost-costitem-classification.png" mode="inline" >}}

Cost items may relate to an external classification system, where a variety of identification codes are used extensively to identify the meaning of the cost. Examples include project phase codes, CSI codes, takeoff sequence numbers, and cost accounts.

Source: IfcCostItem

## A cost item may nest cost items
{{< wiki-image src="/media/ifc-concept-cost-costitem-nest.png" alt="Ifc-concept-cost-costitem-nest.png" mode="inline" >}}

A cost item may have cost items nested within it, typically forming the hierarchy or breakdown of a cost schedule.

Source: IfcCostItem

## A cost item may include arbitrary quantities
{{< wiki-image src="/media/ifc-concept-cost-costitem-costquantity.png" alt="Ifc-concept-cost-costitem-costquantity.png" mode="inline" >}}

A cost item may specify arbitrary quantities. These quantities are not linked to model elements. If multiple quantities are included for a single cost item, each individual quantity is a component which may be summed together to derive the total quantity. For example, this cost item has two components: one with volume of 3m2, another of 2m2. The total quantity is 3 + 2 = 5. All quantities must match the same measurement type (e.g. volume, area, count, etc).

Source: IfcCostItem

## A cost item may have a total monetary cost value
{{< wiki-image src="/media/ifc-concept-cost-costitem-costvalue.png" alt="Ifc-concept-cost-costitem-costvalue.png" mode="inline" >}}

If a cost item has no cost quantities, this cost value represents the total cost of the cost item.

Source: IfcCostItem

## A cost item may have a total cost derived from a unit value and quantities
{{< wiki-image src="/media/ifc-concept-cost-costitem-costvalue-unit.png" alt="Ifc-concept-cost-costitem-costvalue-unit.png" mode="inline" >}}

If a cost item has quantities, the cost value represents a unit cost of the cost item, which is "2" in this case. The total cost of the cost item is derived by multiplying the cost quantities and the unit cost, which is 3 x 2 = 6 in this example.

Source: IfcCostItem

## The value of a cost item may be broken down into categories
{{< wiki-image src="/media/ifc-concept-cost-costitem-costvalue-category.png" alt="Ifc-concept-cost-costitem-costvalue-category.png" mode="inline" >}}

Cost values may be categorised to understand the cost breakdown. Example categories are delivery, labour, installation, overhead, material, storage, transportation, and more.

Source: IfcCostItem, IfcCostValue

## The value of a cost item may be calculated from the sum of its nested cost items
{{< wiki-image src="/media/ifc-concept-cost-costitem-costvalue-category-sum.png" alt="Ifc-concept-cost-costitem-costvalue-category-sum.png" mode="inline" >}}

When the cost value has a special category of "*", this means that its value is calculated from the sum of the costs of all nested cost items.

In this example, the parent cost item has a two nested child cost items. The first nested item has a total unit cost of 3 + 2 = 5, and a total quantity of 5. This gives a total cost of the nested child of 5 x 5 = 25. The second nested item has a total cost of 7. Therefore, the sum of all nested cost items is 25 + 7 = 32.

Source: IfcCostItem

## The value of a cost item may be calculated from the sum of its nested cost items, filtered by a category
{{< wiki-image src="/media/ifc-concept-cost-costitem-costvalue-category-filter.png" alt="Ifc-concept-cost-costitem-costvalue-category-filter.png" mode="inline" >}}

This is very similar to the concept of using the special "*" category to sum the total cost of all nested cost items. However, the difference in that this time, we do not sum the total costs, we only sum the costs that relate to the category specified in the category attribute.

In this example, the first nested cost item has a unit Delivery cost of 3, and a quantity of 5. We don't count the unit Labour cost because it does not match our filter of "Delivery". This gives a total cost of 3 x 5 = 15. The second nested cost item also does not have any cost values belonging to a "Delivery" category. Therefore the final sum of all nested cost items that meet the "Delivery" filter is 15.

This means that if you have a "Category" filled out for a cost value, its value will always be derived if you have nested cost items. If you do not have any cost items, then you are free to fill in a value.

Source: IfcCostItem

## A cost value may be calculated from a formula
{{< wiki-image src="/media/ifc-concept-cost-costitem-costvalue-components.png" alt="Ifc-concept-cost-costitem-costvalue-components.png" mode="inline" >}}

A cost value may be calculated from a formula, like "3 x 2". The operands of this formula ("3" and "2") are known as components. The operator of the formula ("x") is known as t he arithmetic operator. This may be nested, or use summing or category filters to create complex formulas to derive the cost value.

Source: IfcCostItem
