---
name: InstallingMySQL
project: pladipus
layout: default
permalink: /pladipus/wiki/installingmysql.html
github_project: https://github.com/compomics/pladipus
---

#Installing MySQL

This tutorial will demonstrate how to install MySQL on a Windows machine, but similar versions are also available for Linux.

----

## Using an installer

The MySQL database does offer an excellent installer. The wizard will guide you and create the my.ini configuration file and installs MySQL as a service. This option is the recommended solution for novice users. 

* Navigate to the [downloads](http://www.mysql.com/downloads/) page.
* Find the MySQL Community Edition
* Select the MySQL Community Server and continue to download the specific MySQL Installer for your system

<b><u>Note</u></b> : You do not have to create a login on the MySQL website ! There is a small link at the bottom of the page saying 'No thanks, just start my download.'

* Double click the .msi installer. If a previous version of MySQL was detected, it will automatically update
* During the installation, install or upgrade the MySQL server.

----

## Manual Installation

More advanced users may prefer a manual installation, as the user has more control over how and when MySQL runs.

* Navigate to the MySQL Community Server for your operating system from the [downloads](dev.mysql.com/downloads/) page
* Download the “Without installer” version.
* Extract the ZIP file to a destination of your choice and rename the unzipped folder to “mysql”.

<b><u>Note</u></b> : MySQL can be installed anywhere on your system. If you want a lightweight installation, you can remove every sub-folder except for bin, data, scripts and share.

----

## Configuration

* Locate or create the my.ini file in the mysql folder.
* Add or update the following statements : 

\# The TCP/IP Port the MySQL Server will listen on 
port=[insert the port, this is by default 3306] 

\# \#IP address to bind to. 
bind-address=[insert IP address of the MySQL server]

<b><u>Note</u></b> : Updating the bind-address is mandatory. It otherwise defaults to localhost, disallowing all access from outside the server

----

## Starting the server

* Open a command line window and navigate to the bin folder inside the MySQL folder
* Launch the following command : 
 `C:\Program Files\MySQL\MySQL Server 5.0\bin\mysqld`

----

## Stopping the server 

* Open a command line window and navigate to the bin folder inside the MySQL folder
* Launch the following command : 
 `C:\Program Files\MySQL\MySQL Server 5.0\bin\mysqladmin" -u root shutdown`

