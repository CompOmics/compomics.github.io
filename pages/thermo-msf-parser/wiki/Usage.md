---
title: Usage
layout: default
permalink: /projects/thermo-msf-parser/wiki/Usage
tags: wiki, thermo-msf-parser
project: thermo-msf-parser
github_project: https://github.com/compomics/thermo-msf-parser
---

# Usage
# Usage

## Using Thermo MSF Parser as a Maven dependency
Thermo MSF Parser is hosted at our public maven repository.
Add the following code into your `pom.xml` file:

**Repository**
```
    <repositories>
    <!-- Compomics Genesis Maven 2 repository -->
        <repository>
            <id>genesis-maven2-repository</id>
            <name>Genesis maven2 repository</name>
            <url>http://genesis.UGent.be/maven2</url>
            <layout>default</layout>
        </repository>
    </repositories>
```

**Dependency**
```
    <dependencies>
        <dependency>
            <groupId>com.compomics</groupId>
            <artifactId>thermo_msf_parser</artifactId>
            <version>X.Y.Z</version>
            <type>jar</type>
        </dependency>
    </dependencies>
```

Update the version number (X.Y.Z) to latest released version.

Note that the [repository](http://genesis.ugent.be/maven2/com/compomics/thermo_msf_parser/) can be manually accessed to download the *src* or *javadocs*.

Also note that the thermo-msf-parser does not yet build in Maven 3. We are working on fixing this but in the meantime please use Maven 2 to build the thermo-msf-parser.

[Go to top of page](#usage)