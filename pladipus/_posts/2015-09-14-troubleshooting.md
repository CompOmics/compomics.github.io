---
name: Troubleshooting
project: pladipus
layout: default
permalink: /pladipus/wiki/troubleshooting.html
github_project: https://github.com/compomics/pladipus
---

# The management GUI doesn't start

In order to determine the cause of the problem, please go through the following checklist : 

## General issues
* Does the controller/database server/activeMQ server allow connections on the specified hosts/ports?
* Is a firewall blocking traffic?
* Do all machines in the network pool have internet access and can they reach the controller?

## ActiveMQ issues
* Is the ActiveMQ server is running at the host / port that is declared in the network.properties file.
* Are the settings in the network.properties file matching those provided in the activemq.xml configuration file (see the [wiki](/pladipus/wiki/settings) for more information on how to find this out.html).
* Is the host specified in the activemq.xml <b>localhost</b> or <b>127.0.0.1</b> ? Then replace this with the actual IP of the machine hosting the server to allow external connections.

## mySQL issues
* Are the database settings that are declared in the network.properties file correct?
* Does your database account have full privileges on the database?
* Was the Pladipus database schema correctly initiated during the installation?