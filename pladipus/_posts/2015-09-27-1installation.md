---
name: 1Installation
project: pladipus
layout: default
permalink: /pladipus/wiki/1installation.html
github_project: https://github.com/compomics/pladipus
---

# Installation Manual

* [Prerequisites](#prerequisites)
* [Installing Pladipus](#installing-pladipus)

The following sections can be used for advanced installation options that are not covered by the Pladipus installer.

* [Installing MySQL](#installing-mysql)
* [Installing ActiveMQ](#installing-activemq)

----

# Prerequisites


For Pladipus to run correctly, the following is needed : 

* [Java 8](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) must be installed
* Connection to a MySQL database with create privileges (not included in installer)
* Connection to an ActiveMQ host on an available post (optional in installer + automatic download)
* Either Pladipus Management or Executor modes 

----

# Installing Pladipus

Download the pladipus installer [here](http://genesis.ugent.be/pladipus/download/Pladipus-installer-0.3.4.jar) and follow the on screen messages. 

In the case of a headless installation, please download either the complete [Linux version](http://genesis.ugent.be/pladipus/download/pladipus-linux.zip) or [Windows version](http://genesis.ugent.be/pladipus/download/pladipus-windows.zip) and extract the folder contents in the user home directory.

For further details on how to correctly configure pladipus, please consult the [wiki](/pladipus/wiki/pladipus-configuration.html).

<b>Note:</b> The [demonstration video](Pladipus-Demo) shows how to install Pladipus using the installer.

## Settings

The configuration can be done using the installer. 
They can also be changed manually, for example when a headless install is required.
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

----

# Installing MySQL

This tutorial will demonstrate how to install MySQL on a Windows machine, but similar versions are also available for Linux.

----

### Using an installer

The MySQL database does offer an excellent installer. The wizard will guide you and create the my.ini configuration file and installs MySQL as a service. This option is the recommended solution for novice users. 

* Navigate to the [downloads](http://www.mysql.com/downloads/) page.
* Find the MySQL Community Edition
* Select the MySQL Community Server and continue to download the specific MySQL Installer for your system

<b><u>Note</u></b> : You do not have to create a login on the MySQL website ! There is a small link at the bottom of the page saying 'No thanks, just start my download.'

* Double click the .msi installer. If a previous version of MySQL was detected, it will automatically update
* During the installation, install or upgrade the MySQL server.

----

### Manual Installation

More advanced users may prefer a manual installation, as the user has more control over how and when MySQL runs.

* Navigate to the MySQL Community Server for your operating system from the [downloads](dev.mysql.com/downloads/) page
* Download the “Without installer” version.
* Extract the ZIP file to a destination of your choice and rename the unzipped folder to “mysql”.

<b><u>Note</u></b> : MySQL can be installed anywhere on your system. If you want a lightweight installation, you can remove every sub-folder except for bin, data, scripts and share.

----

### Configuration

* Locate or create the my.ini file in the mysql folder.
* Add or update the following statements: 

```
# The TCP/IP Port the MySQL Server will listen on
port=[insert the port, this is by default 3306]

# IP address to bind to.
bind-address=[0.0.0.0 OR the IP address of the MySQL server]
```

<b><u>Note</u></b> : Updating the bind-address is mandatory. It otherwise defaults to localhost, disallowing all access from outside the server.

----

### Starting the server

* Open a command line window and navigate to the bin folder inside the MySQL folder
* Launch the following command: 
 `C:\Program Files\MySQL\MySQL Server 5.0\bin\mysqld`

----

### Stopping the server 

* Open a command line window and navigate to the bin folder inside the MySQL folder
* Launch the following command: 
 `C:\Program Files\MySQL\MySQL Server 5.0\bin\mysqladmin" -u root shutdown`

----

# Installing ActiveMQ

It is highly recommended to use the Pladipus [installer](http://genesis.ugent.be/pladipus/download/Pladipus-installer-0.3.0.jar) or zipped archives for [Windows](http://genesis.ugent.be/pladipus/download/pladipus-windows) or [Linux](http://genesis.ugent.be/pladipus/download/pladipus-linux) to install ActiveMQ. The configuration will automatically be updated doing so. 
On a fresh, manual install, all changes made to this configuration have to be reflected in the [Pladipus Settings](/pladipus/wiki/pladipus-configuration.html) as well. For more advanced configuration parameters, please consult the [ActiveMQ website](http://activemq.apache.org/).

### Manually changing default activeMQ settings

* Locate the configuration file in the 'conf' folder of ActiveMQ. This can be found at `$USER_HOME/.compomics/pladipus/activeMQ/apache-activemq-5.11.1/conf/activemq.xml`when using one of the Pladipus installation options

<font color="red">Do only edit these parameters in case the ports are already in use!!!</font>

### Changing the ActiveMQ port for queues

* Locate the following XML-entry in the config file:

```xml
<transportConnectors>
	<transportConnector name="openwire" uri="tcp://localhost:3389?jms.prefetchPolicy.queuePrefetch=1"/>
</transportConnectors>
```

* replace **3389** with the new, available and open port of your choice 

### Changing the ActiveMQ port for the jmx management console

* Locate the following XML-entry in the config file:

```xml
<managementContext>
	<managementContext connectorPort="1099" createConnector="true"/>
</managementContext> 
```

* Replace **1099** with the new, available and open port of your choice 

----

