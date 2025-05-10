---
title: "ModulesConfiguration"
layout: default
permalink: "/projects/colims/wiki/ModulesConfiguration"
tags: wiki, colims
project: "colims"
github_project: "https://github.com/CompOmics/colims"
---

# Modules Configuration

  * [Introduction](#introduction)
  * [Client module](#client-module)
  * [Storage queuing module](#storage-queuing-module)
  * [Distributed module](#distributed-module)

## Introduction

The colims x.y.z client and distributed modules can be downloaded from the [Downloads](/projects/colims/#downloads) section on the home page.

**IMPORTANT** 

The experiments and FASTA databases directories need to be accessible by the client(s) as well as the distributed module. When a client submits a storage task to the distributed module, no files are copied, only relative paths are being passed. For example, if the MaxQuant experiments are located on some shared storage server (oursharedstorageserver.com/maxquant/experiments), both the client and the distributed need access to it. On a client, this share can be mounted as Z:\\\experiments (on a windows machine) and as /media/storage/experiments on the (linux) machine where the distributed module runs. These different mount locations need to specified in the client and distributed property files, as shown below.

----

## Client module

The client module contains the graphical user interface (GUI). A user can run it on his local machine to
 
  * manage metadata of projects, experiments, samples, runs, users, instruments, materials, protocols...
  * send analytical runs storage tasks to the storage queuing module
  * monitor the storage queuing module   

Multiple clients can be active simultaneously.  

### Configuration

Before running the colims client module for the first time, some database related properties - located in the `colims-client.properties` file in the *config* folder - need to be modified if necessary.

```
db.default_schema = colims
db.url = jdbc:mysql://localhost:3306/colims
db.driver = org.mariadb.jdbc.Driver
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

Finally, the experiments and FASTA databases directories have to defined.

```
#Shared file system properties
#the path of the experiments directory on the shared file system as mapped on your local machine
#linux
experiments.path = /home/user/Experiments
#windows, please use double backslashes "\\" or a forward slash "/" as path separator
#experiments.path = C:\\Users\\user\\Experiments
#the path of the FASTA DB files directory on the shared file system as mapped on your local machine
#linux
fastas.path = /home/user/Fastas
#windows, please use double backslashes "\\" or a forward slash "/" as path separator
#fastas.path = C:\\Users\\user\\Fastas
```

### Running

Run the colims client by double clicking the *.jar* file in the *colims-client-x.y.z* folder. First, the client module needs to connect to the database. The default database url and username values are retrieved from the `colims-client.properties` file, while the database password is not stored for security reasons. Once the connection to the database has been established, a loading screen is shown. Next, the user needs to provide application level log in credentials. The default admin user credentials are

  * name: admin
  * password: adminadmin

It is highly recommended to change the default admin password once the admin user is logged in. This can be done in the admin section. See the [Manual](/projects/colims/wiki/Manual) wiki page for using the client module.

----

## Storage queuing module

### Purpose
[Apache ActiveMQ](http://activemq.apache.org/) is used as an intermediate layer between the client(s) and the storage engine. It contains 3 messaging queues:

  * storage queue: clients send analytical run storage tasks to this queue
  * stored queue: once a run has been stored successfully, the storage engine sends a confirmation message to this queue
  * error queue: if something went wrong while storing, the storage engine wraps the storage task in a storage error and sends it to this queue

Using a separate queueing server has several advantages:

  * ActiveMQ is widely used and has proven to be a stable component in distributed architectures.
  * The storage engine listens to the storage queue and processes storage tasks sequentially. This way, the entries in the protein and modifications tables can be kept unique.
  * If the storage engine cannot be reached by the queuing module (network problems, distributed module crash), the different messages reside on the queues and nothing gets lost.

### Running
Before running, change the default broker name (`localhost`) to `colims_distributed` in the `activemq.xml` file in the *conf* directory:

```
<broker xmlns="http://activemq.apache.org/schema/core" brokerName="colims_distributed" dataDirectory="${activemq.data}">
```

Run the *activemq* file with a command line tool in the _bin_ directory of the ActiveMQ distribution downloaded from the ActiveMQ website. ActiveMQ runs on both Windows and Linux machines.

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

----

## Distributed module

The distributed part is responsible for the storage of analytical runs and associated search settings, identifications and quantifications.

### Configuration

Like the client module, the distributed module needs to connect with the database and the storage queueing module. The connection parameters are located in the `colims-distributed.properties` file in the *config* folder. The only difference is that the database password is stored there as well because the distributed module is managed by the administrator. Regular users should not be able to access it directly.

```
#Connection parameters
#mysql
db.default_schema = colims
db.url = jdbc:mysql://localhost:3306/colims
db.driver = org.mariadb.jdbc.Driver
db.dialect = org.hibernate.dialect.MySQL5Dialect
db.username = root
db.password = root
```

```
#Shared file system properties
#the path of the experiments directory on the shared file system as mapped on the distributed module's machine
#linux
experiments.path = /home/user/Experiments
#windows, please use double backslashes "\\" or a forward slash "/" as path separator
#experiments.path = C:\\Users\\user\\Experiments
#the path of the FASTA DBs directory on the shared file system as mapped on the distributed module's machine
#linux
fastas.path = /home/user/Fastas
#windows, please use double backslashes "\\" or a forward slash "/" as path separator
#fastas.path = C:\\Users\\user\\Fastas
```

### Running

Execute the following command in the `colims-distributed-x.y.z` folder where the *.jar* file is located:

```
java -jar colims-distributed-<version>.jar
```

As mentioned before, this module listens to the storage queue and processes incoming storage tasks. The storage engine keeps on trying to make a connection with the storage queue if the queueing module cannot be reached.