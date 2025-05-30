---
title: "ReleaseNotes"
layout: default
permalink: "/projects/xtandem-parser/wiki/ReleaseNotes"
tags: wiki, xtandem-parser
project: "xtandem-parser"
github_project: "https://github.com/CompOmics/xtandem-parser"
---

# ReleaseNotes

----

**Changes in XTandemParser 1.13.0 - (January 31. 2017):**

* LIBRARY UPDATE: Updated utilities to version 4.10.0.

---

**Changes in XTandemParser 1.12.0 - (December 12. 2016):**

* FEATURE IMPROVEMENT: Removed the references to the deprecated EBI Nexus repository.
* LIBRARY UPDATE: Updated utilities to version 4.8.7.

---

**Changes in XTandemParser 1.11.0 - (June 7. 2016):**

* BUG FIX: Fixed a bug in the parsing of doubly modified peptide terminals.

---

**Changes in XTandemParser 1.10.0 - (January 23. 2016):**

* BUG FIX: Fixed a bug in the parsing of fixed PTMs.

---

**Changes in XTandemParser 1.9.0 - (January 19. 2016):**

* FEATURE IMPROVEMENT: Updated the project web links in the README.txt file to point to the GitHub pages.
* BUG FIX: Fixed bugs in the ID file reader in the way multiple PTMs targeting the same residue was handled, in particular when one PTM was fixed and the other variable, e.g. as in variable TMT on n-term and fixed TMT on (n-term) K.

---

**Changes in XTandemParser 1.8.1 - (October 12. 2015):**

 * FEATURE IMPROVEMENT: Removed the peptide map from the IdfileReader to speed up the processing. 
 * LIBRARY UPDATE: Updated utilities to version 4.0.14.

---

**Changes in XTandemParser 1.8.0 - (August 27. 2015):**

  * LIBRARY UPDATE: Updated utilities to version 4.0.0.

---

**Changes in XTandemParser v1.7.18 - (January 26. 2015):**

  * BUG FIX: Fixed a bug in the PTM mapping where modifications where categorized as fixed or variable based on the PTM mass shift alone. Which broke down for iTRAQ searches where the same mass is found as both a fixed and variable modification. The modified amino acid and the location is now used in addition to the mass.

---

**Changes in XTandemParser v1.7.17 - (December 11. 2014):**

  * LIBRARY UPDATE: Updated utilities to version 3.43.24.

---

**Changes in XTandemParser v1.7.15 - (October 8. 2014):**

  * FEATURE IMPROVEMENT: Minor corrections in the ID file reader.

---

**Changes in XTandemParser v1.7.14 - (September 8. 2014):**

  * LIBRARY UPDATE: Updated utilities to version 3.36.0.

---

**Changes in XTandemParser v1.7.13 - (August 19. 2014):**

  * LIBRARY UPDATE: Updated utilities to version 3.35.0.

---

**Changes in XTandemParser v1.7.11 - (August 12. 2014):**

  * LIBRARY UPDATE: Updated utilities to version 3.32.1.

---

**Changes in XTandemParser v1.7.10 - (August 11. 2014):**

  * LIBRARY UPDATE: Updated utilities to version 3.32.0.

---

**Changes in XTandemParser v1.7.7 - (January 21. 2014):**

  * BUG FIX: The performance parameters are now parsed and kept even when using the skipDetails option.
  * LIBRARY UPDATE: Updated utilities to version 3.21.6.

---


**Changes in XTandemParser v1.7.6 - (January 14. 2014):**

  * LIBRARY UPDATE: Updated utilities to version 3.21.0.

---

**Changes in XTandemParser v1.7.5 - (December 27. 2013):**

  * BUG FIX: Corrected a bug where wrong PTM sites were returned in the XTandemIdfileReader.

---

**Changes in XTandemParser v1.7.4 - (November 21. 2013):**

  * LIBRARY UPDATE: Updated utilities to version 3.18.0.

Download Count: 9

---

