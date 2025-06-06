---
title: "Release notes (July 2011  to  August 2015)"
layout: default
permalink: "/projects/peptide-shaker/wiki/Release-notes-%28July-2011--to--August-2015%29"
tags: wiki, peptide-shaker
project: "peptide-shaker"
github_project: "https://github.com/CompOmics/peptide-shaker"
---

# ReleaseNotes (July 2011 to August 2015)

----

**Changes in PeptideShaker 0.41.1 (July 1. 2015):**

  * BUG FIX: Added support for loading Comet .pep.xml and Tide .txt files via the command line.


---


**Changes in PeptideShaker 0.41.0 (June 30. 2015):**

  * NEW FEATURE: Added support for raw files as spectrum input in PRIDE Reshake.

  * FEATURE IMPROVEMENT: Added support for zip files in the PRIDE Reshake.

  * BUG FIX: Fixed a bug in the PRIDE Reshake were canceling the public/private dialog still downloaded the public data.

  * LIBRARY UPDATE: Updated utilities to version 3.49.21.


---


**Changes in PeptideShaker 0.40.4 (June 28. 2015):**

  * FEATURE IMPROVEMENT: Added a "Download All" option to the files table in PRIDE Reshake.

  * BUG FIX: Fixed a bug that results in the PRIDE XML export not working.


---


**Changes in PeptideShaker 0.40.3 (June 23. 2015):**

  * BUG FIX: Corrected a bug in the validation of datasets with few hits.


---


**Changes in PeptideShaker 0.40.2 (June 21. 2015):**

  * FEATURE IMPROVEMENT: Updated the Example Dataset.

  * BUG FIX: Fixed bugs in accessing private data in PRIDE Reshake.
  * BUG FIX: Fixed a problem with the modification parsing in the mzid parser.
  * BUG FIX: Fixed a possible multi threading issue when loading PSMs.
  * BUG FIX: Fixed a bug in the GO mappings that resulted from a change in the Ensembl BioMart.
  * BUG FIX: Corrected a bug where the assumptions validation level was not set.

  * LIBRARY UPDATE: Updated web-service-model to version 0.2.12.
  * LIBRARY UPDATE: Updated utilities to version 3.49.19.


---


**Changes in PeptideShaker 0.40.1 (June 7. 2015):**

  * BUG FIX: Avoided restoring the database connection when active during saving.

  * LIBRARY UPDATE: Updated utilities to version 3.49.9.


---


**Changes in PeptideShaker 0.40.0 (June 6. 2015):**

  * FEATURE IMPROVEMENT: Made sure the search settings are only editable when they can actually be edited.
  * FEATURE IMPROVEMENT: Made the Group Selection table in the Validation tab resize with the size of the frame.

  * BUG FIX: Fixed a bug in the validation of matches with uncommon distributions of decoys.
  * BUG FIX: Avoiding the creation of empty distributions.

  * LIBRARY UPDATE: Updated utilities to version 3.49.7.


---


**Changes in PeptideShaker 0.39.1 (June 3. 2015):**

  * BUG FIX: Fixed a bug in the progress display when validating matches.

  * LIBRARY UPDATE: Updated utilities to version 3.49.4.


---


**Changes in PeptideShaker 0.39.0 (June 2. 2015):**

  * FEATURE IMPROVEMENT: Parsing big mzIdentML files is now a lot faster and uses less memory.
  * FEATURE IMPROVEMENT: The validation QC filters are available again (beta).
  * FEATURE IMPROVEMENT: Updated the Ensembl mappings to Ensembl 80.
  * FEATURE IMPROVEMENT: Made sure that all fragment ions are annotated when exporting to mzIdentML and PRIDE XML.

  * BUG FIX: Removed an unnecessary white space in the Peptide tag in the mzIdentML export.
  * BUG FIX: The modification specificity rules are now annotated correctly.
  * BUG FIX: Corrected bugs in PTM scoring.
  * BUG FIX: Implemented PTM specific sequence matching preferences.

  * LIBRARY UPDATE: Updated utilities to version 3.49.2.


---


**Changes in PeptideShaker 0.38.5 (May 16. 2015):**

  * FEATURE IMPROVEMENT: Added support for parsing UniRef headers.
  * FEATURE IMPROVEMENT: Sped up the simplification of the protein groups.

  * LIBRARY UPDATE: Updated utilities to version 3.48.5.


---


**Changes in PeptideShaker 0.38.4 (May 12. 2015):**

  * NEW FEATURE: Added the option to start PeptideShaker with opening a zipped project from a URL.
  * NEW FEATURE: Made it possible to load zipped cps files via the PeptideShaker GUI command line.

  * FEATURE IMPROVEMENT: Leading and trailing white space is now removed before parsing FASTA headers.

  * LIBRARY UPDATE: Updated utilities to version 3.48.4.


---


**Changes in PeptideShaker 0.38.3 (May 8. 2015):**

  * BUG FIX: Fixed a bug in calculating the min/max mz value in a spectrum that occurred if the spectrum contained no peaks.

  * LIBRARY UPDATE: Updated utilities to version 3.48.2.


---


**Changes in PeptideShaker 0.38.2 (May 4. 2015):**

  * BUG FIX: Fixed a bug in the PTM scoring that occurred if using Java 7.

  * LIBRARY UPDATE: Updated utilities to version 3.48.1.


---


**Changes in PeptideShaker 0.38.1 (April 25. 2015):**

  * FEATURE IMPROVEMENT: Increased the precision of the PhosphoRS calculation.

  * BUG FIX: Fixed a bug in the spectrum annotation where the intensity limit was not set correctly.
  * BUG FIX: Fixed a bug in the CV term mapping for pyro-cmc.
  * BUG FIX: Fixed a bug in the saving that made it impossible to open saved projects.
  * BUG FIX: Fixed a backwards computability issue with the spectrum annotation.
  * BUG FIX: Fixed a bug in the spectrum annotation where the intensity limit was not set correctly.
  * BUG FIX: Corrected a bug in the setting of temporary folders.

  * LIBRARY UPDATE: Updated utilities to version 3.47.4.


---


**Changes in PeptideShaker 0.38.0 (April 17. 2015):**

  * FEATURE IMPROVEMENT: Multithreaded and thus sped up the validation, filtering and PTM scoring.

  * BUG FIX: Fixed issues in the PhosphoRS scoring.
  * BUG FIX: Corrected a threading issue in the validation of multiple mgf files.
  * BUG FIX: Corrected a memory leak, thus reducing the memory usage.

  * LIBRARY UPDATE: Updated utilities to version 3.47.1.


---


**Changes in PeptideShaker 0.37.7 (March 26. 2015):**

  * FEATURE IMPROVEMENT: Added a simpler way of resetting the spectrum annotation.
  * FEATURE IMPROVEMENT: Updated the Ensembl mappings to Ensembl 79.

  * BUG FIX: Fixed bugs in the peptide annotation where the location of the PTM site was incorrect.
  * BUG FIX: Fixed backwards compatibility issues in the TideParameters.
  * BUG FIX: Fixed a typo in the mass for the TMT130 reporter for 6plex TMT.
  * BUG FIX: Fixed bugs related to starting peptides and PSMs directly in the tables.
  * BUG FIX: The precursor m/z error filter is disabled if very few precursors are found.

  * LIBRARY UPDATE: Updated utilities to version 3.46.9.


---


**Changes in PeptideShaker 0.37.6 (March 11. 2015):**

  * FEATURE IMPROVEMENT: Added protein coverage for the main protein to the mzid export.
  * FEATURE IMPROVEMENT: Made it possible to cancel the batch loading in the table models.
  * FEATURE IMPROVEMENT: PSI-MS CV terms are now used for the fragment and precursor ions instead of PRIDE CV terms.

  * BUG FIX: Corrected a bug in the handling of default paths.
  * BUG FIX: Fixed a possible null pointer in the New Project dialog occurring if the search parameters did not have a FASTA file.
  * BUG FIX: Fixed a null pointer in the PTM tab that occurred if a variable PTM was not detected in any peptides.
  * BUG FIX: Fixed bugs in the equals methods for the Tide parameters.
  * BUG FIX: Removed the text from the precursor m/z field in the PSM tab in the FindDialog.

  * LIBRARY UPDATE: Updated utilities to version 3.45.44.


---


**Changes in PeptideShaker 0.37.5 (February 17. 2015):**

  * FEATURE IMPROVEMENT: Sped up the PSM exports.
  * FEATURE IMPROVEMENT: Improved the format selection when exporting.

  * BUG FIX: The progress bar is now displayed when unzipping PeptideShaker projects.

  * LIBRARY UPDATE: Updated utilities to version 3.45.35.


---


**Changes in PeptideShaker 0.37.4 (February 16. 2015):**

  * FEATURE IMPROVEMENT: It is now possible to open zipped PeptideShaker projects.
    * Follow-up, report, and mzidCLI also support zip file input.
  * FEATURE IMPROVEMENT: Improved the error handling for the command line mode.
  * FEATURE IMPROVEMENT: Made it possible to control the PSM sort order (score or retention time).
  * FEATURE IMPROVEMENT: Removed spaces from the name of the command line exports.

  * BUG FIX: Gene mapping files are now set when starting a command line.
  * BUG FIX: Fixed a bug where the project creation date was not set in the project details.
  * BUG FIX: Fixed a bug in the color coding of the PI column in the peptide table in the PTMs tab.

  * LIBRARY UPDATE: Updated utilities to version 3.45.33.


---


**Changes in PeptideShaker 0.37.3 (January 29. 2015):**

  * BUG FIX: Fixed a bug where neutral losses and reporter ions for user defined modifications disappeared.

  * LIBRARY UPDATE: Updated utilities to version 3.45.25.


---


**Changes in PeptideShaker 0.37.2 (January 29. 2015):**

  * BUG FIX: Fixed a bug in the pepxml reader where only the location of the first variable PTM in a peptide was correct.
  * BUG FIX: Fixed a bug in the parsing iTRAQ PTMs for X!Tandem data.
  * BUG FIX: Fixed bugs in the peptide PTM annotation and tooltips.
  * BUG FIX: Fixed a bug where score\_neutral\_losses had not been included in the list of supported parameters.
  * BUG FIX: Backward compatibility fixes.

  * LIBRARY UPDATE: Updated xtandem parser to version 1.7.18.
  * LIBRARY UPDATE: Updated utilities to version 3.45.24.


---


**Changes in PeptideShaker 0.37.1 (January 23. 2015):**

  * BUG FIX: The example dataset now works again.


---


**Changes in PeptideShaker 0.37.0 (January 23. 2015):**

  * NEW FEATURE: Added support for Tide. (beta)

  * FEATURE IMPROVEMENT: Added retention time to the mzid export.
  * FEATURE IMPROVEMENT: Updated Ensembl Genomes to version 25.

  * BUG FIX: In the New Project dialog loading a project without changing the search settings resulted in a missing FASTA file.
  * BUG FIX: In the Spectrum IDs tab the retention time conversion to minutes was not done for the minimum retention time value.
  * BUG FIX: In the mzid export a test CV term for the upcoming mzid 1.2 format changes was not removed.
  * BUG FIX: The accuracy slider in the spectrum panels had stopped working.
  * BUG FIX: In the MzIdentMLIdfileReader fixed terminal modifications were not handled correctly (which affected TMT among others).

  * LIBRARY UPDATE: Updated utilities to version 3.45.19.


---


**Changes in PeptideShaker 0.36.2 (January 17. 2015):**

  * NEW FEATURE: Added the option to turn on/off the labels for the proteins and peptides in the protein inference graph.
  * NEW FEATURE: Added the option to select all proteins and peptides in the protein inference graph.

  * FEATURE IMPROVEMENT: Added the PeptideShaker PubMed ID to the methods export dialog.

  * BUG FIX: Fixed a bug in the PRIDE Reshake where the drop down menus in the project filtering dialog did not include all values.


---


**Changes in PeptideShaker 0.36.1 (January 11. 2015):**

  * FEATURE IMPROVEMENT: Updated the Example Dataset.


---


**Changes in PeptideShaker 0.36.0 (January 10. 2015):**

  * NEW FEATURE: Mirrored spectra support in the spectrum panels.
  * NEW FEATURE: Protein inference graphs in the protein inference dialogs.
  * NEW FEATURE: neXtProt FASTA headers can now be parsed.

  * FEATURE IMPROVEMENT: Multithreaded the scoring of PTMs.
  * FEATURE IMPROVEMENT: Iterating matches is now faster and requires less memory.
  * FEATURE IMPROVEMENT: Updated the gene and GO mappings to Ensembl version 78.
  * FEATURE IMPROVEMENT: Extended the file size columns in the PRIDE Reshake to "Size (MB)" and added sparklines.
  * FEATURE IMPROVEMENT: The downloading of the PRIDE projects in the Reshake is now done in batches and with a progress bar.
  * FEATURE IMPROVEMENT: Improved the way the selection of multiple PSMs are annotated in the spectrum panel border.
  * FEATURE IMPROVEMENT: Multiple selection in the PTM tables in the Search Settings Dialog no longer requires the use of the Ctrl key.
  * FEATURE IMPROVEMENT: Added the files reprocessed to the PRIDE Reshake report.
  * FEATURE IMPROVEMENT: Added the Enzymatic column to the ProteinInferencePeptideLevelDialog.
  * FEATURE IMPROVEMENT: Scientific notation is now used for the spectrum counting and intensity columns.
  * FEATURE IMPROVEMENT: Retention time is now given in minutes instead of seconds.
  * FEATURE IMPROVEMENT: The search parameters can now be extracted from the SearchGUI zip file.
  * FEATURE IMPROVEMENT: Minor improvements to the command line progress display.
  * FEATURE IMPROVEMENT: Made it possible to set the Java Home from the GUI.
  * FEATURE IMPROVEMENT: Added a shortcut to the PRIDE free text search in the Project filtering dialog in the PRIDE Reshake.
  * FEATURE IMPROVEMENT: Added CV term for the MyriMatch e-values to the mzid and PRIDE XML exports.
  * FEATURE IMPROVEMENT: Improved the selection of the search engine first hit.
  * FEATURE IMPROVEMENT: Added a dialog to edit the path preferences.
  * FEATURE IMPROVEMENT: Improved the handling of an exception at startup.

  * BUG FIX: Fixed a bug in the ExportGraphicsDialog where the last selected folder was not set.
  * BUG FIX: Fixed a bug where the tool failed to start if less than 1GB of memory was the maximum value allowed by the system.
  * BUG FIX: Fixed a bug in the Species Dialog where the text on the Update/Download button was not always correct.
  * BUG FIX: Fixed a minor GUI issue with the progress bar in the PRIDE Reshake.
  * BUG FIX: The sequence matching type is now set to amino acid when checking the fixed modifications.
  * BUG FIX: The PSM PTM mapping no longer ignores the user canceling the process in the waiting dialog.
  * BUG FIX: Fixed a bug with the renderer for the coverage column in the Fractions tab.
  * BUG FIX: Solved issues that resulted in the best match selection being different between Java 7 and 8.

  * LIBRARY UPDATE: Updated omssa-parser to version 1.6.12.
  * LIBRARY UPDATE: Updated xtandem-parser to version 1.7.17.
  * LIBRARY UPDATE: Updated mascotdatfile to version 3.4.28.
  * LIBRARY UPDATE: Updated utilities to version 3.45.18.


