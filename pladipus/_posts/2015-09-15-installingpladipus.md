---
name: InstallingPladipus
project: pladipus
layout: default
permalink: /pladipus/wiki/installingpladipus.html
github_project: https://github.com/compomics/pladipus
---

## Installing Pladipus

----

## Prerequisites
For Pladipus to run correctly, the following is needed : 

* Connection to a MySQL database with create privileges (not included in installer)
* Connection to an ActiveMQ host on an available post (optional in installer + automatic download)
* Either Pladipus Management or Executor modes 

----

## Install

Download the pladipus installer [here](http://genesis.ugent.be/pladipus/download/Pladipus-installer-0.3.0.jar) and follow the on screen messages. 

In the case of a headless installation, please download either the complete [Linux version](http://genesis.ugent.be/pladipus/download/pladipus-linux) or [Windows version](http://genesis.ugent.be/pladipus/download/pladipus-windows) and extract the folder contents in the user home directory.

For further details on how to correctly configure pladipus, please consult the [wiki](/pladipus/wiki/pladipus-configuration.html).

<b>Note:</b> The [demonstration video](Pladipus-Demo) shows how to install Pladipus using the installer.

# Settings

The configuration can be done using the installer. 
They can also be changed manually, for example when a headless install is required.

## Pladipus settings

The configuration file can be found and edited at `$USER_HOME/.compomics/pladipus/config/network.properties`

**Database Settings**

Property | Definition | Default value
-------- | ---------- | -------------
db.host | The hostname or IP-adress of the mySQL server | localhost
db.port | The port that the mySQL-service is listening on | 3306
db.login | The account that can connect with both read and create rights to the mySQL database | root
db.pass | The password for the mySQL login (if any) | 

**ActiveMQ Settings**

Property | Definition | Default value
-------- | ---------- | -------------
AMQ.host | The hostname or IP-adress of the activeMQ server | localhost
AMQ.port.queue | The port that the activeMQ-service is listening on to withdraw jobs from the queue | 3389
AMQ.port.jmx | The port that is used to access the management console (don't change unless the default port is in use) | 1099
AMQ.version | The currently used activeMQ version | 5.11.1
AMQ.max.retry | The amount of times a job can be relaunched due to failure before being discarded by the system | 5

**Other Settings**

Property | Definition | Default value
-------- | ---------- | -------------
logging.level | The level output that will be displayed on the console | INFO
app.classpath | The folder where pladipus steps will be loaded from | $USER_HOME/.compomics/pladipus/external/


