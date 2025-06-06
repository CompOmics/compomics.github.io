---
title: "ReleaseNotes"
layout: default
permalink: "/projects/thermo-msf-parser/wiki/ReleaseNotes"
tags: wiki, thermo-msf-parser
project: "thermo-msf-parser"
github_project: "https://github.com/CompOmics/thermo-msf-parser"
---

# Release notes

**Starting from thermo-msf-parser version 1.0, all subsequent versions of the library are listed here.**

### 2.0.5 (6 August 2013)
 * added support for proteome discoverer 1.4
 * support for files larger than 1 gigabyte has been finalized

### 1.0.8 (30 January 2013)
 * BUGFIX for reading protein headers
 * BUGFIX for creating spectra panels for XML files with incomplete tags
 * BUGFIX for reading rawfiles with differing extensions

### 1.0.6 (20 April 2012)
 * BUGFIX on ProcessigNodeParameter constructor
 * removed cyclic dependency between Rover and thermo-msf-parser

### 1.0.5 (1 March 2012)
 * Added support from PhosphoRS predictions

### 1.0.4 (1 November 2011)
 * Updated SQLLite driver to support 64bit JVM 

### 1.0.3 (14 September 2011)
 * Fixed the Starter on Unix machines.
 * Changed the mvn copy of the Java.properties file (again)
 * Enabled log4j in the Starter

### 1.0.2 (29 June 2011)
 * Bugfix Resolved a bug where a there was a string index out of bound exception when a
spectrum with no peaks was found.

### 1.0.1 (30 May 2011)
 * Refactored the dependency management.

## 1.0 (27 May 2011)
 * Initial release of the thermo-msf-parser library