---


**Changes in PeptideShaker 0.35.6 (December 1. 2014):**

  * BUG FIX: Fixed an issue in the retrieval of public PRIDE projects.
  * BUG FIX: Fixed some possible issues in the Search Settings Dialog.
  * BUG FIX: Improved the handling of canceling the Search Settings and Processing Preferences dialogs.

  * LIBRARY UPDATE: Updated utilities to version 3.43.17.


---


**Changes in PeptideShaker 0.35.5 (November 27. 2014):**

  * BUG FIX: Corrected possible null pointers in the PRIDE XML and mzIdentML exports when processing Mascot scores.
  * BUG FIX: Fixed a bug in the conversion of mgf files for use in Comet where scan numbers resulted in it being impossible to map back to the original mgf file.

  * LIBRARY UPDATE: Updated utilities to version 3.43.16.


---


**Changes in PeptideShaker 0.35.4 (November 18. 2014):**

  * BUG FIX: Fixed a bug in adding decoy sequences to FASTA files containing headers without descriptions.


---


**Changes in PeptideShaker 0.35.3 (November 17. 2014):**

  * FEATURE IMPROVEMENT: Updated Ensembl Genomes to version 24, adding Zootermopsis nevadensis.
  * FEATURE IMPROVEMENT: Added a check for if SearchGUI is started from within a zip file.
  * FEATURE IMPROVEMENT: Added project tags to the project table in PRIDE Reshake.
  * FEATURE IMPROVEMENT: PRIDE Reshake: added sparkline for the file size column.

  * BUG FIX: Fixed a bug that resulted in all keys released when the PSM table had focus resulted in the spectrum annotation disappearing.
  * BUG FIX: Fixed a bug in the download of gene mappings for non-vertebrate species.
  * BUG FIX: Fixed some special case Derby shutdown and restart issues.

  * LIBRARY UPDATE: Added Jung2 dependencies.
  * LIBRARY UPDATE: Updated web-service-model to version 0.2.7.
  * LIBRARY UPDATE: Updated utilities to version 3.43.13.


---


**Changes in PeptideShaker 0.35.2 (November 14. 2014):**

  * FEATURE IMPROVEMENT: Multithreaded the import of PSMs.
  * FEATURE IMPROVEMENT: Minor speed improvements to the tag and peptide mapping.
  * FEATURE IMPROVEMENT: Disabled the batch peptide mapping on low memory setups.

  * BUG FIX: Fixed a bug in the appending of decoy sequence which in some cases altered the FASTA headers.
  * BUG FIX: Corrected a bug when working with very small databases.

  * LIBRARY UPDATE: Updated utilities to version 3.43.10.


---


**Changes in PeptideShaker 0.35.1 (October 26. 2014):**

  * BUG FIX: Fixed a bug in the auto update feature.
  * BUG FIX: Fixed some backward compatibility issues.
  * BUG FIX: Corrected a bug in the tag mapping.

  * LIBRARY UPDATE: Updated utilities to version 3.41.1.


---


**Changes in PeptideShaker 0.35.0 (October 23. 2014):**

  * NEW FEATURE: Comet (or more generally pep.xml) is now supported.
  * NEW FEATURE: Export features as Excel files.
  * NEW FEATURE: Added progress bar when zipping.

  * FEATURE IMPROVEMENT: Updated Ensembl Genomes to version 77, adding Vervet-AGM (Chlorocebus sabaeus).
  * FEATURE IMPROVEMENT: Improved the PTM annotation in tables and tooltips.
  * FEATURE IMPROVEMENT: Improved the handling of ambiguously localized PTMs.
  * FEATURE IMPROVEMENT: Improved the handling of complex PTM combinations.
  * FEATURE IMPROVEMENT: Improved the mapping of PTM scores at the peptide and protein level.
  * FEATURE IMPROVEMENT: Sped up the unzipping of projects in the New Project dialog.
  * FEATURE IMPROVEMENT: Sped up the PTM scoring.
  * FEATURE IMPROVEMENT: Sped up the peptide to protein mapping using multithreading.
  * FEATURE IMPROVEMENT: Added an OK/Cancel option to the save dialog appearing when exporting as zipping and the project is not saved.
  * FEATURE IMPROVEMENT: The list of database types and their occurrences is now included in the FASTA index.
  * FEATURE IMPROVEMENT: The "not a UniProt database" warning is now only shown if the main database type is not UniProt (hence adding custom headers from other databases is no longer an issue.)
  * FEATURE IMPROVEMENT: Renamed "no enzyme" to the more understandable "unspecific".
  * FEATURE IMPROVEMENT: Added support for unspecific cleavage for X!Tandem.
  * FEATURE IMPROVEMENT: Added a button for selecting search settings files in the New Project dialog.

  * BUG FIX: Fixed a bug in the use of the Ensembl gene mappings where a field had been renamed in the Ensembl web service.
  * BUG FIX: Corrected a bug impairing the import of results without decoys sequences.
  * BUG FIX: Fixed a bug in the New Project Dialog where canceling the unzipping still loaded the files.
  * BUG FIX: Fixed a bug in the Spectrum IDs tab where the fixed PTMs where always shown in the Spectrum Identification Results table.
  * BUG FIX: Fixed a bug that resulted in asking if the user wanted to save projects even though nothing had actually changed.
  * BUG FIX: Made sure that the correct sequence matching preferences are set when loading PeptideShaker projects.
  * BUG FIX: The PeptideShaker table in the Spectrum IDs tab now has the correct color for the links even when the row is selected.
  * BUG FIX: Fixed a minor bug in the table to file export for the PSM tables.
  * BUG FIX: The table to file exports now work again for the 3D Structures tab.
  * BUG FIX: Fixed a bug in writing of user parameters with values in the mzid export.
  * BUG FIX: Fixed a bug in the protein coverage panel where the whole protein and top down enzymes were not supported correctly.

  * LIBRARY UPDATE: Updated utilities to version 3.40.0.


---


**Changes in PeptideShaker 0.34.0 (September 19. 2014):**

  * FEATURE IMPROVEMENT: Improved the memory handling when loading data.
  * FEATURE IMPROVEMENT: Tried to speed up the loading of the data.
  * FEATURE IMPROVEMENT: Improved the handling of poorly localized PTMs.
  * FEATURE IMPROVEMENT: Tried to escape regular expressions in protein accession numbers.
  * FEATURE IMPROVEMENT: The waiting handler is now used when unzipping SearchGUI results in PeptideShaker.
  * FEATURE IMPROVEMENT: Fixed an issue with indexing mgf files with empty charge tags.

  * BUG FIX: Fixed a command line bug where the neutral losses were not set, resulting in slightly different results compared to the GUI.
  * BUG FIX: The sequence matching preferences now change according to the search parameters in the New Project Dialog.
  * BUG FIX: Fixed a bug where the show/hide of the fixed PTMs was not working as it should in all tabs.
  * BUG FIX: Corrected a bug where the cleaning of the obsolete protein trees was deleting all files in the folder.

  * LIBRARY UPDATE: Updated jsparklines to version 1.0.4.
  * LIBRARY UPDATE: Updated utilities to version 3.37.3.


---


**Changes in PeptideShaker 0.33.6 (September 8. 2014):**

  * FEATURE IMPROVEMENT: Updated to the new PRIDE web service model (needed for the PRIDE Reshake).
  * FEATURE IMPROVEMENT: Improved the parsing of headers of type genome translated to protein sequence.

  * LIBRARY UPDATE: Updated web-service-model to version 0.2.4.
  * LIBRARY UPDATE: Updated utilities to version 3.35.7.


---


**Changes in PeptideShaker 0.33.5 (August 30. 2014):**

  * FEATURE IMPROVEMENT: Improved the mapping to the protein 3D structure, resulting in a lot more mapped peptides.


---


**Changes in PeptideShaker 0.33.4 (August 30. 2014):**

  * FEATURE IMPROVEMENT: Changed the default PTM localization score to A-score.
  * FEATURE IMPROVEMENT: Added a special fix to the file import to escape Mascot mapping multiple fixed PTMs to the same residue.
  * FEATURE IMPROVEMENT: Updated the example dataset.

  * BUG FIX: Added a missing line break in the display of the extracted search parameters in PRIDE Reshake.

  * LIBRARY UPDATE: Updated utilities to version 3.35.6.


---


**Changes in PeptideShaker 0.33.3 (August 29. 2014):**

  * FEATURE IMPROVEMENT: Updated the getting started slides.
  * FEATURE IMPROVEMENT: Changed the default PRIDE export to mzIdentML.
  * FEATURE IMPROVEMENT: Made the progress bar when unzipping in the New Project dialog indeterminate.
  * FEATURE IMPROVEMENT:  Hid the PRIDE generated mgf and mzTab files from the Reshake as the file links for these do not yet work.

  * BUG FIX: Fixed a bug in the setting of the species in the PRIDE Reshake.
  * BUG FIX: Fixed a bug with the use of custom PTM patterns.
  * BUG FIX: Fixed a bug with the tooltips for the PTMs in the Search Settings dialog.
  * BUG FIX: Fixed a bug in the default peptide export where additional empty columns where added messing.

  * LIBRARY UPDATE: Updated utilities to version 3.35.5.


---


**Changes in PeptideShaker 0.33.1 (August 21. 2014):**

  * FEATURE IMPROVEMENT: Updated Ensembl genomes to release 23.

  * BUG FIX: Fixed an issue in the auto update feature that could occur on specific client machine setups.

  * LIBRARY UPDATE: Updated utilities to version 3.35.3.


---


**Changes in PeptideShaker 0.33.0 (August 19. 2014)**

  * FEATURE IMPROVEMENT: Improvements in the peptide to protein inference.
  * FEATURE IMPROVEMENT: Peptides are now sorted before remapped to proteins, which should be quicker.
  * FEATURE IMPROVEMENT: Peptides with too many Xs are now filtered out.
  * FEATURE IMPROVEMENT: Several fixes related to running PeptideShaker from SearchGUI.

  * BUG FIX: Fixed a bug in the import in the New Project dialog where the listing the mgf files use) was not used if inside a zip file.
  * BUG FIX: Settings files from MS Amanda are no longer selected as identification files.

  * LIBRARY UPDATE: Updated mascotdatfile parser to version 3.4.25.
  * LIBRARY UPDATE: Updated omssa parser to version 1.6.9.
  * LIBRARY UPDATE: Updated xtandem parser to version 1.7.13.
  * LIBRARY UPDATE: Updated utilities to version 3.35.2.


---


**Changes in PeptideShaker 0.32.3 (August 7. 2014)**

  * NEW FEATURE: Added PTM tooltips in the tables in the SearchSettings dialog.

  * FEATURE IMPROVEMENT: Updated the Ensembl mappings to Ensembl 76 and added seven new species: duck, cave fish, flycatcher, cod, spotted gar, sheep and amazon molly.
  * FEATURE IMPROVEMENT: Improved the species names listed for vertebrates.
  * FEATURE IMPROVEMENT: Minor formatting improvement in the PeptideShakerMethods export.

  * BUG FIX: Fixed a bug where the search engine version numbers had gone missing when loading from mzid files.

  * LIBRARY UPDATE: Updated utilities to version 3.31.2.


---


**Changes in PeptideShaker 0.32.2 (August 1. 2014)**

  * FEATURE IMPROVEMENT: Improved the MyriMatch support for terminal PTMs.
  * FEATURE IMPROVEMENT: Improved handling of end of file exceptions occurring when opening a corrupt project.

  * BUG FIX: Corrected a bug where the id filters were not always used.

  * LIBRARY UPDATE: Updated utilities to version 3.30.3.


---


**Changes in PeptideShaker 0.32.1 (July 31. 2014)**

  * NEW FEATURE: Added a new command line parameter called species\_update to the PeptideShakerCLI to control the update of species and GO mappings.

  * FEATURE IMPROVEMENT: Updated the included human gene and GO mappings to Ensembl version 75.
  * FEATURE IMPROVEMENT: Improved the tag to protein mapping.
  * FEATURE IMPROVEMENT: Changed the order of the columns in the PSM export.
  * FEATURE IMPROVEMENT: Fixed issues with automatic update of gene and GO mappings when PeptideShaker was started from SearchGUI.

  * LIBRARY UPDATE: Updated utilities to version 3.30.1.


---


**Changes in PeptideShaker 0.32.0 (July 29. 2014)**

  * NEW FEATURE: Added support for MyriMatch.
  * NEW FEATURE: Support of zip export from the command line.
  * NEW FEATURE: Possible to import zipped SearchGUI projects.
  * NEW FEATURE: Added export functionality for search engine results.

  * FEATURE IMPROVEMENT: Made sure that the column in the exports are always in the same order.
  * FEATURE IMPROVEMENT: Made sure that the PeptideShaker log is saved even if the processing fails when run from SearchGUI.

  * BUG FIX: Fixed a bug in the PRIDE Reshake to support zipped mgf files.
  * BUG FIX: X!Tandem modifications are now added only if X!Tandem results are found.
  * BUG FIX: Corrected the output of the discarded protein mappings.
  * BUG FIX: Corrected minor HTML formatting issues in the help texts.

  * LIBRARY UPDATE: Updated jsparklines to version 0.8.0.
  * LIBRARY UPDATE: Updated utilities to version 3.29.7.


---


**Changes in PeptideShaker 0.31.5 (June 26. 2014)**

  * FEATURE IMPROVEMENT: Improved the way multiple species are supported in the UniProt link in the Reshake Settings dialog.
  * FEATURE IMPROVEMENT: The order of the search engines in the Spectrum IDs tab overview plots is now always the same.
  * FEATURE IMPROVEMENT: Added a remove all filters option in the main PRIDE Reshake window.
  * FEATURE IMPROVEMENT: Made sure that closing a dialog is always considered the same as clicking the cancel button.
  * FEATURE IMPROVEMENT: Extended the PRIDE Reshake help texts.


---


**Changes in PeptideShaker 0.31.4 (June 25. 2014)**

  * FEATURE IMPROVEMENT: Improved the Waiting Dialog to work better for big projects.
  * FEATURE IMPROVEMENT: Cleaned up the closing of the internal database connection.
  * FEATURE IMPROVEMENT: Improved the end of process messages in command lines.

  * BUG FIX: Fixed bugs in the mzid export, which now passes the PRIDE validation.
  * BUG FIX: Fixed a bug in the PRIDE XML export that resulted in the exported files not validating.
  * BUG FIX: Fixed a bug in the e-value parsing in the mzid reader.

  * LIBRARY UPDATE: Updated utilities to version 3.28.30.


