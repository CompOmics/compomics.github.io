---
name: ReleaseNotes
project: searchgui
layout: default
permalink: /searchgui/wiki/releasenotes.html
github_project: https://github.com/compomics/searchgui
---

# Release Notes

----

**Changes in SearchGUI 2.8.2 (April 7. 2016):**

* FEATURE IMPROVEMENT: Updated Comet to version 2016.01 rev. 2.
 * For details, please see: http://comet-ms.sourceforge.net/release/release_201601/.

* LIBRARY UPDATE: Updated utilities to version 4.5.11.

----

**Changes in SearchGUI 2.8.1 (April 1. 2016):**

* FEATURE IMPROVEMENT: Updated Comet to version 2016.01 rev. 1.
 * For details, please see: http://comet-ms.sourceforge.net/release/release_201601/.

* BUG FIX: Fixed bugs in the modification type for "Dimethylation of peptide N-term 2H(4)" and "Dimethylation of peptide N-term".

* LIBRARY UPDATE: Updated utilities to version 4.5.8.

----

**Changes in SearchGUI 2.8.0 (March 16. 2016):**

* NEW FEATURE: Added a check for missing precursor charges when parsing mgf files, and the option of adding them. All controlled via the Advanced Settings.

* FEATURE IMPROVEMENT: Updated Comet to version 2016.01 rev. 0.
 * For details, please see: http://comet-ms.sourceforge.net/release/release_201601/.
* FEATURE IMPROVEMENT: The Advanced Settings are now saved between each time one runs SearchGUI.
* FEATURE IMPROVEMENT: Added new PTM: Dimethylation of K 2H(6) 13C(2), also corrected "Dimethylation of peptide N-term K" to "Dimethylation of peptide N-term" and "Dimethylation of peptide N-term K 2H4" to "Dimethylation of peptide N-term 2H4".
* FEATURE IMPROVEMENT: Updated the Ensembl mappings to version 84.

* BUG FIX: Fixed bugs in the validation of the following parameters when given as input on the command line: IMPORT_PRECURSOR_MZ_PPM, PREC_PPM, FRAG_PPM. Note that that the input is now binary (0 for Da and 1 for ppm, instead of 2 for Da and 1 for ppm as before).
* BUG FIX: Fixed a bug in the PTM dialog where empty patterns were not handled correctly for user defined PTMs.
* BUG FIX: Fixed a bug in the background color for the drop down menus with tooltips.

* LIBRARY UPDATE: Updated jsparklines to version 1.0.8.
* LIBRARY UPDATE: Updated utilities to version 4.5.7.

----

**Changes in SearchGUI 2.7.1 (March 4. 2016):**

* FEATURE IMPROVEMENT: Updated the default PTM localization settings.

* BUG FIX: Correction in the iTRAQ 4-plex 115 mass.
* BUG FIX: It is now possible to open the ProteinInferenceSettingsDialog even if the FASTA file is not set.
* BUG FIX: Fixed a bug in the isSameAs method in PeptideAssumptionFilter.
* BUG FIX: The check for comma in PTM names now actually works.

* LIBRARY UPDATE: Updated utilities to version 4.5.3.

----

**Changes in SearchGUI 2.7.0 (February 29. 2016):**

* FEATURE IMPROVEMENT: Updated X!Tandem to version VENGEANCE (2015.12.15).
 * Note that X!Tandem no longer releases 32 bit versions, only the 64 bit versions will be updated from now on.
* FEATURE IMPROVEMENT: Extended the list of supported output formats for Comet. 
* FEATURE IMPROVEMENT: ProteoWizard is now shown as supported on all platforms (but converting vendor raw files is still only supported in Windows).

* BUG FIX: Improved the test for checking if a user selected Java home folder contains a valid Java installation or not.

* LIBRARY UPDATE: Updated utilities to version 4.3.22.

----

**Changes in SearchGUI 2.6.5 (February 12. 2016):**

* BUG FIX: Minor correction in the command line documentation for the comet_num_ptms option.
* BUG FIX: Corrected an error in the definition of the iTRAQ 8plex 115 ion. 
* BUG FIX: Made sure that the variable PTM names are checked (for if a PTM with that name exists) when setting up the identification parameters from the command line (the fixed PTM names were already checked).
* BUG FIX: Fixed a bug in the ProteinInferencePreferences that resulted in a null pointer if the database was not set (for example when the parameter file was created in DeNovoGUI).
* BUG FIX: Fixed a bug in the command line for displaying the list of supported PTMs, where the -out parameter was required.
* BUG FIX: Renamed the PTM "Dimethylation of K 2H(4)" to "Label of K 2H(4)". 

* LIBRARY UPDATE: Updated utilities to version 4.3.22.

----

**Changes in SearchGUI 2.6.4 (February 8. 2016):**

* FEATURE IMPROVEMENT: If the user cancels a partial search (in the GUI) the user is now asked if he/she wants to keep the partial search results (instead of automatic removal as before).

----

**Changes in SearchGUI 2.6.3 (February 6. 2016):**

* BUG FIX: Fixed a bug in the mass deviation filter where min and max isotope had gotten mixed up.

* LIBRARY UPDATE: Updated utilities to version 4.3.21.

----

**Changes in SearchGUI 2.6.2 (February 5. 2016):**

* BUG FIX: Fixed a bug in the loading of the user PTMs in the SearchSettingsDialog. 
* BUG FIX: The PTM Dialog now checks if reporter ion and neutral loss names are unique before adding them.
* BUG FIX: Fixed a bug in the PTM Dialog where user defined neutral losses where always of type fixed.
* BUG FIX: Changed the default for the MyriMatch MaxPeakCount parameter back to the default of 300.

* LIBRARY UPDATE: Updated jsparklines to version 1.0.7.
* LIBRARY UPDATE: Updated utilities to version 4.3.20.

----

**Changes in SearchGUI 2.6.1 (January 28. 2016):**

* FEATURE IMPROVEMENT: Added support for Arg-N.
* FEATURE IMPROVEMENT: Updated the Andromeda web page link. 

* LIBRARY UPDATE: Updated utilities to version 4.3.18.

----

**Changes in SearchGUI 2.6.0 (January 26. 2016):**

* FEATURE IMPROVEMENT: Updated MS Amanda to version v1.0.0.6299 for Windows and version v1.0.0.6300 for Linux and Mac.
* FEATURE IMPROVEMENT: Added support for setting the X!Tandem output type (all, valid, stochastic).

* BUG FIX: Fixed a bug in the X!Tandem and Tide enzyme setup for enzymes with no restriction amino acids.

* LIBRARY UPDATE: Updated utilities to version 4.3.17.

----

**Changes in SearchGUI 2.5.0 (January 22. 2016):**

* FEATURE IMPROVEMENT: Updated Comet to release 2015.02 rev. 5, improving the mgf parsing.
* FEATURE IMPROVEMENT: Added support for Semi-GluC-(DE).

* BUG FIX: Fixed an issue that resulted in the tool not starting if a custom Java home was set and it could not be found.
* BUG FIX: Fixed a bug in the command line where the parameter file was not added correctly to the zipped output file.

* LIBRARY UPDATE: Updated utilities to version 4.3.16.

----

**Changes in SearchGUI 2.4.1 (January 18. 2016):**

* BUG FIX: Fixed a bug in the use of the time stamp for the zip file output. 

----

**Changes in SearchGUI 2.4.0 (January 15. 2016):**

* FEATURE IMPROVEMENT: Updated Tide to version 2.1.16872, adding a 64 bit version for Windows that is both faster and able to handle bigger FASTA files.

* BUG FIX: Fixed a bug in the advanced settings dialog where the zipping options were not displayed correctly upon reopening the dialog.

* LIBRARY UPDATE: Updated utilities to version 4.3.11.

----

**Changes in SearchGUI 2.3.5 (January 8. 2016):**

* FEATURE IMPROVEMENT: Updated Comet to release 2015.02 rev. 4, improving the mgf parsing.
* FEATURE IMPROVEMENT: Added wiff files to the list of raw file formats supported in msconvert.

* LIBRARY UPDATE: Updated utilities to version 4.3.8.

----

**Changes in SearchGUI 2.3.4 (January 6. 2016):**

* BUG FIX: Fixed a bug in the command line link between SearchGUI and PeptideShaker.
* BUG FIX: Fixed an issue where the enzyme could be reset to Trypsin when using the command line.
* BUG FIX: Corrected the mass for the pY reporter ion.

* LIBRARY UPDATE: Updated utilities to version 4.3.7.

----

**Changes in SearchGUI 2.3.3 (January 5. 2016):**

* FEATURE IMPROVEMENT: Added support for the number of missed cleavages filters to the command line.
* FEATURE IMPROVEMENT: Corrected minor issues with the command line documentation and made it more readable.

* BUG FIX: Fixed a bug in the creation of parameter files from the command line.

* LIBRARY UPDATE: Updated utilities to version 4.3.6.

----

**Changes in SearchGUI 2.3.2 (December 31. 2015):**

* NEW FEATURE: Added import filter for the number of missed cleavages for the peptides when loading in PeptideShaker. 

* FEATURE IMPROVEMENT: Updated the ISAS logo in the splash screen. 
* FEATURE IMPROVEMENT: Removed an unnecessary white space in the modification tag in the MS Amanda settings file.
* FEATURE IMPROVEMENT: Made sure that the 24 hour format is used in all time stamps. 
* FEATURE IMPROVEMENT: Improved the formatting of the file names for the advanced zipping output options.

* LIBRARY UPDATE: Updated utilities to version 4.3.5.

----

**Changes in SearchGUI 2.3.1 (December 28. 2015):**

* BUG FIX: Fixed a bug in the creation of an identification settings file via the GUI.

* LIBRARY UPDATE: Updated utilities to version 4.3.4.

----

