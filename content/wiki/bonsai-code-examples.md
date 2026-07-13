---
title: "Bonsai code examples"
url: "/bonsai-code-examples/"
aliases: ["/BlenderBIM_Add-on/BlenderBIM_Add-on_code_examples/", "/BlenderBIM_Add-on_code_examples/", "/blenderbim-add-on-blenderbim-add-on-code-examples/"]
categories: ["Blender", "Bonsai"]
lastmod: "2022-07-27T14:01:47Z"
---

## Run a script in blender from command line
Blender can run any Python script headlessly. This allows for a lot of automation, which may run on a scheduled time. On Linux or Mac, you can combine this with cron, or use scheduled tasks on Windows. For example, to run the script <code>script.py</code>, just execute:


```bash
blender -b -P script.py
```


## Import an IFC

```python
bpy.ops.import_ifc.bim(filepath='/path/to/your/file.ifc')
```


## Export an IFC

```python
bpy.ops.export_ifc.bim(filepath='/path/to/your/file.ifc')
```


You can also bypass the operator to import or export yourself. This gives you granularity to instantiate the IFC import classes, export classes, quantity calculator class, logging class, settings, and so on. This is useful if you are writing your own script and would like to customise how the import or export works. You are also able to overload the definition of these classes to provide even more control.

To import an IFC:


```python
import bpy
import logging
import bonsai.bim.import_ifc
ifc_import_settings = bonsai.bim.import_ifc.IfcImportSettings.factory(bpy.context, '/home/dion/testa.ifc', logging.getLogger('ImportIFC'))
ifc_importer = bonsai.bim.import_ifc.IfcImporter(ifc_import_settings)
ifc_importer.execute()
```


To export an IFC:


```python
import bpy
import logging
import bonsai.bim.export_ifc
import bonsai.bim.qto
settings = bonsai.bim.export_ifc.IfcExportSettings.factory(bpy.context, '/home/dion/testa.ifc', logging.getLogger('ExportIFC'))
qto_calculator = bonsai.bim.qto.QtoCalculator()
ifc_parser = bonsai.bim.export_ifc.IfcParser(settings, qto_calculator)
ifc_exporter = bonsai.bim.export_ifc.IfcExporter(settings, ifc_parser)
ifc_exporter.export(bpy.context.selected_objects)
```


## Access IFC objects
Access multiple objects of specific criteria.
## Access Elements

```python
import bpy

walls = [obj for obj in bpy.context.scene.objects if obj.name.startswith("IfcWall")]
voids = [obj for obj in bpy.context.scene.objects if obj.name.startswith("IfcBuildingElementProxy/ProvisionForVoid")]
```


## Read object IFC data
Examples affect active object only.

## Element IFC Guid / GlobalId

```python
import bpy
from bonsai.bim.ifc import IfcStore

obj = bpy.context.active_object
IfcStore.get_file().by_id(obj.BIMObjectProperties.ifc_definition_id).GlobalId
```


## Element Storey

```python
import bpy

users_collections = bpy.context.active_object.users_collection
obj_storey = next(iter([coll for coll in users_collections if "IfcBuildingStorey" in coll.name]))
```


## Manipulate object IFC data
Examples affect active object only.
## PropertySet (Pset)

```python
import bpy
# Adding a Pset
pset = bpy.context.active_object.BIMObjectProperties.psets.add()
pset.name = "MyPset"
# Adding a property of type string_value
prop = pset.properties.add()
prop.name = "MyProperty"
prop.string_value = "Hello World !"
```

[Available value types](https://docs.blender.org/api/blender_python_api_current/bpy.props.html)
## QuantityTakeOff (Qto)

```python
import bpy
# Adding a Qto
qto = bpy.context.active_object.BIMObjectProperties.qtos.add()
qto.name = "MyQto"
# Adding a property of type string_value
prop = qto.properties.add()
prop.name = "MyQuantity"
prop.string_value = "10"
```

## Manipulate material IFC data
## PropertySet (Pset)

```python
import bpy
# Adding a Pset
pset = bpy.context.object.active_material.BIMMaterialProperties.psets.add()
pset.name = "MyPset"
# Adding a property of type string_value
prop = pset.properties.add()
prop.name = "MyProperty"
prop.string_value = "Hello World !"
```


## Clash Detection
## Clash Detection on 2 sets of elements
Clash Detection on 3 cubes in two sets in this example:

```python
import bpy
import collision
import numpy as np
import bmesh
import ifcclash


def get_collision_results(set_a=None, set_b=None):
    a_cm = collision.CollisionManager()
    b_cm = collision.CollisionManager()
    add_to_cm(a_cm, set_a)
    add_to_cm(b_cm, set_b)
    return a_cm.in_collision_other(b_cm, return_data=True)


def add_to_cm(cm, object_names):
    for object_name in object_names:
        name = object_name.name
        obj = bpy.data.objects[name]
        triangulated_mesh = triangulate_mesh(obj)
        mat = np.array(obj.matrix_world)
        mesh = ifcclash.Mesh()
        mesh.vertices = np.array([tuple(v.co) for v in triangulated_mesh.vertices])
        mesh.faces = np.array([tuple(p.vertices) for p in triangulated_mesh.polygons])
        cm.add_object(name, mesh, mat)


def triangulate_mesh(obj):
    mesh = obj.evaluated_get(bpy.context.evaluated_depsgraph_get()).to_mesh()
    bm = bmesh.new()
    bm.from_mesh(mesh)
    bmesh.ops.triangulate(bm, faces=bm.faces)
    bm.to_mesh(mesh)
    bm.free()
    del bm
    return mesh


set_a = [
    bpy.data.scenes['Scene'].objects['Cube'],
]
set_b = [
    bpy.data.scenes['Scene'].objects['Cube.001'],
    bpy.data.scenes['Scene'].objects['Cube.002'],
]


err, results = get_collision_results(set_a=set_a, set_b=set_b)

seen_pairs = set()
for result in results:
    result_pair = result.names
    result_names_str = str(result_pair)
    if result_names_str in seen_pairs:
        continue
    seen_pairs.add(str(result_pair))
    print(35 * "-")
    print(result_names_str)
```
