---
name: InstallingActiveMQ
project: pladipus
layout: default
permalink: /pladipus/wiki/installingactivemq.html
github_project: https://github.com/compomics/pladipus
---

## Installing ActiveMQ

It is highly recommended to use the Pladipus [installer](http://genesis.ugent.be/pladipus/download/Pladipus-installer-0.3.0.jar) or zipped archives for [Windows](http://genesis.ugent.be/pladipus/download/pladipus-windows) or [Linux](http://genesis.ugent.be/pladipus/download/pladipus-linux) to install ActiveMQ. The configuration will automatically be updated doing so. 
On a fresh, manual install, all changes made to this configuration have to be reflected in the [Pladipus Settings](/pladipus/wiki/pladipus-configuration.html) as well. For more advanced configuration parameters, please consult the [ActiveMQ website](http://activemq.apache.org/).

## Manually changing default activeMQ settings

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