**Changes in SearchGUI 2.3.0 (December 23. 2015):**

 * NEW FEATURE: A log folder can now be selected when operating in command line.

 * FEATURE IMPROVEMENT: The isotopic correction is now part of the main search parameters. 
 * FEATURE IMPROVEMENT: First attempt at supporting fragment ion tolerance in ppm.
 * FEATURE IMPROVEMENT: Added support for Semi-Arg-C.
 * FEATURE IMPROVEMENT: The mgf file is now given to Comet directly.
 * FEATURE IMPROVEMENT: Updated the Ensembl mappings to version 83. 
 * FEATURE IMPROVEMENT: Updated the Ensembl Genomes mapping to version 30.
 * FEATURE IMPROVEMENT: Corrected the names used for the enzymatic cleavage types in the Comet Advanced Settings dialog (according to corrected documentation for Comet).

 * BUG FIX: Fixed a bug in the MS Amanda setup where the highest charge in the selected range was not added, e.g. [2-4] became [2-3].
 * BUG FIX: Fixed an error in the "Thermolysin, no P rule" enzyme, where the P rule was actually added.
 * BUG FIX: The MS Amanda enzyme file is now generated each time MS Amanda is run, and now supports all enzymes (except Asp-N + Glu-C).
 * BUG FIX: Corrected issues in the Formic Acid and Trypsin + Glu-C enzymes for MS Amanda.
 * BUG FIX: Added a fix for a Java bug where the button for the scroll bar could disappear on certain Java versions.
 * BUG FIX: The UniProt taxonomy mapping is now loaded before working with the identification parameters avoiding a null pointer when loading files containing search parameters only.
 * BUG FIX: Fixed a bug where the identification parameters file was not set in SearchCLI.
 * BUG FIX: Fix the saving of the advanced settings for search engines so that the general search settings are not reset.

 * LIBRARY UPDATE: Updated utilities to version 4.3.3.

----

**Changes in SearchGUI 2.2.2 (December 7. 2015):**

 * BUG FIX: Fixed a bug in the MS-GF+ enzyme mapping for GluC.

 * LIBRARY UPDATE: Updated utilities to version 4.1.15.

----

**Changes in SearchGUI 2.2.1 (December 6. 2015):**

 * FEATURE IMPROVEMENT: Added support for new enzyme: Trypsin + Glu-C.

 * BUG FIX: Fixed a bug where Andromeda changed the general enzyme properties when settings up its own enzymes.

 * LIBRARY UPDATE: Updated utilities to version 4.1.13.

----

**Changes in SearchGUI 2.2.0 (December 2. 2015):**

 * FEATURE IMPROVEMENT: Updated Comet to version 2015.02 rev. 3.
 * FEATURE IMPROVEMENT: Support for LysargiNase and extended enzyme support for MyriMatch and MS-GF+.
 * FEATURE IMPROVEMENT: Added support for partial digest for Andromeda.
 * FEATURE IMPROVEMENT: Partial digest is now set for Tide based on the enzyme selected.
 * FEATURE IMPROVEMENT: Updated the parameters related classes to work with json files.
 * FEATURE IMPROVEMENT: Changed the X!Tandem and OMSSA logos to be the same format as the other logos.

 * BUG FIX: Fixed a bug that affected variable n-term modification without specific targets when running Comet.

 * LIBRARY UPDATE: Updated utilities to version 4.1.13.

----

**Changes in SearchGUI 2.1.4 (October 22. 2015):**

 * BUG FIX: Made the tool work on Java 1.6 again.

 * LIBRARY UPDATE: Updated utilities to version 4.1.8.

----

**Changes in SearchGUI 2.1.3 (October 16. 2015):**

 * FEATURE IMPROVEMENT: Updated Ensembl Genomes to version 29.

 * LIBRARY UPDATE: Updated utilities to version 4.1.1.

----

**Changes in SearchGUI 2.1.2 (October 15. 2015):**

 * BUG FIX: Fixed a bug in the mgf splitting.

----

**Changes in SearchGUI 2.1.1 (October 14. 2015):**

 * FEATURE IMPROVEMENT: Enabled the multithreading for msconvert.
 * FEATURE IMPROVEMENT: Made it possible to cancel msconvert processes.
 * FEATURE IMPROVEMENT: Prevented processes from starting in case the search has been cancelled.

 * LIBRARY UPDATE: Updated utilities to version 4.0.15.

----

**Changes in SearchGUI 2.1.0 (October 12. 2015):**

 * FEATURE IMPROVEMENT: The Andromeda temp folder is only deleted once all mgf files have been searched.
 * FEATURE IMPROVEMENT: Cleaned up the handling of exceptions to avoid printing stack traces.

 * LIBRARY UPDATE: Updated utilities to version 4.0.14.

----

**Changes in SearchGUI 2.0.11 (October 3. 2015):**

 * BUG FIX: Fixed a possible null pointer related to PTMs not targeting specific amino acids when setting up X!Tandem searches.
 * BUG FIX: Fixed a bug in the mgf parser where comments between the peak lists was not supported.

 * LIBRARY UPDATE: Updated utilities to version 4.0.13.

----

**Changes in SearchGUI 2.0.10 (October 1. 2015):**

 * BUG FIX: Fixed bugs in the search parameters where the advanced search engine settings had gone missing.

 * LIBRARY UPDATE: Updated utilities to version 4.0.12.

----

**Changes in SearchGUI 2.0.9 (October 1. 2015):**

 * FEATURE IMPROVEMENT: Improved how some of the dialogs resize in low screen resolution conditions.

 * LIBRARY UPDATE: Updated utilities to version 4.0.11.

----

**Changes in SearchGUI 2.0.8 (October 1. 2015):**
 
 * FEATURE IMPROVEMENT: Updated Comet to version 2015.02 rev. 1.
 * FEATURE IMPROVEMENT: Updated Ensembl to version 82.

 * LIBRARY UPDATE: Updated utilities to version 4.0.10.

----

**Changes in SearchGUI 2.0.7 (September 26. 2015):**

 * FEATURE IMPROVEMENT: Added a command line option (-fasta) that makes it possible to override the FASTA file location in the search parameter file used.

----

**Changes in SearchGUI 2.0.6 (September 23. 2015):**

 * BUG FIX: Improved the handling of the advanced search engine settings in the search parameters.

 * LIBRARY UPDATE: Updated utilities to version 4.0.8.

----

**Changes in SearchGUI 2.0.5 (September 17. 2015):**

 * BUG FIX: Fixed a bug in the Comet command line that occurred when a non-standard Comet temp folder was used.

 * LIBRARY UPDATE: Updated jsparklines to version 1.0.6. 
 * LIBRARY UPDATE: Updated utilities to version 4.0.5.

----

**Changes in SearchGUI 2.0.4 (September 4. 2015):**

 * BUG FIX: Another attempt at fixing a bug where the output folder was deleted instead of the temp folder.

----

**Changes in SearchGUI 2.0.3 (September 4. 2015):**

 * BUG FIX: Fixed a bug where the output folder was deleted instead of the temp folder. Only affected Linux.

----

**Changes in SearchGUI 2.0.2 (September 3. 2015):**

 * BUG FIX: Improved the handling of the file path in the search settings files.
 * BUG FIX: Fixed an issue with the wrapper in handling memory warnings for 32 bit Java 8.

 * LIBRARY UPDATE: Updated utilities to version 4.0.4.

----

**Changes in SearchGUI 2.0.1 (August 30. 2015):**

 * BUG FIX: Fixed a bug that canceled the command line use.

----

**Changes in SearchGUI 2.0.0 (August 27. 2015):**

 * NEW FEATURE: Added support for Andromeda. (beta)
 * NEW FEATURE: PTM masses are now set via the atomic composition.
 * NEW FEATURE: Renamed .cps to .cpsx and .parameters to .par.

 * FEATURE IMPROVEMENT: Updated MS Amanda to version 1.0.0.5242 for Windows and version 1.0.0.5243 for Linux/Mac.
  * Bugfix for n-terminal modifications targeting a specific amino acid.
  * Bugfix for database digestion.
  * Alternative modification site consideration.
  * Performance improvements.
 * FEATURE IMPROVEMENT: Updated Comet to version 2015.02 rev. 0.
 * FEATURE IMPROVEMENT: The user is now asked if the settings should be saved if the advanced search engine settings are changed.
 * FEATURE IMPROVEMENT: The Tide enzyme parameter is now mapped to the Tide enzyme name if possible (to ensure compatibility with TPP when exporting as pepxml.)
 * FEATURE IMPROVEMENT: Updated Ensembl to version 81.

 * BUG FIX: Fixed bugs in PathSettingsCLI where the paths could not be set.
 * BUG FIX: Corrected an error that could occur when working with raw files.
 * BUG FIX: Corrected an error in the handling of filters options for msconvert.

 * LIBRARY UPDATE: Updated utilities to version 4.0.0.

----

**Changes in SearchGUI 1.30.1 (June 30. 2015):**

 * BUG FIX: Removed test code.

----

**Changes in SearchGUI 1.30.0 (June 30. 2015):**

 * NEW FEATURE: Added support for raw files as input to SearchGUI via  PRIDE Reshake.

 * FEATURE IMPROVEMENT: Reduced the height of the SearchGUI main dialog to better fit on smaller screens.

 * LIBRARY UPDATE: Updated utilities to version 3.49.21.

----

**Changes in SearchGUI 1.29.0 (June 21. 2015):**

 * NEW FEATURE: Added pre-processing of raw files using msConvert. 

 * FEATURE IMPROVEMENT: Fixed a backwards compatibility issue with the search settings.

 * BUG FIX: Fixed a bug in the GO mappings that resulted from a change in the Ensembl BioMart.

 * LIBRARY UPDATE: Updated utilities to version 3.49.19.

----

**Changes in SearchGUI 1.28.1 (June 6. 2015):**

 * LIBRARY UPDATE: Updated utilities to version 3.49.7.

----

**Changes in SearchGUI 1.28.0 (June 2. 2015):**

 * FEATURE IMPROVEMENT: Updated MS Amanda to version 1.0.0.4850 for Windows and version 1.0.0.4851 for Linux/Mac.
  * Fixing a bug where n-terminal modifications targeting a specific amino acid caused MS Amanda to crash.
 * FEATURE IMPROVEMENT: Updated the Ensembl mappings to Ensembl 80. 
 * FEATURE IMPROVEMENT: Changed the default isotope correction range for MS-GF+ from [0,1] to [-1,2].

 * BUG FIX: Fixed issues with validating some of the OMSSA parameters when used via the command line.

 * LIBRARY UPDATE: Updated utilities to version 3.49.2.

