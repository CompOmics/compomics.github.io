---
name: 72Custommodules
project: pladipus
layout: default
permalink: /pladipus/wiki/72custommodules.html
github_project: https://github.com/compomics/pladipus
---

# Custom modules

Pladipus is designed to be as versatile as possible. In order to achieve this, it is possible to write custom JAVA wrappers and include them in the processing. Here we will go over the process of adding a new module from scratch.

----

## Creating a new step

Setting up a Processing step is as easy as just extending the ProcessingStep abstract class. It is possible to use parameters directly from the parametermap. We just need to provide these one way or another, either by setting the parameter map through the API or by including it in a template.xml / config.tsv setup.

```
import com.compomics.pladipus.core.model.exception.PladipusProcessingException;
import com.compomics.pladipus.core.model.processing.ProcessingStep;

public class SweetCountdownStep extends ProcessingStep {

    @Override
    public boolean doAction() throws PladipusProcessingException {
        int countDownSize = Integer.parseInt(parameters.get("countDownSize"));
        System.out.println(getDescription());
        for (int i = 0; i <= 10; i++) {
            System.out.println(i);
        }
        return true;
    }

    @Override
    public String getDescription() {
        return "Executing some really fancy countdown code !";
    }
}
```

----

## Preparing the step to run on pladipus

This will work out of the box when using the API. However, to be able to run the new step on the pladipus GRID, it is mandatory to execute two more steps. It is imperative that you make these changes all workers and controllers. This can be done for example through a batch script that updates the workers/controllers. Alternatively, there is the option to broadcast the definition of new steps, but this is a feature under development. 

### 1. Adding the step into the bean definition configuration

Locate the processing-beans.xml file. It is by default placed in the config folder in the pladipus home folder.
Then, add the following entry, but replace "com.compomics.pladipus." with your specific fully classified package name:

```
    <bean id="SweetCountdownStep" class="com.compomics.pladipus.SweetCountdownStep" lazy-init="true"/> 
```

### 2. Adding the step into the bean definition configuration

Create a jar file containing your new class(es). Locate the app.classpath folder as specified in the network.properties file. This file is in the config folder of the pladipus home folder. By default, the app.classpath folder is defined as the "external" folder in the pladipus home folder. Make sure your new jar file is placed here on both controllers and workers, so they have access to this code.

### 3. Using the step into the bean definition configuration

It is now possible to use the new class through the usual template.xml format, for example : 

```xml
<template run='Example' user='pladmin' priority='4'>
 	<steps>
              <step>com.compomics.pladipus.SweetCountdownStep</step>
  	</steps> 
 	<parameters>
 		<run>
 		</run>
   		<job>
                    <param name ='countDownSize' default='10' descr='The size of the countdown'/>
 		</job>
 	</parameters>
 </template> 
```

Note that the "countDownSize" parameter will be set to 10. To override this, edit the job_config.tsv file that needs to be created in order to launch new jobs with this step


