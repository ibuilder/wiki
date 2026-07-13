---
title: "Create your first Blender add-on:Panel"
url: "/create-your-first-blender-add-on-panel/"
aliases: ["/Create_your_first_Blender_add-on:Panel/"]
categories: []
lastmod: "2021-10-24T07:33:13Z"
---

This thread is to talk about a basic UI components - Panel.
Offical Document about Panel
https://docs.blender.org/api/current/bpy.types.Panel.html

First, lets see a simple example of building a Panel.

<pre>
import bpy
class ADDONNAME_PT_hello_world_panel(bpy.types.Panel):
    &quot;here is for description&quot;
    bl_idname = &quot;ADDONNAME_PT_hello_world&quot;
    bl_label = &quot;Hello World&quot;
    bl_space_type = &quot;PROPERTIES&quot;
    bl_region_type = &quot;WINDOW&quot;
    bl_context = &quot;object&quot;
    bl_options = {&quot;DEFAULT_CLOSED&quot;}
    def draw(self, context):
        self.layout.label(text=&quot;Hello World Text&quot;)

bpy.utils.register_class(ADDONNAME_PT_hello_world_panel)
</pre>

Line by line explanation.
<pre>import bpy</pre>
bpy is a module in Blender for creator to access the information/module inside.

<pre>ADDONNAME_PT_hello_world_panel:</pre>
This line is for setting up a Panel class.

**class** - Telling python interpreter a class object is being created

**ADDONNAME_PT_hello_world_panel** - The name of the class. In a python coding situation using **class ADDONNAME_PT_hello_world_panel:** is good enough to create a class. However, for coding in Blender, please follow the naming conversion in here. https://darkfallblender.blogspot.com/2020/07/blender-python-tutorial-class-naming.html

**(bpy.types.Panel)** - For creating a Blender Panel, we need to add this so Blender know it is a Panel object

**"here is for description"** - Normal users can't see this description with mouse hovering on the panel but it helps other creators to understand what this panel do.

**bl_idname = "OBJECT_PT_hello_world"** - custom ID of the panel. It will use the class name if not set.

**bl_label = "Hello World"** - The label of the Panel [Ref:https://i.imgur.com/4skGftj.png]

**bl_space_type = "PROPERTIES"** - This line indicate the Panel will be place inside the space of "PROPERTIES". Space type can refer to official document <https://docs.blender.org/api/current/bpy.types.Panel.html#bpy.types.Panel.bl_space_type> or here <https://i.imgur.com/40bt2d6.jpg>

**bl_region_type = "WINDOW"** - There are different regions under different spaces. However, there is no clear chart indicating the relation. For "PROPERTIES" space, "WINDOW" is the main region of it [ref: https://i.imgur.com/59XAFcu.png]

**bl_context = "object"** - It means the panel will be placed inside object properties. For other tabs, please refer to this [ref: https://i.imgur.com/S5L3c8F.png]

**bl_options = {"DEFAULT_CLOSED"}** - The official document is clearly explained [ref:https://docs.blender.org/api/current/bpy.types.Panel.html#bpy.types.Panel.bl_options]
The only thing that need to aware of is the options need to be wrapped in {}

<pre>
def draw(self, context):
    self.layout.label(text=&quot;Hello World Text&quot;)</pre>
Blender will look into the created panel class and search for some designated function names. 

**def** - This is how python define a function

**draw(self, context):** - This is the function name to let Blender know the following lines are for drawing UI elements. 

**self.layout** - self can be consider as the current class. layout is the function to start drawing the UI [ref: https://docs.blender.org/api/current/bpy.types.Panel.html#bpy.types.Panel.layout]

**.label** - an UI elements

**(text="Hello World Text")** - this is for defining the detail of the label element [ref: https://docs.blender.org/api/current/bpy.types.UILayout.html#bpy.types.UILayout.label]

<pre>bpy.utils.register_class(ADDONNAME_PT_hello_world_panel)</pre>

**bpy.utils.register_class** - This line is the reason why the library need to be imported at the beginning. It goes into the **bpy** module, then inside the **utils** there is a function **register_class()** to register the objects.

**(ADDONNAME_PT_hello_world_panel)** - inside the () is the name of the panel class so **register_class** function will register the panel into Blender
