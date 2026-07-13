---
title: "Representation Context"
url: "/ifc-industry-foundation-classes-representation-context/"
parent: "/ifc-industry-foundation-classes/"
aliases: ["/IFC_-_Industry_Foundation_Classes/Representation_Context/"]
categories: []
lastmod: "2025-04-16T15:55:31Z"
---

A **representation context** in IFC is a way of organizing how geometry and drawings are grouped and understood within a building model. It defines **where** and **how** a shape or graphic is meant to be used—whether it's part of a 3D model, a 2D plan, or even a special kind of view like a section or elevation.

At a basic level, the representation context answers questions like:
- *Is this geometry part of the model or just a drawing?*
- *Is it meant to be seen in 3D or 2D?*
- *What kind of geometry is it—like a full body, a centerline, or just a note?*

By using representation contexts, software can decide which shapes to show in different views (like 3D models, plans, or sections) and how to interpret them correctly.

## ContextType, ContextIdentifier & TargetView
<small>*the following excerpt is from [here](https://community.osarch.org/discussion/comment/15044/#Comment_15044).*</small> 

A context (or specifically, a subcontext, you never use contexts directly) is made of 3 major categories:

- **ContextType** (Model/Plan): Model indicates it stores 3D geometry using XYZ coordinates. Plan indicates it stores 2D geometry using XY coordinates only.  
Note that these are not global XYZ, these are local XYZ coordinates relative to the orientation of the object (i.e. the orange dot). So if the object is rotated, 2D XY may not be pointing exactly up.

- **ContextIdentifier** (Body/Annotation/Axis/Box/etc): we'll focus on 2 here.  
The Body says that the geometry represents the body of the object.  
The Annotation says that the geometry further annotates (e.g. highlights/labels/directs attention to a particular aspect of the element) the element.  
So if you are drawing a plan view of a door where the door panel is wide open, that is part of the Body.  
However, the door swing arc in theory is an Annotation, as it merely annotates the clear extents of the swing and directionality.  
Similarly, the triangle symbol / arrows used for awning and sliding windows are Annotations.  
In your example, your geometry is of the roof tiles, which is the Body.

- **TargetView** (MODEL_VIEW/PLAN_VIEW/SECTION_VIEW/etc):  
This indicates that the geometry is suited towards this particular type of view and should take priority.

In drafting, we always draw the body of the object, and then draw the annotation in addition to the body.  
(e.g. first you draw the window, then you draw the arrow indicating the sliding direction of the window).  
There are additional rules that certain values are special in that they often use particular 2D symbology that is unique to those views that you won't typically find elsewhere (e.g. fire extinguishers have a symbol on a plan, but you'll never use that symbol in a section).

## Rules for Drawing Contexts
So for a given drawing, here are the rules followed:

1. First the Body **ContextIdentifier** is drawn. Then, the Annotation **ContextIdentifier** is drawn in addition.
1. If there are multiple Bodies and Annotations to choose from, the one with a **TargetView** that matches the drawing is prioritised. The **MODEL_VIEW** **TargetView** is the fallback.
1. In addition, we have a special rule that if the drawing has a **PLAN_VIEW** or **REFLECTED_PLAN_VIEW**, the **Plan** **ContextType** is prioritised over **Model**.

## Example: PLAN_VIEW
Let’s imagine we are doing a regular floor plan drawing (i.e. **PLAN_VIEW**).  
If we had all possible Body permutations in theory, this is the priority list:

1. Plan/Body/PLAN_VIEW (top priority, as you'd expect)
1. Plan/Body/MODEL_VIEW (fallback)
1. Model/Body/PLAN_VIEW (fallback again)
1. Model/Body/MODEL_VIEW (final fallback)

Same goes for Annotations — just replace **Body** with **Annotation**.

## Example: SECTION_VIEW
Here’s another example for a section (i.e. **SECTION_VIEW**):

1. Model/Body/SECTION_VIEW (top priority)
1. Model/Body/MODEL_VIEW (final fallback)

Notice we never consider 2D things in a section view.  
There are a number of problems with 2D in sections and elevations that has led to this special third rule.


## A Few Example Contexts
| ContextType | ContextIdentifier | TargetView | Example |
| --- | --- | --- | --- |
| Model | Body | MODEL_VIEW | Full 3D shape of an object - the 3D geometry of a door or window |
| Plan | Axis | GRAPH_VIEW | An axis of a wall or beam |
| Model | Axis | GRAPH_VIEW | The axis of a column or member |
| Model | Box | MODEL_VIEW | The overall bounding box of the 3D geometry |
| Model | Annotation | SECTION_VIEW | An up/down arrow on how window sashes work |
| Model | Annotation | ELEVATION_VIEW | A door swing indicator in elevation |
| Model | Annotation | MODEL_VIEW | Text or symbols in an Orthographic view |
| Model | Profile | ELEVATION_VIEW | Can use a profile, instead a void, to create a void for door or window for example |
| Plan | Annotation | PLAN_VIEW | Text or symbols on a floor plan |
| Model | Annotation | PLAN_VIEW | ? |
| Plan | Annotation | REFLECTED_PLAN_VIEW | Text or symbols on a reflected ceiling plan |
| Plan | Body | PLAN_VIEW | An door swing (arc) in plan |
| Model | Body | PLAN_VIEW | 3D objects you only want to see in plan view |
