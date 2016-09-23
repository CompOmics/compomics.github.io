---
name: 73PladipusMsConvert
project: pladipus
layout: default
permalink: /pladipus/wiki/73pladipusmsconvert.html
github_project: https://github.com/compomics/pladipus
---

# Pladipus-MsConvert

Pladipus-MsConvert is a module to facilitate the conversion of RAW files to other formats. Currently, this step is exclusive to the Windows operating systems.

----

Note that the discussed parameters are the ones mandatory for pladipus execution. For more detailed parameters, please refer to the respective pages.

* [MsConvert](http://proteowizard.sourceforge.net/tools/msconvert.html)

----

## 1. MsConvertSetupStep

This step preprocesses the input data in order to prepare the worker to convert a RAW file into another spectrum format.

The following parameters are required: 

Parameter | Meaning
--- | -------------- | 
f | input file (.raw) 
o | output folder

## 2. MsConvertStep

This step manages the execution of MsConvert's command line. It requires the following parameters (next to the ones specified by the MsConvert command line).

Parameter | Meaning
--- | -------------- | 
f | input file (.raw) 
o | output folder
pwiz_folder | the ProteoWizard folder (selected at installation)
-filter | the optional filters for the conversion


