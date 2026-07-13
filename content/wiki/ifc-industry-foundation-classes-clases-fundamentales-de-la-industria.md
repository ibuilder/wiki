---
title: "IFC (Industry Foundation Classes - Clases fundamentales de la industria)"
url: "/ifc-industry-foundation-classes-clases-fundamentales-de-la-industria/"
aliases: ["/IFC_(Industry_Foundation_Classes_-_Clases_fundamentales_de_la_industria)/"]
categories: ["File formats", "Industry Foundation Classes (IFC)"]
lastmod: "2021-04-13T15:46:31Z"
---

{{< wiki-image src="/media/freecad-ifc-viewer.png" alt="Un archivo IFC siendo analizado en FreeCAD" mode="thumb" caption="Un archivo IFC siendo analizado en FreeCAD" align="right" >}}

El IFC (Industry Foundation Classes) es un esquema [Open Data](/aec-open-data-directory/) y un conjunto de formatos usados para almacenar datos [OpenBIM](/openbim/). Es desarrollado y mantenido por la [BuildingSMART International](/buildingsmart-international/). Los datos IFC pueden describir digitalmente muchos conceptos, entre ellos:

- Objetos físicos o entornos construídos (muros, losas, columnas, cañerías),
- Geometrías 2D y 3D que representan objetos,
- Un conjunto diverso de propiedades y atributos que abarcan muchos dominios,
- Atributos de materiales y colores,
- Planeamiento de proyecto, reubicación de recursos y cronogramas,
- Cuantificación de elementos,
- Roles y responsibilidades de organizaciones e individuos,
- Estrategias de diseño y restricciones legales,
- Modelos analíticos para análisis estructural, análisis de eficiencia energética y de iluminación.

La mayoría de los programas BIM pueden leer y escribir datos IFC. No obstante, la calidad de los datos varían significativamente dependiendo del software.
<div style="float: right; margin: 30px;">{{< youtube "https://www.youtube.com/watch?v=kMpzrUJY7LU" >}}</div>

## Versiones IFC
Actualmente hay dos versiones de IFC soportadas: IFC2x3 e IFC4. Esta última contiene nuevas características en comparación con la versión anterior: representación geométrica mejorada, soporte de geolocalización y más categorías de elementos. Sin embargo, el soporte de IFC4 es menos prominente que el IFC2x3, aunque esto está cambiando. IFC2x3 fue el estándar ISO desde el año 2005 al 2013, cuando lo reemplazó IFC4.

## Formatos IFC
Los datos IFC normalmente están incluídos en una archivo de texto plano, con la extensión <code>.ifc</code>. Un error común es considerar que el IFC es sólo un formato de archivo de intercambio: Se trata de un esquema de datos, y un archivo completo es sólo una de las muchas formas de transferir o almacenar datos OpenBIM. Es posible transferir tanto porciones de datos OpenBIM como modelos completos, usando una variedad de serializaciones. Otras serializaciones incluyen:

- <code>.ifc</code> Formato IFC-SPF: Basado en STEP, es un formato de texto plano comúnmente utilizado,
- <code>.ifczip</code> Formato IfcZIP, donde un simple archivo <code>.ifc</code> es comprimido a un paquete ZIP,
- <code>.ifcxml</code> Formato IfcXML, un formato de texto plano,
- <code>.json</code> Formato JSON, un formato de texto plano,
- <code>.hdf</code> Formato HDF5, un formato binario,
- <code>.sqlite</code> Formato SQLite, un formato binario.

Los formatos más utilizados frecuentemente son <code>.ifc</code> y <code>.ifczip</code>.

## Clases IFC
En IFC, un concepto básico es la *clase IFC*. Hay cientos de clases IFC, algunos ejemplos son <code>IfcWall</code>, <code>IfcBuilding</code> y <code>IfcTask</code>. Las clases pueden tener atributos. Por ejemplo, un objeto <code>IfcWall</code> puede tener un atributo <code>Name</code>.
Las clases también pueden relacionarse con otras clases. Por ejemplo, un objeto <code>IfcWall</code> puede estar relacionado a un objeto <code>IfcBuilding</code>, por estar espacialmente contenido dentro del <code>IfcBuilding</code>.

{{< wiki-image src="/media/ifc-wall.png" alt="Un ejemplo de jerarqúa de clases IFC" mode="thumb" caption="Un ejemplo de jerarqúa de clases IFC" align="right" >}}

Algunas clases pueden desprenderse de otras clases, construyendo una jerarquía de clases. Si una clase pertenece a otra clase, "hereda" todos sus atributos y relaciones. Por ejemplo, la clase <code>IfcProduct</code> posee un atributo <code>Representation</code>, y éste puede almacenar geometrías 3D que representen a esa clase. A partir de ésto, la clase <code>IfcWall</code> posee también el atributo <code>Representation</code> para almacenar geometría 3D, ya que esta clase también se "desprende" de la clase <code>IfcProduct</code>. Sin embargo, la clase <code>IfcPerson</code> *no* se desprende de la clase <code>IfcProduct</code>, por lo que *no* posee un atributo <code>Representation</code>.

Revisa el artículo específico a las [Clases IFC](/ifc-industry-foundation-classes-ifc-classes/)

## Mira también
- El artículo [Categoría: Autodesk Revit](/categories/autodesk-revit/) para ver cómo aplicar IFC en [Autodesk Revit](/autodesk-revit/)
- El artículo [Categoría: Graphisoft_Archicad](/categories/graphisoft-archicad/) para ver cómo aplicar IFC en[ArchiCAD](/archicad/)

## Recursos externos
- La buildingSMART Denmark publicó una [Guía para exportar IFC desde Archicad y Revit](https://anvisninger.molio.dk/Gratis-vaerktojer/buildingSMART/IFC_Export_Guide_EN)