**Changes in XTandemParser v1.7.3 - (November 18. 2013):**

  * FEATURE IMPROVEMENT: Removed the protein remapping in the id file reader.
  * LIBRARY UPDATE: Updated utilities to version 3.17.7.

Download Count: 4

---

**Changes in XTandemParser v1.7.1 - (September 13. 2013):**

  * BUG FIX: The input (and performance) parameters are now again included when in the import when using the skipDetails option, as these were needed when mapping the PTMs.

Download Count: 36

---

**Changes in XTandemParser v1.7.0 - (August 24. 2013):**

  * NEW FEATURE: Added a new import mode where identification details can be skipped.
  * LIBRARY UPDATE: Updated utilities to version 3.14.28.

Download Count: 5

---

**Changes in XTandemParser v1.6.0 - (June 20. 2013):**

  * BUG FIX: Fixed a bug where the fragment ion mass error was hard coded to 0.3. It can now be set as a parameter in the InSilicoDigester constructor and in the getFragmentIonsForPeptide method in the XTandemFile class. (Note that the accuracy is still hard coded to 0.3 in the viewer.)

Download Count: 46

---

**Changes in XTandemParser v1.5.15 - (April 26. 2013):**

  * BUG FIX: Fixed a problem with starting the viewer on the latest Java release.

Download Count: 32

---