---


**Changes in PeptideShaker 0.31.3 (June 18. 2014)**

  * FEATURE IMPROVEMENT: Improved the selections in the PRIDE Reshake Setup Dialog.

  * BUG FIX: Fixed a bug with case sensitivity in the PRIDE PTM mapping.
  * BUG FIX: Improved the PTM mapping during file import.

  * LIBRARY UPDATE: Updated utilities to version 3.28.22.


---


**Changes in PeptideShaker 0.31.2 (June 18. 2014)**

  * BUG FIX: Improved the PTM mapping during file import.
  * BUG FIX: Fixed bugs in the PRIDE Reshake.

  * LIBRARY UPDATE: Updated utilities to version 3.28.20.


---


**Changes in PeptideShaker 0.31.1 (June 18. 2014)**

  * BUG FIX: Fixed bugs in the PRIDE Reshake.


---


**Changes in PeptideShaker 0.31.0 (June 17. 2014)**

  * NEW FEATURE: Redesigned PRIDE Reshake.

  * BUG FIX: Fixed various bugs in the mzid export.

  * LIBRARY UPDATE: Updated utilities to version 3.28.18.


---


**Changes in PeptideShaker 0.30.2 (June 13. 2014)**

  * FEATURE IMPROVEMENT: Made it possible to extract the version number for MS Amanda csv files.
  * FEATURE IMPROVEMENT: Extended the PRIDE PTM mapping.

  * BUG FIX: Fixed a bug where PTM masses in MS Amanda files could not be processed if comma was used as the decimal symbol.
  * BUG FIX: Fixed typos in the spectrum panel help text.

  * LIBRARY UPDATE: Updated utilities to version 3.28.16.


---


**Changes in PeptideShaker 0.30.1 (June 5. 2014)**

  * BUG FIX: Fixed a bug in the parsing of terminal modifications for MS Amanda.
  * BUG FIX: Fixed a bug where MS Amanda results files where not recognized if PeptideShaker was started from SearchGUI.

  * LIBRARY UPDATE: Updated utilities to version 3.28.11.


---


**Changes in PeptideShaker 0.30.0 (June 5. 2014)**

  * NEW FEATURE: mzIdentML export.
  * NEW FEATURE: Import of mzid files from other algorithms than MS-GF+. (beta)

  * FEATURE IMPROVEMENT: Sped up the indexing of mgf files.
  * FEATURE IMPROVEMENT: Improved and extended the Methods Section export.
  * FEATURE IMPROVEMENT: Better formatting of long lines in the waiting handler.
  * FEATURE IMPROVEMENT: Removed the Venn diagram from the Spectrum IDs tab, as they only supported max three search engines.

  * BUG FIX: Fixed issues with opening cps files created on other platforms.
  * BUG FIX: Tried to make the table models more robust against database connection dropped issues.

  * LIBRARY UPDATE: Removed charts4j as a dependency.
  * LIBRARY UPDATE: Removed jdas as a dependency.
  * LIBRARY UPDATE: Updated utilities to version 3.28.10.


---


**Changes in PeptideShaker 0.29.1 (May 20. 2014)**

  * BUG FIX: Fixed a bug with the gene/GO downloads for non-vertebrate species.

  * LIBRARY UPDATE: Updated utilities to version 3.26.41.


---


**Changes in PeptideShaker 0.29.0 (May 20. 2014)**

  * FEATURE IMPROVEMENT: Improved the handling of terminal PTMs.
  * FEATURE IMPROVEMENT: Improved the canceling of the species and GO downloads.
  * FEATURE IMPROVEMENT: Changed the message given if the FASTA file is not found from an error message to a warning message.
  * FEATURE IMPROVEMENT: Updated the Java Settings dialogs.
  * FEATURE IMPROVEMENT: Added a longer time out for some of the IO intensive methods, which could result in issues on slower systems.

  * BUG FIX: Corrected a bug where the PSM precursor errors were sometime added twice.
  * BUG FIX: Corrected an error in the PRIDE XML export.
  * BUG FIX: Fixed a bug in the handling of protein keys that are too long for the database.
  * BUG FIX: Fixed a bug in the peptide filters where the modifications where not set correctly.
  * BUG FIX: Fixed a bug in the sorting in the coverage column.
  * BUG FIX: Fixed a bug in the progress display when downloading gene/GO details.

  * LIBRARY UPDATE: Updated jsparklines to version 0.6.7.
  * LIBRARY UPDATE: Updated utilities to version 3.26.39.


---


**Changes in PeptideShaker 0.28.3 (May 7. 2014):**

  * BUG FIX: Fixed a bug in the sequence coverage panel when using semi specific enzymes.
  * BUG FIX: Fixed a case sensitivity bug in the Find feature in the Spectrum IDs tab.


---


**Changes in PeptideShaker 0.28.2 (May 6. 2014):**

  * FEATURE IMPROVEMENT: Simplified the way SearchGUI can be downloaded and updated from within PeptideShaker.
  * FEATURE IMPROVEMENT: Made it possible to rely on spectrum indexes if an mzid file does not contain the spectrum titles.
  * FEATURE IMPROVEMENT: Updated the example dataset.

  * BUG FIX: Fixed a bug in the sequence coverage panel where the protein accession was used instead of the protein group key.
  * BUG FIX: Added a print out of the stack trace if the estimateSpectrumCounting method finds a non-existing protein key.

  * LIBRARY UPDATE: Updated utilities to version 3.26.33.


---


**Changes in PeptideShaker 0.28.1 (April 29. 2014):**

  * NEW FEATURE: Added new command line options for path configuration.
  * NEW FEATURE: Added a first draft of a methods section writing dialog. (beta)
  * NEW FEATURE: Made the species download available from the command line.
  * NEW FEATURE: Added a reset thresholds button in the Validation tab.

  * FEATURE IMPROVEMENT: The sequence coverage now also shows the doubtful and not validated matches.
  * FEATURE IMPROVEMENT: Added a check and warning if using Java 1.5 or 1.6.
  * FEATURE IMPROVEMENT: Renamed the Reshake button in the WelcomeDialog to PRIDE Reshake.
  * FEATURE IMPROVEMENT: Added the algorithm scores in the export.
  * FEATURE IMPROVEMENT: The validation thresholds are now displayed in the match validation dialog.
  * FEATURE IMPROVEMENT: Made it possible to use the escape button to close the New Project and Getting Started dialogs.
  * FEATURE IMPROVEMENT: Made it possible to cancel the PDB mapping downloads.
  * FEATURE IMPROVEMENT: Added the possibility for the user to turn on and off the auto update.

  * BUG FIX: Fixed a bug in the PtmSiteInferenceDialog where the PTM localization in the two tables were not the same.
  * BUG FIX: Fixed a bug in the PTM panel where the orange icon got stuck.
  * BUG FIX: Added .mzid and .cvs to PeptideShaker command line option description.
  * BUG FIX: Fixed a bug in the MzIdentML Export Dialog where the convert button could be clicked before an output file was selected.
  * BUG FIX: Fixed some issues with incorrect table references in the Overview and 3D Structures tab.
  * BUG FIX: Fixed problems with turning the sparklines on/off.

  * LIBRARY UPDATE: Updated jsparklines to version 0.6.6.
  * LIBRARY UPDATE: Updated utilities to version 3.26.28.


---


**Changes in PeptideShaker 0.28.0 (April 11. 2014):**

  * NEW FEATURE: Added support for MS Amanda (beta).

  * FEATURE IMPROVEMENT: The PSM scoring now adapts to the different fractions when possible.

  * BUG FIX: Fixed problems with creating terminal PTMs with empty modification patterns.
  * BUG FIX: Fixed a bug in the table model in the Modifications tab.

  * LIBRARY UPDATE: Updated utilities to version 3.26.14.


---


**Changes in PeptideShaker 0.27.4 (April 1. 2014):**

  * BUG FIX: Fixed a bug in the PRIDE export where the PRIDE XML validation failed.
  * BUG FIX: Fixed a bug in the export of accession numbers in the Annotation panel where also the validation status was included.


---


**Changes in PeptideShaker 0.27.3 (April 1. 2014):**

  * BUG FIX: Fixed a bug in the peptide to protein mapping where the final protein was not included.

  * LIBRARY UPDATE: Updated utilities to version 3.26.4.


---


**Changes in PeptideShaker 0.27.2 (March 29. 2014):**

  * FEATURE IMPROVEMENT: Updated the example dataset.
  * FEATURE IMPROVEMENT: The first number in the Spectrum IDs tab border title is now the number of validated PSMs.
  * FEATURE IMPROVEMENT: Updated the getting started slides to include MS-GF+.

  * BUG FIX: Fixed a bug in the protein filters that resulted in all protein filters returning false.
  * BUG FIX: The Spectrum IDs tab is now updated if the validation changes in the Validation tab.
  * BUG FIX: Fixed a bug in the SpectrumIDs tab where the spectrum panel border was not reset when selecting a spectrum without a PSM.
  * BUG FIX: Tried to fix a possible null pointer in the peptide border title.

  * LIBRARY UPDATE: Updated utilities to version 3.25.15.


---


**Changes in PeptideShaker 0.27.1 (March 27. 2014):**

  * BUG FIX: Fixed a bug in the method for getting all non fixed modifications.

  * LIBRARY UPDATE: Updated utilities to version 3.25.14.


---


**Changes in PeptideShaker 0.27.0 (March 26. 2014):**

  * NEW FEATURE: Added support for MS-GF+.
  * NEW FEATURE: Added PSM quality filters.

  * FEATURE IMPROVEMENT: Added an ID software color legend below the Spectrum Identification Results table in the Spectrum IDs tab.
  * FEATURE IMPROVEMENT: Added search engine specific file filters to the New Project dialog.
  * FEATURE IMPROVEMENT: Minor GUI fixes to the protein inference dialogs, also added the number of rows to the table border titles.
  * FEATURE IMPROVEMENT: Improved the display of non confident PTM sites.
  * FEATURE IMPROVEMENT: Improved the display of the protein table when scrolling.
  * FEATURE IMPROVEMENT: Added the protein description in the peptide output.

  * BUG FIX: Fixed a problem with parsing FASTA files containing headers with empty sequences.
  * BUG FIX: Fixed a bug in the settings dialog that closed the dialog if the user canceled the save as dialog.

  * LIBRARY UPDATE: Updated utilities to version 3.25.12.


---


**Changes in PeptideShaker 0.26.2  (March 6. 2014):**

  * BUG FIX: Fixed a icon image bug that occurred if one used the New Project option in the main frame.


---


**Changes in PeptideShaker 0.26.1  (March 6. 2014):**

  * FEATURE IMPROVEMENT: Added a high resolution option for the spectrum annotation.
  * FEATURE IMPROVEMENT: Added more advanced scrolling support for the tables.

  * BUG FIX: Fixed a bug in the parsing of FASTA files with unknown headers.
  * BUG FIX: Fixed errors with the TMT 10-plex reporter ion masses.

  * LIBRARY UPDATE: Updated utilities to version 3.23.18.


---


**Changes in PeptideShaker 0.26.0  (March 3. 2014):**

  * FEATURE IMPROVEMENT: The loading of search results is now a lot quicker!
  * FEATURE IMPROVEMENT: Reformatted the Spectrum IDs tab.
  * FEATURE IMPROVEMENT: Mass errors are no longer in absolute values.
  * FEATURE IMPROVEMENT: Updated the TMT modifications to support the new TMT 10-plex.
  * FEATURE IMPROVEMENT: Tried to improve the x-axis for the MS2 Quant QC plot.
  * FEATURE IMPROVEMENT: Improved the robustness of the FDR estimation.
  * FEATURE IMPROVEMENT: Replaced PSI-MOD modification mappings with Unimod.
  * FEATURE IMPROVEMENT: Added table column header tooltips for the MatchValidationDialog.

  * BUG FIX: Corrected a bug in the import of the quick pyro and acetyl options of X!Tandem.
  * BUG FIX: Separated the PTM mass tolerance from the fragment mass tolerance in the PTM mapping of Mascot and X!Tandem, that could result in protein inference issues.
  * BUG FIX: Fixed a bug in the psm validation code that resulted in the loading being canceled if an mgf file contained no validated psms.
  * BUG FIX: Fixed a bug in the progress bar when loading spectrum files when loading a project.
  * BUG FIX: Fixed a bug where using the Save option in the Save Dialog resulted in a null pointer if the project was not previously saved.
  * BUG FIX: Fixed some issues with the hiding of the jsparklines.
  * BUG FIX: Corrected a bug in the custom PSM and peptide exports.
  * BUG FIX: Unified the separators in peptide exports.
  * BUG FIX: Improved the handling of protein tree creation crashes.
  * BUG FIX: Fixed a bug where the orange waiting icon was not used in the New Project dialog when updating the species.
  * BUG FIX: If the protein mapping is not present when calling the isDecoy method of a peptide, the peptide will be mapped.
  * BUG FIX: Fixed a minor GUI bugs in the Peptide tab in the Export dialog.
  * BUG FIX: Corrected minor bugs in the exports.
  * BUG FIX: Fixed a bug in the table column header tooltips for the ProteinInferencePeptideLevelDialog.
  * BUG FIX: Fixed is a problem with unmapped search engine advocates.

  * LIBRARY UPDATE: Updated utilities to version 3.23.13.


---


**Changes in PeptideShaker 0.25.2  (February 10. 2014):**

  * BUG FIX: Fixed a bug in the report command line export, where two options with the same name (-out) could get confused.


---


**Changes in PeptideShaker 0.25.1  (February 8. 2014):**

  * BUG FIX: Fixed a memory issue occurring during the protein database loading for Mac and Linux.
  * BUG FIX: Added a test for no enzyme set, as old search parameter files could result in a null pointer exception.
  * BUG FIX: Tried to get rid of one of the reasons for the "please contact the developers" message when moving around in the Overview tab.

  * LIBRARY UPDATE: Updated utilities to version 3.21.30.


---


