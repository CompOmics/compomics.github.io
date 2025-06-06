---
title: "ReleaseNotes"
layout: default
permalink: "/projects/fragmentation-analyzer/wiki/ReleaseNotes"
tags: wiki, fragmentation-analyzer
project: "fragmentation-analyzer"
github_project: "https://github.com/CompOmics/fragmentation-analyzer"
---

# Release Notes

----

**Changes in FragmentationAnalyzer v1.5.17 - (August 14. 2017):** 

* FEATURE IMPROVEMENT: The OMSSA modification names are now shown instead of just the modification indexes when importing data from omx files.

----

**Changes in FragmentationAnalyzer v1.5.16 - (July 11. 2017):** 

* BUG FIX: Fixed a bug that made it impossible to create new projects based on OMSSA omx files.

* LIBRARY UPDATE: Updated omssa-parser to version 1.9.0.
* LIBRARY UPDATE: Updated utilities to version 4.10.0.

----

**Changes in FragmentationAnalyzer v1.5.15 - (November 12. 2016):** 

* LIBRARY UPDATE: Updated xtandem-parser to version 1.8.0.
* LIBRARY UPDATE: Updated omssa-parser to version 1.12.0.
* LIBRARY UPDATE: Updated mascotdatfile to version 3.5.0.
* LIBRARY UPDATE: Updated utilities to version 4.8.7.

----

**Changes in FragmentationAnalyzer v1.5.14 - (April 1. 2016):** 

* BUG FIX: Fixed a bug in the popup menu for the internal frames not appearing. 

----

**Changes in FragmentationAnalyzer v1.5.13 - (September 3. 2015):** 

 * BUG FIX: Fixing an issue with the wrapper in handling memory warnings on 32 bit Java 1.8.

 * LIBRARY UPDATE: Updated utilities to version 4.0.4. 

----

**Changes in FragmentationAnalyzer v1.5.12 - (June 22. 2015):** 

 * FEATURE IMPROVEMENT: Updated the look and feel to be more in line with newer compomics tools. 
 * BUG FIX: Fixed a problem with the setting of the default memory. 
 * BUG FIX: Fixed JavaDoc errors so that it builds again in Java 8. 
 * LIBRARY UPDATE: Updated the maven-javadoc-plugin to version 2.9.1. 
 * LIBRARY UPDATE: Updated mascotdatfile to version 3.4.11, fixing a possible null pointer. 
 * LIBRARY UPDATE: Updated utilities to version 3.49.19. 

----

**Changes in FragmentationAnalyzer v1.5.11 - (May 21. 2013):**

 * LIBRARY UPDATE: Updated mascotdatfile to version 3.4.11, fixing a possible null pointer.

----

**Changes in FragmentationAnalyzer v1.5.10 - (April 26. 2013):**

 * BUG FIX: Fixed a problem with starting the tool on the latest Java release. 

Download Count: 20

----

**Changes in FragmentationAnalyzer v1.5.9 - (April 2. 2013):**

 * FEATURE IMPROVEMENT: Improved the look and feel of the spectra.
 * FEATURE IMPROVEMENT: The project now supports Maven 3.
 * BUG FIX: Fixed an issue with the pom file that could results in issues on NetBeans 7.2.
 * BUG FIX: Made it possible to run the tool from inside NetBeans.
 * LIBRARY UPDATE: Updated ms-lims to version 7.7.7.
 * LIBRARY UPDATE: Updated utilities to version 3.11.29.
 * LIBRARY UPDATE: Updated ommsa parser to version 1.5.9.
 * LIBRARY UPDATE: Updated mascotdatfile to version 3.4.10.
 * LIBRARY UPDATE: Updated jsparklines to version 0.5.45.

Download Count: 17

----

**Changes in FragmentationAnalyzer v1.5.8 - (March 10. 2011):**

 * LIBRARY UPDATE: utilities updated to 3.0.46.

Download Count: 671

----

**Changes in FragmentationAnalyzer v1.5.7 - (February 27. 2011):**

 * NEW FEATURE: Added JSparklines to the tables displaying some of the numbers as numbers and bar charts.
 * LIBRARY UPDATE: utilities updated to 3.0.40.

Download Count: 9

----

**Changes in FragmentationAnalyzer v1.5.6 - (January 25. 2011):**

 * BUG FIX: Fixed a bug in the Fragment Ion Probability plots x-axis labelling.

Download Count: 13

----

