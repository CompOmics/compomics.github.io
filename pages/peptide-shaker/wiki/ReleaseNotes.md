---
title: "ReleaseNotes"
layout: default
permalink: "/projects/peptide-shaker/wiki/ReleaseNotes"
tags: wiki, peptide-shaker
project: "peptide-shaker"
github_project: "https://github.com/compomics/peptide-shaker"
---

# ReleaseNotes

---

**Changes in PeptideShaker 2.2.16 (October 24. 2022):**

* BUG FIX: Fixed a bug in the NewEnzymeDialog.
* LIBRARY UPDATE: Updated utilities to version 5.0.50.

---

**Changes in PeptideShaker 2.2.15 (October 5. 2022):**

* FEATURE IMPROVEMENT: Minor improvement to the scaling for mirrored spectra.
* LIBRARY UPDATE: Updated utilities to version 5.0.49.

---

**Changes in PeptideShaker 2.2.14 (October 5. 2022):**

* BUG FIX: Fixed a bug in the Modifications tab where the mirrored spectrum was not always updated correctly.
* LIBRARY UPDATE: Updated jackson-databind to version 2.13.4.
* LIBRARY UPDATE: Updated jackson-annotations to version 2.13.4.

---

**Changes in PeptideShaker 2.2.13 (October 3. 2022):**

* LIBRARY UPDATE: Updated utilities to version 5.0.48, supporting Java version numbers with + as separator.

---

**Changes in PeptideShaker 2.2.12 (September 27. 2022):**

* LIBRARY UPDATE: Updated utilities to version 5.0.47, updating from http to https in the software setup dialogs.

---

**Changes in PeptideShaker 2.2.11 (September 27. 2022):**

* BUG FIX: Fixed a bug in the Ensembl mappings.
* LIBRARY UPDATE: Updated utilities to version 5.0.46, fixing a bug for Java versions without decimals, e.g. just 19.

---

**Changes in PeptideShaker 2.2.10 (September 20. 2022):**

* FEATURE IMPROVEMENT: Updated Ensembl to version 104 and Ensembl Genomes to version 51.

---

**Changes in PeptideShaker 2.2.9 (June 8. 2022):**

* BUG FIX: Updated the link in the check for new versions.

---

**Changes in PeptideShaker 2.2.8 (April 27. 2022):**

* LIBRARY UPDATE: Updated utilities to version 5.0.41, fixing a bug in the Total Spectrum Intensity export.

---

**Changes in PeptideShaker 2.2.7 (April 22. 2022):**

* FEATURE IMPROVEMENT: Added support for Cl, Co, Ni and Mn.
* LIBRARY UPDATE: Updated utilities to version 5.0.40.

---

**Changes in PeptideShaker 2.2.6 (March 1. 2022):**

* BUG FIX: Fixed a null pointer in the algorithm matches export for tags.

---

**Changes in PeptideShaker 2.2.5 (January 31. 2022):**

* BUG FIX: Fixed a null pointer in the algorithm matches export for peptides.
* LIBRARY UPDATE: Updated utilities to version 5.0.39.

---

**Changes in PeptideShaker 2.2.4 (January 13. 2022):**

* LIBRARY UPDATE: Updated utilities to version 5.0.37.

---

**Changes in PeptideShaker 2.2.3 (January 5. 2022):**

* LIBRARY UPDATE: Updated omssa-parser to version 2.0.4.
* LIBRARY UPDATE: Updated utilities to version 5.0.35.

---

**Changes in PeptideShaker 2.2.2 (November 15. 2021):**

* LIBRARY UPDATE: Updated omssa-parser to version 2.0.3.
* LIBRARY UPDATE: Updated utilities to version 5.0.34.

---

**Changes in PeptideShaker 2.2.1 (November 8. 2021):**

* FEATURE IMPROVEMENT: Added support for TMTpro 18-plex.
* FEATURE IMPROVEMENT: Added a command line option for setting the project type: project_type. 
* LIBRARY UPDATE: Updated utilities to version 5.0.33.

---

**Changes in PeptideShaker 2.2.0 (August 23. 2021):**

* LIBRARY UPDATE: Updated utilities to version 5.0.29, fixing a PTM alignment issue.

---

**Changes in PeptideShaker 2.1.1 (August 16. 2021):**

* LIBRARY UPDATE: Updated utilities to version 5.0.28, fixing a multi-threading null pointer in the cache handling.

---

**Changes in PeptideShaker 2.1.0 (August 13. 2021):**

* LIBRARY UPDATE: Updated xpp3 to version 1.1.6.
* LIBRARY UPDATE: Replaced commons-lang3 with commons-text version 1.9.
* LIBRARY UPDATE: Updated poi to version 5.0.0.
* LIBRARY UPDATE: Updated spring-webmvc to version 5.3.9.
* LIBRARY UPDATE: Updated jackson-databind to version 2.12.4.
* LIBRARY UPDATE: Updated jackson-annotations to version 2.12.4.
* LIBRARY UPDATE: Updated utilities to version 5.0.27.

---

**Changes in PeptideShaker 2.0.35 (August 11. 2021):**

* LIBRARY UPDATE: Updated utilities to version 5.0.26.

---

**Changes in PeptideShaker 2.0.34 (August 10. 2021):**

* LIBRARY UPDATE: Updated utilities to version 5.0.25.

---

**Changes in PeptideShaker 2.0.33 (June 20. 2021):**

* FEATURE IMPROVEMENT: Added support for Java 16.
* LIBRARY UPDATE: Updated utilities to version 5.0.24.

---

**Changes in PeptideShaker 2.0.32 (June 16. 2021):**

* BUG FIX: Fixed a gene mapping issue.

---

**Changes in PeptideShaker 2.0.31 (June 15. 2021):**

* FEATURE IMPROVEMENT: Updated the example dataset.
* FEATURE IMPROVEMENT: Updated Ensembl to version 104 and Ensembl Genomes to version 51.
* FEATURE IMPROVEMENT: Turned off illegal access log messages for more of the CLIs.
* LIBRARY UPDATE: Updated utilities to version 5.0.23.

---

**Changes in PeptideShaker 2.0.30 (June 2. 2021):**

* BUG FIX: Updated the cms file in the example dataset.

---

**Changes in PeptideShaker 2.0.29 (June 1. 2021):**

* BUG FIX: Fixed a bug in opening the example dataset on non-Windows setups.

---

**Changes in PeptideShaker 2.0.28 (May 28. 2021):**

* BUG FIX: Fixed an issue with opening the example dataset.
* LIBRARY UPDATE: Updated utilities to version 5.0.22.

---

**Changes in PeptideShaker 2.0.27 (May 21. 2021):**

* FEATURE IMPROVEMENT: Updated the PDB web service.
* LIBRARY UPDATE: Updated utilities to version 5.0.20.

---

**Changes in PeptideShaker 2.0.26 (May 19. 2021):**

* BUG FIX: Fixed an issue with the PTM scoring when there are more than 20 possible sites for the same PTM.
* LIBRARY UPDATE: Updated utilities to version 5.0.19.

---

**Changes in PeptideShaker 2.0.25 (April 29. 2021):**

* FEATURE IMPROVEMENT: Removed a stack trace that was printed if the export factory was not found.
* LIBRARY UPDATE: Updated utilities to version 5.0.18, fixing a rare cms-related bug.

---

**Changes in PeptideShaker 2.0.24 (April 26. 2021):**

* BUG FIX: Removed a custom settings file that caused the spectrum parsing to fail.

---

**Changes in PeptideShaker 2.0.23 (April 26. 2021):**

* BUG FIX: Fixed a backwards compatibility bug for the cms files.
* LIBRARY UPDATE: Updated utilities to version 5.0.17.