**Changes in XTandemParser v1.5.14 - (April 2. 2013):**

  * FEATURE IMPROVEMENT: Spectrum titles are now corrected in the id file reader.
  * BUG FIX: Refinement modifications are now considered as variable and not fixed as before.
  * BUG FIX: Fixed a bug where the residueModificationMass values where not parsed correctly. (These are the secondary sets of modifications added to support multiple sets of modifications analyzed simultaneously. See http://www.thegpm.org/tandem/api/refmm.html for details.)
  * BUG FIX: Made a minor change to the pom file to handle a recursive issues that can occur when opening the project in NetBeans 7.2.
  * BUG FIX: Fixed some UTF-8 code issues.
  * BUG FIX: Tried to fix an issue in the XTandemIdfileReader where X!Tandem's adding of the retention time to the spectrum tiles caused problems.
  * BUG FIX: Fixed some issues detected by FindBugs.

Download Count: 12

---

**Changes in XTandemParser v1.5.10 - (December 31. 2012):**

  * FEATURE IMPROVEMENT: Added the code required to be able to get the complete protein description tag. (In the Protein object the getDescription method should now be used instead of the getLabel method, as getLabel often returns a shortened version of the description. The getLabel method is kept for cases where the protein note tag with the protein description is not provided.)
  * FEATURE IMPROVEMENT: Improved the error message thrown if an unknown amino acid is found when calculating the peptide mass.
  * FEATURE IMPROVEMENT: Removed the fixed modifications from the IDfilereader.
  * FEATURE IMPROVEMENT: JavaDoc and source is now part of the build.
  * LIBRARY UPDATE: Updated utilities to version 3.10.24.

Download Count: 43

---

**Changes in XTandemParser v1.5.3 - (September 19. 2012):**

  * BUG FIX: Fixed a bug in the XTandemIdfileReader where fixed modifications were handled incorrectly, resulting in issues when more than one fixed modification was found on the same peptide.
  * FEATURE IMPROVEMENT: Made the code Maven 3 compliant.
  * LIBRARY UPDATE: Updated utilities to version 3.8.12.

Download Count: 58

---

**Changes in XTandemParser v1.5.0 - (August 13. 2012):**

  * BUG FIX: Fixed a reported issue where substitutions where not treated correctly.
  * BUG FIX: Fixed a reported issues where proteins with multiple domains were not parsed correctly.

Download Count: 10

---

**Changes in XTandemParser v1.4.1 - (July 9. 2012):**

  * BUG FIX: Fixed a typo in InputParams where C\_TERMRESMODMASS could not be extracted.

Download Count: 10

---

**Changes in XTandemParser v1.4 - (April 28. 2012):**

  * BUG FIX: Fixed a bug where domain id was assumed to be unique (something it not always is...).
  * NOTE: Version 1.4 is not fully backwards compatible. The method getDomainKey() now ought to be used instead of getDomainID() as domain id is not always unique. Additionally proteinMap.getProtein(domain.getProteinKey()) replaces getProteinWithDomainKey(domain.getDomainID()).

Download Count: 43

---

**Changes in XTandemParser v1.3.11 - (April 8. 2012):**

  * BUG FIX: Corrected a bug impairing the parsing of files when other ions than b and y were searched.

Download Count: 11

---

**Changes in XTandemParser v1.3.10 - (March 1. 2012):**

  * NEW FEATURE: Added support for for the "scoring, algorithm" input parameter.

Download Count: 32

---

**Changes in XTandemParser v1.3.9 - (February 28. 2012):**

  * BUG FIX: Fixed a bug in the database URL mappings where the URLs were overwritten due to the key used not being unique.

Download Count: 4

---

**Changes in XTandemParser v1.3.8 - (February 26. 2012):**

  * NEW FEATURE: Precursor retention time can now be extracted using the getPrecursorRetentionTime method in the Spectrum class.

Download Count: 4

---

**Changes in XTandemParser v1.3.7 - (February 24. 2012):**

  * BUG FIX: The parser now returns a null object (instead of crashing) if X!Tandem was unable to construct a reasonable estimate of the protein expectation value. (This can happen when none of the peptide assignments has an e-value < 1, which means that all of the assignments are no better than would be expected at random.)

Download Count: 5

---

**Changes in XTandemParser v1.3.6 - (December 19. 2011):**

  * FEATURE IMPROVEMENT: Changed several variables from int to long in PerformParams, to be able to handle larger numbers.
  * BUG FIX: If the look and feel is not supported the default Java look and feel is used instead.

Download Count: 38

---

**Changes in XTandemParser v1.3.5 - (September 23. 2011):**

  * BUG FIX: Added refine modification mass from the input parameters section and fixed the double conversion problem.
  * BUG FIX: Fixed bug for exporting the identifications results.
  * BUG FIX: Changed line 304 in InputParams.java to: if(map.get("SPECMAXPRECURSORCHANGE") != null)

Download Count: 36

---

**Changes in XTandemParser v1.3.4 - (July 18. 2011):**

  * BUG FIX: Corrected a bug in the peptide map creation.
  * BUG FIX: Corrected bugs resulting in incorrect modification site assignement.

Download Count: 50

---

**Changes in XTandemParser v1.3.2 - (April 1. 2011):**

  * BUG FIX: According to the X!Tandem API documentation the default value for iScoring\_bIons and iScoring\_yIons should be true and not false.
  * BUG FIX: The peptide's fasta file path isn't set in PeptideMap.
  * BUG FIX: X! Tandem supports multiple modification masses, this is now also supported by the XTandem Parser.

Download Count: 72

---

**Changes in XTandemParser v1.3.1 - (April 1. 2011):**

  * BUG FIX: fixed two null pointer exceptions that crashed the viewer.

Download Count: 8

---

**Changes in XTandemParser v1.3 - (March 31. 2011):**

  * NEW FEATURE: Multiple domain are supported. e.g. peptide identifications within the same protein. Each peptide now has a list of possible domains.
  * BUGFIX: The values for input and other parameter were set to NULL as default.

Download Count: 6

---

**Changes in XTandemParser v1.2.7 - (March 9. 2011):**

  * LIBRARY UPDATE: Updated compomics-utilities to 3.0.46 with an improved spectrum panel.

Download Count: 21

---

**Changes in XTandemParser v1.2.6 - (February 27. 2011):**

  * NEW FEATURE: Improved parsing of the accession numbers. Now split into accession number and protein description.
  * FEATURE IMPROVEMENT: Made sure that the first row in the Spectra Files table is selected when a file is opened, thus displaying the first spectrum.
  * LIBRARY UPDATE: Updated compomics-utilities to 3.0.40 with an improved spectrum panel.

Download Count: 11

---

**Changes in XTandemParser v1.2.5 - (September 03. 2010):**

  * BUGFIX: The identified field is now set to ON or OFF when spectrum has been identified or not.

Download Count: 85

---

**Changes in XTandemParser v1.2.4 - (August 18. 2010):**

  * FEATURE IMPROVEMENT: Made some usefull methods available outside of the package by making them `public`.

Download Count: 56

---

**Changes in XTandemParser v1.2.3 - (August 17. 2010):**

  * FEATURE IMPROVEMENT: The XTandem Parser icon is now included in the build and shows up in the target folder.
  * FEATURE IMPROVEMENT: In XTandem Viewer the spectrum panel now also increases in size when the frame is resized.
  * LIBRARY UPDATE: Updated compomics-utilities to 3.0.9

Download Count: 6

---

**Changes in XTandemParser v1.2.2 - (June 16. 2010):**

  * BUG FIX: A serious bug concerning multiple modifications on a single peptide was fixed. The error was reported previously by Ron Beavis from the X!Tandem project.

Download Count: 30

---

**Changes in XTandemParser v1.2.1 - (June 15. 2010):**

  * FEATURE IMPROVEMENT: All types of ions with NH3 and H2O losses as well as MH ions are now supported. (Thanks again to Marc Vaudel!)
  * FEATURE IMPROVEMENT: Ions with a charge +2, +3 etc. are included.
  * FEATURE IMPROVEMENT: Fixed and variable modifications are shown separately in the table and legend of the viewer.
  * BUG FIX: A bug concering wrong indexing of the modifications in the viewer was removed.

---

**Changes in XTandemParser v1.2 - (May 18. 2010):**

  * FEATURE IMPROVEMENT: Fixed and variable modifications are separated by the parser as given by the XTandem input.
  * FEATURE IMPROVEMENT: Memory heap was increased for parsing bigger XML files.
  * FEATURE IMPROVEMENT: Javadoc comes with the current version 1.2.
  * BUG FIX: Incorrect parsing with empty string tags was corrected.
  * BUG FIX: A bug was removed concerning the retrieval of the proteinId by the peptideID if the list has more than 9 hits (thanks Marc!).

---

**Changes in XTandemParser v1.1.1 - (Jan. 14. 2010):**

  * BUG FIX: The accessions are now shown correctly in the identifications section.

Download Count: 58

---

**Changes in XTandemParser v1.1 - (Nov. 24. 2009):**

  * NEW FEATURE: The memory settings are no longer hard coded. Error messages in the XTandemViewer are now sent to the `ErrorLog` text file.
  * FEATURE IMPROVEMENT: Spaces in file names is now supported on all Windows platforms.
  * BUG FIX: Pressing the Alt key no longer makes the wait icon appear in the main frame.
  * BUG FIX: Help dialog: the "go to top of page link" now works.

Download Count: ?

---

**Changes in XTandemParser v1.0.1:**

  * BUG FIX: the application would not start if double-clicked from a folder with a space in the folder name
  * BUG FIX: the open file dialog was too small on certain resolution settings
  * BUG FIX: sequence annotation contained a bug that caused errors to be thrown after program completion, and failed to correctly annotate terminal residues. All these problems have now been fixed.

Download Count: 7

---

**Changes in XTandemParser v1.0.:**

  * The XTandem Parser is now fully functional. The parser has got a bootstrapper class for the memory management. The viewer now supports all ion types and has also a
function to export identification and spectra information.

Download Count: 19

---

**Changes in XTandemParser v0.75:**

  * The spectrum viewer class now supports a reasonable exception handling.

---

**Changes in XTandemParser v0.7:**

  * The program supports now b and y fragment ions and they are shown in the spectrum viewer.

---

**Changes in XTandemParser v0.6:**

  * The parser contains now a basic viewer which loads a xtandem output file and shows spectra and identified peptides with modifications.