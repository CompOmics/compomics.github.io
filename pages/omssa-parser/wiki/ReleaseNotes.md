---
title: "ReleaseNotes"
layout: default
permalink: "/projects/omssa-parser/wiki/ReleaseNotes"
tags: wiki, omssa-parser
project: "omssa-parser"
github_project: "https://github.com/CompOmics/omssa-parser"
---

# Release Notes

----

**Changes in omssa-parser v2.0.4 - (January 5. 2022):**

* LIBRARY UPDATE: Updated log4j-core to version 2.17.1.
* LIBRARY UPDATE: Updated log4j-api to version 2.17.1.
* LIBRARY UPDATE: Updated utilities to version 5.0.35.

---

**Changes in omssa-parser v2.0.3 - (November 15. 2021):**

* LIBRARY UPDATE: Updated utilities to version 5.0.34.

---

**Changes in omssa-parser v2.0.1 - (November 20. 2020):**

* FEATURE IMPROVEMENT: Added support for parsing spectrum titles with leading or trailing white space.
* LIBRARY UPDATE: Updated utilities to version 5.0.1.

---

**Changes in omssa-parser v2.0.0 - (November 4. 2020):**

* FEATURE IMPROVEMENT: Made the code compatible with Java 9 and newer.
* LIBRARY UPDATE: Updated JSparklines to version 1.0.12.
* LIBRARY UPDATE: Updated utilities to version 5.0.0.

---

**Changes in omssa-parser v1.9.0 - (January 31. 2017):**

* LIBRARY UPDATE: Updated utilities to version 4.10.0.

---

**Changes in omssa-parser v1.8.0 - (December 11. 2016):**

* FEATURE IMPROVEMENT: Removed the references to the deprecated EBI Nexus repository.
* LIBRARY UPDATE: Updated utilities to version 4.8.7.

---

**Changes in omssa-parser v1.7.1 - (October 12. 2015):**

 * FEATURE IMPROVEMENT: Removed the peptide map from the IdfileReader to speed up the processing.
 * LIBRARY UPDATE: Updated utilities to version 4.0.14.

---

**Changes in omssa-parser v1.7.0 - (August 27. 2015):**

  * LIBRARY UPDATE: Updated utilities to version 4.0.0.

---

**Changes in omssa-parser v1.6.12 - (December 11. 2014):**

  * LIBRARY UPDATE: Updated utilities to version 3.43.24.

---

**Changes in omssa-parser v1.6.11 - (October 8. 2014):**

  * FEATURE IMPROVEMENT: Minor corrections in the ID file reader.

---

**Changes in omssa-parser v1.6.10 - (September 8. 2014):**

  * LIBRARY UPDATE: Updated utilities to version 3.36.0.

---

**Changes in omssa-parser v1.6.9 - (August 19. 2014):**

  * LIBRARY UPDATE: Updated utilities to version 3.35.0.

---

**Changes in omssa-parser v1.6.6 - (August 11. 2014):**

  * LIBRARY UPDATE: Updated utilities to version 3.32.0.

---

**Changes in omssa-parser v1.6.3 - (January 21. 2014):**

  * LIBRARY UPDATE: Updated utilities to version 3.21.6.

---

**Changes in omssa-parser v1.6.2 - (January 14. 2014):**

  * LIBRARY UPDATE: Updated utilities to version 3.21.0.

---

**Changes in omssa-parser 1.6.1 (November 18. 2013):**

  * LIBRARY UPDATE: Updated utilities to version 3.17.7.

---

**Changes in omssa-parser 1.6.0 (August 25. 2013):**

  * NEW FEATURE: Created a new low memory usage mode.
  * FEATURE IMPROVEMENT: Added some tests to escape null pointers that could occur when loading (corrupt?) omx files.
  * LIBRARY UPDATE: Updated utilities to version 3.14.27.

Download count: 36

---

**Changes in omssa-parser 1.5.11 (June 10. 2013):**

  * BUG FIX: Fixed a problem with starting the viewer on the latest Java release.