**Changes in FragmentationAnalyzer v1.5.5 - (November 7. 2010):**

 * FEATURE IMPROVEMENT: Changed the x-axis of the Fragment Ion Probability plots from "Fragment Ion Number" to "Residue Number" when analyzing a single peptide sequence.
 * LIBRARY UPDATE: utilities updated to 3.0.23.

Download Count: 80

----

**Changes in FragmentationAnalyzer v1.5.4 - (September 9. 2010):**

 * BUG FIX: Fixed a bug in the export figure to file feature that resulted in only parts of the figure being exported.
 * LIBRARY UPDATE: utilities updated to 3.0.21.

Download Count: 30

----

**Changes in FragmentationAnalyzer v1.5.3 - (Aug. 17. 2010):**

 * LIBRARY UPDATE: ms_lims updated to 7.4.1 
 * LIBRARY UPDATE: mascotdatfile updated to 3.2 
 * LIBRARY UPDATE: omssa-parser updated to 1.4 

Download Count: 16

----

**Changes in FragmentationAnalyzer v1.5.2 - (July 4. 2010):**

 * FEATURE IMPROVEMENT: Lots of minor changes to the GUI to make it look better on Windows 7.
 * LIBRARY UPDATE: utilities updated to 3.0.9 

Download Count: 32

----

**Changes in FragmentationAnalyzer v1.5.1 - (May 18. 2010):**

 * NEW FEATURE: ms_lims version 7.3 is now supported.
 * LIBRARY UPDATE: ms_lims updated to 7.3
 * LIBRARY UPDATE: mascotdatfile updated to 3.0.2
 * LIBRARY UPDATE: utilities updated to 3.0.1

Download Count: 32

----

**Changes in FragmentationAnalyzer v1.5 - (Feb. 27. 2010):**

 * NEW FEATURE: New plotting type: Intensity Correlation.
 * NEW FEATURE: New plotting type: Intensity Meta Plots.
 * FEATURE IMPROVEMENT: Made sure that b ions are blue and y ions red in all plots.

Download Count: 144

----

**Changes in FragmentationAnalyzer v1.4.3 - (Jan. 11. 2010):**

 * FEATURE IMPROVEMENT: Renamed and reordered the scoring types in the preference dialog.
 * BUG FIX: The value selected in the accuracy drop down menu for the 'Individual Spectra' table was sometimes replaced by the current value from the 'Search Results' accuract drop down menu when doing the analysis. Has now been fixed.
 * LIBRARY UPDATE: mascot_datfile updated from 2.2.2 to 2.2.3.

Download Count: 21

----

**Changes in FragmentationAnalyzer v1.4.2 - (Dec. 04. 2009):**

 * NEW FEATURE: It's now possible to duplicate some of the plot internal frames without having to redo the plotting. 
 * FEATURE IMPROVEMENT: Moved the text for the fragment ion markers so that singly charged b and y ions no longer overlap.
 * BUG FIX: A bug occurred if a bar chart was created when the legends were hidden.
 * BUG FIX: Exporting heat maps to PNG by right clicking on the heat map now works even when the complete heat map is not visible.

Download Count: 8

----

**Changes in FragmentationAnalyzer v1.4.1 - (Nov. 25. 2009):**

 * NEW FEATURE: All plots can now be exported as PDF, PNG, JPG and TIFF (in addition to the already supported SVG format).
 * NEW FEATURE: On Windows platforms `FragmentationAnalyzer` can now be run from paths containing spaces.
 * BUG FIX: Plot title names containing < or > (mainly for modifications) will now be altered before suggesting them as export plot title. (In order to make the suggested file names valid).
 * LIBRARY UPDATES: `pdf-transcoder` and `xerces` added for SVG to PDF conversion.

Download Count: 3

----

**Changes in FragmentationAnalyzer v1.4 - (Nov. 23. 2009):**

 * NEW FEATURE: All plots can now be exported as SVG files.
 * NEW FEATURE: Heat Maps with correlation data for comparing fragmentation patterns have been added.
 * NEW FEATURE: Box plots showing the spead for the combined fragment ion probability plots have been added.
 * NEW FEATURE: Peptide sequence length is now included in the tables. 
 * NEW FEATURE: Implemented a simple way of selecting x peptides of length y in the Search Results table.
 * BUG FIX: The error bars in the fragment ion probability plot is now correctly hidden.
 * BUG FIX: Removed the data point markers in the combined fragment ion probability plots.
 * BUG FIX: Fixed a bug in the Single/Combine drop down box for the spectra table.
 * LIBRARY UPDATE: Commons-Math updated to version 2.0.
 * LIBRARY UPDATE: New library added: `batik` for SVG file creation.