----

**Changes in SearchGUI 1.27.4 (May 16. 2015):**

 * FEATURE IMPROVEMENT: Added support for parsing UniRef headers.

 * LIBRARY UPDATE: Updated utilities to version 3.48.5.

----

**Changes in SearchGUI 1.27.3 (May 12. 2015):**

 * FEATURE IMPROVEMENT: Leading and trailing white space is now removed before parsing FASTA headers.

 * LIBRARY UPDATE: Updated utilities to version 3.48.4.

----

**Changes in SearchGUI 1.27.2 (April 25. 2015):**

 * BUG FIX: Corrected bugs in the setting of temporary folders.
 * BUG FIX: Fixed a bug in the CV term mapping for pyro-cmc.

 * LIBRARY UPDATE: Updated utilities to version 3.47.4. 

----

**Changes in SearchGUI 1.27.1 (April 13. 2015):**

 * FEATURE IMPROVEMENT: Updated MS Amanda to version 1.0.0.4484 for Windows and version 1.0.0.4458 for Linux/Mac.
  * Fixing an issue with the test for FASTA file file name length.

 * LIBRARY UPDATE: Updated utilities to version 3.46.13. 

----

**Changes in SearchGUI 1.27.0 (April 11. 2015):**

 * FEATURE IMPROVEMENT: Updated MS Amanda to version 1.0.0.4456 for Windows and version 1.0.0.4457 for Linux/Mac.
  * Adding a low memory option.
  * Support for mgf files with empty charge tags.
  * Better error message for too long FASTA file names.
 * FEATURE IMPROVEMENT: Updated Comet to version 2015.01 rev. 1.

 * BUG FIX: Fixed a bug in temp folder used for Comet and Tide where the folder was not created if it didn't already exist.
 * BUG FIX: Fixed a bug with the link to the parameter file in the Comet temp folder.
 * BUG FIX: Fixed a bug in the path to X!Tandem when run on Windows in command line mode.
 * BUG FIX: The Tide and Comet results files are now actually moved from the temp folder to the results folder instead of just copied.

 * LIBRARY UPDATE: Updated utilities to version 3.46.12. 

----

**Changes in SearchGUI 1.26.6 (March 30. 2015):**

 * BUG FIX: Fixed bugs related to running in command line mode on systems without an X11 DISPLAY.

----

**Changes in SearchGUI 1.26.5 (March 26. 2015):**

 * FEATURE IMPROVEMENT: Updated the Ensembl mappings to Ensembl 79.
 * FEATURE IMPROVEMENT: Updated Ensembl Genomes to version 26.

 * BUG FIX: Fixed a typo in the mass for TMT130 report for 6plex TMT.
 * BUG FIX: Fixed backwards compatibility issues in the TideParameters.
 * BUG FIX: Fixed a bug that made it impossible to run Tide and PeptideShaker post-processing at the same time.

 * LIBRARY UPDATE: Updated utilities to version 3.46.9. 

----

**Changes in SearchGUI 1.26.4 (March 11. 2015):**

 * FEATURE IMPROVEMENT: Added a check for supported MyriMatch and Tide  output formats if PeptideShaker is selected.

 * BUG FIX: Fixed bugs related to the Tide output format not being text.
 * BUG FIX: The enzyme is now set correctly in the Comet pepXML output.
 * BUG FIX: The user selected MyriMatch output format is now actually used.
 * BUG FIX: Corrected a bug in the handling of default paths.

 * LIBRARY UPDATE: Updated utilities to version 3.45.44. 

----

**Changes in SearchGUI 1.26.3 (February 21. 2015):**

 * BUG FIX: The enzyme is now set for Tide, instead of always defaulting to trypsin.
 * BUG FIX: Tide can now be run without any PTMs.
 * BUG FIX: Fixed bugs in the comparison of Tide parameters.

 * LIBRARY UPDATE: Updated utilities to version 3.45.36. 

----

**Changes in SearchGUI 1.26.2 (February 18. 2015):**

 * BUG FIX: Fixed bugs for the setting of the default search engine locations (for OMSSA and X!Tandem) in the command line mode.

----

**Changes in SearchGUI 1.26.1 (February 17. 2015):**

 * BUG FIX: Renamed the default X!Tandem folder into XTandem, as '!' is not allowed in paths on Linux.

 * LIBRARY UPDATE: Updated utilities to version 3.45.35. 

----

**Changes in SearchGUI 1.26.0 (February 16. 2015):**

 * FEATURE IMPROVEMENT: Fixed an issue with using high resolution data in Tide. (Could also affect Comet results.)

 * LIBRARY UPDATE: Updated utilities to version 3.45.33. 

----


**Changes in SearchGUI 1.25.7 (February 11. 2015):**

 * FEATURE IMPROVEMENT: Improved the command line error handling.

 * BUG FIX: Fixed a bug in the CV term name for TMT6plex, hindering the use of TMT 6-plex (and 10-plex) in MS Amanda.

 * LIBRARY UPDATE: Updated utilities to version 3.45.32. 

----

**Changes in SearchGUI 1.25.6 (February 4. 2015):**

 * BUG FIX: Fixed a bug where the adding of decoys also removed the target sequences.

----

**Changes in SearchGUI 1.25.5 (February 2. 2015):**

 * BUG FIX: Removed GUI code from the process builders.

----

**Changes in SearchGUI 1.25.4 (January 30. 2015):**

 * BUG FIX: Corrected the default paths to the search engines.

----

**Changes in SearchGUI 1.25.3 (January 29. 2015):**

 * BUG FIX: The command line now works again.

----

**Changes in SearchGUI 1.25.2 (January 29. 2015):**

 * BUG FIX: Fixed a bug where neutral losses and reporter ions for user defined modifications disappeared.

 * LIBRARY UPDATE: Updated utilities to version 3.45.25.

----

**Changes in SearchGUI 1.25.1 (January 29. 2015):**

 * NEW FEATURE: Added pepXML as an output option for OMSSA.

 * FEATURE IMPROVEMENT: User modifications are now also mapped to Unimod for MS Amanda.
 * FEATURE IMPROVEMENT: Made it possible to automatically remove the Tide temp folders when a Tide search is complete.

 * LIBRARY UPDATE: Updated utilities to version 3.45.24.

----

**Changes in SearchGUI 1.25.0 (January 23. 2015):**

 * NEW FEATURE: Added support for Tide. (beta)

 * FEATURE IMPROVEMENT: Updated MS Amanda to version 1.0.0.3948 for Windows and 1.0.0.3947 for Linux/Mac.
  * New weighted probability/e-value in the output.
  * Bugfix for whole protein/already digested databases.
  * Bugfix for decoy database creation.
  * Bugfix for water/ammonia loss consideration.
 * FEATURE IMPROVEMENT: PTMs are now given as Unimod for MS Amanda, which improves the PSMs.
 * FEATURE IMPROVEMENT: Updated Ensembl Genomes to version 25.

 * LIBRARY UPDATE: Updated utilities to version 3.45.19.

----

**Changes in SearchGUI 1.24.0 (January 10. 2015):**

 * FEATURE IMPROVEMENT: Updated MS-GF+ to version "Beta (v10282) (12/19/2014)".
  * Fixing an issue with parsing mgf files where scan numbers are not numbers.
  * Improves the multi threaded performance. 
  * Fixing a bug that occurs when C-term mod mass is below -57Da.
  * Adds a test that checks whether the output path is valid before processing the data.
 * FEATURE IMPROVEMENT: Updated MS Amanda to version 1.0.0.3858 for Windows and version 1.0.0.3859 for Linux/Mac. 
  * Fixing an issue with loading mgf with long scan numbers/tags and improved.
 * FEATURE IMPROVEMENT: Updated the gene and GO mappings to Ensembl version 78.
 * FEATURE IMPROVEMENT: Added quotes around the species type in the PeptideShaker command line.
 * FEATURE IMPROVEMENT: The search engine installation error dialog is now actually shown if a search engine fails the startup test, and the dialog now includes links to the trouble shooting section and to Mono download for MS Amanda on Mac/Linux.
 * FEATURE IMPROVEMENT: Made it possible to set the Java Home from the GUI.
 * FEATURE IMPROVEMENT: Added a dialog to edit the path preferences.

 * BUG FIX: Fixed a bug in the Species Dialog where the text on the Update/Download button was not always correct.

 * LIBRARY UPDATE: Updated utilities to version 3.45.18.

----

**Changes in SearchGUI 1.23.3 (November 27. 2014):**

 * FEATURE IMPROVEMENT: Updated MS Amanda to version 1.0.0.3764 for Windows and 1.0.0.3675 for Linux/Mac.
  * no output file generated if the search fails
  * bug fix for n-terminal modifications
  * better logging
  * bug fix for FASTA parsing with special identifiers.

 * BUG FIX: Fixed a bug in the conversion of mgf files for use in Comet where scan numbers resulted in it being impossible to map back to the original mgf file.

 * LIBRARY UPDATE: Updated utilities to version 3.43.16.

----

**Changes in SearchGUI 1.23.2 (November 18. 2014):**

 * BUG FIX: Fixed a bug in adding decoy sequences to FASTA files containing headers without descriptions.

----

**Changes in SearchGUI 1.23.1 (November 17. 2014):**

 * FEATURE IMPROVEMENT: Updated Ensembl Genomes to version 24, adding Zootermopsis nevadensis.
 * FEATURE IMPROVEMENT: Added a check for if SearchGUI is started from within a zip file.

 * BUG FIX: Fixed a bug in the download of gene mappings for non-vertebrate species.
 * BUG FIX: Fixed some special case Derby shutdown and restart issues.

 * LIBRARY UPDATE: Updated utilities to version 3.43.13.

----

