---
name: 4AdvancedOperations
project: pladipus
layout: default
permalink: /projects/pladipus/wiki/4advancedoperations.html
github_project: https://github.com/compomics/pladipus
---

# Advanced Operations

There are a lot of features readily built in Pladipus to make it a secure environment for a wide variety of tasks. This chapter handles the more advanced features in detail.

----

## The Admin Console

An admin console is available to users with the admin privilege. This option become available at the Edit -> Admin Settings menu item.

![alt text](https://github.com/compomics/pladipus/wiki/Administration_Console.png)

----

## Creating a custom template 

* It is possible create your own template file outside of the Run Creation dialog. Please ensure the template file has the following layout : 

```xml
<template run='Example' user='pladmin' priority='4'>
 	<steps>
  	</steps> 
 	<parameters>
 		<run>
 		</run>
   		<job>
 		</job>
 	</parameters>
 </template> 
```

----

## Chaining jobs

In some cases it is mandatory that jobs are executed sequentially. As of version 1.1.0 this is possible by either : 

* adding a "chain" flag in the template
```
<template run='Pladipus_demo' user='pladmin' priority='4' chain='true'>
```
* enabling the "retain job order" checkbox in the run creation GUI

 ![alt text](https://github.com/compomics/pladipus/wiki/Chain_Jobs.png)

----

## Using other software on the Pladipus network

The main idea behind Pladipus is to provide a simple platform to run a broad range of tasks, including custom in house algorithms and software. Setting up such a run happens as follows : 

* Write a wrapper in java for your tool. This can easily be done by extending the `com.compomics.pladipus.core.model.processing.ProcessingStep` class. An example can be found in the [Blast module](https://github.com/compomics/pladipus/blob/master/Pladipus-blast/src/main/java/com/compomics/pladipus/blast/BlastStep.java)

* Place the wrapper jar, including the required dependencies, in the `$USER_HOME/.compomics/pladipus/external` folder. 

* Append the following line to the `$USER_HOME/pladipus/config/processing-beans.xml` , but replace "MyCustomClass" by your new classes name and "my.custom.MyCustomClass" with the fully defined classpath: 

 `<bean id="MyCustomClass" class="my.custom.MyCustomClass" lazy-init="true"/>`

<b> Important Note 1</b>: The changes need to be applied to all pladipus instances on the network. The new step can then be used in runs and jobs.

<b> Important Note 2</b>: The parameters that are used in your custom class can be used by requesting them in the parameters HashMap in the processing step object. The values will be return as a string and will be loaded from the run template and job configuration file.



