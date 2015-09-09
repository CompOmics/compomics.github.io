---
name: Examplejobconfiguration
project: pladipus
layout: default
permalink: /pladipus/wiki/examplejobconfiguration.html
github_project: https://github.com/compomics/pladipus
---

#Example configuration
----

###Example template

The following is an example template for a denovoGUI run. Note that:

* The location of the jar is a parameter that doesn't change, hence it is a run parameter (fixed)
* Input, parameter and output are all declared per task, they are job parameters (variable)

```xml
<template run='Example_DenovoGUI' user='pladmin' priority='4'>
	<steps>
		<step class="com.compomics.pladipus.denovo.processsteps.DenovoGUISetupStep"/>
		<step class="com.compomics.pladipus.denovo.processsteps.DenovoGUIStep"/> 
	</steps> 
	<parameters>
		<run>
			<param name='DenovoGUI' value='/home/compomics/.compomics/pladipus/tools/DenovoGUI-1.7.0/DenovoGUI-1.7.0.jar'/>
		</run>
		<job>
			<param name='input' default='default'/>
			<param name='parameterFile' default='default'/>
			<param name='outputFolder' default='default'/>
		</job>
	</parameters>
</template>
```

----
###Example job config
This is what the corresponding TSV file could look like. Note that:

* Every job parameter is represented in a column in a file. Pladipus will not accept files with missing or additional parameters, except when these are declared in the provided template
* Every line is internally translated to a job. In this example, there will be n jobs generated for the 'Example_DenovoGUI' run

Example:

input | parameterFile | outputFolder
----- | ------------- | ------------
/mnt/pladipus/data/test_1.mgf | /mnt/pladipus/data/test_1.par | /mnt/pladipus/output/result_1/
/mnt/pladipus/data/test_2.mgf | /mnt/pladipus/data/test_2.par | /mnt/pladipus/output/result_2/
/mnt/pladipus/data/test_3.mgf | /mnt/pladipus/data/test_3.par | /mnt/pladipus/output/result_3/
... | ... | ...
/mnt/pladipus/data/test_n.mgf | /mnt/pladipus/data/test_n.par | /mnt/pladipus/output/result_n/