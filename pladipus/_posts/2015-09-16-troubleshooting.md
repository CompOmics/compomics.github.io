---
name: Troubleshooting
project: pladipus
layout: default
permalink: /pladipus/wiki/troubleshooting.html
github_project: https://github.com/compomics/pladipus
---

# Installation issues

* `ActiveMQ can not be reached`

Is the ActiveMQ server correctly installed and running?
You can verify this by connection to the IP of the connector at port 8161 in a browser, for example : 192.168.22.45:8161. When you see you are able to connect OR the website prompts you for credentials, the ActiveMQ console is running. See [the ActiveMQ installation manual](http://compomics.github.io/pladipus/wiki/installingactivemq.html) for more details...


* `java.sql.SQLException: Unknown system variable 'language' `

This error is due to a bug in the MySQL software prior to the 5.5.x versions. Please upgrade your MySQL version. For more details, please refer to [the MySQL installer manual](http://compomics.github.io/pladipus/wiki/installingmysql.html).

* `java.sql.SQLException: Unknown system variable 'lower_case_table_names' `

This error can occur on MySQL versions 5.5.x and up. It is commonly solved by adding the following lines into the my.ini file. 

`[mysqld]`

`lower_case_table_names=1`

For more information, please refer to [the MySQL installer manual](http://compomics.github.io/pladipus/wiki/installingmysql.html).

----

# Operation issues

* I'm using a template, but I don't see a new run appear

Please verify that the run you are trying to create has a different name from existing ones for your user account. Otherwise, new jobs will get added to the existing run.

----

# My problem is not yet listed here

In order to determine the cause of the problem, please go through the following checklist : 

----

## General issues
* Does the controller/database server/activeMQ server allow connections on the specified hosts/ports?
* Is a firewall blocking traffic?
* Do all machines in the network pool have internet access and can they reach the controller?
* Does the user running pladipus have adequate user privileges, for example to create a new file?

----

## ActiveMQ issues
* Is the ActiveMQ server is running at the host / port that is declared in the network.properties file.
* Are the settings in the network.properties file matching those provided in the activemq.xml configuration file (see the [wiki](/pladipus/wiki/settings) for more information on how to find this out.html).
* Is the host specified in the activemq.xml <b>localhost</b> or <b>127.0.0.1</b> ? Then replace this with the actual IP of the machine hosting the server to allow external connections.

----

## mySQL issues
* Are the database settings that are declared in the network.properties file correct?
* Does your database account have full privileges on the database?
* Was the Pladipus database schema correctly initiated during the installation?