**Changes in PeptideShaker 0.25.0  (February 4. 2014):**

  * NEW FEATURE: The versions of the search engines are now stored in the project details and showed in the project report.
  * NEW FEATURE: The PeptideShaker report is now saved together with the cps file.
  * NEW FEATURE: Added the possibility to create identification parameters files from the command line.
  * NEW FEATURE: Added a simple swath export.
  * NEW FEATURE: New auto updater feature for PeptideShaker and SearchGUI.
  * NEW FEATURE: Added an "Open Example Dataset" option to the file menu.

  * FEATURE IMPROVEMENT: Improved the memory handling.
  * FEATURE IMPROVEMENT: The number of confident/doubtful proteins/peptides/PSMs can now be changed by the user.

  * BUG FIX: Fixed a bug in the SpectrumFactory where one ended up with partial index files if the process was canceled by the user.
  * BUG FIX: Fixed a bug in the sorting of the #Peptides and #Spectra columns, causing the sorting to be fairly random.
  * BUG FIX: Corrected a bug resulting in a null pointer when the A-score was used and only multiply modified peptides are found at a given charge.
  * BUG FIX: Corrected a bug where modifications were disappearing from the GUI.
  * BUG FIX: Fixed a backwards compatibility issues with the precursor accuracy in the search parameters.
  * BUG FIX: Fixed a bug in the peptide keys used in the spectrum and Progenesis exports.

  * LIBRARY UPDATE: Updated xtandem parser to version 1.7.7.
  * LIBRARY UPDATE: Updated omssa parser to version 1.6.3.
  * LIBRARY UPDATE: Updated mascotdatfile to version 3.4.19.
  * LIBRARY UPDATE: Updated utilities to version 3.21.26.
  * LIBRARY UPDATE: Updated jsparklines to version 0.6.5.

---

**Changes in PeptideShaker 0.24.3  (January 10. 2014):**

  * BUG FIX: Corrected the peptide key used in the spectrum and Progenesis exports.

Download Count: 92

---

**Changes in PeptideShaker 0.24.2  (January 10. 2014):**

  * LIBRARY UPDATE: Updated ols-dialog to version 3.4.2, fixing a bug in the View Term Hierarchy Graph.

Download Count: 2


---

**Changes in PeptideShaker 0.24.1  (January 9. 2014):**

  * BUG FIX: Fixed an issue with the fragment ion annotation in the PRIDE export.

  * LIBRARY UPDATE: Updated utilities to version 3.20.3.

Download Count: 12

---

**Changes in PeptideShaker 0.24.0  (January 8. 2014):**

  * NEW FEATURE: Validated protein, peptide and PSM matches are now also filtered for quality and marked if doubtful, e.g., less than 2 peptides detected for a given protein.
  * NEW FEATURE: The user can now click the id and spectrum files text field in the New Project dialog to see and edit the list of selected files.

  * FEATURE IMPROVEMENT: The peptide and spectrum count columns plus the QC plots now include the new "doubtful" category.
  * FEATURE IMPROVEMENT: PeptideShaker now corrects for input where the same ptm is found multiple times.
  * FEATURE IMPROVEMENT: PeptideShaker projects zipped on Windows can now also be opened on Mac and Linux.
  * FEATURE IMPROVEMENT: Improved the way export to zip is performed if the project is not already saved.

  * BUG FIX: Fixed an issue where the height if the spectrum sub plots ended up as too small if hidden and then re-displayed.
  * BUG FIX: Corrected bugs in the sparklines for the protein table in the GO and Fractions tabs.
  * BUG FIX: Fixed bugs in the hide/show of the Score/Confidence column.
  * BUG FIX: Fixed a bug in the jump to feature where strings that could not be converted to amino acid characters broke the search.
  * BUG FIX: Corrected a typo impairing the calculation of NSAF indexes.

  * LIBRARY UPDATE: Updated jsparklines to version 0.6.4.
  * LIBRARY UPDATE: Updated xtandem parser to version 1.7.5.
  * LIBRARY UPDATE: Updated utilities to version 3.20.2.

Download Count: 12

---

**Changes in PeptideShaker 0.23.0  (December 9. 2013):**

  * NEW FEATURE: Improved protein inference handling, i.e., peptide to protein mapping.
  * NEW FEATURE: Added a first version of a basic graph database export for Cytoscape, Gephi and Neo4j to the follow up export dialog.
  * NEW FEATURE: A low memory and Java version check is now performed when starting the tool and a warning is shown in the waiting dialog.
  * NEW FEATURE: The species can now be provided as input to SearchGUI (for use when reprocessing in PRIDE).

  * FEATURE IMPROVEMENT: Extended the list of PRIDE project available in the reshaking.
  * FEATURE IMPROVEMENT: Improved the Search Settings dialog, which is now identical to the one in SearchGUI and also displays the fixed PTMs.
  * FEATURE IMPROVEMENT: Reshake now supports a default enzyme mapping, and user selection of enzyme if the mapping fails. Also now supports multiple enzymes.
  * FEATURE IMPROVEMENT: Added MD Score localization to the to the export.
  * FEATURE IMPROVEMENT: Better support for semi-specific enzymes.
  * FEATURE IMPROVEMENT: Updated the tips of the day.
  * FEATURE IMPROVEMENT: Updated the getting started slides.
  * FEATURE IMPROVEMENT: Added some options to the fragment ion export.
  * FEATURE IMPROVEMENT: The intensity, mass error and bubble plots now include all currently selected ions, and not only the default a-c and x-z ions.
  * FEATURE IMPROVEMENT: Mgf validation is now performed in SearchGUI, and the information is saved so that is does not have to be done more than once.
  * FEATURE IMPROVEMENT: Added the possibility to score PTMs with phosphoRS.
  * FEATURE IMPROVEMENT: Added the number of missed cleavages in the peptide and PSM exports.
  * FEATURE IMPROVEMENT: If the id file parsers run out of memory this is now picked up, the search canceled and a message shown to the user.
  * FEATURE IMPROVEMENT: Slightly reduced the height needed for the content in the Annotation tab.
  * FEATURE IMPROVEMENT: Got rid of the derby.log file.
  * FEATURE IMPROVEMENT: Improved the default name of the search results folder for reshake results.
  * FEATURE IMPROVEMENT: Implemented memory usage reduction during PSM processing.
  * FEATURE IMPROVEMENT: Closing the Reshake dialog before starting the reshaking now takes the user back to the Welcome dialog.
  * FEATURE IMPROVEMENT: Sequence coverage is now estimated/displayed using indistinguishable amino acids.
  * FEATURE IMPROVEMENT: Replaced the FTP file downloaded with a version that is faster on the EBI wireless.
  * FEATURE IMPROVEMENT: Added a check if the PRIDE XML file exists locally before downloading the file from the FTP server.

  * BUG FIX: Fixed various minor bugs in the PRIDE export dialogs.
  * BUG FIX: Fixed a bug in the mass error type tooltip in the PSM table.
  * BUG FIX: Enzymes without a value (i.e., an enzyme name) in the PRIDE XML file no longer breaks the reshake feature.
  * BUG FIX: Semicolons are no longer supported in project and sample name (as these result in issues with Derby).
  * BUG FIX: Fixed a bug where the FDR corrected p-values of the hypergeometric test in the GO tab could become bigger than 1.
  * BUG FIX: Fixed a bug in the protein QC plots where the numbers didn't add up.
  * BUG FIX: Corrected bugs in the Follow Up command line for the accession and inclusion list export options.
  * BUG FIX: Fixed various bugs in the command line reports and follow up analysis exports.
  * BUG FIX: Fixed a bug where empty decoy tags were not handled correctly.
  * BUG FIX: Fixed an issue for the peptide export where shared peptides did not list all parent proteins.
  * BUG FIX: Fixed a bug where TMT reporter ions were not displayed again if hidden as these had no variable modifications with reporter ions, unlike iTRAQ.
  * BUG FIX: Fixed a bug with changing the reporter and neutral ions in the PtmDialog.
  * BUG FIX: Fixed various minor GUI issues in the Fractions tab.
  * BUG FIX: Fixed a bug where the project could not be saved after loading results in the Fractions tab.
  * BUG FIX: Fixed a bug with the handling of corrupt PRIDE PTM mapping files.

  * LIBRARY UPDATE: Removed sqlite as a transitive dependency.
  * LIBRARY UPDATE: Removed twitter4j-core  as a dependency.
  * LIBRARY UPDATE: Updated ols-dialog to version 3.4.1.
  * LIBRARY UPDATE: Updated omssa parser to version 1.6.1.
  * LIBRARY UPDATE: Updated xtandem parser to version 1.7.3.
  * LIBRARY UPDATE: Updated utilities to version 3.19.5.

Download Count: 103

---

**Changes in PeptideShaker 0.22.6 (August 10. 2013):**

  * FEATURE IMPROVEMENT: Added an edit modifications option to the SearchPreferencesDialog.
  * FEATURE IMPROVEMENT: Removed spectrum file renaming for Mascot Distiller files.

  * BUG FIX: Fixed a bug in the handling of missing mgf files.

  * LIBRARY UPDATE: Updated omssa parser to version 1.5.13.
  * LIBRARY UPDATE: Updated mascotdatfile parser to version 3.4.15.
  * LIBRARY UPDATE: Updated utilities to version 3.14.19.

Download Count: 331

---

**Changes in PeptideShaker 0.22.5 (July 14. 2013):**

  * FEATURE IMPROVEMENT: Improved the progress display in the Progenesis export.

  * BUG FIX: Fixed an issue with the sorting order indicator icons.
  * BUG FIX: Made the tool Java 6 compatible again.

  * LIBRARY UPDATE: Updated omssa parser to version 1.5.12.
  * LIBRARY UPDATE: Updated xtandem parser to version 1.6.2.
  * LIBRARY UPDATE: Updated mascotdatfile parser to version 3.4.14.
  * LIBRARY UPDATE: Updated utilities to version 3.14.16.

Download Count: 115

---

**Changes in PeptideShaker 0.22.4 (July 4. 2013):**

  * NEW FEATURE: Extended the species support. (beta)
  * NEW FEATURE: New database details dialog.

  * FEATURE IMPROVEMENT: Added fragment ion annotation in the exports as well as modified sequence.
  * FEATURE IMPROVEMENT: Renamed the Validation plot from Benefit/Cost to Cost/Benefit.

  * BUG FIX: Fixed a bug in the PSM table where the row selection was not cleared before the table was updated.
  * BUG FIX: Fixed a bug where the id filters were absent when creating a new project.

  * LIBRARY UPDATE: Updated utilities to version 3.14.7.

Download Count: 71

---

**Changes in PeptideShaker 0.22.3 (June 27. 2013):**

  * FEATURE IMPROVEMENT: Added gene name and chromosome number to the default protein report.
  * FEATURE IMPROVEMENT: Gene name and chromosome is no longer exported for decoy sequences.
  * FEATURE IMPROVEMENT: Improved the way the progress bar is canceled when the Progenesis export is done.
  * FEATURE IMPROVEMENT: The Validation settings not applied warning is now only shown when leaving the Validation tab.

  * BUG FIX: Fixed a bug in the Progenesis export where a method was called recursively without stop.
  * BUG FIX: Fixed bugs in the custom exports for gene name and chromosome where column separators where missing.
  * BUG FIX: The simple protein description now include the "-reverse" tag for decoy sequences.
  * BUG FIX: Tried to fix the reason for the table model number conversion exception being thrown.

  * LIBRARY UPDATE: Updated utilities to version 3.13.56.

Download Count: 49

---

**Changes in PeptideShaker 0.22.2 (June 25. 2013):**

  * NEW FEATURE: The tool now checks if 64 bit Java is used the first time PeptideShaker is started.

  * FEATURE IMPROVEMENT: Added gene details in the default custom exports.

  * BUG FIX: Corrected a bug in the Progenesis export.
  * BUG FIX: Fixed a bug where the coverage panel had gone missing.
  * BUG FIX: Fixed a bug in the gene name comparison as part of the protein inference grouping where gene names of length 1-2 resulted in issues.
  * BUG FIX: Corrected bugs in the custom exports.

  * LIBRARY UPDATE: Updated utilities to version 3.13.55.

Download Count: 18


---


**Changes in PeptideShaker 0.22.1 (June 20. 2013):**

  * FEATURE IMPROVEMENT: Cleaned up the use of the New Project dialog when called from the Welcome dialog.

  * BUG FIX: Fixed a bug where missing mgf files that had to be relocated where not indexed.
  * BUG FIX: Fixed a bug in the code for locating a FASTA file if it was not in the location given in the cps file.
  * BUG FIX: Fixed a bug that made is impossible to set the species if no species was selected when loading the project.
  * BUG FIX: Handled a possible null pointer in the Overview tab.

Download Count: 37


---


**Changes in PeptideShaker 0.22.0 (June 19. 2013):**

  * NEW FEATURE: New an improved example dataset.
  * NEW FEATURE: Cleaned up and improved the protein inference groupings, relying more on gene names when available.
  * NEW FEATURE: A simplified shorter protein description is now used for UniProt headers.

  * FEATURE IMPROVEMENT: Sped up the batch db interaction, making it possible to save projects a lot faster when having limited memory.
  * FEATURE IMPROVEMENT: Updated the Ensembl human mappings to Ensembl 71.
  * FEATURE IMPROVEMENT: Added better handling of PeptideShaker errors when PeptideShaker is started from SearchGUI.
  * FEATURE IMPROVEMENT: Changed the PRIDE export to use a CV term instead of a user term for the search engine inferred charge state.
  * FEATURE IMPROVEMENT: The indexes in the legend in the bubble plot now start on 1 instead of 0, corresponding to the row numbers.
  * FEATURE IMPROVEMENT: HTML in spectrum titles are now escaped when exporting to PRIDE XML.
  * FEATURE IMPROVEMENT: The a-score is no longer added as a user parameter to the PRIDE XML export if there are no PTMs in the peptide.
  * FEATURE IMPROVEMENT: Added better error handling in the PRIDE Reshake dialog.
  * FEATURE IMPROVEMENT: The title in the main frame is now reset when loading a new project, and not after the project is done loading as before.
  * FEATURE IMPROVEMENT: PeptideShaker now stays in the task bar when the New Project dialog is displayed.
  * FEATURE IMPROVEMENT: Improved the handling of equally scoring peptides.
  * FEATURE IMPROVEMENT: Included the null confidence proteins in the protein inference process.
  * FEATURE IMPROVEMENT: Added gene name and chromosome to the old school text export options.
  * FEATURE IMPROVEMENT: Re-implemented the follow up exports making it ready for command line support.
  * FEATURE IMPROVEMENT: If there are multiple identical search parameter file options when loading search result files, the first will now be automatically selected.

  * BUG FIX: Fixed a bug in the DatabaseHelpDialog add decoys option where the SearchGUI icon was used even though it was not available, thus crashing the tool.
  * BUG FIX: Fixed a bug in the PRIDE export where the terminal modifications were incorrectly annotated.
  * BUG FIX: Fixed a bug in the PRIDE PSI-MOD mapping for oxidations.
  * BUG FIX: Fixed a bug in the spectrum and plots export to figure feature that included a see through area between the spectrum and the plots.
  * BUG FIX: Fixed a bug with the default values for the min and max peptide length in the IdFilter that resulted in issues for the possible protein coverage, the spectrum counting and the peptide to protein mapping.
  * BUG FIX: The gene ontology is now saved when chosen in the New Project dialog.
  * BUG FIX: Fixed a minor issue in the FileImporter where general exceptions was caught before the specific out of memory error.
  * BUG FIX: Tried to fix a threading issue in the protein fractions tab.
  * BUG FIX: The project is now labeled as unsaved after applying new validation settings.
  * BUG FIX: Inclusion list export now works again.
  * BUG FIX: Fixed a bug in the way column delimiters including backslashes were supported, resulting in \t in the export instead of tabs

  * LIBRARY UPDATE: Added commons-lang3 has a dependency.
  * LIBRARY UPDATE: Updated utilities to version 3.13.54.