Download count: 16

---

**Changes in omssa-parser 1.5.10 (April 26. 2013):**

  * BUG FIX: Fixed a problem with starting the viewer on the latest Java release.

Download count: 19

---

**Changes in omssa-parser 1.5.9 (January 11. 2013):**

  * FEATURE IMPROVEMENT: Made a minor change to the pom file to handle recursive issues that can occur when opening the project in NetBeans 7.2.
  * FEATURE IMPROVEMENT: Spectrum titles are now decoded in the id file reader.
  * BUG FIX: Minor code cleanups.

Download count: 19

---

**Changes in omssa-parser 1.5.8 (November 28. 2012):**

  * FEATURE IMPROVEMENT: Removed the fixed modifications from the OMSSAIdfileReader.
  * BUG FIX: Fixed an issue with one of the constructors of OmxParser.
  * LIBRARY UPDATE: Updated utilities to version 3.10.24.

Download count: 11

---

**Changes in omssa-parser 1.5.6 (November 14. 2012):**

  * NEW FEATURE: The code now supports Maven 3.
  * FEATURE IMPROVEMENT: Added new constructors to the OmxParser, making it possible to provide the input as files instead of the paths to the files.
  * FEATURE IMPROVEMENT: Improved the fixMgfTitle method in the OMSSAIdfileReader.
  * FEATURE IMPROVEMENT: The source and JavaDoc is now included when building.
  * LIBRARY UPDATE: Updated utilities to version 3.10.8

Download count: 15

---

**Changes in omssa-parser 1.5.2 (August 21. 2012):**

  * BUG FIX: Fixed a bug in the OMSSA Viewer were fixed n- and c-terminal PTMs were annotated more than once in the legend.

Download count: 29

---

**Changes in omssa-parser 1.5.1 (August 20. 2012):**

  * BUG FIX: Fixed a bug in the OMSSA Viewer were fixed n- and c-terminal PTMs were not annotated.
  * LIBRARY UPDATE: Updated utilities to version 3.7.6, improving the look and feel of the spectrum viewer.

Download count: 0

---

**Changes in omssa-parser 1.5 (April 16. 2012):**

  * FEATURE IMPROVEMENT: Upgraded the OMSSA Viewer to the PeptideShaker look and feel.
  * FEATURE IMPROVEMENT: Updated the help and about texts.
  * LIBRARY UPDATE: Added jsparklines as a dependency.
  * LIBRARY UPDATE: Removed jgoodies and swingx as a dependencies.

Download count: 36

---

**Changes in omssa-parser 1.4.7 (January 31. 2012):**

  * BUG FIX: Changed the OMSSA abundance scale from a long to a double (as detailed in OMSSA.mod.xsd).

Download count: 61

---

**Changes in omssa-parser 1.4.6 (September 9. 2011):**

  * NEW FEATURE: Added the possibility to not import peak lists.

Download count: 109

---

**Changes in omssa-parser 1.4.5 (March 10. 2011):**

  * LIBRARY UPDATE: utilities library to version 3.0.46.

Download count: 117

---

**Changes in omssa-parser 1.4.4 (February 27. 2011):**

  * BUG FIX: Fixed some minor GUI details in the OMSSA Viewer.
  * LIBRARY UPDATE: utilities library to version 3.0.40.

Download count: 14

---

**Changes in omssa-parser 1.4.3 (February 22. 2011):**

  * FEATURE IMPROVEMENT: Improved the parsing of the protein accession number details from the omx file in OMSSA Viewer.

Download count: 6

---

**Changes in omssa-parser 1.4.2 (December 5. 2010):**

  * FEATURE IMPROVEMENT: Made some minor GUI changes to the viewer.
  * BUG FIX: Fixed an index bug in Spectrum to HitSetMap that occurred if not all spectrum indices were used.
  * LIBRARY UPDATE: utilities library to version 3.0.30.

Download count: 49

---

