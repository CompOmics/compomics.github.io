---
title: "ReleaseNotes"
layout: default
permalink: "/projects/mascotdatfile/wiki/ReleaseNotes"
tags: wiki, mascotdatfile
project: "mascotdatfile"
github_project: "https://github.com/CompOmics/mascotdatfile"
---

# Release notes

*Starting from MascotDatfile version 3.0, all subsequent versions of the library are listed here.*

### 3.6.1 (4 September 2019)
 * fix for new distiller version in the processMGFTitleToFilename method. Support for the new "Sum of 2 scans. 
   Range" title format as well as the old "Sum of 2 scans in range".

### 3.6.0 (31 January 2017)
 * Minor change in the compomics id file reader.
 * Updated utilities to version 4.10.0.

### 3.5.0 (12 December 2016)
 * Removed the references to the deprecated EBI Nexus repository.
 * Fixed https://github.com/compomics/mascotdatfile/issues/14.
 * Updated utilities to version 4.8.7.

### 3.4.32 (12 October 2015)
 * Removed the peptide map from the IdfileReader to speed up the processing. 
 * Updated utilities to version 4.0.0.

### 3.4.31 (27 August 2015)

 * Updated utilities to version 4.0.0.

### 3.4.19 (21 January 2014)

 * Disabled the error logging in the `getAllSpectrumMatches` method in the `MascotIdfileReader` class.
 * Corrected a JavaDoc error where the Mascot version was annotated as the database version.
 * Updated utilities to version 3.21.6.

### 3.4.18 (16 January 2014)

 * Removed the protein mappings from the `IdfileReader` class.

### 3.4.17 (16 January 2014)

 * Fixed a logic bug in the parsing of the compound number.

### 3.4.16 (15 January 2014)

 * Updated utilities to version 3.21.0.

### 3.4.15 (1 August 2013)

 * Removed spectrum file renaming for Mascot distiller files which should not be needed anymore. 
 * Update utilities  to version 3.14.16.

### 3.4.14 (9 July 2013)

 * Updated utilities to version 3.14.13.

### 3.4.13 (25 June 2013)

 * Started with refactoring.
 * Fixed a problem which allowed nulls in a List to not be removed.

### 3.4.11 (21 May 2013)

 * Fixed a bug where the first element in a vector was used without checking that the vector actually contained any elements first.

### 3.4.10 (14 March 2013)

 * The PeptideHit object's warning "Warning, more than two ';' semicolons used in the peptidehit String" is now only shown if the debug variable is turned on.
 * Fixed an issue with recursive folder generation when building the project using Maven 3 and NetBeans.
 * Fixed JavaDoc warnings.

### 3.4.9 (13 February 2013)

 * The secondary databases (if searching with more than one database) can now be extracted from the search parameters using the new `getSecondaryDatabases()` method.

### 3.4.8 (13 February 2013)

 * Prevented an exception thrown in the id file reader due to empty peptide assumption lists returned by the parser.

### 3.4.7 (6 December 2012)

 * Changed the location of the iText dependency from the Genesis repository to the common Maven repository, as there were some issues using the Genesis version.

### 3.4.6 (13 November 2012)

 * The code now works with Maven 3
 * Improved the formatting of a peptide hit warning message.

### 3.3 (26 July 2012)

 * Support for mascot 2.4

###3.2.9 (20 January 2012)

 * Added boolean parameter for `getDecoyQueryToPeptideMap()` method which will or will not throw an exception if the Decoy section is not in the Mascot result file.

### 3.2.8 (20 December 2011)

 * Fixed an issue with temp file indexing, introduced while fixing bug with newline auto-detection.

### 3.2.7 (19 December 2011)

 * Fixed an issue with Distiller filename parsing

### 3.2.6 (11 October 2011)

 * Fixed an issue where different kinds of newlines at the beginning would upset the indexing of a file

### 3.2.5 (22 July 2011)

 * Removed the maven filter for generating the log4j configuration file as this lead to NumberFormatExceptions.

### 3.2.4 (4 July 2011)

 * Created a dedicated tmp directory that is automatically cleaned.

### 3.2.3 (1 May 2011)

 * Added new optional parameters to be used by the MSF parser.

### 3.2.2 (27 October 2010)

 * Created a MascotDatfileException for library specific RuntimeExceptions.

### 3.2.1 (21 September 2010)

 * Create a setter for the ModifiacationMap so that this can be adapted from ms-lims.


### 3.2 (18 September 2010)

 * Add support for protein like '"DDI00062040.1":0:325:329:1,"DDI00100151.4":0:642:646:1'.

### 3.1 (23 April 2010)

 * Introduced log4j framework into MascotDatfile.

### 3.0.2 (1 April 2010)

 * Bugfix from Pride submission. When the unimod.xml section encompassed in a Mascot results file contains a custom modification with a accented 'é' character, the indexing algorithm failed on UNIX.
 * Bugfix from Pride submission. IPI protein accessions with multiple Trembl references are separated by a ";" character, and this caused an error while parsing the second half of a peptidehit String.

### 3.0.1 (24 February 2010)

 * When more then 10 variable modifications are applied, the modification id becomes hexadecimal ('A' for the tenth modification) and caused an parsing error in MascotDatfile.

### 3.0

 * Initial import of the MascotDatfile library into google code.
 * Note that all MascotDatfile packages have been changed from `be.proteomics.mascotdatfile` to `com.compomics.mascotdatfile`.