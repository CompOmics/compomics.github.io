---
name: 213CreatingARun
project: pladipus
layout: default
permalink: /pladipus/wiki/213creatingarun.html
github_project: https://github.com/compomics/pladipus
---

### Run Creation

The user can create a run template by starting the Run Creation dialog. This window can be reached through the File menu or the + button next to the Run-window. A preview of the XML file is then displayed to the right. 

![alt text](https://github.com/compomics/pladipus/wiki/Run_Creation_GUI.png)

There are several options:

* The priority of a run can be set using the slider. This is especially useful to create background tasks.

* Several presets are included in the Pladipus build, making it easy to cobble together powerful processing pipelines.

![alt text](https://github.com/compomics/pladipus/wiki/Run_Creation_Window_presets.png)

* The default process step parameters are automatically loaded. More can be added, a useful feature for custom processes.

![alt text](https://github.com/compomics/pladipus/wiki/Run_Creation_Window_parameters.png)

* The checkbox in the Run column indicates whether the variable should be used across the entire run. For example: a FASTA file could be used for every job in the run, so it should be set as a **fixed** parameter, whereas the input file can be different for every search, turning it into a **variable** parameter


![alt text](https://github.com/compomics/pladipus/wiki/Run_Creation_Window_preferences.png)

* Machine preferences can be set for this run by clicking the "Preferences" tab at the top of the window. By selecting these prerequisites, the worker will first scan if it is capable of running the given job. If it is incapable, the job gets rolled back to the queue, not increasing the failcount.
These preferences include the operating system, architecture (32 or 64 bit), the amount of usable memory (RAM), the amount of processing cores for multi-threading  and the amount of available disk space.

Example: a search is requested using Andromeda, which is not available for Linux systems. Should a non-windows worker receive this job, it will detect that it is not able to fully run the job, passing it back to the controller

----

# Creating a run from Command Line

* After clicking "create" an XML file is generated for future use, along with an empty configuration file. The latter is a TSV file Every column represents a parameter, where each row will form a job. An example is available [here](/pladipus/wiki/example-configuration.html). It is of the greatest importance that the TSV file is correctly populated.

* A run can be imported as an existing template XML file, as long as these are complying to the standard schema. This schema is further specified in the [Advanced Operations](https://github.com/compomics/pladipus/wiki/3.-Advanced-Operations).

----