**Changes in omssa-parser 1.4.1 (September 30. 2010):**

  * FEATURE IMPROVEMENT: Export option now includes spectral filenames (or ´not available´ if not specified).

Download count: 30

---

**Changes in omssa-parser 1.4 (July 16. 2010):**

  * NEW FEATURE: OMSSA Parser has been extended to support OMSSA 2.1.9.
  * NEW FEATURE: All variables corresponding to XML tags in the OMSSA.mod.xsd file are now annotated with Javadoc based on the annotation used in the OMSSA.mod.xsd file.
  * NEW FEATURE: Mappings of all enumerations used in the OMSSA.mod.xsd file (see OmssaEnumerators.java) has been implemented, making it possible to map an integer ID to the corresponding text description.

Download count: 26

---

**Changes in omssa-parser 1.3.7 (May 31. 2010):**

  * FEATURE IMPROVEMENT: In some files the abundance scale was too big for an `int` value. Has now been replaced by a `long`.
  * LIBRARY UPDATE: utilities library to version 3.0.1

Download count: 15

---

**Changes in omssa-parser 1.3.6 (Apr. 26. 2010):**

  * FEATURE IMPROVEMENT: All data classes are now serializable.

Download count: 6

---

**Changes in omssa-parser 1.3.5 (Nov. 25. 2009):**

  * NEW FEATURE: On Windows platforms OMSSA Parser can now be run from paths containing spaces.
  * FEATURE IMPROVEMENT: Updated the JOptionPane dialogs by simplifying and shortening the text. Also fixed some minor typos.
  * BUG FIX: Altered the default subject in the mailto links in order to work on non-Windows platforms.

Download count: 39

---

**Changes in omssa-parser 1.3.4 (Aug. 19. 2009):**

  * OMSSA Viewer: Fixed a bug where the neutral loss of 'H2O' was written using the number '0' instead of the letter 'O'.
  * Updated the utilities library to version 2.9.9.

Download count: 31

---

**Changes in omssa-parser 1.3.3 (July 28. 2009):**

  * OMSSA Parser: Extended the support for neutral losses. Instead of returning a boolean variable, it now returns -1 if no neutral loss or a number -> 0 for water, 1 for ammonium. As detailed in the annotation of OMSSA omx files.
  * OMSSA Viewer: Updated the fragment ion annotations to support neutral losses and immonium ions.

Download count: 5

---

**Changes in omssa-parser 1.3.2 (Jun. 03. 2009):**

  * Default MSResponse\_scale (for scaling m/z values) is 100, if not given.
  * OMSSA Viewer: Spectrum name is not mandatory, use spectrum number if no name is given.
  * OMSSA Viewer: Increased the size of the first column in the Spectrum Files table somewhat to support longer row ids, i.e., bigger omx files.
  * OMSSA Viewer: Fixed a bug where the OMSSA Viewer tried to validate the modification files. Validation is now turned off.
  * OMSSA Viewer: Added an export all identifications (best hits only) feature.
  * OMSSA Viewer: Fixed a bug that resulted in the parser crashing when encountering multiple modifications on the same residue.
  * OMSSA Viewer: Fixed a couple of minor gui bugs.

Download count: 12

---

**Changes in omssa-parser 1.3.1 (May 29. 2009):**

  * OMSSA Viewer: Fixed a bug in the dta export function. The m/z values have to be converted to MH+ values, and this was previously not done (the m/z values were used directly).

Download count: 1

---

