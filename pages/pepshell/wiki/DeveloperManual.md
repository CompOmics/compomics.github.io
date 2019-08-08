---
title: DeveloperManual
layout: default
permalink: /projects/pepshell/wiki/DeveloperManual
tags: wiki, pepshell
project: pepshell
github_project: https://github.com/compomics/pepshell
---

# DeveloperManual
# Developer manual

## Use PepShell as Maven dependency

Include the following dependency

```
    <dependency>
        <groupId>com.compomics</groupId>
        <artifactId>pepshell</artifactId>
        <version>X.Y</version>
    </dependency>
```

and the following repository in your _pom.xml_ file:

```
    <repositories>                   
        <repository>
            <id>genesis-maven2-repo</id>
            <name>Genesis maven2 repository</name>
            <url>http://genesis.UGent.be/maven2</url>
            <layout>default</layout>
        </repository>              
    </repositories>
```