---

**Changes in PeptideShaker 2.0.22 (April 26. 2021):**

* BUG FIX: Fixed a bug that occurred if not using a log folder and not exporting a psdb file.

---

**Changes in PeptideShaker 2.0.21 (April 23. 2021):**

* LIBRARY UPDATE: Updated utilities to version 5.0.16.

---

**Changes in PeptideShaker 2.0.20 (April 21. 2021):**

* FEATURE IMPROVEMENT: Greatly sped up the parsing/indexing of the spectrum files.
* FEATURE IMPROVEMENT: Removed the Java 1.9 requirement, i.e. only Java 1.8 is now required.
* FEATURE IMPROVEMENT: Made sure that also the error messages are sent to the standard output when not using the log.
* LIBRARY UPDATE: Updated utilities to version 5.0.15.

---

**Changes in PeptideShaker 2.0.19 (April 13. 2021):**

* NEW FEATURE: Added a new command line option (use_log_folder) that makes it possible to override the log folder and send the log details directly to the standard output.

---

**Changes in PeptideShaker 2.0.18 (March 30. 2021):**

* BUG FIX: Fixed a bug in the check for duplicate accession numbers in FASTA files.
* LIBRARY UPDATE: Updated utilities to version 5.0.14.

---

**Changes in PeptideShaker 2.0.17 (March 30. 2021):**

* FEATURE IMPROVEMENT: Re-added the check for duplicate accession numbers in FASTA files.
* LIBRARY UPDATE: Updated utilities to version 5.0.13.

---

**Changes in PeptideShaker 2.0.16 (March 16. 2021):**

* FEATURE IMPROVEMENT: Extended the protein exports to also include organism identifiers for UniProt headers.
* LIBRARY UPDATE: Updated utilities to version 5.0.12.

---

**Changes in PeptideShaker 2.0.15 (March 14. 2021):**

* BUG FIX: Fixed bugs in parsing the user-defined exports.
* LIBRARY UPDATE: Updated utilities to version 5.0.11.

---

**Changes in PeptideShaker 2.0.14 (March 10. 2021):**

* BUG FIX: Fixed a bug with the fragmentation setting for MS-GF+ when using the command line.
* LIBRARY UPDATE: Updated utilities to version 5.0.10.

---

**Changes in PeptideShaker 2.0.13 (March 8. 2021):**

* FEATURE IMPROVEMENT: Made the FASTA header parsing (slightly) more robust.
* LIBRARY UPDATE: Updated utilities to version 5.0.9.

---

**Changes in PeptideShaker 2.0.12 (February 24. 2021):**

* FEATURE IMPROVEMENT: Added the search engine raw score for peptides and tags.
* LIBRARY UPDATE: Updated omssa-parser to version 2.0.2.
* LIBRARY UPDATE: Updated utilities to version 5.0.8.

---

**Changes in PeptideShaker 2.0.11 (January 29. 2021):**

* FEATURE IMPROVEMENT: The Java version warning now appears if using Java 8 or older.
* LIBRARY UPDATE: Updated utilities to version 5.0.7.

---

**Changes in PeptideShaker 2.0.10 (January 21. 2021):**

* BUG FIX: Fixed a bug in the export of non-enzymatic peptides.
* LIBRARY UPDATE: Updated utilities to version 5.0.6.

---

**Changes in PeptideShaker 2.0.9 (January 18. 2021):**

* BUG FIX: Fixed a bug in the protein inference graphs for displaying non-enzymatic peptides.
* LIBRARY UPDATE: Updated utilities to version 5.0.5.

---

**Changes in PeptideShaker 2.0.8 (December 22. 2020):**

* BUG FIX: Fixed an issue with indexing mgf files with empty spectra.
* LIBRARY UPDATE: Updated utilities to version 5.0.4.

---

**Changes in PeptideShaker 2.0.7 (December 18. 2020):**

* BUG FIX: Fixed an issue with checking for new versions when running in Conda.
* LIBRARY UPDATE: Updated utilities to version 5.0.3.

---

**Changes in PeptideShaker 2.0.6 (December 2. 2020):**

* BUG FIX: Fixed a bug in loading datasets without any validated PSMs.
* LIBRARY UPDATE: Updated utilities to version 5.0.2.

---

**Changes in PeptideShaker 2.0.5 (November 20. 2020):**

* FEATURE IMPROVEMENT: Added support for parsing spectrum titles with leading or trailing white space.
* FEATURE IMPROVEMENT: Hid the kryo illegal reflective access warning messages.
* BUG FIX: Added missing mgf file extensions in the follow up exports.
* LIBRARY UPDATE: Updated utilities to version 5.0.1.

---

**Changes in PeptideShaker 2.0.4 (November 18. 2020):**

* BUG FIX: Fixed bugs with locating moved FASTA and spectrum files.
* BUG FIX: The out option is now mandatory for the PeptideShakerCLI command line if the zip option is used.

----

**Changes in PeptideShaker 2.0.3 (November 17. 2020):**

* BUG FIX: Fixed a drawing bug in the validation plots.

----

**Changes in PeptideShaker 2.0.2 (November 11. 2020):**

* BUG FIX: Fixed a bug in opening the example dataset.

----

**Changes in PeptideShaker 2.0.1 (November 11. 2020):**

* BUG FIX: Fixed bugs in the gzip options for the MzidCLI and ReportCLI command lines.

----

**Changes in PeptideShaker 2.0.0 (November 4. 2020):**

* NEW FEATURE: Added support for spectrum files in mzML format.
* NEW FEATURE: Added support for loading Morpheus mzIdentML files files.
* FEATURE IMPROVEMENT: Novor results are now parsed as tags instead of complete peptides.
* FEATURE IMPROVEMENT: New faster and more memory efficient database backend.
* FEATURE IMPROVEMENT: Enabled launching of several instances on one computer.
* FEATURE IMPROVEMENT: Decreased file sizes when storing PS projects.
* FEATURE IMPROVEMENT: Increased GUI performance.
* FEATURE IMPROVEMENT: Sped up and reduced the memory load when parsing several of the search and de novo engine file formats.
* FEATURE IMPROVEMENT: Added support for gzipped search and de novo result files.
* FEATURE IMPROVEMENT: Moved the FASTA file out of the search parameters.
* FEATURE IMPROVEMENT: Added support for loading IdentiPy pep.xml files.
* FEATURE IMPROVEMENT: Added support for TMTpro (i.e. TMT 16-plex).
* FEATURE IMPROVEMENT: Updated Ensembl to version 101 and Ensembl Genomes to version 48.
* FEATURE IMPROVEMENT: Updated the validation icons and added a new icon for "Not Validated".
* FEATURE IMPROVEMENT: Refactored the command lines.
* FEATURE IMPROVEMENT: Enabled partial projects processing (i.e. PSMs or peptide and PSMs only).
* FEATURE IMPROVEMENT: Moved the code to Java 14. Note that Java 9 or newer is now required to run PeptideShaker!
* FEATURE IMPROVEMENT: Removed charge/modification grouping of PSM/peptides during scoring.
* FEATURE IMPROVEMENT: Better use of secondary hits.
* FEATURE IMPROVEMENT: Filtered hits are now visible in the interface.
* FEATURE IMPROVEMENT: Refactored the PTM alignment between peptides.
* FEATURE IMPROVEMENT: Improved the use of multiple threads.
* LIBRARY UPDATE: Updated utilities to version 5.0.0.

----

**Changes in PeptideShaker 1.16.45 (April 23. 2020):**

* BUG FIX: Peptides and spectra occurring in only one spectrum file are no longer excluded.

----

