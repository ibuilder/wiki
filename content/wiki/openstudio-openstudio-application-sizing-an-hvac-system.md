---
title: "Sizing an HVAC System"
url: "/openstudio-openstudio-application-sizing-an-hvac-system/"
aliases: ["/OpenStudio/OpenStudio_Application/Sizing_an_HVAC_System/"]
categories: ["OpenStudio Application"]
lastmod: "2025-04-23T15:37:51Z"
---

## HVAC Sizing Summary versus Estimated Cooling Peak Load
HVAC Sizing Summary (and other sizing outputs) are the answers resulting from the full heat balance sizing calculations and user sizing inputs. Use these results to calculate cooling capacity inside a building[^1].

The *Estimated* Cooling Peak Load Components are just that - a side calculation that gives estimates of the various instant and delayed heat gain components that contribute to the peak load. This separation of the various heat flows back to the original sources is not perfect and is useful only to see the relative contributions of the various load components.

## Example
The following results show the discrepancy between the *HVAC Sizing Summary* and the *Estimated Cooling Peak Loads Components* reports.

{{< wiki-image src="/media/os-application-hvac-sizing-summary.jpg" alt="OSApplication HVAC Sizing Summary.jpg" mode="inline" width="1000" >}}

As you can see the sensible cooling load for the zone is 19.47 kW.

{{< wiki-image src="/media/os-application-estimated-cooling-peak-load-components-report.jpg" alt="OSApplication Estimated Cooling Peak Load Components report.jpg" mode="inline" >}}

From the cooling load breadown, the total sensible cooling load is 17.8 kW and the latent cooling load is 1.87. The sensible cooling load is quire different with the HVAC Sizing Summary.

## Notes


[^1]: “Unmet Hours.” Unmethours.com, 2018, unmethours.com/question/34465/sizing-hvac-cooling-capacity/. Accessed 23 Apr. 2025.