**Changes in omssa-parser 1.3.0 (Apr. 26. 2009):**

  * Now only requires Java version 1.5 (previously 1.6).
  * Two new dependencies added (swingx-0.9.1 (for JXTable) and swing-layout-1.0.3 (for Java 1.6 GUI stuff).
  * Fixed a minor bug in the "automatic check for updates" feature.

Download count: 3

---

**Changes in omssa-parser 1.2.1 (Mar. 26. 2009):**

  * Updated the check for new versions, due to a minor change in the way google code annotated deprecated downloads.

Download count: 8

---

**Changes in omssa-parser 1.2.0 (Mar. 16. 2009):**

  * Fixed a bug in the overloading of constructors in the OmssaOmxFile class. Now all constructors should work.

---

**Changes in omssa-parser 1.1.2 (Feb. 04. 2009):**

  * The automatic check for new versions now also handles deprecated downloads.
  * Minor updates of the help files.

---

**Changes in omssa-parser 1.1.1 (Jan. 16. 2009):**

  * A dialog with details about the error now appears if an exception is caught.

---

**Changes in omssa-parser 1.1.0 (Jan. 15. 2009):**

  * OMSSA Viewer: Modified peptide terminals are now supported.
  * OMSSA Viewer: Modification that are not found in mods.xml or usermods.xml (when these files are provided), no longer results in an error. The modification is simply labeled as "unknown".
  * OMSSA Viewer: Fixed a bug that resulted in an incorrect mapping of modifications that had modification numbers higher than 9.
  * OMSSA Viewer: Fixed a bug that occured when opening a new omx file after having sorted the previous file in the Spectra Files table. (An exception was previously thrown.)
  * OMSSA Viewer: Fixed a bug that resulted in making it imposible to update the ion coverage annotations by using the ion type selection or by selecting a different hit in the Identification table.
  * OMSSA Viewer The Spectrum panel ion coverage now also displays parent, internal, immonium and unknown ions if they are annotated in the omx file.
  * Fixed the lockstack issue in the XML parsing.

---

**Changes in omssa-parser 1.0.0 (Jan. 14. 2009):**

  * The m/z-axis now starts at 0.0 and not at the lowest m/z value in the spectrum.
  * Changed the export format from csv files to tab separated text files.
  * Updated OMSSA Viewer to version 1.3.
  * Increased the default height of the Spectrum table.
  * Added some tooltips to the File and Export menus.
  * Improved the representation of the E- and P-values in the Identifications table by using scientific notation.
  * If more than one charge is found the charge is now considered as unknown and is set to 0 in the Spectra Files table.

---

**Changes in omssa-parser 0.9.7 (Jan. 11. 2009):**

  * Fixed a bug that resulted in the OMSSA Viewer not being able to start.
  * Upgraded the OMSSA Viewer to version 1.2

---

**Changes in omssa-parser 0.9.6 (Jan. 7. 2009):**

  * Removed two unused libs (mail and activation).
  * Fixed the problem with the labels on the vertical axis in the SpectrumPanel where the font size was too small to read.
  * Updated the utilites jar to version 2.9.1.

---

**Changes in omssa-parser 0.9.5 (Dec. 16. 2008):**

  * Added a way of turning on/off the different annotations in the spectrum panel.
  * Fixed the scale issue yet again. Now individual MSSpectrum\_iscale scales are used for each spectrum.
  * Added charge to the spectrum panel ion coverage.
  * The ion coverage in the spectrum panel now changes relative to the identification selected in the identification table.
  * Added theoretical and experimental mass to the identification table.
  * Added file filters when doing file selection.
  * Added export functionality: all spectra file details (to csv files), all identifications (to csv files), all spectra (to dta files) and selected spectrum (to csv file).

---

**Changes in omssa-parser 0.9.4 (Dec. 14. 2008):**

  * Added a simple, lightweight viewer for omx files: OMSSA Viewer v1.0.
  * Removed the hardcoding of the scale value. The scale is now extracted from the omx file.
  * The OMSSA modifications are now also parsed if the mods.xml and usermods.xml files are provided.

---

**Changes in omssa-parser 0.9.3:**

  * Cleaned up the package structure.

---

**Changes in omssa-parser 0.9.2:**

  * Javadoc added and extended.

---

**Changes in omssa-parser 0.9.1:**

  * Logging functionality added (log4j)
  * Added methods for extracting the "real" m/z and abundance values. (The original values can still be extracted, but have to be divided by 1000 to get the "real" values.)
  * Javadoc added for the methods and variables involved in the previous point.