**Changes in PeptideShaker 1.16.44 (February 6. 2020):**

* BUG FIX: Fixed a bug in the Unipept export where unnecessary white space was added in the XML. 

----

**Changes in PeptideShaker 1.16.43 (January 17. 2020):**

* NEW IMPROVEMENT: Added support for exporting peptide sequences to [Unipept](https://unipept.ugent.be). 

----

**Changes in PeptideShaker 1.16.42 (July 10. 2019):**

* FEATURE IMPROVEMENT: Updated the example dataset.

----

**Changes in PeptideShaker 1.16.41 (July 7. 2019):**

* FEATURE IMPROVEMENT: Re-implemented the PRIDE Reshake to not show all projects but rather the results of the user's search.

* LIBRARY UPDATE: Updated utilities to version 4.12.15.

----

**Changes in PeptideShaker 1.16.40 (May 15. 2019):**

* BUG FIX: Fixed a bug in the use of user-defined terminal PTMs.

* LIBRARY UPDATE: Updated utilities to version 4.12.14.

----

**Changes in PeptideShaker 1.16.39 (May 8. 2019):**

* BUG FIX: The paths are now updated before the IdentificationParametersCLI is executed.

----

**Changes in PeptideShaker 1.16.38 (February 1. 2019):**

* FEATURE IMPROVEMENT: Made the -out option non-mandatory, making it possible to, for example, only generate an mzid file as output.

* BUG FIX: Fixed a bug in the closing of the PeptideShaker db when ran via the command line.

----

**Changes in PeptideShaker 1.16.37 (January 21. 2019):**

* FEATURE IMPROVEMENT: Non-standard characters in the submitter details (i.e. the Person and Organization elements) are now escaped when exporting to mzIdentML.

----

**Changes in PeptideShaker 1.16.36 (December 13. 2018):**

* FEATURE IMPROVEMENT: Changed the order of the files in zip for faster access to reports and indexes when read as a stream.
* FEATURE IMPROVEMENT: Included the path to the log file in the error message printed if the command line fails.

----

**Changes in PeptideShaker 1.16.35 (November 18. 2018):**

* FEATURE IMPROVEMENT: Added support for hyperplexing combining SILAC and TMT.

* LIBRARY UPDATE: Updated utilities to version 4.12.13.

----

**Changes in PeptideShaker 1.16.34 (November 13. 2018):**

* FEATURE IMPROVEMENT: Added support for Iron atoms. 
* FEATURE IMPROVEMENT: Added support for iodoTMT.
* FEATURE IMPROVEMENT: Added Heme B as a default PTM.

* LIBRARY UPDATE: Updated utilities to version 4.12.12.

----

**Changes in PeptideShaker 1.16.33 (November 9. 2018):**

* BUG FIX: Fixed issues with http/https when accessing UniProt. 
* LIBRARY UPDATE: Updated utilities to version 4.12.11.

----

**Changes in PeptideShaker 1.16.32 (November 5. 2018):**

* FEATURE IMPROVEMENT: Added support for TMT 11-plex.
* LIBRARY UPDATE: Updated httpclient to version 4.3.6.
* LIBRARY UPDATE: Updated utilities to version 4.12.10.

----

**Changes in PeptideShaker 1.16.31 (October 9. 2018):**

* BUG FIX: Removed a reference to GUI code in the PathSettingsCLI. 

----

**Changes in PeptideShaker 1.16.30 (October 4. 2018):**

* BUG FIX: Cleanup of the temp path options when used as options for the other command lines.
* BUG FIX: Made it possible to use the MzidCLI options directly on the PeptideShakerCLI command line.

----

**Changes in PeptideShaker 1.16.29 (September 18. 2018):**

* FEATURE IMPROVEMENT: Added default protein, peptide and PSM reports that also include the non-validated hits. Note: Some of the numbers for the reports have changed and that you may need to update your command lines.

----

**Changes in PeptideShaker 1.16.28 (September 17. 2018):**

* BUG FIX: The accuracy slider in the spectrum panel now works again.
* BUG FIX: Improved the way the gene and GO mappings are checked and updated.

* LIBRARY UPDATE: Updated utilities to version 4.12.8.

----

**Changes in PeptideShaker 1.16.27 (July 9. 2018):**

* BUG FIX: Fixed a bug in the algorithm details features export.

----

**Changes in PeptideShaker 1.16.26 (June 24. 2018):**

* BUG FIX: Fixed a bug where the PathSettingsCLI options where not supported when using the ReportCLI.

----

**Changes in PeptideShaker 1.16.25 (June 15. 2018):**

* FEATURE IMPROVEMENT: Updated the example dataset.

* BUG FIX: Fixed a bug in the clear filter feature in the PRIDE Reshake dialog. 

----

**Changes in PeptideShaker 1.16.24 (June 14. 2018):**

* FEATURE IMPROVEMENT: Ensured that Novor results can be loaded across operating systems, e.g. run on Windows and open on Linux.

* LIBRARY UPDATE: Updated utilities to version 4.12.7.

----

**Changes in PeptideShaker 1.16.23 (May 8. 2018):**

* LIBRARY UPDATE: Updated utilities to version 4.12.6.

----

**Changes in PeptideShaker 1.16.22 (May 3. 2018):**

* BUG FIX: Fixed a bug in the search setting dialog regarding the use of semi-specific enzymes.

* LIBRARY UPDATE: Updated utilities to version 4.12.5.

----

**Changes in PeptideShaker 1.16.21 (April 27. 2018):**

* BUG FIX: Fixed a bug in the IdentificationParametersInputBean where a break was missing when setting the cleavage preferences for MS-GF+ and MyriMatch.
* BUG FIX: Fixed a bug where upper case mgf file endings resulted in a null pointer when indexing such files.

* LIBRARY UPDATE: Updated utilities to version 4.12.4.

----

**Changes in PeptideShaker 1.16.20 (April 25. 2018):**

* BUG FIX: Fixed a memory leak in the mgf and mzIdentML exports.
* BUG FIX: Fixed a bug in the IdentificationParametersInputBean where a break was missing when setting the cleavage preferences for MS-GF+.

* LIBRARY UPDATE: Updated utilities to version 4.12.3.

----

**Changes in PeptideShaker 1.16.19 (April 13. 2018):**

* BUG FIX: Fixed bugs in the automatic detection of enzyme specificity that failed if non-enzymatic digestion was used.

* LIBRARY UPDATE: Updated utilities to version 4.12.2.

----

**Changes in PeptideShaker 1.16.18 (April 11. 2018):**

* FEATURE IMPROVEMENT: Updated the example dataset.
* FEATURE IMPROVEMENT: Added support for Pyrrolysine immonium ions.

* BUG FIX: Updated the parsing of the organism information from UniProt headers (after UniProt added the NCBI tax id to the headers)
* BUG FIX: Fixed backwards compatibility issues with opening old projects.

* LIBRARY UPDATE: Updated utilities to version 4.12.1.

---

**Changes in PeptideShaker 1.16.17 (March 15. 2018):**

* BUG FIX: Fixed backwards compatibility issues with opening old projects.

* LIBRARY UPDATE: Updated utilities to version 4.12.0.

---

**Changes in PeptideShaker 1.16.16 (March 9. 2018):**

* BUG FIX: Fixed issues with the PRIDE Reshake.

* LIBRARY UPDATE: Updated the PRIDE web-service-model to version 1.0.2.

---

**Changes in PeptideShaker 1.16.15 (November 9. 2017):**

* BUG FIX: Fixed issues with getting data from PRIDE (changed from http to https).

---

**Changes in PeptideShaker 1.16.14 (October 9. 2017):**

* BUG FIX: Fixed issues with getting data from QuickGO (changed from http to https).

---

**Changes in PeptideShaker 1.16.13 (September 5. 2017):**

* BUG FIX: Fixed issues with getting data from the new QuickGO, mainly required in the GO Analysis tab.

---

**Changes in PeptideShaker 1.16.12 (July 17. 2017):**

* BUG FIX: Fixed a broken link to the PDB for getting the protein structure information.

* LIBRARY UPDATE: Updated utilities to version 4.11.19.

---

**Changes in PeptideShaker 1.16.11 (June 23. 2017):**

* FEATURE IMPROVEMENT: Updated the example dataset.
* FEATURE IMPROVEMENT: Updated Ensembl Genomes to version 36.

* LIBRARY UPDATE: Updated utilities to version 4.11.17.

---

**Changes in PeptideShaker 1.16.10 (June 9. 2017):**

* FEATURE IMPROVEMENT: Updated Ensembl to version 89.
* FEATURE IMPROVEMENT: Cleaned up the help files. (work in progress)

* BUG FIX: Corrected errors in the mzIdentML export where only one modification was exported when having multiple modifications with the same mass shift.
* BUG FIX: Fixed bugs in the mzid export where only the main modifications were exported.
* BUG FIX: Fixed a bug where the default project name in the PRIDE Reshake could end up as too long.
* BUG FIX: Fixed a bug in the PRIDE Reshake that occurred if the enzyme was extracted from the mzid file but not mapped to utilities.

* LIBRARY UPDATE: Updated utilities to version 4.11.15.

---

**Changes in PeptideShaker 1.16.9 (May 16. 2017):**

* FEATURE IMPROVEMENT: Added a check for quotation marks in accession numbers when parsing FASTA files.

* BUG FIX: Corrected the links to the compomics.github.io wiki pages.

* LIBRARY UPDATE: Updated utilities to version 4.11.12.

---

**Changes in PeptideShaker 1.16.8 (May 14. 2017):**

* FEATURE IMPROVEMENT: Made it possible to export mzIdentML from the command line. 

* LIBRARY UPDATE: Updated utilities to version 4.11.11.

---

**Changes in PeptideShaker 1.16.7 (May 8. 2017):**

* BUG FIX: Fixed a typo in the "Dimethylation of K 2H4" PTM.

* LIBRARY UPDATE: Updated utilities to version 4.11.9.

---

**Changes in PeptideShaker 1.16.6 (May 8. 2017):**

* FEATURE IMPROVEMENT: Added "Dimethylation of K 2H4" to the standard list of PTMs.

* LIBRARY UPDATE: Updated utilities to version 4.11.8.

---

**Changes in PeptideShaker 1.16.5 (April 25. 2017):**

* FEATURE IMPROVEMENT: Updated Ensembl Genomes to version 35. 

* LIBRARY UPDATE: Updated utilities to version 4.11.7.

---

**Changes in PeptideShaker 1.16.4 (April 1. 2017):**

* FEATURE IMPROVEMENT: Updated Ensembl to version 88. 

* LIBRARY UPDATE: Updated JSparklines to version 1.0.9.
* LIBRARY UPDATE: Updated utilities to version 4.11.5.

---

**Changes in PeptideShaker 1.16.3 (March 17. 2017):**

* BUG FIX: Corrected errors in the handling of the validation QC parameters. 
* BUG FIX: Fixed bugs in the set up of the identification parameters from the command line. 

* LIBRARY UPDATE: Updated utilities to version 4.11.4.

---

**Changes in PeptideShaker 1.16.2 (March 5. 2017):**

* FEATURE IMPROVEMENT: Updated the Example Dataset.

---

**Changes in PeptideShaker 1.16.1 (March 2. 2017):**

* BUG FIX: Fixed a bug in the mzIdentML file reader that resulted in only the first SpectrumIdentificationItem being loaded for each SpectrumIdentificationResult element.
* BUG FIX: Removed the upper limitation for the number of threads/cores in the Processing Preferences dialog.
* BUG FIX: Increased the project batch size in the PRIDE Reshake from 100 to 200.

* LIBRARY UPDATE: Updated web-service-model to version 0.2.13.
* LIBRARY UPDATE: Updated utilities to version 4.11.2.

---

**Changes in PeptideShaker 1.16.0 (February 15. 2017):**

* BUG FIX: Fixed issues in the FASTA file indexing.
* BUG FIX: PSMs are now all accounted for PTM localization of the peptide.
* BUG FIX: Improved the interaction between the object cache and database. 

* LIBRARY UPDATE: Updated utilities to version 4.11.2.

---

**Changes in PeptideShaker 1.15.1 (February 8. 2017):**

* BUG FIX: Fixed a bug in the handling of neutral losses in the mzIdentML export.
* BUG FIX: Improved the interaction between the object cache and database. 

* LIBRARY UPDATE: Updated utilities to version 4.11.0.

---

**Changes in PeptideShaker 1.15.0 (January 31. 2017):**

* FEATURE IMPROVEMENT: Sped ups in the protein inference.
* FEATURE IMPROVEMENT: Increased the number of decimals for the scores in the mzIdentML export from two to four.

* BUG FIX: Cleaned-up the de novo import code. 

* LIBRARY UPDATE: Updated utilities to version 4.10.0.

---

**Changes in PeptideShaker 1.14.6 (December 21. 2016):**

* BUG FIX: Fixed bugs in the use of unspecific and whole protein as the digestion method.

* LIBRARY UPDATE: Updated utilities to version 4.8.9.

---

**Changes in PeptideShaker 1.14.5 (December 21. 2016):**

* BUG FIX: Fixed bugs in the IdentificationParametersInputBean for checking the isotope range where negative values were not allowed.

* LIBRARY UPDATE: Updated utilities to version 4.8.8.

---

**Changes in PeptideShaker 1.14.4 (December 12. 2016):**

* LIBRARY UPDATE: Updated xtandem-parser to version 1.8.0.
* LIBRARY UPDATE: Updated omssa-parser to version 1.12.0.
* LIBRARY UPDATE: Updated mascotdatfile to version 3.5.0.

---

**Changes in PeptideShaker 1.14.3 (December 11. 2016):**

* FEATURE IMPROVEMENT: Updated Ensembl to version 87.
* FEATURE IMPROVEMENT: Updated Ensembl genomes to version 34.
* FEATURE IMPROVEMENT: Deprecated the PRIDE XML export.

* BUG FIX: Refinement PTMs are no longer handled as variable PTMs in PeptideShaker.
* BUG FIX: Fixed format issues in the certificate of analysis.
* BUG FIX: Fixed a bug where the annotation sliders could get stuck.

* LIBRARY UPDATE: Updated utilities to version 4.8.7.

---

**Changes in PeptideShaker 1.14.2 (December 7. 2016):**

* BUG FIX: Added the PRIDE cluster confidence categories to PRIDE Reshake.
* BUG FIX: Fixed an issue in the Find feature where the focus was lost in the text input field.
* BUG FIX: Fixed a bug in the use of unspecific enzyme in the search settings dialog.
* BUG FIX: Fixed a bug in the spectrum annotator where the spectrum index was not reset when the intensity annotation limit changed.

* LIBRARY UPDATE: Updated utilities to version 4.8.6.

---

**Changes in PeptideShaker 1.14.1 (December 5. 2016):**

* BUG FIX: Fixed the backwards compatibility.

* LIBRARY UPDATE: Updated utilities to version 4.8.5.

---

**Changes in PeptideShaker 1.14.0 (December 4. 2016):**

* NEW FEATURE: Implemented the hyperscore for de novo mathces.

* FEATURE IMPROVEMENT: Extended and simplified the enzyme support.
* FEATURE IMPROVEMENT: Improved the use of the cache.
* FEATURE IMPROVEMENT: Improved some of the command line error messages.
* FEATURE IMPROVEMENT: Updated Ensembl genomes to version 33.
* FEATURE IMPROVEMENT: Minor speed improvements.
* FEATURE IMPROVEMENT: Improved the handling of the exception encountered when attempting to index too large databases.

* BUG FIX: Escaped a potential null exception that could occur when downloading gene mappings.
* BUG FIX: Corrected a bug where only the identified spectra were included in the export of non-validated PSMs.
* BUG FIX: Corrections to the PepXML export.

* LIBRARY UPDATE: Updated utilities to version 4.8.4.

----

**Changes in PeptideShaker 1.13.6 (October 10. 2016):**

* BUG FIX: Fixed a bug in the annotation of spectra with variable modifications.

* LIBRARY UPDATE: Updated utilities to version 4.7.5.

----

**Changes in PeptideShaker 1.13.5 (October 6. 2016):**

* FEATURE IMPROVEMENT: Updated Ensembl to version 86.
* FEATURE IMPROVEMENT: Added an export to file option for the default and user modifications.

* LIBRARY UPDATE: Updated utilities to version 4.7.4.

----

**Changes in PeptideShaker 1.13.4 (September 27. 2016):**

* FEATURE IMPROVEMENT: Added the option to include the protein sequences in the mzid export.
* FEATURE IMPROVEMENT: Speedups to the spectrum annotation processing.

* BUG FIX: Made sure that the log parameter is recognized when using the command line.
* BUG FIX: Corrected some exit process values with non zero on error conditions.
* BUG FIX: Minor correction in the tag mapper.

* LIBRARY UPDATE: Updated utilities to version 4.7.3.

----

**Changes in PeptideShaker 1.13.3 (September 10. 2016):**

* FEATURE IMPROVEMENT: Export the spectrum as an array list formatted as a string (via the identification feature export).

* BUG FIX: Fixed a null pointer that occurred if PeptideShakerCLI was used with path settings options.

* LIBRARY UPDATE: Updated utilities to version 4.7.2.

----

**Changes in PeptideShaker 1.13.1 (August 19. 2016):**

* NEW FEATURE: Added support for loading PEAKS Studio mzIdentML files.
* NEW FEATURE: Added support for loading Protein Pilot mzIdentML files.

* FEATURE IMPROVEMENT: Speed-ups in the use of the cache.

* BUG FIX: Fixed potential multithreading issues.

* LIBRARY UPDATE: Updated utilities to version 4.7.1.

----

**Changes in PeptideShaker 1.13.0 (August 13. 2016):**

* NEW FEATURE: Added support for loading Morpheus pepXML files.
* NEW FEATURE: Made it possible to export the fragment ions of secondary matches.

* FEATURE IMPROVEMENT: Updated GO and gene mappings to Ensembl 85 and 32.
* FEATURE IMPROVEMENT: Made the probability estimation of intermediate scores more conservative.
* FEATURE IMPROVEMENT: The consensus score is now estimated based on the confidence.

* FEATURE IMPROVEMENT: Spectra are now batch loaded prior to tag mapping.
* FEATURE IMPROVEMENT: The cache size is now set according to the memory available.
* FEATURE IMPROVEMENT: Attempt at making the command line exit codes follow the Unix convention.
* FEATURE IMPROVEMENT: Removed the upper limit for the number of amino acids shown before/after the peptide sequence.

* BUG FIX: Moved the instantiation of factories to after the setting of temporary paths in the CLIs.

* LIBRARY UPDATE: Updated utilities to version 4.7.0.

----

**Changes in PeptideShaker 1.12.3 (July 27. 2016):**

* BUG FIX: Fixed issues in the mzid export: made the file paths valid URIs and corrected a CV term name.

----

**Changes in PeptideShaker 1.12.2 (July 7. 2016):**

* FEATURE IMPROVEMENT: Fixed an issue in the mgf reader where lines ending with \r could cause problems.

* BUG FIX: Corrected a bug in the pepxml parser where start_scan was used instead if index to extract the spectrum number.
* BUG FIX: Corrected issues in the mzid export with regards to the annotation of neutral losses in mzid v1.1.

* LIBRARY UPDATE: Updated utilities to version 4.6.3.

----

**Changes in PeptideShaker 1.12.1 (June 26. 2016):**

 * BUG FIX: Corrected errors in the command line documentation and parameter testing.

 * LIBRARY UPDATE: Updated utilities to version 4.6.2.

----

**Changes in PeptideShaker 1.12.0 (June 24. 2016):**

 * FEATURE IMPROVEMENT: Updated the URIs for the PSI-MS and UO ontologies in the mzid export. 
 * FEATURE IMPROVEMENT: Removed the "final PSM list" CV term as it is no longer required.
 * FEATURE IMPROVEMENT: Added amino acid before/after and position to the default PSM export, and position to the default peptide export.

 * BUG FIX: Corrected the annotation of neutral losses in the mzid export.
 * BUG FIX: Fixed a minor formatting bug in the position output in the peptide export.
 * BUG FIX: Corrected typos in the documentation for the Validation terms in the custom exports at the peptide and PSM level.

 * LIBRARY UPDATE: Updated utilities to version 4.6.1.

----

**Changes in PeptideShaker 1.11.0 (June 7. 2016):**

 * NEW FEATURE: Added an export to PepXML as follow-up file. 
 * NEW FEATURE: It is now possible to skip the peptide PTM alignment step. 
 * NEW FEATURE: Added the possibility to tune the protein inference.

 * FEATURE IMPROVEMENT: Significantly sped up the peptide to protein mapping.
 * FEATURE IMPROVEMENT: PSM PTM site inference is now done after PTM site scoring. 
 * FEATURE IMPROVEMENT: Multithreaded the estimation of PSM scores. 
 * FEATURE IMPROVEMENT: Corrected potential threading issues and improved the multithreaded performance of the input and target decoy map.
 * FEATURE IMPROVEMENT: Peptides that are shorter or longer than the min/max peptide length allowed in the filters are now filtered out before the peptide validation starts.
 * FEATURE IMPROVEMENT: Changed the CV term for the immonium ions to the generic immonium ion CV term in the mzid export.
 * FEATURE IMPROVEMENT: Precursor ions (also with H20 and NH3 neutral losses) are now annotated in the mzIdentML export.
 * FEATURE IMPROVEMENT: Extended the list of supported neutral losses in the mzid export. 
 * FEATURE IMPROVEMENT: Added CV terms for the TMT and iTRAQ reporter ions in the mzid export. 

 * BUG FIX: Fixed a bug in the mzid export that could occur if a PSM had different PTM locations and/or PTM confidences than the parent peptide.

 * LIBRARY UPDATE: Updated xtandem parser to version 1.11.0, fixing a bug in the parsing of doubly modified terminals.
 * LIBRARY UPDATE: Updated utilities to version 4.5.20.

----

**Changes in PeptideShaker 1.10.3 (May 10. 2016):**

 * BUG FIX: Fixed a potential null pointer in the gene factory that could occur if there were no valid species in the FASTA file.

 * LIBRARY UPDATE: Updated utilities to version 4.5.17.

----

**Changes in PeptideShaker 1.10.2 (May 2. 2016):**

 * BUG FIX: Corrected a bug in the setting of the precursor mass filter. 
 * BUG FIX: Corrected a bug in the Gene Preferences dialog resulting in an error when no internet connection was available.

 * LIBRARY UPDATE: Updated utilities to version 4.5.16.

----

**Changes in PeptideShaker 1.10.1 (April 21. 2016):**

 * FEATURE IMPROVEMENT: Non-html characters are now escaped when exporting to protein descriptions in mzIdentML files.

 * BUG FIX: The maximum number of missed cleavage is now included in the certificate of analysis.

----

**Changes in PeptideShaker 1.10.0 (April 19. 2016):**

 * FEATURE IMPROVEMENT: Set the mass filter based on the search settings. 

 * BUG FIX: Corrected a bug in PhosphoRS leading to rounding errors. 
 * BUG FIX: Corrected potential threading issues in the estimation of masses.
 * BUG FIX: Corrected an error in the parsing of the maximal precursor deviation allowed in the import filters.
 * BUG FIX: Minor correction in the command line documentation for the import_precurosor_mz and import_precurosor_mz_ppm parameters.
 * BUG FIX: Corrected a bug in the annotation of confident sites.
 * BUG FIX: Corrected the target/decoy histogram plot.

 * LIBRARY UPDATE: Updated utilities to version 4.5.13.

----

**Changes in PeptideShaker 1.9.3 (April 7. 2016):**

 * FEATURE IMPROVEMENT: Multiple fixes and enhancements in PhosphoRS as suggested by @david-bouyssie.

 * BUG FIX: Corrected CV terms in the mzIdentML export.

 * LIBRARY UPDATE: Updated utilities to version 4.5.11.

----

**Changes in PeptideShaker 1.9.2 (April 1. 2016):**

* BUG FIX: Re-added the example dataset to the zip file.

----

**Changes in PeptideShaker 1.9.1 (April 1. 2016):**

 * FEATURE IMPROVEMENT: Updated Ensembl Genomes to version 31. 

 * BUG FIX: Fixed bugs in the modification type for "Dimethylation of peptide N-term 2H(4)" and "Dimethylation of peptide N-term".

 * LIBRARY UPDATE: Updated utilities to version 4.5.8.

----

**Changes in PeptideShaker 1.9.0 (March 16. 2016):**

 * FEATURE IMPROVEMENT: Speed improvements for the PTM scoring.
 * FEATURE IMPROVEMENT: Speed improvements for some of the exports.
 * FEATURE IMPROVEMENT: Added new PTM: Dimethylation of K 2H(6) 13C(2), also corrected "Dimethylation of peptide N-term K" to "Dimethylation of peptide N-term" and "Dimethylation of peptide N-term K 2H4" to "Dimethylation of peptide N-term 2H4".
 * FEATURE IMPROVEMENT: Updated the Ensembl mappings to version 84.

 * BUG FIX: Fixed bugs in the PTM scoring that could occur in rare cases.
 * BUG FIX: Fixed a bug in the background color for the drop down menus with tooltips.
 * BUG FIX: Fixed a bug in the PTM dialog where empty patterns were not handled correctly for user defined PTMs.
 * BUG FIX: Corrected a bug in the phosphorylation exports. 
 * BUG FIX: Fixed bugs in the validation of the following parameters when given as input on the command line: IMPORT_PRECURSOR_MZ_PPM, PREC_PPM, FRAG_PPM. Note that that the input is now binary (0 for Da and 1 for ppm, instead of 2 for Da and 1 for ppm as before).

 * LIBRARY UPDATE: jsparklines to version 1.0.8. 
 * LIBRARY UPDATE: Updated utilities to version 4.5.7.

----

**Changes in PeptideShaker 1.8.1 (March 4. 2016):**

* FEATURE IMPROVEMENT: Updated the default PTM localization settings. 

* BUG FIX: Correction in the iTRAQ 4-plex 115 mass.
* BUG FIX: It is now possible to open the ProteinInferenceSettingsDialog even if the FASTA file is not set.
* BUG FIX: The check for comma in PTM names now actually works.
* BUG FIX: Fixed bugs in the loading of de novo data.

* LIBRARY UPDATE: Updated utilities to version 4.5.3.

----

**Changes in PeptideShaker 1.8.0 (February 29. 2016):**

* FEATURE IMPROVEMENT: Sped up and corrected bugs in the PhosphoRS PTM scoring.
* FEATURE IMPROVEMENT: Extended the reports to include more information on peptide uniqueness.
* FEATURE IMPROVEMENT: Avoided very long mgf files missing warnings when selecting the id files.

* BUG FIX: Corrected a bug in the display of PTM scores in the PTMs tab.
* BUG FIX: Improved the test for checking if a user selected Java home folder contains a valid Java installation or not.

* LIBRARY UPDATE: Updated utilities to version 4.5.1.

----

**Changes in PeptideShaker 1.7.6 (February 12. 2016):**

* BUG FIX: Fixed a bug in the command line for locating FASTA files in other locations than the one in the parameter file.
* BUG FIX: Updated the certificate of analysis export.

----

**Changes in PeptideShaker 1.7.5 (February 12. 2016):**

* FEATURE IMPROVEMENT: Extended the peptide and PSM reports.

* BUG FIX: Fixed bugs in the PSM export that resulted in null pointers when exporting the algorithm scores.
* BUG FIX: If the output file on the command line is given as the file name only, this is now picked up and an error displayed.
* BUG FIX: Fixed GUI alignment issues in the Welcome dialog. 
* BUG FIX: Minor correction in the command line documentation for the comet_num_ptms option.
* BUG FIX: Corrected an error in the definition of the iTRAQ 8plex 115 ion. 
* BUG FIX: Made sure that the variable PTM names are checked (for if a PTM with that name exists) when setting up the identification parameters from the command line (the fixed PTM names were already checked).
* BUG FIX: Fixed a bug in the ProteinInferencePreferences that resulted in a null pointer if the database was not set (for example when the parameter file was created in DeNovoGUI).
* BUG FIX: Fixed a bug in the command line for displaying the list of supported PTMs, where the -out parameter was required.
* BUG FIX: Renamed the PTM "Dimethylation of K 2H(4)" to "Label of K 2H(4)". 

* LIBRARY UPDATE: Updated utilities to version 4.3.22.

----

**Changes in PeptideShaker 1.7.4 (February 8. 2016):**

* BUG FIX: Fixed bugs in the PSM export that resulted in null pointers when exporting the algorithm scores.

----

**Changes in PeptideShaker 1.7.3 (February 6. 2016):**

* BUG FIX: Fixed a bug in the mass deviation filter where min and max isotope had gotten mixed up.

* LIBRARY UPDATE: Updated utilities to version 4.3.21.

----

**Changes in PeptideShaker 1.7.2 (February 5. 2016):**

* BUG FIX: Fixed a bug in the loading of the user PTMs in the SearchSettingsDialog. 
* BUG FIX: User defined neutral losses and reporter ions are now loaded correctly when reading the PTM factory.
* BUG FIX: The PTM Dialog now checks if reporter ion and neutral loss names are unique before adding them.
* BUG FIX: Fixed a bug in the PTM Dialog where user defined neutral losses where always of type fixed.
* BUG FIX: Fixed a bug in the isSameAs method in ReporterIon that relied on theoretical mass and not composition.
* BUG FIX: Fixed bugs in the Gene Details dialog where protein groups was not supported.
* BUG FIX: Fixed a bug in the command line where a moved FASTA file could not be found even when in the SearchGUI zipped output.
* BUG FIX: Fixed a bug that resulted in it not being possible to sort on the Chromosome column.

* LIBRARY UPDATE: Updated jsparklines to version 1.0.7.
* LIBRARY UPDATE: Updated utilities to version 4.3.20.

----

**Changes in PeptideShaker 1.7.1 (February 1. 2016):**

* BUG FIX: Fixed an uncommon issue in the PTM scoring that could cause the processing of the data to fail.

----

**Changes in PeptideShaker 1.7.0 (January 28. 2016):**

* FEATURE IMPROVEMENT: Added support for Arg-N. 
* FEATURE IMPROVEMENT: Updated the Andromeda web page link.

* BUG FIX: Solved a potential threading issue in the peptide mass estimation.
* BUG FIX: Improved the handling of target only databases.
* BUG FIX: Corrected bugs in the PTM localization. 
* BUG FIX: Corrected the text relative to precursor filtering.

* LIBRARY UPDATE: Updated utilities to version 4.3.18.

----

**Changes in PeptideShaker 1.6.0 (January 26. 2016):**

* FEATURE IMPROVEMENT: Added support for isotope filtering.
* FEATURE IMPROVEMENT: Added the possibility to export neighboring amino acids in the PSM export.
* FEATURE IMPROVEMENT: Corrected the name of the precursor m/z deviation in the assumption filter.

* LIBRARY UPDATE: Updated utilities to version 4.3.17.

----

**Changes in PeptideShaker 1.5.1 (January 23. 2016):**

* LIBRARY UPDATE: Updated X!Tandem Parser to version 1.10.0, fixing a bug in the handling of multiple fixed PTMs of the same type on the same peptide.

----

**Changes in PeptideShaker 1.5.0 (January 22. 2016):**

* NEW FEATURE: Added peptide level modification QC plots.

* FEATURE IMPROVEMENT: Added support for Semi-GluC-(DE).

* BUG FIX: Improved the parsing of PTMs when parsing pepxml files. 
* BUG FIX: Fixed an issue that resulted in the tools not starting if a custom Java home was set and it could not be found.
* BUG FIX: Fixed issues in the mzIdentML and PRIDE XML exports in the escaping if quotes.
* BUG FIX: Fixed bugs in the protein coverage display.
* BUG FIX: Corrected bug in the PTM localization. 
* BUG FIX: Fixed a bug in the related ions where not all ions where added to the list.

* LIBRARY UPDATE: Updated X!Tandem Parser to version 1.9.0, fixing bugs in the ID file reader in the way multiple PTMs targeting the same residue was handled, in particular when one PTM was fixed and the other variable, e.g. as in variable TMT on n-term and fixed TMT on (n-term) K.
* LIBRARY UPDATE: Updated utilities to version 4.3.16.

----

**Changes in PeptideShaker 1.4.0 (January 15. 2016):**

* NEW FEATURE: Added support for related ions in the spectrum annotation. 

* FEATURE IMPROVEMENT: Improved the handling of datasets where variable modifications targeting termini and amino acids are searched together.
* FEATURE IMPROVEMENT: Updated the documentation of the peptide export.
* FEATURE IMPROVEMENT: Improved the handling of backed-up PTMs.

* BUG FIX: Fixed a bug where PTM names could be incorrectly assigned between PTMs of same mass.
* BUG FIX: Fixed a bug resulting in a duplicate key exception when not using PhosphoRS.
* BUG FIX: Fixed a bug in the neutral losses map where the reverse neutral losses were not added.

* LIBRARY UPDATE: Updated utilities to version 4.3.11.

----

**Changes in PeptideShaker 1.3.6 (January 8. 2016):**

* FEATURE IMPROVEMENT: Updated the ISAS logo in the Welcome and Getting Started dialogs.

* BUG FIX: Fixed an issue in the pepxml parser where peptides with both a fixed and a variable modification on the same residue (for example carbamidomethyl and pyro-c on the n-term) were not parsed correctly.

* LIBRARY UPDATE: Updated utilities to version 4.3.8.

----

**Changes in PeptideShaker 1.3.5 (January 7. 2016):**

* BUG FIX: Fixed bugs in the escaping of non-standard characters in the mzIdentML and PRIDE XML exports, which resulted in invalid files.

----

**Changes in PeptideShaker 1.3.4 (January 6. 2016):**

* BUG FIX: Fixed a bug in the command line link between SearchGUI and PeptideShaker.
* BUG FIX: Fixed an issue where the enzyme could be reset to Trypsin when using the command line.
* BUG FIX: Corrected the mass for the pY reporter ion.

* LIBRARY UPDATE: Updated utilities to version 4.3.7.

----

**Changes in PeptideShaker 1.3.3 (January 5. 2016):**

* FEATURE IMPROVEMENT: Added support for the number of missed cleavages filters to the command line.
* FEATURE IMPROVEMENT: Corrected minor issues with the command line documentation and made it more readable.

* BUG FIX: Fixed a bug in the creation of parameter files from the command line.

* LIBRARY UPDATE: Updated utilities to version 4.3.6.

----

**Changes in PeptideShaker 1.3.2 (December 31. 2015):**

* NEW FEATURE: Added import filter for the number of missed cleavages for the peptides. 

* FEATURE IMPROVEMENT: Made sure that the 24 hour format is used in all time stamps.
* FEATURE IMPROVEMENT: Updated the ISAS logo in the splash screen.

* BUG FIX: Fixed possible issues in the methods for checking if a peptide is at the protein terminals.

* LIBRARY UPDATE: Updated utilities to version 4.3.5.

----

**Changes in PeptideShaker 1.3.1 (December 28. 2015):**

* BUG FIX: Fixed a bug in the creation of an identification settings file via the GUI.

* LIBRARY UPDATE: Updated utilities to version 4.3.4.

----

**Changes in PeptideShaker 1.3.0 (December 23. 2015):**

* NEW FEATURE: A log folder can now be selected when operating in command line.

* FEATURE IMPROVEMENT: Added options for starting PRIDE Reshake with a given PX accession from the command line.
* FEATURE IMPROVEMENT: Added support for Semi-Arg-C.
* FEATURE IMPROVEMENT: Added links to PRIDE Inspector and ProteomeXchange in the mzIdentML export complete dialog.
* FEATURE IMPROVEMENT: The protein inference database is now also updated if it is the same as the search database and not found when loading search result files.
* FEATURE IMPROVEMENT: Updated the Ensembl mappings to version 83.
* FEATURE IMPROVEMENT: Updated the Ensembl Genomes mapping to version 30.
* FEATURE IMPROVEMENT: Improved the names of the plots in the Validation tab and updated the help text accordingly.
* FEATURE IMPROVEMENT: First attempt at supporting fragment ion tolerance in ppm. 
* FEATURE IMPROVEMENT: The precursor and fragment ion tolerance types are now extracted from PRIDE XML files when using PRIDE Reshake.

* BUG FIX: Improved the mzIdentML reader to be able to distinguish fixed and variable terminal modifications with the same accession and mass.
* BUG FIX: The UniProt taxonomy mapping is now loaded before working with the identification parameters avoiding a null pointer when loading files containing search parameters only.
* BUG FIX: Fixed a bug in the Filter dialogs where it was impossible to add filters unless there was at least one filter already in the table.
* BUG FIX: Fixed a minor bug in the canceling of the Filter dialogs.
* BUG FIX: Fixed bugs in the reprocessing of private PRIDE data. 
* BUG FIX: Added a fix for a Java bug where the button for the scroll bar could disappear on certain Java versions.
* BUG FIX: Corrected the escaping if illegal characters when exporting to PRIDE XML and mzIdentML.
* BUG FIX: The H2O neutral losses are now back in the FragmentIonTable. 
* BUG FIX: The bubble plots now react to the user annotation settings.
* BUG FIX: Fixed an error in the "Thermolysin, no P rule" enzyme, where the P rule was actually added.
* BUG FIX: Corrected a bug where the Tide format was not displayed properly.
* BUG FIX: Fixed a bug where the processing of the neutral losses could cancel the loading of the data.

* LIBRARY UPDATE: Updated utilities to version 4.3.3.

----

**Changes in PeptideShaker 1.2.2 (December 7. 2015):**

* LIBRARY UPDATE: Updated utilities to version 4.1.15.

----

**Changes in PeptideShaker 1.2.1 (December 6. 2015):**

* FEATURE IMPROVEMENT: Added support for new enzyme: Trypsin + Glu-C.

* BUG FIX: Added a temporary fix for importing c-terminal modifications for Comet.
* BUG FIX: Fixed a null pointer that occurred if trying to open a new project from inside PeptideShaker.

* LIBRARY UPDATE: Updated utilities to version 4.1.14.

----

**Changes in PeptideShaker 1.2.0 (December 2. 2015):**

* FEATURE IMPROVEMENT: Added support for LysargiNase.
* FEATURE IMPROVEMENT: Improved the Validation plots.
* FEATURE IMPROVEMENT: Updated the parameters related classes to work with json files
* FEATURE IMPROVEMENT: Added support for exporting the sequence coverage plot. 
* FEATURE IMPROVEMENT: Implemented speed ups in the protein groups handling.
* FEATURE IMPROVEMENT: Re-added the CV term for the Andromeda result files to the mzid export.
* FEATURE IMPROVEMENT: Added tooltips to all validation plots.
* FEATURE IMPROVEMENT: The methods report now includes the occurrence of the species. 
* FEATURE IMPROVEMENT: Updated the Example Dataset.

* BUG FIX: Fixed issues with the high resolution exports of the plots in the Spectrum IDs tab.
* BUG FIX: Added a temporary fix to the Progenesis export.
* BUG FIX: Fixed a rare bug in the Confidence plot that occurred if two consecutive x-values were identical, which messed up the color coding.
* BUG FIX: Fixed a bug in the #Unique PSMs plot in the Spectrum IDs tab.
* BUG FIX: Fixed a possible null pointer in the protein inference peptide level dialog.

* LIBRARY UPDATE: Updated utilities to version 4.1.13.

----

**Changes in PeptideShaker 1.1.3 (October 22. 2015):**

* BUG FIX: Made the tool work on Java 1.6 again.

* LIBRARY UPDATE: Updated utilities to version 4.1.8.

----

**Changes in PeptideShaker 1.1.2 (October 16. 2015):**

 * FEATURE IMPROVEMENT: Updated Ensembl Genomes to version 29.

 * BUG FIX: Fixed a typo in the Annotation tab.

 * LIBRARY UPDATE: Updated utilities to version 4.1.1.

----

**Changes in PeptideShaker 1.1.1 (October 14. 2015):**

 * FEATURE IMPROVEMENT: Extended the user selected file methods to support suggested/default file names.

 * LIBRARY UPDATE: Updated utilities to version 4.0.15.

----

**Changes in PeptideShaker 1.1.0 (October 12. 2015):**

 * FEATURE IMPROVEMENT: Sped up the peptide to protein mapping.

 * BUG FIX: Corrected a bug in the use of the temp folder in command line (thanks to Jean-Francois Lucier).
 * BUG FIX: Cleaned up some of the saving code which would not work without a waiting handler.

 * LIBRARY UPDATE: Updated omssa-parser to version 1.7.1.
 * LIBRARY UPDATE: Updated xtandem-parser to version 1.8.1.
 * LIBRARY UPDATE: Updated mascotdatfile to version 3.4.32.
 * LIBRARY UPDATE: Updated utilities to version 4.0.14.

----

**Changes in PeptideShaker 1.0.9 (October 3. 2015):**

 * LIBRARY UPDATE: Updated utilities to version 4.0.13.

----

**Changes in PeptideShaker 1.0.8 (October 1. 2015):**

 * LIBRARY UPDATE: Updated utilities to version 4.0.12.

----

**Changes in PeptideShaker 1.0.7 (October 1. 2015):**

 * BUG FIX: Corrected references to the outdated cps file format (now cpsx) for some of the command lines.

----

**Changes in PeptideShaker 1.0.6 (October 1. 2015):**

 * FEATURE IMPROVEMENT: Updated Ensembl to version 82.

 * LIBRARY UPDATE: Updated utilities to version 4.0.10.

----

**Changes in PeptideShaker 1.0.5 (September 29. 2015):**

 * FEATURE IMPROVEMENT: Made sure that the default PTM scoring is the same for both the GUI and the command line.
 * FEATURE IMPROVEMENT: Cleaned up the GUI for handling the PTM score selection.

 * LIBRARY UPDATE: Updated utilities to version 4.0.9.

---

**Changes in PeptideShaker 1.0.4 (September 27. 2015):**

 * BUG FIX: Fixed a bug in the mzIdentML export required to be compatible with the next Skyline release.
 * BUG FIX: Fixed a bug in the mzIdentML export where the file format for MyriMatch was set to tab delimited instead if mzid.

---

**Changes in PeptideShaker 1.0.3 (September 23. 2015):**

 * FEATURE IMPROVEMENT: Extended the timeout when mapping peptides to proteins.
 * FEATURE IMPROVEMENT: Improved the handling of the advanced search engine settings in the search parameters.
 * FEATURE IMPROVEMENT: Added the version number to the Welcome and About dialogs. 
 * FEATURE IMPROVEMENT: Started improving and extending the protein inference dialogs. 

 * LIBRARY UPDATE: Updated utilities to version 4.0.8.

---

**Changes in PeptideShaker 1.0.2 (September 12. 2015):**

 * FEATURE IMPROVEMENT: The XYPlottingDialog can now be opened by right clicking the column headers as well, and now opens the given column as a density chart as a default.

 * BUG FIX: Corrected a bug in the validation of PSMs that could cancel the processing.
 * BUG FIX: Fixed a possible null pointer in the output exporter.
 * BUG FIX: Fixed a possible null pointer in the PTM tab.
 * BUG FIX: Fixed bugs in the spectrum annotation menu where the mz ion table and bubble plot bar options could not be turned on.

 * LIBRARY UPDATE: Updated jsparklines to version 1.0.6.
 * LIBRARY UPDATE: Updated utilities to version 4.0.5.

---

**Changes in PeptideShaker 1.0.1 (September 3. 2015):**

 * BUG FIX: Fixed an issue with the wrapper in handling memory warnings for 32 bit Java 8.

 * LIBRARY UPDATE: Updated utilities to version 4.0.4.

---

**Changes in PeptideShaker 1.0.0 (August 27. 2015):**

 * NEW FEATURE: PTM masses are now set via the atomic composition.
 * NEW FEATURE: Added a spectrum export.
 * NEW FEATURE: Added the normalized spectrum counting to the export.
 * NEW FEATURE: Renamed .cps to .cpsx and .parameters to .par.

 * FEATURE IMPROVEMENT: Updated Ensembl to version 81.
 * FEATURE IMPROVEMENT: Made sure that the content of CV and user parameters is escaped for non-supported characters when exporting to XML. 
 * FEATURE IMPROVEMENT: Improved the naming of the peptide and PSM subgroups in the Validation tab.

 * BUG FIX: Fixed bugs in PathSettingsCLI where the paths could not be set. 
 * BUG FIX: Corrected potential concurrency issues.
 * BUG FIX: Fixed a bug in the Find feature where the peptide matches were added to the protein map, which resulted in them not being batch loaded.
 * BUG FIX: Fixed a bug where search mzIdentML results without PTMs could not be parsed.

 * LIBRARY UPDATE: Updated mascotdatfile to version 3.4.31.
 * LIBRARY UPDATE: Updated xtandem-parser to version 1.8.0.
 * LIBRARY UPDATE: Updated omssa-parser to version 1.7.0.
 * LIBRARY UPDATE: Updated utilities to version 4.0.0.

---