Download Count: 8


---


**Changes in PeptideShaker 0.21.0 (June 1. 2013):**

  * NEW FEATURE: Species is now selected when creating a project.
  * NEW FEATURE: Added a species tag to the command line for setting the species.
  * NEW FEATURE: The protein evidence level is now used when selecting the "main match" in a protein group. (UniProt databases only.)

  * FEATURE IMPROVEMENT: The species selection is now stored in the project.
  * FEATURE IMPROVEMENT: Removed the species selection section in the GO tab.
  * FEATURE IMPROVEMENT: Updated the Ensembl species list.
  * FEATURE IMPROVEMENT: Added a check for duplicate spectrum titles when selecting mgf files.
  * FEATURE IMPROVEMENT: Replace protein evidence level number with text in the protein inference dialogs.
  * FEATURE IMPROVEMENT: Added chromosome mapping to the protein inference dialogs.
  * FEATURE IMPROVEMENT: The gene name is now used when comparing the proteins in a protein group, if different or missing the description is still used. (UniProt databases only.)
  * FEATURE IMPROVEMENT: Added a more visible "add new report type" option to the custom export dialog.

  * BUG FIX: Fixed a bug with the hiding and reshowing of the spectrum panel in the Overview tab.
  * BUG FIX: Fixed a bug with updating in the gene and GO mappings where a file could not be deleted.
  * BUG FIX: Fixed some resizing issues in the PRIDE annotation dialogs.
  * BUG FIX: Improved the handling of errors occurring when establishing a database connection when importing a PeptideShaker project.
  * BUG FIX: Fixed the background color for the ProjectDetailsDialog.
  * BUG FIX: Fixed a bug in the peptide selection when changing the protein selection where the selected row was not made visible.
  * BUG FIX: Tried to fix issues related to maintaining the sorting in the tables.
  * BUG FIX: Fixed a problem that could occur with the size of the Venn diagrams in the Spectrum IDs tab.
  * BUG FIX: Fixed a bug in the setting of the OMSSA indexes for older search parameter files.
  * BUG FIX: Fixed a bug with the icon not turning gray again after selecting a peptide in the Overview tab.

  * LIBRARY UPDATE: Updated mascot dat file to version 3.4.11.
  * LIBRARY UPDATE: Updated utilities to version 3.13.30.

Download Count: 68


---


**Changes in PeptideShaker 0.20.1 (May 13. 2013):**

  * BUG FIX: Fixed a bug where white space was not allowed in the installation path.
  * LIBRARY UPDATE: Updated utilities to version 3.13.18.

Download Count: 101


---


**Changes in PeptideShaker 0.20.0 (May 11. 2013):**

  * NEW FEATURE: New self updating tables with better support for bigger datasets.
  * NEW FEATURE: Added a chromosome mapping column to the protein table.

  * FEATURE IMPROVEMENT: Improved the peptide inference method for miscleaved peptides.
  * FEATURE IMPROVEMENT: Sped up the PTM inference processing.
  * FEATURE IMPROVEMENT: Improved the way extracted PRIDE search parameters are displayed.
  * FEATURE IMPROVEMENT: The waiting dialog now has "close when complete" turned on as the default.
  * FEATURE IMPROVEMENT: If a bubble plot displays more that 20 spectra the plot legend is now hidden as to not cover too much of the plotting area.
  * FEATURE IMPROVEMENT: Re-added the PRIDE and project zip exports to the Export menu.
  * FEATURE IMPROVEMENT: Improve the way selections are handled across the tabs.

  * BUG FIX: Fixed a problem with starting the tool on the latest Java release.
  * BUG FIX: Fixed a bug where the tooltips and popup menus in the sequence coverage plot included all peptides even when a subset (enzymatic/non-enzymatic) was selected.
  * BUG FIX: Added a check that the matches folder exists before deleting or listing it's files.
  * BUG FIX: Fixed an issue with locating SearchGUI via the PrideSearchParametersDialog if the provided SearchGUI folder could not be found.
  * BUG FIX: Removed a GUI references in the FileImporter class, improving the command line support.

  * LIBRARY UPDATE: Updated jsparklines to version 0.6.0.
  * LIBRARY UPDATE: Updated utilities to version 3.13.16.

Download Count: 8


---


**Changes in PeptideShaker 0.19.3 (April 2. 2013):**

  * FEATURE IMPROVEMENT: Further developed the Progenesis export with more options.
  * LIBRARY UPDATE: Updated xtandem-parser to version 1.5.14, fixing a problem with the parsing of spectrum titles with retention time in them.
  * LIBRARY UPDATE: Updated utilities to version 3.11.29.

Download Count: 172


---


**Changes in PeptideShaker 0.19.2 (March 25. 2013):**

  * BUG FIX: Fixed a bug that made it impossible to change the memory settings.
  * BUG FIX: Fixed a typo in the PRIDE Reshake dialog, PumMed > PubMed.
  * LIBRARY UPDATE: Updated utilities to version 3.11.27.

Download Count: 33


---


**Changes in PeptideShaker 0.19.1 (March 24. 2013):**

  * NEW FEATURE: PRIDE Reshake feature added for re-analyzing data in PRIDE. (beta)
  * NEW FEATURE: Created PRIDE XML files are now schema validated with user feedback if the validation fails.
  * NEW FEATURE: Added a new Save & Export dialog.
  * NEW FEATURE: Added simple data filters for the Plotting Dialog.
  * NEW FEATURE: Added a new total peptide count per fraction plot to the fraction tab.
  * NEW FEATURE: Added an option for exporting the extended spectrum panel (the spectrum and the corresponding plots) in the Overview tab as a single figure.
  * NEW FEATURE: A new custom report export option (beta).

  * FEATURE IMPROVEMENT: Search engines assumptions are now compared without accounting for PTM localization.
  * FEATURE IMPROVEMENT: The observed molecular weights are now recalculated if the user hides proteins via the FiltersDialog.
  * FEATURE IMPROVEMENT: Improved backward compatibility for older projects.
  * FEATURE IMPROVEMENT: Updated the Getting Started slides.
  * FEATURE IMPROVEMENT: Added a warning in case too many hits are kicked out by the filter.
  * FEATURE IMPROVEMENT: Cleaned up the error given if a protein cannot be found in the FASTA file.
  * FEATURE IMPROVEMENT: Added complete protein group (in alphabetical order) as an export option.
  * FEATURE IMPROVEMENT: The parsing of mgf (and mzml) files now support both upper and lower case file extensions.
  * FEATURE IMPROVEMENT: Added retention time to the PRIDE export.

  * BUG FIX: Removed some incorrect tooltips in the new project dialog.
  * BUG FIX: Fixed an inconsistency in the protein inference class descriptions used.
  * BUG FIX: Fixed a bug in the remapping of PTMs.
  * BUG FIX: Fixed a minor bug in the project export option where extra tabs were added at the end of each line for the PSMs.
  * BUG FIX: Fixed issues detected by FindBugs.

  * LIBRARY UPDATE: Updated MascotDatFile to version 3.4.10.
  * LIBRARY UPDATE: Updated pride-jaxb to version 1.0.9.
  * LIBRARY UPDATE: Updated utilities to version 3.11.25.

Download Count: 13


---


