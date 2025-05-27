# Model of Bovine Respiratory Diseases for veal calves

This model is part of deliverable D2.3 of the DECIDE Project.

![CC-BY-NC-SA 4.0](https://img.shields.io/badge/license-CC_BY_NC_SA_4.0-8cd0c3.svg)

## Authors
- Stan Jourquin, Gent University
- Baptiste Sorin, INRAE, France

## Model description
This model is intended to adapt the latest BRD model (with co-infection, metaphylaxis and vaccination), initially developed for young beef cattle in France, to a different production system (veal calves) in a different country (Belgium). It was mainly developed by Stan Jourquin (UGent) and Baptiste Sorin (INRAE). The model accounts for the co-circulation of the BRSV and _Mannheimia haemolytica_ with a focus on vaccination-based prevention and on early detection of lung lesions based on lung ultrasound (which is considered a very promising early detection method and targeted treatment of pneumonia in calves). 

To simulate detection through lung ultrasound, the model implements the development of pneumonia for infected veal calves. Pneumonia and other clinical signs are increased in co-infected animals, as well as the mortality. The vaccine can be either monovalent (BRSV only) or divalent (BRSV + _M. haemolytica_) and reduces the infectious duration, the severity of clinical signs, and the transmission of pathogens to susceptible animals. In a next stage, vaccination could also be modelled to influence pneumonia as such, as there is some evidence that vaccination reduces the development of ultra-sound confirmed pneumonia in the later stages of production (week 10 after arrival), at which point it is associated with losses in average daily growth and cold carcass weight.

At this stage, two steps are still needed to improve the model: the calibration from available datasets, and the fine-tuning of the contact structure to better account for building structure in actual fattening facilities.

This model will also be adapted in the coming months for the French veal calves’ facilities by IDELE.