**Changes in SearchGUI 1.23.0 (November 14. 2014):**

 * NEW FEATURE: MS Amanda is now supported on Mac.
  * Requires that [http://www.mono-project.com Mono] is installed.

 * BUG FIX: Fixed a bug in the appending of decoy sequence which in some cases altered the FASTA headers.

 * LIBRARY UPDATE: Updated utilities to version 3.43.10.

----

**Changes in SearchGUI 1.22.2 (October 30. 2014):**

 * BUG FIX: Fixed a bug in the handling of variable modifications for X!Tandem. 

----

**Changes in SearchGUI 1.22.1 (October 26. 2014):**

 * BUG FIX: Fixed a bug in the auto update feature. 
 * BUG FIX: Fixed some backward compatibility issues.

 * LIBRARY UPDATE: Updated utilities to version 3.41.1.

----

**Changes in SearchGUI 1.22.0 (October 23. 2014):**

 * NEW FEATURE: Added support for Comet.
 * NEW FEATURE: Updated MS Amanda to version 1.0.0.3585: 
  * Faster when a high number of variable PTMs are used. 
  * Bug fix for lower-case FASTA sequences.
  * Bug fix for different modifications targeting the same amino acid.
 * NEW FEATURE: MS Amanda is now supported on Linux (v1.0.0.3635). (beta)
  * Requires that [http://www.mono-project.com mono] is installed.

 * FEATURE IMPROVEMENT: Updated Ensembl Genomes to version 77, adding Vervet-AGM (Chlorocebus sabaeus).
 * FEATURE IMPROVEMENT: Added progress bar when zipping.
 * FEATURE IMPROVEMENT: The list of database types and their occurrences is now included in the FASTA index.
 * FEATURE IMPROVEMENT: Renamed "no enzyme" to the more understandable "unspecific".
 * FEATURE IMPROVEMENT: Added support for unspecific cleavage for X!Tandem.

 * BUG FIX: Fixed a bug that made it impossible to re-select MyriMatch if it was deselected in the GUI.
 * BUG FIX: Fixed a bug in the use of the Ensembl gene mappings where a field had been renamed in the Ensembl web service.

 * LIBRARY UPDATE: Updated utilities to version 3.40.0.

----

**Changes in SearchGUI 1.21.0 (September 19. 2014):**

 * FEATURE IMPROVEMENT: In MyriMatch the MonoisotopeAdjustmentSet parameter is now automatically set to 0 when the MonoPrecursorMzTolerance is wide (as defined by MyriMatch).
 * FEATURE IMPROVEMENT: Added quotation marks so that the MyriMatch, MS-GF+ and MS Amanda command lines printed to the log file can be run directly from the command line.
 * FEATURE IMPROVEMENT: Fixed an issue with indexing mgf files with empty charge tags.

 * LIBRARY UPDATE: Updated jsparklines to version 1.0.4.
 * LIBRARY UPDATE: Updated utilities to version 3.37.3.

----

**Changes in SearchGUI 1.20.8 (September 8. 2014):**

 * FEATURE IMPROVEMENT: Improved the parsing of headers of type genome translated to protein sequence.

 * LIBRARY UPDATE: Updated utilities to version 3.35.7.

----

**Changes in SearchGUI 1.20.7 (August 30. 2014):**

 * FEATURE IMPROVEMENT: Changed the default PTM localization score to A-score for PeptideShaker.

 * LIBRARY UPDATE: Updated utilities to version 3.35.6. 

----

**Changes in SearchGUI 1.20.6 (August 29. 2014):**

 * BUG FIX: Fixed a bug with the tooltips for the PTMs in the Search Settings dialogs.
 * BUG FIX: Fixed a bug with the use of custom PTM patterns.

 * LIBRARY UPDATE: Updated utilities to version 3.35.5. 

----

**Changes in SearchGUI 1.20.5 (August 21. 2014):**

 * FEATURE IMPROVEMENT: Updated Ensembl genomes to release 23.

 * BUG FIX: Fixed an issue in the auto update feature that could occur on specific client machine setups.

 * LIBRARY UPDATE: Updated utilities to version 3.35.3. 

----

**Changes in SearchGUI 1.20.4 (August 19. 2014):**

 * FEATURE IMPROVEMENT: Several fixes related to running PeptideShaker from SearchGUI.
 * FEATURE IMPROVEMENT: Added MS Amanda settings file to the zip file.

 * LIBRARY UPDATE: Updated utilities to version 3.35.2.

----

**Changes in SearchGUI 1.20.3 (August 7. 2014):**

 * NEW FEATURE: Added PTM tooltips in the tables in the SearchSettings dialog.

 * FEATURE IMPROVEMENT: Updated the Ensembl mappings to Ensembl 76 and added seven new species: duck, cave fish, flycatcher, cod, spotted gar, sheep and amazon molly.
 * FEATURE IMPROVEMENT: Improved the species names listed for vertebrates.

 * LIBRARY UPDATE: Updated utilities to version 3.31.2.

----

**Changes in SearchGUI 1.20.2 (August 1. 2014):**

 * FEATURE IMPROVEMENT: MyriMatch: Added an HCD option to the fragmentation rules.
 * FEATURE IMPROVEMENT: MyriMatch: Added the MaxPeakCount parameter to the advanced settings.
 * FEATURE IMPROVEMENT: MyriMatch: Added the use of the cpus parameter to set the number of threads/cores used.
 * FEATURE IMPROVEMENT: MyriMatch: ComputeXCorr option now defaults to false, as it is not used in PeptideShaker.
 * FEATURE IMPROVEMENT: MyriMatch: Added support for terminal fixed modifications. (Note that fixed protein terminal modifications and fixed terminal modifications at a given amino acid are not supported, and are therefore treated as variable and later filtered in PeptideShaker.)

 * BUG FIX: Made sure that the zipping is not performed if the search is canceled.

 * LIBRARY UPDATE: Updated utilities to version 3.30.3.

----

**Changes in SearchGUI 1.20.1 (July 31. 2014):**

 * FEATURE IMPROVEMENT: Updated the included human gene and GO mappings to Ensembl version 75.
 * FEATURE IMPROVEMENT: Improved the way auto updating of GO and gene mappings are done when starting PeptideShaker from SearchGUI.
 * FEATURE IMPROVEMENT: Reordered the search engines in the main frame and in the SearchEnginesSettingsDialog.

 * LIBRARY UPDATE: Updated utilities to version 3.30.1.

----

**Changes in SearchGUI 1.20.0 (July 29. 2014):**

 * NEW FEATURE: Added support for MyriMatch.
 * NEW FEATURE: Added indicators of the supported platforms for each search engine.
 * NEW FEATURE: Added an advanced feature option to zip the search results output.
 * NEW FEATURE: Updated MS Amanda to version 1.0.0.3253, fixing problems with parsing strange retention times in mgf files.

 * FEATURE IMPROVEMENT: Made sure that the PeptideShaker log is saved even if the processing fails.
 * FEATURE IMPROVEMENT: Made sure that closing a dialog is always considered the same as using the cancel button.

 * LIBRARY UPDATE: Updated jsparklines to version 0.8.0.
 * LIBRARY UPDATE: Updated utilities to version 3.29.7.

----

**Changes in SearchGUI 1.19.5 (June 25. 2014):**

 * FEATURE IMPROVEMENT: The search engines are now run in the order listed in the GUI.
 * FEATURE IMPROVEMENT: Improved the Unimod cv term mappings.
 * FEATURE IMPROVEMENT: Tried to improve the monitoring of the search engine processes.
 * FEATURE IMPROVEMENT: Improved the Waiting Dialog.
 * FEATURE IMPROVEMENT: Renamed Protein Tree to Protein Index in the Advanced Settings dialog and help text.

 * BUG FIX: Fixed a bug with case sensitivity in the PRIDE PTM mapping.

 * LIBRARY UPDATE: Updated utilities to version 3.28.30.

----

**Changes in SearchGUI 1.19.4 (June 18. 2014):**

 * BUG FIX: Fixed a bug in the auto update functionality.

----

**Changes in SearchGUI 1.19.3 (June 17. 2014):**

 * BUG FIX: Corrected typos in the help files.
 * BUG FIX: Fixed some typos in the error messages in the CLI.

 * LIBRARY UPDATE: Updated utilities to version 3.28.18.

----

**Changes in SearchGUI 1.19.2 (June 13. 2014):**

 * NEW FEATURE: Updated MS Amanda to version 1.0.0.3196, which includes the MS Amanda version in the output file.

 * LIBRARY UPDATE: Updated utilities to version 3.28.16.

----

**Changes in SearchGUI 1.19.1 (June 5. 2014):**

 * BUG FIX: Fixed a bug in the parsing of terminal modifications for MS Amanda.
 * BUG FIX: Fixed a bug where MS Amanda results files where not recognized if PeptideShaker was started from SearchGUI.

 * LIBRARY UPDATE: Updated utilities to version 3.28.11.

----

**Changes in SearchGUI 1.19.0 (June 5. 2014):**

 * NEW FEATURE: Updated MS Amanda to version 1.0.0.3120, with extended enzyme support and a fix for fixed terminal PTMs.
 * NEW FEATURE: Added support for semi specific enzymes in MS Amanda.

 * FEATURE IMPROVEMENT: Sped up the indexing of mgf files.
 * FEATURE IMPROVEMENT: The JVM arguments given to SearchGUI are now also used for MS-GF+ when run in command line mode.
 * FEATURE IMPROVEMENT: Added support for keyboard input to find modifications in the Search Settings Dialog.
 * FEATURE IMPROVEMENT: Renamed the protein_tree command line option to the more understandable protein_index.
 * FEATURE IMPROVEMENT: Set the protein tree creation to off by default in command line mode.
 * FEATURE IMPROVEMENT: Mgf files are now checked for missing spectrum titles.

 * BUG FIX: MS Amanda is now properly disabled for non Windows platforms (when used in GUI mode).
 * BUG FIX: Fixed a bug with SwissProt headers being changed from sp to sw when adding decoys.

 * LIBRARY UPDATE: Updated utilities to version 3.28.10.

----

**Changes in SearchGUI 1.18.7 (May 20. 2014):**

 * BUG FIX: Fixed a bug with the gene/GO downloads for non-vertebrate species.

 * LIBRARY UPDATE: Updated utilities to version 3.26.41.

----

**Changes in SearchGUI 1.18.6 (May 20. 2014):**

 * FEATURE IMPROVEMENT: Updated the Java Settings dialog.

 * LIBRARY UPDATE: Updated utilities to version 3.26.39.

----

**Changes in SearchGUI 1.18.5 (May 14. 2014):**

 * NEW FEATURE: Updated MS-GF+ to version v10024, fixing an issue with using large memory.

 * FEATURE IMPROVEMENT: If SearchGUI is moved (or a parent folder is renamed) the paths to the search engines will be tried reset to the default paths at the new location.

 * BUG FIX: The MS-GF+ and MS Amanda processes are now canceled if the search is canceled.
 * BUG FIX: Fixed a bug in the mgf_splitting option where using large values could break the option and start splitting files smaller than the provided limit.

 * LIBRARY UPDATE: Updated utilities to version 3.26.33.

----

**Changes in SearchGUI 1.18.4 (May 4. 2014):**

 * NEW FEATURE: Made it possible to set the makeblastdb location in the GUI.
 * NEW FEATURE: Added support for 64 bit Linux for makeblastdb.

 * FEATURE IMPROVEMENT: Added an option to makeblastdb that is mandatory in newer versions.

 * BUG FIX: Fixed a bug in the use of non-default install folders for MS Amanda.

 * LIBRARY UPDATE: Updated utilities to version 3.26.30.

----

**Changes in SearchGUI 1.18.3 (May 2. 2014):**
 
 * NEW FEATURE: Added command line support for setting the makeblastdb folder. 
 * NEW FEATURE: Added command line support for setting the decoy suffix tag when adding decoys using FastaCLI.

 * BUG FIX: Fixed a bug in the command line version of MS-GF+ where the search could be canceled if the SearchGUI path was not set.

----

**Changes in SearchGUI 1.18.2 (April 29. 2014):**

 * NEW FEATURE: Added new command line options for path configuration. 
 * NEW FEATURE: Added an option for turning the protein tree generation on/off from the command line.

 * FEATURE IMPROVEMENT: Added a check and warning if using Java 1.5 or 1.6.
 * FEATURE IMPROVEMENT: Added the possibility for the user to turn on and off the auto update.

 * BUG FIX: Fixed a bug in the processing of the search parameters from the command line where the min charge was set to the same value as the max charge.
 * BUG FIX: Fixed a bug in the PeptideShakerSettingsDialog where the wrong icons was used for the species downloading.

 * LIBRARY UPDATE: Updated utilities to version 3.26.28.

----

**Changes in SearchGUI 1.18.1 (April 12. 2014):**

 * BUG FIX: Fixed a bug in the modification mapping for MS Amanda where peptide and protein n terminal modifications were switched.

----

**Changes in SearchGUI 1.18.0 (April 11. 2014):**

 * NEW FEATURE: Added support for MS Amanda for Windows (beta).

 * FEATURE IMPROVEMENT: Added the option to turn the protein tree creation on/off in the AdvancedSettings Dialog.

 * BUG FIX: Fixed problems with creating terminal PTMs with empty modification patterns.

 * LIBRARY UPDATE: Updated utilities to version 3.26.14.

----

**Changes in SearchGUI 1.17.3 (April 1. 2014):**
 
 * BUG FIX: Fixed a bug in the peptide to protein mapping where the final protein was not included.

 * LIBRARY UPDATE: Updated utilities to version 3.26.4.

----

**Changes in SearchGUI 1.17.2 (March 27. 2014):**

 * NEW FEATURE: Updated MS-GF+ to version MS-GF+ Beta (v9979) (3/26/2014).

 * FEATURE IMPROVEMENT: Improved the error handling when index files cannot be written to during the validation of mgf files.

 * LIBRARY UPDATE: Updated utilities to version 3.25.15.

----

**Changes in SearchGUI 1.17.1 (March 27. 2014):**

 * BUG FIX: Fixed a bug with using relative paths for the database file in the X!Tandem taxonomy file.
 * BUG FIX: Added the MS-GF+ parameters to the command lines shown when using SearchCLIdentificationParametersCLIParams.
 * BUG FIX: Fixed a bug in the method for getting all non fixed modifications.
 * BUG FIX: Fixed a formatting issue in the command line output.

 * LIBRARY UPDATE: Updated utilities to version 3.25.14.

----

**Changes in SearchGUI 1.17.0 (March 26. 2014):**

 * NEW FEATURE: Added support for MS-GF+.

 * BUG FIX: Added a check for "&" in the spectrum, database and output files/folder when X!Tandem is used, as "&" makes the X!Tandem XML input files unreadable.
 * BUG FIX: Fixed a bug in the settings dialog that closed the dialog if the user canceled the save as dialog.
 * BUG FIX: Fixed problems with parsing FASTA files containing headers with empty sequences.
 * BUG FIX: Using a relative path for the database is now supported in the command line mode when creating the search parameters file.

 * LIBRARY UPDATE: Updated utilities to version 3.25.12.

----

**Changes in SearchGUI 1.16.4 (March 6. 2014):**

 * BUG FIX: Fixed a bug in the parsing of FASTA files with unknown headers.
 * BUG FIX: Fixed errors with the TMT 10-plex reporter ion masses.

 * LIBRARY UPDATE: Updated utilities to version 3.23.18.

----

**Changes in SearchGUI 1.16.3 (March 3. 2014):**

 * FEATURE IMPROVEMENT: Mgf files are now checked for if they contain peaks at all.
 * FEATURE IMPROVEMENT: Updated the TMT modifications to support the new 10-plex TMT.
 * FEATURE IMPROVEMENT: Improved the handling of the search engine output in the Waiting Dialog by supporting line breaks.
 * FEATURE IMPROVEMENT: Changed the PSI-MOD modification mappings to Unimod.
 * FEATURE IMPROVEMENT: Made it possible to click the software names/icons to enable/disable the different tools (in addition to just the check box as before).

 * BUG FIX: Fixed a bug in the index files when splitting mgfs.
 * BUG FIX: PeptideShaker will not be started if there are no search result files to process.
 * BUG FIX: Made sure that canceling the Search Engine Settings Dialog does not result in the enabling of search engines that are not validated.

 * LIBRARY UPDATE: Updated utilities to version 3.23.11.

----

**Changes in SearchGUI 1.16.2 (February 10. 2014):**

 * BUG FIX: Fixed a backwards compatibility issue with the refinement modifications.
 * BUG FIX: Made the identification parameters mandatory when using the SearchGUI command line.

 * LIBRARY UPDATE: Updated utilities to version 3.21.31.

----

**Changes in SearchGUI 1.16.1 (February 8. 2014):**

 * BUG FIX: Fixed a memory issue occurring during the protein database loading for Mac and Linux.
 * BUG FIX: Fixed a bug in the command line where spectrum files where not closed and duplicated spectrum titles could not be corrected.
 * BUG FIX: Fixed a bug in the command line where the FASTA file was not set in the SearchCLIInputBean.
 * BUG FIX: Improved the command line test for duplicate titles to only fixing titles if there are titles to fix, and not always as before.
 * BUG FIX: If the search crashed in command line mode the JVM is now shut down.

 * LIBRARY UPDATE: Updated utilities to version 3.21.30.

----

**Changes in SearchGUI 1.16.0 (February 4. 2014):**
 
 * NEW FEATURE: Updated X!Tandem to version SLEDGEHAMMER (2013.09.01) for all platforms.
 * NEW FEATURE: The user can now decide how to handle duplicate spectrum titles: rename, remove or do nothing.
 * NEW FEATURE: The mgf files are now checked for peak picking (a simple zero intensity test) when loading.
 * NEW FEATURE: Added new auto update functionality of SearchGUI.
 * NEW FEATURE: Added the possibility to modify most search engine parameters, X!Tandem and OMSSA, from both the GUI and the command line.
 * NEW FEATURE: Added the possibility to create identification parameters files from the command line.

 * FEATURE IMPROVEMENT: GUI improvements to the SearchGUI main frame.

 * BUG FIX: Fixed a bug in the SpectrumFactory where one ended up with partial index files if the process was canceled by the user.
 * BUG FIX: Stopped the "PTM Definition Obsolete" error from occurring when it should not.
 * BUG FIX: Fixed bugs in the correction of duplicate spectrum titles.
 * BUG FIX: Fixed a backwards compatibility issues with the precursor accuracy in the search parameters.

 * LIBRARY UPDATE: Updated utilities to version 3.21.26.

----

**Changes in SearchGUI 1.15.2 (January 9. 2014):**

 * FEATURE IMPROVEMENT: The protein tree is now only created parallel with the searches if the provided memory is at least 4GB, to reduce the chance of memory issues occurring.

 * LIBRARY UPDATE: Updated utilities to version 3.20.3.

Download Count: 87 (68+15)

----

**Changes in SearchGUI 1.15.1 (January 8. 2014):**

 * NEW FEATURE: The user can now click the spectrum text field to see and edit the list of selected files.

 * FEATURE IMPROVEMENT: Re-added the Save As option in the Search Settings dialog.
 * FEATURE IMPROVEMENT: Refinement modifications in X!Tandem are now turned off whenever a conflict can occur with main modifications.
 * FEATURE IMPROVEMENT: Improved the handling of n-term acetylation and pyro modifications.

 * BUG FIX: Tried to fix a bug where canceling a search and then starting a second search resulted in the waiting dialog acting strange.
 * BUG FIX: The waiting dialog text report file format is now set as html.

 * LIBRARY UPDATE: Updated utilities to version 3.20.2.

Download Count: 9 (7+2)

----

**Changes in SearchGUI 1.15.0 (December 9. 2013):**

 * NEW FEATURE: The peptide to protein mapping needed in PeptideShaker is now generated parallel to the searches.
 * NEW FEATURE: Added command line support for FASTA file manipulation.
 * NEW FEATURE: The species can now be provided as input to SearchGUI (for use when reprocessing in PRIDE).

 * FEATURE IMPROVEMENT: Added better support for semi-specific enzymes.
 * FEATURE IMPROVEMENT: Cleaned up the help and about texts.
 * FEATURE IMPROVEMENT: Added tip of the day to the waiting dialog.
 * FEATURE IMPROVEMENT: The validation of the mgf files has been merged with the indexing of the files, instead of being two separate steps as before. And validation status is now saved in the file. Results in quicker validation that only has to be done once.
 * FEATURE IMPROVEMENT: Added a memory and Java version check to the PeptideShaker settings dialog.
 * FEATURE IMPROVEMENT: Got rid of the derby.log file.
 * FEATURE IMPROVEMENT: Removed .mgf from the default PRIDE project names, and added support for names with multiple files.
 * FEATURE IMPROVEMENT: The dialog asking the user if he/she wants to overwrite existing search result files is now only shown once (and not once per files as before).
 * FEATURE IMPROVEMENT: Removed the config file panel from the SearchSettings Dialog.

 * BUG FIX: Fixed a bug where choosing to not fix duplicated spectrum titles resulted in the mgf file not being selected.
 * BUG FIX: Made sure that only valid search parameter files can be selected.
 * BUG FIX: Fixed some bugs with editing the reporter and neutral ions in the Modification Details dialog.
 * BUG FIX: Fixed the X!Tandem enzyme formatting for the Whole Protein and Top Down enzymes.
 * BUG FIX: Fixed a bug in the parsing of sequence headers of type Generic_Split_Header.
 * BUG FIX: Fixed a bug with the handling of corrupt PRIDE PTM mapping files.

 * LIBRARY UPDATE: Updated utilities to version 3.19.5.

Download Count: 73 (53+20)

----

**Changes in SearchGUI 1.14.4 (August 10. 2013):**

 * LIBRARY UPDATE: Updated utilities to version 3.14.19.

Download Count: 313 (234+79)

----

**Changes in SearchGUI 1.14.3 (July 14. 2013):**

 * BUG FIX: Made the tool Java 6 compatible again.
 * LIBRARY UPDATE: Updated utilities to version 3.14.16.

Download Count: 91 (68+23)

----

**Changes in SearchGUI 1.14.2 (July 9. 2013):**

 * BUG FIX: Fixed a bug in the command line where the process got stopped before the searches could get started.
 * LIBRARY UPDATE: Updated utilities to version 3.14.14.

Download Count: 34 (31+3)

----

**Changes in SearchGUI 1.14.1 (July 4. 2013):**

 * NEW FEATURE: Extended the species support.
 * NEW FEATURE: Database details dialog.

 * BUG FIX: Fixed a bug in the Mac/Linux assembly that resulted in a corrupt jar file.
 * BUG FIX: Fixed a problem with the permissions on Mac/Linux.

 * LIBRARY UPDATE: Updated utilities to version 3.14.7.

Download Count: 29 (23+6)

----

**Changes in SearchGUI 1.14.0 (June 19. 2013):**

 * NEW FEATURE: Updated X!Tandem to version Jackhammer (2013.6.15) for all platforms.
 * NEW FEATURE: Added the option of setting the number of threads to use, both from the GUI and from the command line.

 * FEATURE IMPROVEMENT: Better handling of PeptideShaker errors when PeptideShaker is started from SearchGUI.
 * FEATURE IMPROVEMENT: Updated Ensembl human mappings to Ensembl 71.

 * BUG FIX: Fixed a bug that occurred in the tool hanging if splitting had to be carried out when selecting an mgf file.
 * BUG FIX: Reset the settings before splitting mgf to 1000 MB and 25000 spectra per file.
 * BUG FIX: Fixed a bug where the results files were deleted no matter what the user choose for the overwrite existing files question when starting the search.
 * BUG FIX: Fixed a bug with missing peptide length filters for the PeptideShaker post-processing.
 * BUG FIX: Fixed a null pointer that occured in the PeptideShakerSettingsDialog and in the SearchHandler if PeptideShaker had never been installed before.

 * LIBRARY UPDATE: Updated utilities to version 3.13.54.

Download Count: 98 (63+35)

----

**Changes in SearchGUI 1.13.3 (June 1. 2013):**

 * NEW FEATURE: The species can now be set in the PeptideShakerSettingsDialog.
 * NEW FEATURE: Added a check for duplicate spectrum titles when selecting mgf files.

 * LIBRARY UPDATE: Updated utilities to version 3.13.30.

Download Count: 59 (43+16)

----

**Changes in SearchGUI 1.13.2 (May 13. 2013):**

 * BUG FIX: Fixed a bug where white space was not allowed in the installation path.
 * LIBRARY UPDATE: Updated utilities to version 3.13.18.

Download Count: 68 (53+15)

----

**Changes in SearchGUI 1.13.1 (May 12. 2013):**

 * BUG FIX: Fixed a bug related to setting the OMSSA modification indexes when running SearchGUI from the command line.
 * LIBRARY UPDATE: Updated utilities to version 3.13.17.

Download Count: 8 (6+2)

----

**Changes in SearchGUI 1.13.0 (May 11. 2013):**

 * NEW FEATURE: Added MGF splitting options to the command line.
 * NEW FEATURE: The size of the MGF files is now also checked when using the PeptideShaker PRIDE Reshake feature.

 * FEATURE IMPROVEMENT: Tried to improve the error message displayed if the SearchGUI to PeptideShaker link fails.
 * FEATURE IMPROVEMENT: Added an extra test to check that the provided PeptideShaker path actually exists before starting the PeptideShaker processing.
 * FEATURE IMPROVEMENT: Only mgf files are now supported as spectrum file input, as this is the only format currently supported in PeptideShaker.

 * BUG FIX: Fixed a problem with starting the tool on the latest Java release.
 * BUG FIX: Fixed a bug in the SearchGUI command line where fixed modification was used instead of variable modification, making all PTMs fixed. (Only affected command lines where the PTMs were provided directly.)
 * BUG FIX: Fixed a bug that resulted in the PTMs not actually being used even when provided directly on the command line.
 * BUG FIX: Renamed the X!Tandem Linux binaries so that they can be auto detected.
 * BUG FIX: OMSSA PTM indexes are now set for all search parameters.

 * LIBRARY UPDATE: Updated utilities to version 3.13.16.

Download Count: 7 (3+4)

----

**Changes in SearchGUI 1.12.2 (April 2. 2013):**

 * BUG FIX: Fixed a problem with the renaming of X!Tandem files.
 * LIBRARY UPDATE: Updated utilities to version 3.11.29.

Download Count: 168 (128+40)

----

**Changes in SearchGUI 1.12.1 (March 25. 2013):**

 * FEATURE IMPROVEMENT: The search report now includes the search parameters, and is also created when ran from the command line (but then with just the search parameters).
 * BUG FIX: Fixed a bug that made it impossible to change the memory settings. 
 * LIBRARY UPDATE: Updated utilities to version 3.11.27.

Download Count: 40 (28+12)

----

**Changes in SearchGUI 1.12.0 (March 24. 2013):**

 * NEW FEATURE: Added command line options for setting the search engine locations.

 * FEATURE IMPROVEMENT: Updated X!Tandem to version CYCLONE (2013.2.01) for all platforms.
 * FEATURE IMPROVEMENT: The SettingsDialog now tries to check if the search parameters have changed when the user clicks the OK button, and if any changes are detected ask the user if he/she wants to save the changes.
 * FEATURE IMPROVEMENT: Added a check for if the PeptideShaker jar file actually exists in the PeptideShakerSettingsDialog.

 * BUG FIX: Fixed a bug in the on/off settings for the search engines when run from the command line.
 * BUG FIX: Fixed some issues that occurred when opening SearchGUI with search parameters and/or mgf files.
 * BUG FIX: Fixed a bug in the check for new versions for SearchGUI that assumed that new versions for all operating systems were always released at the same time.
 * BUG FIX: Tried to fix a problem occurring with X!Tandem file names with regular expressions in them.
 * BUG FIX: Fixed minor code issues detected by FindBugs.

 * LIBRARY UPDATE: Excluded unused transitive dependency ssj.
 * LIBRARY UPDATE: Updated utilities to version 3.11.25.

Download Count: 25 (20+5)

----

**Changes in SearchGUI 1.11.0 (February 6. 2013):**

 * NEW FEATURE: Brand new more userfriendly frontend!
 * NEW FEATURE: Search results can now be automatically processed in PeptideShaker.
 * NEW FEATURE: Reimplemented the SearchGUI command line support from scratch. (http://code.google.com/p/searchgui/wiki/SearchCLI) 
 * NEW FEATURE: Modifications can now be defined using sequence patterns. (Note that the patterns are ignored until the data is loaded in PeptideShaker, as the search engines do not support the patterns directly.)
 * NEW FEATURE: Added an option to the Advanced Settings (and the command line) to export the OMSSA results in the OMSSA csv format.
 * NEW FEATURE: Made it possible to set the Java options from the Edit menu. (Not really needed for SearchGUI, but comes in handy when starting PeptideShaker from SearchGUI.)
 * NEW FEATURE: Made it possible to select which PTMs to label as default and thus show up in the "most used modifications" table.
 * NEW FEATURE: Improved the X!Tandem input format to support more advanced modification setups.

 * FEATURE IMPROVEMENT: Changed the X!Tandem parameter "use noise suppression" from "yes" to "no", such that all spectra are searched and that the user's maximum precursor charge value is now respected. (Previously spectra with a charge higher than 3+ were ignored by X!Tandem...)
 * FEATURE IMPROVEMENT: An exception is now thrown if multiple fixed modifications have the same target, as this is not really supported by X!Tandem.
 * FEATURE IMPROVEMENT: The main progress bar in the waiting dialog is longer stuck at 0% until the first search is completed, but instead shows that some progress has been made.
 * FEATURE IMPROVEMENT: SearchGUI can be run from paths containing special characters.
 * FEATURE IMPROVEMENT: The spectrum files used in the OMSSA search can now have both lower and upper case file name types, e.g., mgf and MGF. (And not only mgf as before.)
 * FEATURE IMPROVEMENT: Replaced the modification lists with tables so that more information can be shown, plus allows the users to set the ptm colors.
 * FEATURE IMPROVEMENT: The OMSSA and X!Tandem processes are now actually canceled if the user cancels the search.
 * FEATURE IMPROVEMENT: Added a check for duplicate entries when loading FASTA files.

 * BUG FIX: Fixed a bug with the masses of user defined PTMs in the PRIDE export being set to null if a CV mapping was set.
 * BUG FIX: Fixed a shortcoming in the TandemProcessBuilder where multiple variable modifications with the same target were not handled correctly.
 * BUG FIX: Removed the indexing of the mgf files, as there seemed to be a bug in the indexing when splitting mgfs. Indexing is now done in PeptideShaker instead.
 * BUG FIX: Made a minor change to the pom file to handle a recursive issue that occured when opening the project in NetBeans 7.2.

 * LIBRARY UPDATE: Updated the X!Tandem windows versions to version 2011.12.01.1.
 * LIBRARY UPDATE: Updated utilities to version 3.11.2.

Download Count: 414 (355+59)

----

**Changes in SearchGUI 1.10.4 (September 15. 2012):**

 * LIBRARY UPDATE: Updated utilities to version 3.8.9, to be compatible with PeptideShaker 0.18.3.

Download Count: 368 (284+84)

----

**Changes in SearchGUI 1.10.3 (September 13. 2012):**

 * BUG FIX: SearchGUI no longer resets the PeptideShaker memory settings.
 * FEATURE IMPROVEMENT: The code now supports Maven 7.
 * LIBRARY UPDATE: Updated ols-dialog to version 3.4.0
 * LIBRARY UPDATE: Updated jsparklines to version 0.5.40.
 * LIBRARY UPDATE: Updated jmzml to version 1.6.8.
 * LIBRARY UPDATE: Updated utilities to version 3.8.9.

Download Count: 26 (20+6)

----

**Changes in SearchGUI 1.10.2 (September 7. 2012):**

 * FEATURE IMPROVEMENT: Minor fixes to make SearchGUI better compatible with PeptideShaker v0.18.0
 * BUG FIX: Fixed a path bug that occurred when running SearchGUI from PeptideShaker.
 * LIBRARY UPDATE: Updated utilities to version 3.8.6.

Download Count: 26 (23+3)

----

**Changes in SearchGUI 1.10.1 (August 26. 2012):**

 * NEW FEATURE: The selected output folder can now be created if it does not already exist.
 * FEATURE IMPROVEMENT: Added right click Edit popup menus for the tables in the modification tab.
 * BUG FIX: Fixed an issue with the indexing of the FASTA file when appending decoys.
 * BUG FIX: The mgf files are now re-indexed if needed.
 * LIBRARY UPDATE: Updated utilities to version 3.8.2.

Download Count: 46 (39+7)

----

**Changes in SearchGUI 1.10.0 (August 22. 2012):**

 * FEATURE IMPROVEMENT: Dramatically reduced the time required to index and split files, and add decoys.
 * FEATURE IMPROVEMENT: Improved the canceling of searches, such that the actual search processes are now canceled if the user clicks the cancel button.
 * FEATURE IMPROVEMENT: Set the default splitting limit to 1000 MB, and 25000 spectra per MGF file.
 * FEATURE IMPROVEMENT: Replaced uses of "\n" with System.getProperty("line.separator").
 * LIBRARY UPDATE: Updated utilities to version 3.7.6.

Download Count: 9 (5+4)

----

**Changes in SearchGUI 1.9.0 (July 19. 2012):**

 * FEATURE IMPROVEMENT: Double clicking in the defaults PTM table now brings up the PTM details.
 * FEATURE IMPROVEMENT: Added a test so that the user does not load different mgf files with the same name.
 * FEATURE IMPROVEMENT: Re-indexes the mgf files if the indexes do not contain precursor intensities.
 * FEATURE IMPROVEMENT: Re-added the database selection to the Settings tab.
 * FEATURE IMPROVEMENT: Improved the handling of errors in the user input.
 * FEATURE IMPROVEMENT: Improved the look and feel of the titled borders when using Java 7.
 * BUG FIX: Corrected a bug in the PTM jump to table feature.
 * BUG FIX: Fixed an issue in the ProgressDialogX that resulted in threading issues and deadlock on Java 7.
 * LIBRARY UPDATE: Updated utilities to version 3.6.10. 

Download Count: 56 (38+18)

----

**Changes in SearchGUI 1.8.9 (June 25. 2012):**

 * FEATURE IMPROVEMENT: The tool will now detect if the user tries to start it from within a zip file.
 * FEATURE IMPROVEMENT: Fixed the font color of the titled borders to look better when using Java 7.
 * BUG FIX: Made it possible to edit the user defined PTMs.
 * BUG FIX: The progress bars shown when adding decoy sequences and splitting mgf files are now working again.
 * LIBRARY UPDATE: Updated utilities to version 3.5.6.

Download Count: 58 (51+7)

----

**Changes in SearchGUI 1.8.8 (June 19. 2012):**

 * FEATURE IMPROVEMENT: File shortcuts (lnk files) are now shown in the file selection dialogs.
 * BUG FIX: Corrected a bug in the handling of neutral losses.

Download Count: 44 (41+3)

----

**Changes in SearchGUI 1.8.7 (June 5. 2012):**

 * FEATURE IMPROVEMENT: Increased the default size before the user is asked if he/she wants to split mgf files (> 2 0000 MB, > 25 000 000 spectra).
 * BUG FIX: Fixed a thread issue that could cause the GUI to hang.

Download Count: 33 (25+8)

----

**Changes in SearchGUI 1.8.6 (June 5. 2012):**

 * FEATURE IMPROVEMENT: Split the fragment ion types into forward (a,b,c) and backward (x,y,z) ions. (Such that the same ion type cannot be selected twice.)
 * LIBRARY UPDATE: Updated utilities to version 3.4.23.

Download Count: 3 (3+0)

----

**Changes in SearchGUI 1.8.5 (May 10. 2012):**

 * FEATURE IMPROVEMENT: SearchGUI will not complain about the settings if a parameter file is loaded.
 * FEATURE IMPROVEMENT: Completed the missing help files.
 * FEATURE IMPROVEMENT: Displays in the search tab whether a file has been loaded or user settings used.
 * LIBRARY UPDATE: Updated utilities to version 3.4.19.

Download Count: 41 (37+7)

----

**Changes in SearchGUI 1.8.4 (May 6. 2012):**

 * FEATURE IMPROVEMENT: Re-added the config settings to the Search tab.
 * BUG FIX: Fixed an issue with some missing icons in the PtmDialog resulting in an error opening the dialog.
 * LIBRARY UPDATE: Updated utilities to version 3.4.13.

Download Count: 16 (13+3)

----

**Changes in SearchGUI 1.8.3 (April 28. 2012):**

 * FEATURE IMPROVEMENT: Made it possible to cancel processes related to reading FASTA sequences and adding decoy sequences.
 * FEATURE IMPROVEMENT: Improved the SearchGUI icon.
 * FEATURE IMPROVEMENT: Simplified the folder structure in the zip file.
 * FEATURE IMPROVEMENT: If the user tries to start a search without having visited the Settings tab first a warning message is now displayed.
 * LIBRARY UPDATE: Updated utilities to version 3.4.11. 

Download Count: 17 (14+3)

----

**Changes in SearchGUI 1.8.2 (April 18. 2012):**

 * BUG FIX: Fixed an issue with spaces in the splash screen graphics path on Windows. 

Download Count: 22 (16+6)

----

**Changes in SearchGUI 1.8.1 (April 18. 2012):**

 * NEW FEATURE: Added a SearchGUI splash screen.
 * FEATURE IMPROVEMENT: Cleaned up the folder structure in the zip file.
 * BUG FIX: Fixed a bug in the method for setting the path for the icon and target in the desktop shortcut that occurred when running SearchGUI from network drives.

Download Count: 1 (1+0)

----

**Changes in SearchGUI 1.8 (April 16. 2012):**

 * NEW FEATURE: On Windows (on supported architectures) the user is now asked if a desktop shortcut should be added the first time he/she starts the tool.
 * NEW FEATURE: Included the neutral losses in X!Tandem.
 * NEW FEATURE: Added a README file.
 * NEW FEATURE: PSI-MOD mappings have been added.
 * FEATURE IMPROVEMENT: Numerous GUI improvements.
 * FEATURE IMPROVEMENT: Updated the SearchGUI icon.
 * BUG FIX: Corrected a minor bug in the PTM search option.
 * BUG FIX: Fixed a typo in the SearchPanel.
 * FEATURE IMPROVEMENT: Extended the list of supported enzymes.
 * FEATURE IMPROVEMENT: Square brackets are now allowed in the path were SearchGUI is installed.
 * LIBRARY UPDATE: Updated utilities to version 3.4.8.
 * LIBRARY UPDATE: Added ols-dialog as a dependency.
 * LIBRARY UPDATE: Added jshortcut as a dependency.

Download Count: 5 (4+1)

----

**Changes in SearchGUI 1.7.3 (February 20. 2012):**

 * FEATURE IMPROVEMENT: Extended the list of supported enzymes.
 * BUG FIX: Corrected a minor bug in the PTM search option.
 * LIBRARY UPDATE: Updated utilities to version 3.3.36.

Download Count: 101 (76+25)

----

**Changes in SearchGUI 1.7.2 (February 6. 2012):**

 * BUG FIX: Minor fix to avoid issues in protein selection.
 * BUG FIX: Fixed a GUI bug in the Modification Editor where the next arrow turned into a previous arrow on mouse over.
 * LIBRARY UPDATE: Updated utilities to version 3.3.35.

Download Count: 74 (39+35)

----

**Changes in SearchGUI 1.7.1 (January 16. 2012):**

 * BUG FIX: Added 'N' as a legal amino acid when adding user defined modifications.
 * LIBRARY UPDATE: Updated utilities to version 3.3.24.

Download Count: 35 (25+10)

----

**Changes in SearchGUI 1.7 (January 13. 2012):**

 * NEW FEATURE: Updated the X!Tandem version to CYCLONE (2010.12.01) for Windows 32 and 64 bit.
 * NEW FEATURE: Allowed the user to manage modifications directly in the GUI.
 * FEATURE IMPROVEMENT: Improved the way missing ptms are handled.
 * LIBRARY UPDATE: Updated utilities to version 3.3.22. 
 * LIBRARY UPDATE: Added jsparklines 0.5.31 as a dependency.

Download Count: 10 (8+2)

----

**Changes in SearchGUI 1.6.6 (January 6. 2012):**

 * BUG FIX: Fixed some minor formatting issues in the error messages.
 * BUG FIX: Fixed a bug with the indexing in the split mgf method.
 * LIBRARY UPDATE: Updated utilities to version 3.3.17.

Download Count: 16 (13+3)

----

**Changes in SearchGUI 1.6.5 (January 4. 2012):**

 * NEW FEATURE: Added the possibility to split mgf files and to disable indexing.
 * FEATURE IMPROVEMENT: Extended the database help.
 * FEATURE IMPROVEMENT: Minor additions to the 'User-defined Modifications' part of the manual.
 * FEATURE IMPROVEMENT: Added four user defined modifications. 
 * BUG FIX: Fixed an issue with the titles of the open dialogs.

Download Count: 8 (5+3)

----

**Changes in SearchGUI 1.6.4 (December 15. 2011):**

 * FEATURE IMPROVEMENT: Moved the database help to the SearchGUI home page.
 * BUG FIX: Fixed a bug where the progress bar stayed as indeterminate  (i.e., not showing the actual progress) when loading a FASTA file before adding decoy sequences.
 * LIBRARY UPDATE: Updated utilities to version 3.3.7.

Download Count: 26 (18+8)

----

**Changes in SearchGUI 1.6.3 (December 7. 2011):**

 * NEW FEATURE: Added a database help link next to the decoy button, with database creation help.
 * NEW FEATURE: When selecting the FASTA file the file is now tested for if it seems to contain decoy sequences or not. If is doesn't the user is asked if he/she wants to add decoys.
 * FEATURE IMPROVEMENT: The enzymes are now sorted alphabetically.
 * FEATURE IMPROVEMENT: Improved the text for the "Open/Save" buttons in the file choosers.
 * FEATURE IMPROVEMENT: The last used folder is now stored and used when opening the file choosers.
 * BUG FIX: Fixed a bug in the decoy creation for unknown FASTA headers.
 * BUG FIX: Fixed some bugs where the icon was not reset to the default version if an error occurred.
 * LIBRARY UPDATE: Updated utilities to version 3.3.5.

Download Count: 17 (11+6)

----

**Changes in SearchGUI 1.6.2 (November 19. 2011):**

 * FEATURE IMPROVEMENT: The checkForNewVersion method no longer displays the "SearchGUI failed to start" dialog if an Internet connection is not available.
 * BUG FIX: Updated the manual with a command line syntax fix.
 * LIBRARY UPDATE: Updated utilities to version 3.2.18.

Download Count: 30 (16+14)

----

**Changes in SearchGUI 1.6.1 (September 10. 2011):**

 * FEATURE IMPROVEMENT: Reduced the default max memory setting to 1024M, to ensure that memory issues should not cause SearchGUI to not start.
 * FEATURE IMPROVEMENT: SearchGUI will now default to use the Java 64 bit version on Windows systems if detected.
 * LIBRARY UPDATE: Updated utilities to version 3.2.12.

Download Count: 109 (83+26)

----

**Changes in SearchGUI 1.6 (August 18. 2011):**

 * NEW FEATURE: SearchGUI now indexes the MGF files in parallel with the searches for simpler access in other *compomics* software.
 * NEW FEATURE: FASTA files are now indexed and the sequences are not loaded into the memory anymore.
 * FEATURE IMPROVEMENT: Fixed some issues with the Linux support.
 * BUG FIX: Corrected a bug which resulted in user modifications not being taken into account in the search.

Download Count: 22 (18+4)

----

**Changes in SearchGUI 1.5.3 (July 26. 2011):**

 * FEATURE IMPROVEMENT: FASTA files with white space in the files names will now be automatically renamed by replacing white space with {{{"_"}}}, as required by the makeblastdb command.

Download Count: 27

----

**Changes in SearchGUI 1.5.2 (July 25. 2011):**

 * NEW FEATURE: Added Linux 64 bit support for OMSSA and X!Tandem.
 * NEW FEATURE: Added a PeptideShaker link at the bottom of the Waiting dialog.
 * FEATURE IMPROVEMENT: Simplified the error message given if the tool fails to start.  
 * FEATURE IMPROVEMENT: Improved the way the log file is created.
 * FEATURE IMPROVEMENT: The same mgf file cannot be loaded several times.
 * FEATURE IMPROVEMENT: Added a warning if more than 6 variable modifications are selected in search. 
 * FEATURE IMPROVEMENT: Made the Save Report option a bit less prominent.
 * BUG FIX: Typo correction in the Parameters Editor tab.
 * BUG FIX: Fixed some bugs related to the saving of the report.

Download Count: 0

----

**Changes in SearchGUI 1.5.1 (July 4. 2011):**

 * NEW FEATURE: The number of currently selected modifications are now displayed above the corresponding modification lists.
 * NEW FEATURE: Made it possible to resize the dialog.
 * FEATURE IMPROVEMENT: Increased the height of the dialog slightly so that the scroll bars in the modification lists are displayed correctly in the default size.
 * BUG FIX: Fixed a bug where the automatically stored SearchGUI properties were stored in a .parameters file instead of in a .properties file.

Download Count: 20

----

**Changes in SearchGUI 1.5 (June 14. 2011):**

 * NEW FEATURE: Simple decoy databases creation.
 * NEW FEATURE: Possible to turn OMSSA charge detection on or off.
 * NEW FEATURE: Search parameters are now output in the result folder.
 * NEW FEATURE: Export of the input with the identification files.
 * NEW FEATURE: Tests to check if OMSSA and X!Tandem are correctly installed before starting the search.
 * NEW FEATURE: Added a wrapper to start the tool with increased memory boundaries. 
 * FEATURE IMPROVEMENT: Made sure that exception stack traces are always printed and sent to the error log.
 * FEATURE IMPROVEMENT: The database will be formated only if OMSSA is enabled. 
 * FEATURE IMPROVEMENT: Better handling of redundant modifications for X Tandem.
 * FEATURE IMPROVEMENT: Better parsing of sequence ids.
 * FEATURE IMPROVEMENT: Updated the look and feel to Nimbus.
 * FEATURE IMPROVEMENT: Improved GUI.
 * FEATURE IMPROVEMENT: Updated the waiting dialog to show the actual progress of the search.
 * BUG FIX: Fixed a bug where the values for OMSSA_PRECURSOR_ELIMINATION and OMSSA_PRECURSOR_SCALING where interchanged when extracted from the properties file.
 * LIBRARY UPDATE: Updated utilities to 3.1.10.

Download Count: 12

----

**Changes in SearchGUI 1.4.2 (November 15. 2010):**

 * NEW FEATURE: Added tooltips to the modification lists showing modification mass, residues affected etc.
 * BUG FIX: Fixed a bug that occurred when switching between "Most Used Modifications" and "All Modifications" in the drop down menu.

Download Count: 128

----

**Changes in SearchGUI 1.4.1 (November 9. 2010):**

 * NEW FEATURE: Added default versions of the search engines for Mac to the release.
 * NEW FEATURE: SearchGUI now defaults to the correct OS versions of OMSSA and XTandem at first startup.
 * FEATURE IMPROVEMENT: The permissions for the search engine (and makeblastdb) files are always set to 'executable' before being ran.
 * BUG FIX: Fixed several Mac related search engine bugs. 
 * BUG FIX: Fixed a bug in the command line interface where switching xtandem off was ignored.
 * BUG FIX: Fixed a bug with the -no and -nox parameters for peptide length limits.
 * NOTE: Java 1.6 is now required.

Download Count: 0

----

**Changes in SearchGUI 1.4 (November 2. 2010):**

 * FEATURE IMPROVEMENT: Simpler selection of modifications.
 * FEATURE IMPROVEMENT: Improved graphical user interface.
 * FEATURE IMPROVEMENT: Redesigned the underlying architecture.
 * NOTE: Please note that modifications will not be loaded from configuration files generated with SearchGUI older than version 1.4. 

Download Count: 3

----

**Changes in SearchGUI 1.3.3 (October 25. 2010):**

 * NEW FEATURE: Added command line support, i.e., SearchGUI can now be ran from the command line with parameters, and even without the GUI being displayed.

Download Count: 2

----

**Changes in SearchGUI 1.3.2 (September 3. 2010):**

 * BUG FIX: Fixed a bug in the return enzyme as a string for X!Tandem method. 
 * BUG FIX: Fixed a bug resulting the OMSSA modification files not being written to the results folder. 
 * BUG FIX: Fixed some typos in the XTandem XML file names.

Download Count: 15

----

**Changes in SearchGUI 1.3.1 (September 2. 2010):**

 * NEW FEATURE: Added a test for new versions of SearchGUI when starting the tool.
 * FEATURE IMPROVEMENT: Updated Manual.
 * FEATURE IMPROVEMENT: Now uses makeblastdb instead of the deprecated formatdb. This also makes it possible to support Linux and Mac OSX versions of OMSSA without having to install this file manually.
 * FEATURE IMPROVEMENT: Removed unused files from the OMSSA Windows installations.
 * FEATURE IMPROVEMENT: Added ".fas" as an allowed extension for FASTA files.
 * BUG FIX: Removed a detected Java 1.6 dependency for loading the configuration file.

Download Count: 0

----

**Changes in SearchGUI 1.3 (August 31. 2010):**

 * FEATURE IMPROVEMENT: Added an error log feature, resulting in all SearchGUI errors ending up in the ErrorLog file in the conf folder.

Download Count: 6

----

**Changes in SearchGUI 1.2 (August 31. 2010):**

 * NEW FEATURE: It is now possible to start SearchGUI from another tools.
 * NEW FEATURE: New search parameters added: it is now possible to select the fragment ions to search for. 
 * NEW FEATURE: Additional parameters for OMSSA were added for ETD searches as well as no-enzyme and semi-tryptic searches.
 * FEATURE IMPROVEMENT: Improvements user interface.
 * FEATURE IMPROVEMENT: Modifications and Enzyme handling has been externalized in the compomics-utilities package to ensure compatibility with the other tools we develop. The latest OMSSA developments are now taken into account with more PTMs and enzymes supported.

Download Count: 1

----

**Changes in SearchGUI 1.1 (August 23. 2010):**

 * The first public release of SearchGUI.

Download Count: 4

----