Download Count: 0

----

**Changes in FragmentationAnalyzer v1.3.2 - (Nov. 16. 2009):**

 * NEW FEATURE: It is now possible to edit the title of the plots/analyses frames. 
 * FEATURE IMPROVEMENT: The numbers in the results dialog are now formatted, e.g., 12345 becomes 12,345. 
 * FEATURE IMPROVEMENT: The coloring scheme for bubble and scatter plots when using the fragment ion type label type is now the same as for fragment ion probability plots.
 * FEATURE IMPROVEMENT: The combined fragment ion probability plots now ignore ions that can not be found for a given peptide, e.g., a y10 ion for a peptide of length 8 etc. (Earlier these were counted as a value of 0.) 
 * FEATURE IMPROVEMENT: The combined fragment ion probability plots now only use the average value for each peptide sequence to hinder that a more frequent peptide would influence the combined plot more than a less frequent peptide.
 * FEATURE IMPROVEMENT: In combined fragment ion probability plots the upper and lower boundaries can now be shown.
 * BUG FIX: Moved the Help menu to the far right in the menu bar.

Download Count: 3

----

**Changes in FragmentationAnalyzer v1.3.1 - (Nov. 06. 2009):**

 * NEW FEATURE: The search parameters section can now be hidden or shown by the user. 
 * NEW FEATURE: The number of plots per row and column in the plotting panel can now be set by the user in the Preferences dialog.
 * NEW FEATURE: Importing user settings from previous versions is now supported.
 * FEATURE IMPROVEMENT: In the search results dialog 'unique identifications' has been changed to 'unique peptides'.
 * FEATURE IMPROVMENT: A dialog is now shown if the data is to be removed from category plots explaining that this process is irreversible.
 * BUG FIX: Fixed a bug in the dialog shown when plotting more than 10 plots at once. It was shown too often.
 * BUG FIX: A bug was detected in the fragment ion counter shown after using the DataSeriesSelection dialog. The fragment ion counter is therefore now removed after using the DataSeriesSelection dialog. Hopefully it will be re-added in the future.

Download Count: 5

----

**Changes in FragmentationAnalyzer v1.3 - (Nov. 04. 2009):**

 * NEW FEATURE: Fragment Ion Probability plots can now be created.
 * NEW FEATURE: Intensity box plot is now supported for the spectra table as well.
 * NEW FEATURE: Made it possible to plot the unnormalized intensities as well. (Selected on the Edit menu.)
 * FEATURE IMPROVEMENT: Made sure that the sequence and spectra and fragment ion counters are always shown in the plot title bar when possible.
 * FEATURE IMPROVEMENT: The average mass error line has been made wider.
 * FEATURE IMPROVEMENT: Added icons to the `Select Analysis Type` drop down menus.
 * FEATURE IMPROVEMENT: The number of fragment ions shown in the title bar of the plots is now updated when data is hidden.
 * FEATURE IMPROVEMENT: The spectrum ID is now always shown in the title bar of the plot frames when possible.
 * FEATURE IMPROEVMENT: A dialog with a warning is now shown if more than 10 plots will be created when clicking the a.
 * FEATURE IMPROEVMENT: The occurrence counts in the drop down menus are now formatted, i.e., 1,473,567 instead of 1473567.
 * BUG FIX: Fixed a bug that resulted in a dialog appearing when closing the tool if used off-line.
 * BUG FIX: Fixed a bug in the data source selection that could result in an incorrect data set being opened when the table was sorted.
 * BUG FIX: Made sure that the drop down boxes are always wide enough to display the widest element.
 * BUG FIX: Fixed a bug in progress bar that resulted in limited information showed during intensity plot creation for spectra.
 * BUG FIX: Fixed a bug in the code for ordering the plot frames when deleting a plot. The new order was not always correct.

Download Count: 0

----

