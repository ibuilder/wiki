---
title: "Ifccityjson"
url: "/ifccityjson/"
aliases: ["/Ifccityjson/"]
categories: []
lastmod: "2021-11-02T14:08:30Z"
---

## Installation
Install dependencies: CJIO & IfcOpenShell-python

IfcCityJSON is a python library that is based on two libraries: IfcOpenShell (for IFC manipulation) and CJIO (for CityJSON manipulation). These need to be installed first. CJIO (python 3.6+ only) is installed with:


```
python -m pip install cjio
```


The IfcOpenShell-python library is needed (with API included). Unfortunately, the API is not yet shipped with the releases on [www.ifcopenshell.org/python](http://www.ifcopenshell.org/python), but [this IfcOpenShell commit](https://github.com/IfcOpenBot/IfcOpenShell/commit/93c5906ad7f363fd1b1d9e49eb28d10212ce9173#comments) has the API included. Copy this folder to your python site-packages folder, that is found under your python folder/Lib (for example: 'C:/Users/user/AppData/Local/Programs/Python/Python39/Lib/site-packages').

## Usage
Now both packages are installed, IfcCityJSON is ready to be used. Download the repo https://github.com/IfcOpenShell/IfcOpenShell and navigate to src/ifccityjson. Open your command prompt in this directory. The following command will execute a conversion from CityJSON to IFC.

```
python ifccityjson.py [-i input file] [-o output file] [-n name of identification attribute]
```

So, for example, you would like to convert the file C:/Users/user/Documents/3DBAG.json, where the naming attribute is 'identificatie' this is possible with the following command:

```
python ifccityjson.py -i C:/Users/user/Documents/3DBAG.json -o C:/Users/user/Documents/3DBAG.ifc -n identificatie
```


This will provide an IFC file 3DBAG.ifc that can be opened with your favourite IFC viewer!