**Changes in PeptideShaker 0.19.0 (February 6. 2013):**

  * NEW FEATURE: Added a new ID Rate column, and added a separate row for the total PeptideShaker results in the Spectrum IDs tab.
  * NEW FEATURE: Made it possible to show/hide the fixed modifications in most tabs.
  * NEW FEATURE: Added a new Plotting dialog, opened by right clicking in most tables.
  * NEW FEATURE: Reimplemented the PeptideShaker command line support from scratch. (http://code.google.com/p/peptide-shaker/wiki/PeptideShakerCLI)
  * NEW FEATURE: Added an open example dataset option to the WelcomeDialog.
  * NEW FEATURE: Added a settings pop up menu to the WelcomeDialog.
  * NEW FEATURE: Implemented False LocationRate (FLR) for modifications.
  * NEW FEATURE: Modification patterns defined as part of a SearchGUI search are now supported.
  * NEW FEATURE: Added precursor intensity to the spectrum table in the Spectrum IDs tab.
  * NEW FEATURE: Added neXtProt and PDB links to the Annotation tab.
  * NEW FEATURE: Added an option for exporting the maximal protein set (the accession numbers) to a file.
  * NEW FEATURE: The precursor mass error now takes into account wrong isotope selection.

  * FEATURE IMPROVEMENT: Simplified the way the user selected parameters are applied when moving away from the Validation tab.
  * FEATURE IMPROVEMENT: Changed the precursor intensity shown in the Fractions tab from average to sum.
  * FEATURE IMPROVEMENT: Added lower and upper ranges for the fraction molecular weights in the FractionDetailsDialog.
  * FEATURE IMPROVEMENT: Made it possible to cancel the progress bars in the Validation tab.
  * FEATURE IMPROVEMENT: Improved the search engine PTM recognition.
  * FEATURE IMPROVEMENT: Improved the default PTM selection for X!Tandem.
  * FEATURE IMPROVEMENT: Removed the use of UniProt to get the basic protein information. Now taken from the FASTA files instead.
  * FEATURE IMPROVEMENT: Gene name and protein evidence level are now shown in the protein inference dialogs for UniProt data.
  * FEATURE IMPROVEMENT: Improved the progress dialog in the Spectrum IDs tab.
  * FEATURE IMPROVEMENT: PeptideShaker can now be run from paths containing special characters.
  * FEATURE IMPROVEMENT: Mgf files with spectrum titles encoded in unicode are now supported.
  * FEATURE IMPROVEMENT: The modal progress dialog is now closed if an error occurs during the saving of a project.
  * FEATURE IMPROVEMENT: Added protein inference type, star property, tagged peptide sequence, is enzymatic, the surrounding peptide information for shared peptides and fixed modification details to the peptide exports.
  * FEATURE IMPROVEMENT: Added total number of peptides and spectra, overall sequence coverage, has non-enzymatic peptides, MW and peptide and spectrum spread to the fractions export.
  * FEATURE IMPROVEMENT: The filters in the FindDialog are now previewed in the tables only after the user stops typing. And the previewing of the filters in the FindDialog can now be turned on or off by the user.
  * FEATURE IMPROVEMENT: Improved the tooltips in the molecular weight box plot in the Fractions tab.
  * FEATURE IMPROVEMENT: Sped up the PRIDE export.
  * FEATURE IMPROVEMENT: Generalized the "show tryptic/non tryptic peptides" to "show enzymatic/non enzymatic peptides".
  * FEATURE IMPROVEMENT: Added a check for duplicate entries when loading a FASTA file.

  * BUG FIX: Fixed a bug in the mass of the glutamic acid amino acid.
  * BUG FIX: Fixed a bug where the masses of user defined PTMs in the PRIDE export where set to null if a CV term mapping was added.
  * BUG FIX: Fixed a bug that occurred if the user clicked the SE column for a PSM in the Overview tab before loading the Spectrum IDs tab.
  * BUG FIX: Fixed a bug with multiple fixed modifications on the same peptide, e.g., when using iTRAQ or TMT labeling.
  * BUG FIX: Fixed a bug that made the saving of bigger projects very very slow.
  * BUG FIX: Fixed a bug in the export spectrum as mgf feature that made it impossible to export as mgf.
  * BUG FIX: Fixed a bug in the average precursor intensity calculation for the proteins.
  * BUG FIX: Fixed the progress bars in the Validation and PTM tabs to show actual progress.
  * BUG FIX: Fixed an issues in the Spectrum IDs tab where the number of unassigned spectra was incorrect.
  * BUG FIX: Fixed a bug with the maximum sparkline values in the Fractions tab.
  * BUG FIX: Fixed a bug so that the icon doesn't stay orange when finished exporting/zipping a PeptideShaker project.
  * BUG FIX: Fixed a bug in the possible sequence coverage displayed in the coverage panel, where the first residue and the last non-enzymatic peptide was not included.
  * BUG FIX: Fixed an inconsistency in the sequence coverage output in the exports, as both 0-100 and 0-1 was used for percent values.
  * BUG FIX: Fixed a bug i the restart after changing the memory setting, it crashed if a project was currently open.
  * BUG FIX: Made a minor change to the pom file to handle a recursive issues that can occur when opening the project in NetBeans 7.2.
  * BUG FIX: Fixed a bug resulting in the filters having to be applied twice. Also added the option of deleting filters.
  * BUG FIX: Fixed a bug in the protein export where two columns had gotten mixed up.
  * BUG FIX: Fixed a bug in the New Project dialog where opening the FASTA file didn't display the last selected folder.
  * BUG FIX:  Fixed a bug where the enzyme was reset when manually loading a FASTA file in the New Project dialog.
  * BUG FIX: Fixed a bug where the progress bar was not closed in the New Project dialog if an error occurred when checking the FASTA file.
  * BUG FIX: Fixed a bug with the use of "whole protein" as the enzyme.

  * LIBRARY UPDATE: Removed unitprotjapi as a dependency.
  * LIBRARY UPDATE: Added twitter4j as a dependency.
  * LIBRARY UPDATE: Added mzdata-parser 1.2.1 as a dependency.
  * LIBRARY UPDATE: Updated the default Ensembl human to version 69.
  * LIBRARY UPDATE: Updated jsparklines to version 0.5.44.
  * LIBRARY UPDATE: Updated omssa parser to version 1.5.8.
  * LIBRARY UPDATE: Updated xtandem parser to version 1.5.12.
  * LIBRARY UPDATE: Updated mascot dat file parser to version 3.4.7.
  * LIBRARY UPDATE: Updated utilities to version 3.11.2.

Download Count: 257


---


**Changes in PeptideShaker 0.18.3 (September 15. 2012):**

  * FEATURE IMPROVEMENT: Improved the PRIDE export dialog.
  * FEATURE IMPROVEMENT: It is now possible to add more than one contact in the PRIDE export.
  * FEATURE IMPROVEMENT: The PRIDE settings are now stored in the PeptideShaker Project.
  * FEATURE IMPROVEMENT: Re-enabled the improved (but slower) ptm location code.
  * LIBRARY UPDATE: Updated ols-dialog to version 3.4.0, containing many GUI improvements.
  * LIBRARY UPDATE: Updated utilities to version 3.10.67.

Download Count: 348


---


**Changes in PeptideShaker 0.18.2 (September 12. 2012):**

  * BUG FIX: Had to (temporarily) disabled the new improved PTM location code as could result in null pointers.
  * LIBRARY UPDATE: Updated mascotdatfile to version 3.4.2, such that the Mascot search results can be loaded again.
  * LIBRARY UPDATE: Updated utilities to version 3.8.9, fixing an issues with the EBI proxy settings.

Download Count: 37


---


**Changes in PeptideShaker 0.18.1 (September 11. 2012):**

  * FEATURE IMPROVEMENT: Better support for spectrum titles in OMSSA files with special characters in them, e.g., \ or ".
  * FEATURE IMPROVEMENT: The code now supports Maven 3.
  * LIBRARY UPDATE: Added the OMSSA, X!Tandem and Mascot parsers as dependencies.
  * LIBRARY UPDATE: Updated utilities to version 3.8.8.
  * LIBRARY UPDATE: Updated jmzml to version 1.6.8.

Download Count: 5


---


**Changes in PeptideShaker 0.18.0 (September 7. 2012):**

  * NEW FEATURE: A brand new database based backend.
  * NEW FEATURE: New improved and simplified Fractions tab.
  * NEW FEATURE: Automatic de novo sequencing can now be done using one or two charges for the fragment ions.
  * NEW FEATURE: Spaces are now allowed in protein accession numbers.
  * NEW FEATURE: The report created when loading a project in the waiting dialog is now automatically saved as part of the project details.
  * NEW FEATURE: Automated the delta thresholding.
  * NEW FEATURE: Added support for Mascot Server 2.4.
  * NEW FEATURE: Added a contextual options icon to the coverage tables, making is possible for the users to decide which peptides to show.
  * NEW FEATURE: The FragmentIonTable now supports multiple PSMs in the traditional theoretical m/z values setup as well.

  * FEATURE IMPROVEMENT: Replaced uses of "\n" with System.getProperty("line.separator"), making the export less system dependent.
  * FEATURE IMPROVEMENT: Minor GUI improvement to the Search Parameters dialog.
  * FEATURE IMPROVEMENT: Minor GUI improvement to the New Project dialog.
  * FEATURE IMPROVEMENT: Minor GUI fixes in the BugReport dialog.
  * FEATURE IMPROVEMENT: Added MW to the protein export options.
  * FEATURE IMPROVEMENT: Increased the length of the recent files displayed to 20.
  * FEATURE IMPROVEMENT: Updated human ENSEMBL to version 68.
  * FEATURE IMPROVEMENT: Better support for spectrum titles with "\\" in them.
  * FEATURE IMPROVEMENT: Changed the table export in the ptm tab so that it retrieves the same information as the overview table.
  * FEATURE IMPROVEMENT: Improved and extended the PRIDE Export, which now also includes PTM scores, spectrum file names and titles.
  * FEATURE IMPROVEMENT: A warning will now be displayed if the user tries to start the tool from within a zip file.
  * FEATURE IMPROVEMENT: GUI updates to make the tool look better on Java 7.
  * FEATURE IMPROVEMENT: Added the maximal coverage in the protein export.

  * BUG FIX: Fixed a bug that occurred if the user typed in the name of a file to load and the file was not found.
  * BUG FIX: Fixed a bug in the SearchPreferencesDialog where the the precursor accuracy was set incorrectly when loading a SearchGUI properties file.
  * BUG FIX: Fixed a bug in the BugReport dialog where it was impossible to export/save the log.
  * BUG FIX: Fixed a bug where the width of the accession columns were not set correctly.
  * BUG FIX: Fixed a couple of calls to convertRowIndexToModel that could be called on an incorrect row.
  * BUG FIX: Fixed a bug in the last selected folder feature that defaulted to the user home folder if the file did not have the correct file name (e.g., .txt).
  * BUG FIX: Fixed an issue in the ProgressDialog that resulted in threading issues and deadlock on Java 7.
  * BUG FIX: Fixed a bug in the spectrum annotation where the precursor charge interfered with the fragment ion charge.
  * BUG FIX: Fixed a null pointer that could occur if trying to close an empty/canceled project.
  * BUG FIX: Fixed a bug where the final y-ion was not annotated in the spectrum panel.
  * BUG FIX: Fixed the "Modification not found" error that occurred if opening two projects in a row without closing the tool.
  * BUG FIX: Fixed a bug where the list of spectrum files were not reset when opening a second project.
  * BUG FIX: Fixed a bug in the 3D tab where an error could occur if the user moved too fast in the pdb chains table.
  * BUG FIX: Fixed a bug in the ProteinInferenceDialog that could result in a null pointer as the wrong map was used.
  * BUG FIX: Made it possible to edit the user defined PTMs.
  * BUG FIX: Fixed various issues related to the canceling of progress dialogs.
  * BUG FIX: Fixed a bug in the FindDialog that resulted in protein filters that only filtered on protein confidence were considered as empty filters.
  * BUG FIX: Fixed a bug in the PRIDE export where it was impossible to select "Other" as the species and select your own CV term instead.

  * LIBRARY UPDATE: Updated uniprotapi to version 2012.06.
  * LIBRARY UPDATE: Updated jsparklines to version 0.5.40.
  * LIBRARY UPDATE: Updated utilities to version 3.8.6.

Download Count: 14


---


**Changes in PeptideShaker 0.17.3 (June 7. 2012):**

  * NEW FEATURE: Added automatic de novo sequencing.

  * FEATURE IMPROVEMENT: Re-enabled row sorting in the spectrum table in the Spectrum IDs tab.
  * FEATURE IMPROVEMENT: Sorting by clicking the table headers now results in the cursor changing into a waiting cursor and the PeptideShaker icon turning orange.
  * FEATURE IMPROVEMENT: The size of the accession column in the Fractions tab is now set to the same width as the other tabs.
  * FEATURE IMPROVEMENT: Updated the default human GO mappings to Ensembl version 67.

  * BUG FIX: Fixed a bug where the row selection in the Overview tab was not reset correctly after closing the SearchParameters dialog.
  * BUG FIX: Fixed some bugs with the contextual export options for the spectrum panel in the PTM tab.
  * BUG FIX: Fixed a bug in the GO tab that could result in issues if switching between rows in the GO table too fast.

Download Count: 290


---


**Changes in PeptideShaker 0.17.2 (June 4. 2012):**

  * NEW FEATURE: The amino acids Selenocysteine and Pyrrolysine are now supported.

  * FEATURE IMPROVEMENT: Improved the look and feel of the manual de novo sequencing.
  * FEATURE IMPROVEMENT: The Search Parameters dialog is now resizable.
  * FEATURE IMPROVEMENT: Missing GO conf files during startup no longer crash the tool.

  * BUG FIX: Fixed a bug in the wrapper where the upper memory limit was not automatically set when using Java 1.7.

  * LIBRARY UPDATE: Updated utilities to version 3.4.23.

Download Count: 18


---


**Changes in PeptideShaker 0.17.1 (May 30. 2012):**

  * NEW FEATURE: Added an initial Command Line Interface (CLI) functionality. (see [wiki page](http://code.google.com/p/peptide-shaker/wiki/PeptideShakerCLI) for details)

  * FEATURE IMPROVEMENT: Allowed the user to tune the default FDR and disable A-score calculation.
  * FEATURE IMPROVEMENT: Improved the spectra recalibration method.

  * BUG FIX: Corrected bugs in the stats panel where thresholds were not remembered/saved.
  * BUG FIX: Fixed a bug where the BugReport could not locate the log file.
  * BUG FIX: Fixed a bug impairing the modification of the PTM list from the new dialog.

  * LIBRARY UPDATE: Updated utilities to version 3.4.22.

Download Count: 20


---


**Changes in PeptideShaker 0.17.0 (May 10. 2012):**

  * NEW FEATURE: Added a Protein Fractions tab.
  * NEW FEATURE: Added method for spectra recalibration.

  * FEATURE IMPROVEMENT: Simplified and sped up the setting of the width for the Accession columns.
  * FEATURE IMPROVEMENT: Spectra with out spectrum titles are now supported as input.
  * FEATURE IMPROVEMENT: Help files extended.

  * BUG FIX: Corrected a bug in mgf export output.
  * BUG FIX: Fixed a GUI resizing issue in the SearchPreferencesDialog.

  * LIBRARY UPDATE: Updated utilities to version 3.4.19.

Download Count: 50


---


**Changes in PeptideShaker 0.16.3 (April 29. 2012):**

  * NEW FEATURE: It is now possible to start SearchGUI directly from the Welcome dialog or from the File menu. (Requires SearchGUI v1.8.3 or newer.)
  * NEW FEATURE: Added a Getting Started tutorial to the Welcome Dialog.
  * NEW FEATURE: Added a gradient color coding panel below the A-score and Delta-score tables in the PTM tab displaying the PTM score certainty.

  * FEATURE IMPROVEMENT: Updated all the Welcome Dialog icons.
  * FEATURE IMPROVEMENT: Made it possible to close progress dialogs that track processes that previously could not be canceled. A warning is now instead showed and the user can decide if he/she still wants to cancel the process.
  * FEATURE IMPROVEMENT: Fixed the issue with the UniProt Java API needing its own proxy settings file.
  * FEATURE IMPROVEMENT: Updated the help files.
  * FEATURE IMPROVEMENT: Added protein description to the peptide, PSM and search engine feature export options.
  * FEATURE IMPROVEMENT: Improved the GUI of the Export Features dialog.
  * FEATURE IMPROVEMENT: Simplified the folder structure in the zip file.

  * BUG FIX: Fixed a bug in the selection of PSMs in the PTM tab, and for removing expected PTMs in the SearchPreferencesDialog.
  * BUG FIX: Fixed a bug that removed the dialog title for the Waiting Dialog.

  * LIBRARY UPDATE: Updated utilities to version 3.4.12.

Download Count: 30


---


**Changes in PeptideShaker 0.16.2 (April 18. 2012):**

  * BUG FIX: Fixed an issue with spaces in the splash screen graphics path on Windows.

Download Count: 57


---


**Changes in PeptideShaker 0.16.1 (April 18. 2012):**

  * NEW FEATURE: Added a PeptideShaker splash screen.
  * FEATURE IMPROVEMENT: Updated the Welcome dialog.
  * FEATURE IMPROVEMENT: Cleaned up the folder structure in the zip file.
  * BUG FIX: Fixed a bug in the method for setting the path for the icon and target in the desktop shortcut that occurred when running PeptideShaker from network drives.

Download Count: 6


---


**Changes in PeptideShaker 0.16.0 (April 16. 2012):**

  * NEW FEATURE: On Windows (on supported architectures) the user is now asked if a desktop shortcut should be added the first time he/she starts the tool.
  * NEW FEATURE: Added Request Validated to the Export Features dialog for the Search Engine export.
  * NEW FEATURE: The users can now change the spectrum annotation colors, plus the color and width of the peaks.
  * NEW FEATURE: Neutral losses and reporter ions are now ptm dependent and their selection is automated.
  * NEW FEATURE: Made it possible to add/edit PSI-MOD terms, neutral losses and reporter ions for the PTMs.
  * NEW FEATURE: Added a new tag to the search engine agreement columns. Orange is now used to indicate that one of the search engines failed to identify a spectrum that was identified by the other search engines used.
  * NEW FEATURE: Added a README file.
  * NEW FEATURE: The proteins for a given GO terms is now listed in a separate table in the GO tab.

  * FEATURE IMPROVEMENT: Tried to make the progress bar stay visible in the Overview tab until the data is finish loading.
  * FEATURE IMPROVEMENT: Redesigned the Export Features dialog.
  * FEATURE IMPROVEMENT: Improved the GUI for the SearchPreferencesDialog.
  * FEATURE IMPROVEMENT: Extended the protein outputGenerator to be able to export just the list of the main accession numbers. As needed for the Annotation tab.
  * FEATURE IMPROVEMENT: Refurbished the AnnotationPreferencesDialog.
  * FEATURE IMPROVEMENT: Updated the default human GO mappings to Ensembl version 66.
  * FEATURE IMPROVEMENT: Page up and page down will now result in selection updates in the tables (before only up and down was used).
  * FEATURE IMPROVEMENT: The sorting order in the tables are now kept when updating the table models.
  * FEATURE IMPROVEMENT: Replaced all the check boxes in tables with our own home made check mark.
  * FEATURE IMPROVEMENT: All progress dialogs can now be closed/canceled.
  * FEATURE IMPROVEMENT: Added progress dialogs to the Validation tab where missing.
  * FEATURE IMPROVEMENT: In the GO tab the number of GO mapped proteins for Ensembl and for the project is now shown.
  * FEATURE IMPROVEMENT: Updated the PeptideShaker icon.
  * FEATURE IMPROVEMENT: The precursor charge QC plot now uses the max charge detected in the project as the max value.
  * FEATURE IMPROVEMENT: Improved the GUI of the ImportSettingsDialog.

  * BUG FIX: Tried to fix the threading issues in the PtmPanel.
  * BUG FIX: Fixed a bug in the clearData method that resulted in issues when opening a second project.
  * BUG FIX: Fixed a threading issue that could result in a null pointer exception when closing the tool.
  * BUG FIX: Fixed a bug in the peptide export in the Export Features dialog where the order of the boolean variables had gotten mixed up.
  * BUG FIX: Fixed a serious bug in the GO tab: the max value used for the dataset was incorrect (and could result in an exception).
  * BUG FIX: Fixed a bug in the GO tab where the sorting of the table resulted in the wrong p-values being shown.
  * BUG FIX: Fixed a bug where the saving and closing of a project started at the same time.
  * BUG FIX: Fixed some bugs in the Modification tab related to selecting multiple PSMs.
  * BUG FIX: Corrected a bug in the new dialog which made it impossible to load data when not from SearchGUI.
  * BUG FIX: Corrected bugs concerning modifications and spectrum counting maximum.

  * LIBRARY UPDATE: Updated utilities to version 3.4.8.
  * LIBRARY UPDATE: Updated uniprotjapi to version 2012.03.
  * LIBRARY UPDATE: Added jshortcut as a dependency.
  * LIBRARY UPDATE: Removed swingx as a dependency.

Download Count: 45


---


**Changes in PeptideShaker 0.15 (March 22. 2012):**

  * NEW FEATURE: PRIDE Export is now supported.
  * NEW FEATURE: Allowed the user to change the number of displayed aa before and after the sequence improved the sequence coverage panel for multiply detected peptides.
  * NEW FEATURE: Made it possible to save the bug report to user defined file.
  * NEW FEATURE: Allowed the user to change the PTM thresholds.
  * NEW FEATURE: Allowed the user to tune the Java available memory directly from the user interface.
  * FEATURE IMPROVEMENT: Improved the peptide output accounting for protein inference and adding surrounding amino acids.
  * FEATURE IMPROVEMENT: Speed up fix for X!Tandem files loading.
  * FEATURE IMPROVEMENT: Added the use of buffered IO wherever possible.
  * FEATURE IMPROVEMENT: Square brackets are now allowed in the path were PeptideShaker is installed.
  * FEATURE IMPROVEMENT: Improved the way shared peptides are handled when loading the file.
  * FEATURE IMPROVEMENT: The SE column now points to the spectrum id tab to inspect search engine conflict.
  * FEATURE IMPROVEMENT: The tables in the Overview tab now loads faster.
  * FEATURE IMPROVEMENT: Improved cancel option of the import process.
  * BUG FIX: Corrected two minor bugs occurring when importing files.
  * BUG FIX: Corrected a very nasty bug in the export of ptm scores resulting in a null pointer exception. Preventing this bug from happening anywhere else.
  * BUG FIX: Re-enabled the filters.
  * BUG FIX: Corrected a bug in the modification position.
  * LIBRARY UPDATE: Updated utilities to version 3.3.51.
  * LIBRARY UPDATE: Updated uniprotjapi to version 2012.02.

Download Count: 27


---


**Changes in PeptideShaker 0.14.7 (February 28. 2012):**

  * FEATURE IMPROVEMENT: Added progress bars when importing the PSMs in the id file readers.
  * FEATURE IMPROVEMENT: Improved the way missing or wrong mgf files are handled.
  * FEATURE IMPROVEMENT: Some of the metrics are calculated earlier to improve import speed.
  * FEATURE IMPROVEMENT: Improved the PTM output for proteins.
  * FEATURE IMPROVEMENT: Find feature: Added a delay such that the search is not carried out until the user stops typing.
  * FEATURE IMPROVEMENT: Find feature: made the protein filtering non case sensitive on the description.
  * FEATURE IMPROVEMENT: Find feature: made it possible to jump to spectra in the Spectrum ID tab.
  * LIBRARY UPDATE: Updated utilities to version 3.3.42, fixing an issue with unknown protein expect values in X!Tandem files.

Download Count: 81


---


**Changes in PeptideShaker 0.14.6 (February 20. 2012):**

  * NEW FEATURE: Added a bug report dialog so that the user does not need to open the file every time.
  * FEATURE IMPROVEMENT: The loading of the files is slightly faster.
  * FEATURE IMPROVEMENT: Improved the way the retention time is displayed in the FindDialog.
  * FEATURE IMPROVEMENT: Made the interaction with big datasets in the Overview tab a lot faster.
  * FEATURE IMPROVEMENT: Removed the cancel button in the New Project dialog and increased the size of the Create button.
  * FEATURE IMPROVEMENT: Made the Create project button and the Validate and Apply buttons in the Validation tab green when they can be clicked.
  * FEATURE IMPROVEMENT: Minor GUI updates to the Validation tab.
  * FEATURE IMPROVEMENT: Improved the way ptms are handled.
  * FEATURE IMPROVEMENT: Improved the handling of strange spectrum titles.
  * FEATURE IMPROVEMENT: Improved the handling of unspecified cleavage site.
  * FEATURE IMPROVEMENT: Improved the way the max m/z value is set in the FindDialog.
  * FEATURE IMPROVEMENT: Improved the way the retention time is displayed in the FindDialog.
  * BUG FIX: The updates in the stats panel are now shown in the other tabs and the tool no longer crashes when executing the changes.
  * BUG FIX: Corrected a bug in the spectrum counting method resulting in proteins not found for old projects.
  * BUG FIX: Made the protein inference dialog interacting with the data again.
  * BUG FIX: Fixed a bug in the 3D Structure tab where the validation status for the peptides was not included.
  * BUG FIX: Corrected a minor bug occurring when opening a file.
  * LIBRARY UPDATE: Updated utilities to version 3.3.39, improving the support for home made FASTA files.
  * LIBRARY UPDATE: Added ols-dialog version 3.3.2 as a dependency.

Download Count: 22


---


**Changes in PeptideShaker 0.14.5 (February 6. 2012):**

  * FEATURE IMPROVEMENT: Improved the GUI of the 'Exclude Unknown PTMs' check box, and updated the corresponding help text
  * FEATURE IMPROVEMENT: Reduced manually the memory consumption before parsing an identification file.
  * FEATURE IMPROVEMENT: Added secondary progress when loading data.
  * FEATURE IMPROVEMENT: Disabled the protein inference for omssa and Mascot PSMs.
  * FEATURE IMPROVEMENT: Tried to avoid the fetching of precursors when loading PSMs.
  * FEATURE IMPROVEMENT: Added date and version to the error log.
  * FEATURE IMPROVEMENT: Improved the PTM processing.
  * FEATURE IMPROVEMENT: Grouped the PSM saving with the peptide and protein generation.
  * FEATURE IMPROVEMENT: Improved the NSAF index for shared peptides.
  * FEATURE IMPROVEMENT: Improved the handling of missing FASTA file.
  * BUG FIX: Corrected a bug in the protein inference dialog where the protein inference could not be changed.
  * BUG FIX: Tried to fix the bug where the main progress bar in waiting dialog goes beyond 100%.
  * BUG FIX: The fix that makes sure that the accuracy and intensity sliders do not get stuck, is now independent of the max value for the slider.
  * BUG FIX: Corrected a bug in the peptide to protein mapping test.
  * LIBRARY UPDATE: Updated the UniProt API to 2012.01.
  * LIBRARY UPDATE: Updated utilities to version 3.3.35.

Download Count: 46


---


**Changes in PeptideShaker 0.14.4 (January 30. 2012):**

  * NEW FEATURE: It is now possible to zoom in the protein sequence coverage panel. The protein sequence coverage panel is now also a lot more accurate when the user is to select peptides in the sequence.
  * FEATURE IMPROVEMENT: The backend of the Spectrum IDs tab has been imporved and interaction with bigger projects in this tab is now lot faster.
  * FEATURE IMPROVEMENT: Three improvements to the Progenesis export: 1) multiple ptms on the same residue is now supported. 2) Protein descriptions are now included. 3) Only validated PSMs are now included.
  * FEATURE IMPROVEMENT: Allowed the removal of unexpected modifications.
  * FEATURE IMPROVEMENT: Improved the import filter to consider multiple first hits.
  * FEATURE IMPROVEMENT: Improved the best hit selection method.
  * FEATURE IMPROVEMENT: Fixed various issues in the Spectrum IDs tab related to having multiple mgf files in the same project.
  * BUG FIX: Fixed a bug occuring in the Spectrum ID tab if the charge was missing.
  * BUG FIX: Corrected a bug in the project csv export .
  * BUG FIX: Fixed a bug in the getUserSelectedFile method where the user was asked if he/she wanted to overwrite the file when opening a file (and not just when saving).
  * LIBRARY UPDATE: Removed the parser dependencies from the pom, these should be taken from the utilities pom instead.
  * LIBRARY UPDATE: Added swingx 0.9.1 as a dependency, was only a transitive dependency before.
  * LIBRARY UPDATE: Updated utilities to version 3.3.30