**Changes in FragmentationAnalyzer v1.2 - (Oct. 29. 2009):**

 * NEW FEATURE: Resizing of the main frame is now supported.
 * NEW FEATURE: The total number of fragment ions is now shown in the title bar of some of the mass error plots.
 * NEW FEATURE: Mass Error Box Plots can now be created.
 * NEW FEATURE: The identification ID can now be used as the data point label in bubble and scatter plots.
 * FEATURE IMPROVEMENT: If the ms_lims connection goes down, it is now possible to reconnect without having to reload the dataset. 
 * FEATURE IMPROVEMENT: Added a 'Select Highlighted' option to the series selection dialog.
 * BUG FIX: Fixed a bug that resulted in the spectrum annotations not showing up for data from ms_lims.
 * BUG FIX: Fixed a possible 'null pointer exception' in the table header column tips.
 * BUG FIX: Fixed a bug where the markers were being turned on when changing the data series selection

Download Count: 1

----

**Changes in FragmentationAnalyzer v1.1.1 - (Oct. 20. 2009):**

 * NEW FEATURE: The spectrum total intensity is now extracted from the ms_lims database (if avaiable) (requires ms_lims 7.1). This drastically decreased the time required to plot Mass Error Bubble Plots and Intensity Box Plots.
 * NEW FEATURE: The option of using the mass error threshold as the data label has been added (for ms_lims only). 
 * BUG FIX: Empty ms_lims data sets (and folder) are now deleted if the data extraction is canceled. 
 * BUG FIX: The progress bar shown when retrieving identifications from ms_lims no longer halts too long at 100%.
 * BUG FIX: The insert data set feature could result in an error if the folder contained non-valid data sets.
 * BUG FIX: The OK button in the database login dialog can now become enabled when pasting content into the fields and not just when typing.

Download Count: 4

----

**Changes in FragmentationAnalyzer v1.1 - (Oct. 17. 2009):**

 * NEW FEATURE: Tooltips have been added to both mass error plot types. 
 * NEW FEATURE: Instrument, fragment ion type or fragment ion scoring type (ms_lims only) can now be selected as the data point label when plotting the mass error.
 * NEW FEATURE: It is now possible to add markers highlighting the different fragment ion types to the mass error plots.
 * NEW FEATURE: Average fragment ion mass errors can now be plotted.
 * NEW FEATURE: Added `Select All` options to the instrument and terminals drop down menus.
 * NEW FEATURE: Added a general series selection dialog for mass error type plots.
 * FEATURE IMPROVEMENT: The import/load process has been simplified and improved.
 * FEATURE IMPROVEMENT: The highlight markers can now be turned on and off.
 * FEATURE IMPROVEMENT: Made it possible to turn the legends on/off.
 * FEATURE IMPROVEMENT: Increased the number of simultaneously visible elements in the drop down menus.
 * FEATURE IMPROVEMENT: Peptide sequence is now included in title of mass error plots when only one sequence is analyzed and "combine" is selected.
 * FEATURE IMPROVEMENT: The peptide sequence is now included in the title for "combine type plots" if all have rows contain the same modified peptide sequence.
 * FEATURE IMPROVMENT: Added dividers to the internal frame popup menu.
 * BUG FIX: Instrument 2 and 3 are now reset if instrument 1 is set to "- Select -". Same for instrument 3 when instrument 2 is set to "- Select -". Same fix also added for the modifications.
 * BUG FIX: Update visible series selection did not update the last added plot.
 * BUG FIX: Fixed some serious ms_lims connection issues that resulted in the connection terminating too soon.
 * BUG FIX: The analysis buttons did not get disabled when doing a new search.

Download Count: 1

----

**Changes in FragmentationAnalyzer v1.0.2 - (Oct. 08. 2009):**

 * NEW FEATURE: Added support for selecting/deselecting highlighted rows in the tables.
 * FEATURE IMPROVEMENT: The selection popup menus are now available for all columns and not just the selection column.
 * BUG FIX: Fixed a bug in the inverse selection in the search results table.
 * BUG FIX: Turned off sorting in the spectra table when inserting new rows, which makes inserting new rows much faster.
 * BUG FIX: If the ms_lims connection goes down, reloading the dataset now resets the connection.
 * BUG FIX: Fixed an incorrect default subject in the mailto links.

Download Count: 3

----

**Changes in FragmentationAnalyzer v1.0.1 - (Sep. 17. 2009):**

 * FEATURE IMPROVEMENT: The search button is now always enabled, and instead a message is shown if the required parameters are not selected.
 * FEATURE IMPROVEMENT: Minor updates of the help files.
 * BUG FIX: Fixed a bug where the ms_lims database connection was closed before it could be used.

Download Count: 21

----

**Changes in FragmentationAnalyzer v1.0 - (Sep. 10. 2009):**

 * (initial version)

Download Count: 2

----