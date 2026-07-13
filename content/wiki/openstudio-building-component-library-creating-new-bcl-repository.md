---
title: "Creating New BCL Repository"
url: "/openstudio-building-component-library-creating-new-bcl-repository/"
aliases: ["/OpenStudio/Building_Component_Library/Creating_New_BCL_Repository/"]
categories: ["Building Component Library"]
lastmod: "2025-04-29T01:20:27Z"
---

In order to publish measures to the Building Component Library it is necessary to format the measure files and folders in a particular format. This NREL BCL page titled *[Contribute Data](https://bcl.nrel.gov/contribute#step1)* ideally should provide guidance for the following instructions. It suggests creating a [new extension gem](https://github.com/NREL/openstudio-extension-gem#initializing-a-new-extension-gem), although the rake task [bundle exec rake init_new_gem] is outdated.

According to this [UnmetHours post](https://unmethours.com/question/99607/current-best-practice-for-creating-new-bcl-measure-repo/), the folders must be organized as such:

  openstudio-measure-repo/  
  ├── README.md  
  ├── LICENSE  
  └── lib/  
      └── measures/  
          ├── measure1/  
          │   ├── measure.rb  
          │   ├── measure.xml  
          │   ├── resources/  
          │   │   └── helper.rb  
          │   └── test/  
          │       └── measure1_test.rb  
          └── measure2/  
              ├── measure.rb  
              ├── measure.xml  
              ├── resources/  
              │   └── helper.rb  
              └── test/  
                  └── measure2_test.rb
