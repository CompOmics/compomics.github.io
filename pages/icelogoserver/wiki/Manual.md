---
title: "Manual"
layout: default
permalink: "/projects/icelogoserver/wiki/Manual"
tags: wiki, icelogoserver
project: "icelogoserver"
github_project: "https://github.com/CompOmics/icelogoserver"
---

# Installation instructions

Before you try to install the iceLogo server you must have a fully functional Tomcat (or similar) server installed

1. Copy the created icelogoserver.war file to your local *Tomcat/webapps* directory.
2. (Re)Start Tomcat.
3. Download *uniprot_sprot.fasta.gz* from ftp://ftp.ebi.ac.uk/pub/databases/uniprot/current_release/knowledgebase/complete/
4. Unzip the fasta database to *Tomcat/webapps/icelogoserver*.
5. Change the soap.properties file (*Tomcat/webapps/icelogoserver/WEB-INF/classes*) so that the parameter "location" point to your *Tomcat/webapps/icelogoserver* folder.
6. Change the save.properties file (*Tomcat/webapps/icelogoserver/WEB-INF*) so that the parameter "saveLocation" point to your *Tomcat/webapps/icelogoserver/images/logo* folder.
7. Delete the *icelogoserver.war* file from the *Tomcat/webapps* folder.
8. Now you can stop and restart the Tomcat server and the iceLogo server will be running. The web application can be accessed via http://localhost:8080/icelogoserver/main.html and the SOAP server via http://localhost:8080/icelogoserver/services/icelogo (These urls only works if your Tomcat installation uses port 8080).
