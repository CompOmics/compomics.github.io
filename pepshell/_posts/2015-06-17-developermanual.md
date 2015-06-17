---
name: Developermanual
project: pepshell
layout: default
permalink: /pepshell/wiki/developermanual.html
---

# Use PepShell as Maven dependency

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

[Go to top of page](#use-pepshell-as-maven-dependency)

----