Download Count: 22


---


**Changes in PeptideShaker 0.14.3 (January 23. 2012):**

  * NEW FEATURE: Added FASTA and CSV export options for the identified and unidentified proteins to the Follow Up export dialog.
  * FEATURE IMPROVEMENT: Major overhaul of the export options: replaced most of the slow export to clipboard options with faster export to file options.
  * FEATURE IMPROVEMENT: Minor code improvements to FileImporter, slightly reducing the memory required.
  * FEATURE IMPROVEMENT: Big Mascot files are now indexed. Slower, but makes it possible to open bigger files.
  * BUG FIX: Fixed a bug where the location of the Score column in the Peptide table in the Overview tab was incorrect.
  * BUG FIX: Fixed a bug where the confidence column in the Peptide table was not hidden when hiding the sparklines.
  * LIBRARY UPDATE: Updated utilities to version 3.3.26.

Download Count: 24


---


**Changes in PeptideShaker 0.14.2 (January 17. 2012):**

  * NEW FEATURE: The possible coverage is now shown in the protein sequence coverage panel in the Overview tab.
  * NEW FEATURE: Added precursor charge(s) to the peptide features export.
  * NEW FEATURE: Added precursor end position to the peptide features export.
  * NEW FEATURE: Added the MW column to the Structure tab.
  * FEATURE IMPROVEMENT: Fixed it so that the selections in the Overview and Structure tabs are not re-loaded if they are the same as the current selections.
  * FEATURE IMPROVEMENT: Improved the GUI of the PDB-Protein overlap column in the Structure tab.
  * FEATURE IMPROVEMENT: Improved the GUI for the RT column in the Spectrum IDs tab.
  * FEATURE IMPROVEMENT: Improved the way the start index of the peptides is displayed in the Overview and Structure tabs. (Removed the End index.)
  * FEATURE IMPROVEMENT: The jsparkline for the p-value in the GO tab is now light gray when not significant and green when significant. Also replaced the gray color of the Log2 Diff column with light gray in order to be consistent.
  * BUG FIX: Fixed a bug where the Score column in the protein table in the Overview tab did not have at the correct location when displayed.
  * BUG FIX: Fixed some GUI bugs related to changing the spectrum counts method.
  * BUG FIX: Fixed various issues related to always making sure that the same protein, peptide and psm is selected when moving between tabs.
  * BUG FIX: Fixed a bug in the protein export where there was no separator between protein accession numbers in the Other proteinScoreColumn(s) column.
  * LIBRARY UPDATE: Updated jsparklines to version 0.5.34.
  * LIBRARY UPDATE: Updated utilities to version 3.3.23.

Download Count: 12


---


**Changes in PeptideShaker 0.14.1 (January 13. 2012):**

  * NEW FEATURE: Added the display of the unassigned spectra count to the Spectrum IDs tab.
  * NEW FEATURE: Added the option of exporting the unidentified proteins to a tab separated text file from the Follow-Up Analysis Dialog.
  * BUG FIX: Solved a bug impairing the portability of projects.
  * BUG FIX: Solved a bug in the protein inference dialog related to especially complicated protein inference issues.

Download Count: 11


---


**Changes in PeptideShaker 0.14 (January 13. 2012):**

  * NEW FEATURE: Added the observable coverage in the Overview tab.
  * NEW FEATURE: PeptideShaker now keeps in memory the most recent results.
  * NEW FEATURE: Added a first attempt at a Progenesis export option. Needs more testing!
  * FEATURE IMPROVEMENT: Improved the way missing ptms are handled.
  * FEATURE IMPROVEMENT: Improved the use of the jsparklines for the peptide and spectra columns in the Overview tab.
  * FEATURE IMPROVEMENT: Improved the color used for the non-validated jsparklines.
  * FEATURE IMPROVEMENT: GUI improvements to the Export Features dialog.
  * FEATURE IMPROVEMENT: Improved the use of the waiting icon when exporting data.
  * BUG FIX: Fixed a minor bug in the Find feature.
  * BUG FIX: Fixed a bug in the addDatabaseLinks method: when multiple accession numbers were provided the html link color was used even when no links were added.
  * LIBRARY UPDATE: Updated utilities to version 3.3.20.
  * LIBRARY UPDATE: Updated jsparklines to version 0.5.33.

Download Count: 4


---


