---
title: "Shortcuts"
url: "/bonsai-shortcuts/"
parent: "/bonsai/"
aliases: ["/BlenderBIM_Add-on/Shortcuts/", "/blenderbim-add-on-shortcuts/"]
categories: []
lastmod: "2024-09-01T03:00:00Z"
---

#### Blender
- g -> grab (move) selected objects (press x,y,z to constraint to the axis)
- / -> isolate the view on currently selected object. Press again to return to normal view
- shift + rmb -> move the cursor
- Numpad 7 -> top view (z-normal plane)
- Numpad 1 -> side view (x-normal plane)
- Numpad 3 -> side view (y-normal plane)
- Numpad . -> center the zoom to selected objects
- ctrl + alt + q -> (quad view) split the 3D Viewport into four views: three orthographic side views and one user perspective view. Press again to return to normal.
- shift + tab -> toggle snap
- shift + s -> cursor snap menu
- h -> hide selected objects
- alt + h -> unhide objects
- ctrl + i -> invert selection
- t -> toggle the t-panel (the left panel in the viewport)
- n -> toggle the n-panel (the right panel in the viewport)
- F2 -> pop-up menu to rename the active object
- ctrl + F2 -> pop-up menu to batch rename multiple objects
- F3 -> [VIEWPORT] pop-up menu with access to all blender tool (simply start typing)
- F4 -> [VIEWPORT] pop-up menu with access to file context menu (save, open, etc ...)
- e -> [EDITMODE] extend. Useful for draw a line from the selected vertex
- ctrl + r -> [EDITMODE] loop cut and slide. Useful for add a vertex when modifying profiles
- tab -> toggle [EDITMODE] vs. [OBJECTMODE] modes
- ctrl + spacebar -> toggle [VIEWPORT] expands viewport to fullscreen, hiding other panels

#### Bonsai
- ctrl + s -> save file
- ctrl + o -> open file
- x -> delete selected objects
- tab -> change selected object profile
- shift + d -> duplicate selected objects
- shift + ctrl + d ->duplicate aggregate https://github.com/IfcOpenShell/IfcOpenShell/pull/3328
- shift + e -> pie menu containing Bonsai quick functions
- shift + g -> [TOOL] regenerate (redraw) the selected object
- ctrl + p -> [TOOL] aggregate selected objects to the active IfcElementAssembly object (similar to blender object parenting)
- alt + p -> [TOOL] remove an aggregate (no need to select parent here)
- shift + a -> [TOOL]  add the active construction type shown in the Type Manager
- shift + q -> [TOOL] calculate all quantities of all selected objects.
- shift + e -> [ANNOTATION TOOL] pop-up menu to edit text
