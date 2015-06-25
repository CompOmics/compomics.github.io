---
name: Modulesconfiguration
project: colims
layout: default
permalink: /colims/wiki/modulesconfiguration.html
github_project: https://github.com/compomics/colims
---

# Modules Configuration



  * [Introduction](#introduction)

  * [Client module](#client-module)

  * [Storage queueing module](#storage-queueing-module)

  * [Distributed module](#distributed-module)



## Introduction



Colims x.y.z can be downloaded from the [Downloads](/colims/#downloads.html) section on the home page. The zipped archive contains 3 folders:



  * `colims-client-x.y.z`: the graphical user interface module

  * `apache-activemq-5.9.0`: the storage queueing module

  * `colims-distributed-x.y.z`: the storage engine module



----



## Client module



The client module contains the graphical user interface (GUI). A user can run it on his local machine to

 

  * manage metadata of projects, experiments, samples, runs, users, instruments, materials, protocols...

  * send analytical run storage tasks to the storage queueing module

  * monitor the storage queueing module   



Multiple clients can be active simultaneously.  



### Configuration



Before running the colims client module for the first time, some database related properties - located in the `colims-client.properties` file in the *config* folder - need to be modified if necessary.



```

db.default_schema = colims

db.url = jdbc:mysql://localhost:3306/colims

db.driver = com.mysql.jdbc.Driver

db.dialect = org.hibernate.dialect.MySQL5Dialect

db.username = root

```



Change these property values according to your database settings. The client module will use these values to establish a database connection.



The client module needs to connect to the storage queueing module as well. Following properties located in the same properties file hold the ActiveMQ connection parameters:



```

distributed.connectionfactory.broker.url = tcp://localhost:61616

distributed.jmx.service.url = service:jmx:rmi:///jndi/rmi://localhost:1099/jmxrmi

```



Adjust these URLs if necessary.



### Running



Run the colims client by double clicking the *.jar* file in the *colims-client-x.y.z* folder. First, the client module needs to connect to the database. The default database url and username values are retrieved from the `colims-client.properties` file, while the database password is not stored for security reasons. Once the connection to the database has been established, a loading screen is shown. Next, the user needs to provide application level log in credentials. The default admin user credentials are



  * name: admin

  * password: adminadmin



It is highly recommended to change the default admin password once the admin user is logged in. This can be done in the admin section.



#### Admin section



If a user belongs to the admin group, the admin management menu is visible. It has four sub menus



  1. users: manage users and associated groups, roles and permissions

  2. instruments: manage instrument metadata

  3. materials: manage material metadata

  4. protocols: manage protocol metadata



Colims uses controlled vocabularies (see [ols](http://www.ebi.ac.uk/ontology-lookup/)) for defining instrument, material and protocol properties.



A user can be linked to groups, a group to roles and roles to permissions. Colims has four default self explanatory permissions:



  1. read: read data from the database

  2. create: insert new records into the database

  3. update: update existing records

  4. delete: delete existing data



A warning dialog will pop up if the user doesn't have the right permissions for a specific action (e.g. create a project).



#### Projects management



In this panel, projects, experiments, samples and related entities can be added, updated and deleted. A new storage task can be set up by selecting a sample and clicking on the _add run_ button. For the moment, [PeptideShaker](http://peptide-shaker.googlecode.com/) *.cps* files and [MaxQuant](http://www.maxquant.org/) experiments can be stored. A warning message is shown if the client cannot make a connection with the queueing module. The client can monitor the different queues (see further) by selecting *storage monitoring* in the *View* menu.



#### Projects overview



The stored data can be explored in this panel.



----



## Storage queueing module



### Purpose

[Apache ActiveMQ](http://activemq.apache.org/) is used as an intermediate layer between the client(s) and the storage engine. It contains 3 messaging queues:



  * storage queue: clients send analytical run storage tasks to this queue

  * stored queue: once a run has been stored successfully, the storage engine sends a confirmation message to this queue

  * error queue: if something went wrong while storing, the storage engine wraps the storage task in a storage error and sends it to this queue



Using a separate queueing server has several advantages:



  * ActiveMQ is widely used and has proven to be a stable component in distributed architectures.

  * The storage engine listens to the storage queue and processes storage tasks sequentially. This way, the entries in the protein and modifications tables can be kept unique.

  * If the storage engine cannot be reached by the queueing module (network problems, distributed module crash), the different messages reside on the queues and nothing gets lost.



### Running

Run the *activemq* file with a command line tool in the _bin_ directory of the provided `apache-activemq-5.9.0` distribution. ActiveMQ runs on both Windows and Linux machines.



#### Remote

When running ActiveMQ on a remote server, configure the JMX ports you want to use in the `activemq.xml` file in the *conf* directory:



```

<managementContext>

  <managementContext createConnector="true" connectorPort="<connectorPortNumber>" rmiServerPort="<rmiServerPortNumber>"/>

</managementContext>

```



instead of



```

<managementContext>

  <managementContext createConnector="true"/>

</managementContext>

```



The `distributed.jmx.service.url` in the `colims-client.properties` and `colims-distributed.properties` files becomes



```

distributed.jmx.service.url = service:jmx:rmi://<host>:<rmiServerPortNumber>

                              /jndi/rmi://<host>:<connectorPortNumber>/jmxrmi

```



instead of



```

distributed.jmx.service.url = service:jmx:rmi:///jndi/rmi://localhost:1099/jmxrmi

```



You also need to change the `wrapper.conf` file in the *bin/<win/linux version>*:



```

wrapper.java.additional.16=-Djava.rmi.server.hostname=127.0.0.1

```



becomes



```

wrapper.java.additional.16=-Djava.rmi.server.hostname=<host>

```



----



## Distributed module



The distributed part is responsible for the storage of analytical runs and associated search settings, identifications and quantifications.



### Configuration



Like the client module, the distributed module needs to connect with the database and the storage queueing module. The connection parameters are located in the `colims-distributed.properties` file in the *config* folder. The only difference is that the database password is stored there as well because the distributed module is managed by the administrator. Regular users should not be able to access it directly.



### Running



Execute the following command in the `colims-distributed-x.y.z` folder where the *.jar* file is located:



```

java -jar colims-distributed-<version>.jar

```



As mentioned before, this module listens to the storage queue and processes incoming storage tasks. The storage engine keeps on trying to make a connection with the storage queue if the queueing module cannot be reached.
