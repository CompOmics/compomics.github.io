---
name: PladipusDemo
project: pladipus
layout: default
permalink: /pladipus/wiki/pladipusdemo.html
github_project: https://github.com/compomics/pladipus
---

# Video tutorial

<a href="https://www.youtube.com/watch?v=ZQff2Yqhgrk" target="_blank"><img src="http://img.youtube.com/vi/ZQff2Yqhgrk/0.jpg" 
alt="Pladipus video tutorial" width="240" height="180" border="10" /></a>

[Click here for the video](https://www.youtube.com/watch?v=ZQff2Yqhgrk)

----

## Installing the framework

Installing Pladipus can be easily done by running the pladipus installer [here](http://genesis.ugent.be/pladipus/download/Pladipus-installer-0.3.0.jar) and follow the on screen messages. 

In the case of a headless installation : 

* Download the correct version for your operating system : 

[Linux](http://genesis.ugent.be/pladipus/download/pladipus-linux) | [Windows](http://genesis.ugent.be/pladipus/download/pladipus-windows) 

* Extract the folder contents in the user home directory (for example : `C:\Users\Kenneth` for Windows or `/home/Kenneth` for Linux)

For further details on how to correctly configure pladipus, please consult the [wiki](/pladipus/wiki/settings.html) and the [troubleshooting page](/pladipus/wiki/troubleshooting.html). For further questions, feel free to  [contact the developers](mailto:kenneth.verheggen@ugent.be)

Please consult the manual on how to install and setup a pladipus network.

----

## Running a Pladipus network

* Start the activeMQ server by double clicking the executable file that was created on your desktop during the installation. Alternatively, you can run the following command : 

`java -jar $USER_HOME/.compomics/pladipus/activeMQ/apache-activemq-5.11.1/bin/activemq.jar start`

* Verify that the mySQL server is running

* Launch one or more Pladipus executing instances on the machines that will connect to the Pladipus network. This is done by running the following command on those machines. 

`java -jar $USER_HOME/.compomics/pladipus/Pladipus-execution-0.3.0/Pladipus-execution-0.3.0.jar -auto_pull -u [pladipus_user] -p [pladipus_password]`

----

## Pladipus Demo

* A preconfigured setup is available online. In order to launch the run, please download the following files : 

- [Example template file](http://genesis.ugent.be/pladipus/examples/sequence_database_search/configuration/example_template.xml)

- [Example job configuration file](http://genesis.ugent.be/pladipus/examples/sequence_database_search/configuration/example_configuration.tsv)

<b><u>Note</u></b>: The example configuration will work out of the box, but the output folder needs to be specified to a <b> location that is accessible by all pladipus executors in the Example Template File</b>. This can be a location local to the executors, a network folder or a shared drive. The "outputFolder" parameter will direct to the data repository for the results, in the case of the tutorial this ment that all workers had a central repository at `/mnt/pladipus/Pladipus/GENESIS_OUTPUT` .

* Launch the Pladipus management console by double clicking the generated shortcut on the desktop or by executing the following command

`java -jar $USER_HOME/.compomics/pladipus/Pladipus-execution-0.3.0/Pladipus-execution-0.3.0.jar` 

* Log in using the credentials provided by the Pladipus administrator or that was created during the installation

![alt text](https://github.com/compomics/pladipus/wiki/Pladipus_login.png)

* In the main GUI, go to File -> Import Run...

![alt text](https://github.com/compomics/pladipus/wiki/Import_Run_GUI.png)

* Select the template and job configuration files that were downloaded earlier. You can adjust the slider to specify the priority of this run. Click "create" to continue.

![alt text](https://github.com/compomics/pladipus/wiki/Import_Run_GUI_files.png)

* Select the run that has now appeared in the upper section. All the tasks related to this RUN will be loaded.

![alt text](https://github.com/compomics/pladipus/wiki/Run_Selection_GUI.png)

* Right click the selected run. A pop-up menu shows up. Select "Start" to push the tasks onto the queue.

![alt text](https://github.com/compomics/pladipus/wiki/Run_Start.png)

* The jobs should now automatically be distributed to the connected workers. When all tasks are completed, an automatically generated e-mail will be delivered to the user's specified e-mail address.

![alt text](https://github.com/compomics/pladipus/wiki/Run_End.png)


----