**Changes in PeptideShaker 0.13.1 (January 6. 2012):**

  * NEW FEATURE: The GO analysis now uses ENSEMBL 65.
  * FEATURE IMPROVEMENT: The QC plots are now only loaded when selected, and also not reloaded if not needed.
  * FEATURE IMPROVEMENT: Improved the use of the primary progress bar in the WaitingDialog.
  * FEATURE IMPROVEMENT: Removed the 'Starred' column when exporting and 'Request Starred' was not selected.
  * BUG FIX: Fixed a bug with the parsing of mgf files with spectrum titles containing `\`.
  * LIBRARY UPDATE: Updated utilities to version 3.3.17.

Download Count: 28


---


**Changes in PeptideShaker 0.13.0 (January 4. 2012):**

  * NEW FEATURE: It is now possible to change the location of a given PTM in the Modifications tab.
  * NEW FEATURE: Added a new protein QC plot: protein sequence length.
  * NEW FEATURE: PTMs are now indicated in the protein sequence coverage panel in the Overview tab.
  * FEATURE IMPROVEMENT: Added progress bars when changing modification type or peptide selection in the Modifications tab.
  * FEATURE IMPROVEMENT: The tool now remembers the hidden/shown panels when maximizing the spectrum panel in the Overview tab, so that a second click on the maximize button resets the previously shown panels.
  * FEATURE IMPROVEMENT: Changed the selected peptide color in the protein coverage from red to blue, as red represents non-validated and blue is the row selection color in the tables.
  * BUG FIX: Fixed an issue where 'Request Starred' was included in the 'Select All' features in the 'FeaturesPreferencesDialog' resulting in empty exports if nothing was starred.
  * BUG FIX: Fixed a bug in the PTM tab where the tabbed pane moved to the PTM table tab when selecting a related peptide.
  * LIBRARY UPDATE: Updated jsparklines to version 0.5.31.

Download Count: 15


---


**Changes in PeptideShaker 0.12.2 (December 28. 2011):**

  * NEW FEATURE: Split the display of the number of peptides and spectra into validated and non-validated.
  * FEATURE IMPROVEMENT: Removed the hardcoded white chart color for selected rows.
  * BUG FIX: Re-enabled the FASTA protein inference parsing.
  * BUG FIX: Fixed minor GUI bugs in the FilterDialog.
  * BUG FIX: Fixed a couple of filtering bugs in the FindDialog related to the fact that the names of the columns had changed.
  * BUG FIX: Minor GUI fixes in the export dialog.
  * BUG FIX: The sequence coverage panel is now updated when changing the main match in the protein table in the Overview or 3D Structure tab.
  * BUG FIX: Fixed it so that the same PI colors are used in the PTM tab as for the other tabs.
  * LIBRARY UPDATE: Updated jsparklines to version 0.5.30.
  * LIBRARY UPDATE: Updated utilities to version 3.3.14.

Download Count: 17


---


**Changes in PeptideShaker 0.12.1 (December 21. 2011):**

  * NEW FEATURE: Added the handling of hide/star properties in the export options.
  * NEW FEATURE: Added the modified sequence in the protein export.
  * NEW FEATURE: NCBI accession numbers will now be turned into HTML links similar to for UniProt.
  * NEW FEATURE: MGF files with multiple precursor charges are now supported.
  * NEW FEATURE: Protein descriptions that are too long for the column width are now shown as tooltips for the Overview and 3D Structure tabs.
  * BUG FIX: Better handling of closing a New Project dialog.
  * BUG FIX: Minor bug fix in the jump to dialog.
  * BUG FIX: Fixed a bug that occurred when trying to reload the data with the new validation settings.
  * BUG FIX: Fixed a bug where the protein accession number HTML links where not active in the two protein inference dialogs.
  * BUG FIX: Fixed a bug where the fragment ion menu bar had gone missing in the Spectrum IDs tab.
  * LIBRARY UPDATE: Updated jsparklines to version 0.5.28.
  * LIBRARY UPDATE: Updated utilities to version 3.3.12.

Download Count: 22


---


**Changes in PeptideShaker 0.12.0 (December 15. 2011):**

  * NEW FEATURE: Added a peptide length QC plot.
  * NEW FEATURE: Added Confidence and Search Engine Agreement column to the psm table in the Overview tab.
  * NEW FEATURE: Added the Search Engine Agreement column to the Spectrum IDs tab. Also changed the PSM column in the same tab into a Search Engine Agreement column.
  * NEW FEATURE: The identification charge is now used instead of the precursor charge.
  * NEW FEATURE: Added advanced star/hide filter options.
  * NEW FEATURE: Added a Find feature to the menu bar of the main frame.
  * NEW FEATURE: Set up the use of user preferences object saved in the user home folder.
  * NEW FEATURE: Added selected/starred columns to all tabs where possible.
  * NEW FEATURE: Implemented a first attempt at a PTM overview table.

  * FEATURE IMPROVEMENT: Improved the cleaning of the project: preferences were not reset.
  * FEATURE IMPROVEMENT: Made sure that the same protein/peptide/spectrum is always selected.
  * FEATURE IMPROVEMENT: Fastened the loading of the Overview tab.
  * FEATURE IMPROVEMENT: The enzymes are now sorted alphabetically in the SearchPreferencesDialog.
  * FEATURE IMPROVEMENT: mods.xml and usermods.xml are now excluded when browsing for search result files.
  * FEATURE IMPROVEMENT: Memory errors are now caught even when opening a file.
  * FEATURE IMPROVEMENT: Tried to make the wrapper a bit smarter. Increased the max default memory setting to -Xmx1500M.
  * FEATURE IMPROVEMENT: Added file filters for the graphics export dialog.
  * FEATURE IMPROVEMENT: Extended the default PTM profile.
  * FEATURE IMPROVEMENT: When opening results from SearchGUI in the New Project dialog the FASTA and MGF files are now searched for in the same folder as the SearchGUI properties file if not found at the given locations.

  * BUG FIX: Fixed a bug where the waiting icon was not turned off when updating the spectrum selection in the Spectrum ID tab.
  * BUG FIX: Fixed a bug where using the keyboard to move around in the peptide table in the PTM tab did not update the PSM selections.
  * BUG FIX: The progress dialog now shows the actual progress when loading a FASTA file.
  * BUG FIX: Fixed a bug that occured if using ptms with more than one residue type.
  * BUG FIX: Avoided that PeptideShaker gets stuck when an error occurs in the peptide to protein map creation.
  * BUG FIX: Corrected a bug when creating a new project while another one is loaded.

  * LIBRARY UPDATE: Updated utilities to version 3.3.9.
  * LIBRARY UPDATE: Updated the uniprot api to version 2011.12.

Download Count: 24


---


**Changes in PeptideShaker 0.11.2 (November 24. 2011):**

  * NEW FEATURE: Added a maximize button to the Spectrum panel in the Overview tab.
  * BUG FIX: Fixed a bug in the protein filter for the confidence and score filters.
  * BUG FIX: Fixed a minor GUI bug when the user tried to hide all panels in the Overview tab.

Download Count: 77


---


**Changes in PeptideShaker 0.11.1 (November 21. 2011):**

  * FEATURE IMPROVEMENT: Reduced the time required to save a project using the `Save` option compared to the `Save As` option.
  * FEATURE IMPROVEMENT: "N/A" is now shown in the retention time columns if the retention time is -1.
  * FEATURE IMPROVEMENT: Background highlighting of modifications in the sequence fragmentation plots with tooltips, similar to what us used in the tables.
  * FEATURE IMPROVEMENT: The spectrum sliders (accuracy and intensity level) are now hidden by default.
  * FEATURE IMPROVEMENT: The p-value shown in the GO Enrichment tab is now the FDR-corrected p-value.
  * BUG FIX: Fixed some bugs related to changing the protein inference in the protein table in the Overview tab.
  * BUG FIX: Made sure that the color coding for protein inference is the same in both the Overview tab and the 3D Structures tab.
  * BUG FIX: Fixed a bug with the sorting of the Log2 Diff column in the GO Enrichemnt tab, that sorted on absolute value.
  * BUG FIX: Fixed a bug in the GO Enrichment mapping where unmapped GO terms were added to the table and frequencies.
  * BUG FIX: Corrected a bug in the export of unidentified spectra.
  * LIBRARY UPDATE: Updated jsparklines to version 0.5.27.
  * LIBRARY UPDATE: Updated utilities to version 3.3.3.

Download Count: 9


---


**Changes in PeptideShaker 0.11.0 (November 17. 2011):**

  * NEW FEATURE: Added a GO Enrichment Analysis tab.
  * NEW FEATURE: Added molecular weight to the protein table in the Overview tab.
  * NEW FEATURE: Added Save in addition to Save As in the File menu.
  * NEW FEATURE: Added Tip of the Day to the Waiting dialog.
  * NEW FEATURE: The modified residues are now indicated by a star above the given residue in the sequence fragmentation plot.
  * NEW FEATURE: Added the option of hiding proteins in the Overview tab.
  * NEW FEATURE: Added the option of highlighting/marking proteins in the Overview tab.
  * NEW FEATURE: Made the recent projects appear in the welcome dialog. Also updated the Welcome dialog GUI.
  * NEW FEATURE: The main tabs are now loaded individually, i.e., not all at once when opening a project.

  * FEATURE IMPROVEMENT: Made the importing of PeptideShaker projects a bit smarter.
  * FEATURE IMPROVEMENT: Simplified the default PTM short names for oxidation (mox > ox) and phosphorylation (phopho > p), as the long names took up too much space.
  * FEATURE IMPROVEMENT: The delta masses used when manually de novo sequencing the spectra are now based on the currently selected modifications and not hardcoded to the default set.
  * FEATURE IMPROVEMENT: Replaced HelpWindow with HelpDialog, identical in every way but a JDialog instead of a JFrame, which makes the modal exclusion handling simpler.
  * FEATURE IMPROVEMENT: Made it possible to interact with the tool when the ProteinFilter dialog is being displayed, e.g., select proteins in the Overview tab without having to close the filtering dialog.
  * FEATURE IMPROVEMENT: Fixed some minor GUI details for when using the backup look and feel.
  * FEATURE IMPROVEMENT: The export folder when zipping a PeptideShaker project can now be chosen by the user.
  * FEATURE IMPROVEMENT: Sectrumpanel now displays all spectra.
  * FEATURE IMPROVEMENT: Added horizontal scroll bars to the peptide tables in the PTM tab, displayed when required.
  * FEATURE IMPROVEMENT: Improved the focus traversal order in the protein filtering dialog.
  * FEATURE IMPROVEMENT: Removed the index column in the ptm selection panel in the Modifications tab to make more room for the peptides tables.
  * FEATURE IMPROVEMENT: Spectrum IDs tab: added more space for the label in the retention time cell renderer to show higher retention time values.
  * FEATURE IMPROVEMENT: Retention time is now shown for the PSMs in the Modification tab.
  * FEATURE IMPROVEMENT: Improved the error handling if a required mgf file is missing when trying open a new project.
  * FEATURE IMPROVEMENT: Moved the identification filter settings in a separate dialog.

  * BUG FIX: Fixed a GUI bug with the spectrum slidersin the Spectrum IDs tab.
  * BUG FIX: Fixed a bug in the Da/ppm selection when importing the value from a SearchGUI properties file (it always defaulted to ppm...).
  * BUG FIX: Fixed some minor bugs related to the export PeptideShaker project to zip file feature.
  * BUG FIX: Fixed a bug in the ProteinInferencePeptideLevelDialog where one of the tables was editable, and thus the UniProt link didn't work.
  * BUG FIX: Minor GUI fixes for the PSM column in the Spectrum IDs tab.
  * BUG FIX: Fixed a problem with the location of the popup menus in the contextual export options when the tool was not maximized.
  * BUG FIX: Fixed a bug where the spectrum annotations could not be changed from the annotation menu bar in the Spectrum IDs and PTM tabs.
  * BUG FIX: Fixed a bug where the tool was not always reset correctly when opening a new project.
  * BUG FIX: Fixed a problem with the validation tab when editing both threshold and PEP window at the same time and then moving to a different tab.

  * LIBRARY UPDATE: Updated the UniProt API to version 2011.11.
  * LIBRARY UPDATE: Updated utilities to version 3.3.2.
  * LIBRARY UPDATE: Updated jsparklines to version 0.5.26.

Download Count: 8


---


**Changes in PeptideShaker 0.10.3 (October 24. 2011):**

  * BUG FIX: The help text in the Modifications tab is now visible.
  * LIBRARY UPDATE: Updated utilities to version 3.2.22, which now also supports the special amino acid Selenocysteine (U).

Download Count: 30


---


**Changes in PeptideShaker 0.10.2 (October 21. 2011):**

  * BUG FIX: Fixed a minor GUI issue related to the left hand part of the spectrum panel not aligning correctly when the peptide/psm panel was hidden.
  * BUG FIX: Fixed some resizing issues for modification profile plots in the modification tab where part of the profile could be cut off if one profile was longer than the other.
  * BUG FIX: Fixed some resizing issues in the Spectrum ID and Validation tabs.
  * LIBRARY UPDATE: Updated utilities to version 3.2.21, which now supports the special Mascot amino acids B, Z and X.

Download Count: 4


---


**Changes in PeptideShaker 0.10.1 (October 20. 2011):**

  * NEW FEATURE: Added hide options to all the contextual menus in the Overview tab.
  * LIBRARY UPDATE: Updated uniprotjapi to version 2011.10, fixing a problem with the UniProt connection.

Download Count: 6


---


**Changes in PeptideShaker 0.10.0 (October 19. 2011):**

  * NEW FEATURE: QC plot tab added.
  * NEW FEATURE: Annotation tab with links to other protein resources.
  * NEW FEATURE: Made it possible to use relative of absolute error in the mass error and bubble plots.
  * NEW FEATURE: Added a new sequence coverage plot with all the found peptides indicated.
  * NEW FEATURE: PTM location confidence scoring.
  * NEW FEATURE: Added a Welcome dialog.
  * NEW FEATURE: Protein inference is now displayed also at the peptide level.
  * NEW FEATURE: PTM color coding.
  * NEW FEATURE: Modification profile plots.
  * NEW FEATURE: The 10 last recently opened projects can now be opened directly from the File menu.
  * NEW FEATURE: Simpe export of identification features, and contextual exports for each panel.
  * NEW FEATURE: FASTA and spectrum files are now indexed and not loaded into memory anymore.
  * NEW FEATURE: Identification matches are stored in a separate folder and not loaded in the memory anymore.
  * NEW FEATURE: Annotation intensity level slider and annotation accuracy sliders added to the spectrum plots.
  * FEATURE IMPROVEMENT: A global maximum is now used for the sparklines for all charge and mass error columns.
  * FEATURE IMPROVEMENT: Updated most of the help texts.
  * FEATURE IMPROVEMENT: The peptides are now sorted according to their number of spectra.
  * FEATURE IMPROVEMENT: Modifications are now shown directly on the peptide sequence. Modifications are now also mapped onto the 3D structure.
  * FEATURE IMPROVEMENT: Y-axis auto zoom in the spectrum plots now disregards unannotated peaks (unless all peaks are shown).
  * FEATURE IMPROVEMENT: Changed the default -Mxm option from 1500M to 1024M, to make sure that the tool starts on all machines.
  * FEATURE IMPROVEMENT: Spectrum annotation selection has been made simpler by the addition of an annotation menu bar.
  * FEATURE IMPROVEMENT: Added a secondary progress bar in the WaitingDialog showing progress for the current process.
  * FEATURE IMPROVEMENT: Added terminals to the sequence fragmentation plots.
  * FEATURE IMPROVEMENT: Use of subscript for the numbers in all peak annotations in all plots.
  * FEATURE IMPROVEMENT: Improved automatic spectrum annotation.
  * FEATURE IMPROVEMENT: The mgf paths in the search result files OS independent.
  * FEATURE IMPROVEMENT: The two residues in front of and after the selected peptide is now shown in the panel title of the spectrum panel.
  * FEATURE IMPROVEMENT: Improved the way exceptions related to proteins not found in the FASTA file are handled. PeptideShaker now stops the loading of a project if such an exception is thrown.
  * BUG FIX: Removed peptides without PSMs from the display.
  * LIBRARY UPDATE: Updated utilities to 3.2.20.
  * LIBRARY UPDATE: Updated jsparklines to version 0.5.20.
  * LIBRARY UPDATE: Updated xtandem parser to version 1.3.5.
  * LIBRARY UPDATE: Updated xtandem parser to version 1.4.6.
  * LIBRARY UPDATE: Updated mascotdatfile to version 3.2.6.

Download Count: 6


---


**Changes in PeptideShaker 0.9.3 (July 17. 2011):**

  * FEATURE IMPROVEMENT: The link between the Overview and the Structure tab is now smarter, and updates less frequently.
  * FEATURE IMPROVEMENT: The maximum initial Java memory size is now set to 1500M (the magic number for 32 bit Java...).
  * FEATURE IMPROVEMENT: Improved the wrapper so that it now defaults to using the 64 bit Java version if available.
  * BUG FIX: Fixed a bug in the dialog displayed when detecting an unknown protein, where the title and the message was interchanged.
  * BUG FIX: The files selection dialog (for multiple SearchGUI property files) is now located relative to its parent.

Download Count: 122


---


**Changes in PeptideShaker 0.9.2 (July 14. 2011):**

  * BUG FIX: Corrected a minor bug in the preferences dialog.
  * LIBRARY UPDATE: Updated utilities to 3.1.30, for more compatible databases.

Download Count: 11

---

**Changes in PeptideShaker 0.9.1 (July 14. 2011):**

  * NEW FEATURE: Added protein HTML links to all columns displaying protein accession numbers.
  * NEW FEATURE: Made it possible to include more than one protein HTML link in the same cell in the tables.
  * NEW FEATURE: The 3D protein model now rotates slowly as a default.
  * FEATURE IMPROVEMENT: Minor GUI updates to the protein inferences dialog.
  * FEATURE IMPROVEMENT: Changed all the protein links from pointing the the SRS web page to pointing to UniProt.
  * FEATURE IMPROVEMENT: Extended the 3D Structure help text.
  * BUG FIX: Fixed various minor GUI issues related to using the backup look and feel, i.e., not using Nimbus.
  * LIBRARY UPDATE: Updated utilities to 3.1.29, fixing a bug in the XTandem parsing.

Download Count: 2

---

**Changes in PeptideShaker 0.9 (July 11. 2011):**

  * The first public beta release of PeptideShaker.

Download Count: 7

---