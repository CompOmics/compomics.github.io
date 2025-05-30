---
title: "Tutorial"
layout: default
permalink: "/projects/fragmentation-analyzer/wiki/Tutorial"
tags: wiki, fragmentation-analyzer
project: "fragmentation-analyzer"
github_project: "https://github.com/CompOmics/fragmentation-analyzer"
---

# Tutorial
## Contents

 * [Loading Data Sets](#loading-data-sets)
 * [Selecting Search Parameters](#selecting-search-parameters)
 * [General Search](#general-search)
 * [Search Results](#search-results)
 * [Individual Spectra](#individual-spectra)
 * [Analyze/Plot](#analyzeplot)
 * [Resizing Plots](#resizing-plots)
 * [Plot Types](#plot-types)
  * [Heat Maps](#heat-maps)
 * [Plot Options](#plot-options)
 * [Plot Tool Bars](#plot-tool-bars)
 * [Spectrum Plot Options](#spectrum-plot-options)
 * [Remove All Plots](#remove-all-plots)
 * [Modification Search](#modification-search)
 * [Identification/Sequence Pairs](#identificationsequence-pairs)
 * [Intensity Box Plots](#intensity-box-plots)
 * [Normalization](#normalization)

----

### Loading Data Sets
This section contains a brief tutorial on how to use *Fragmentation Analyzer*.
After starting the tool the data selection dialog will be shown. (The
dialog can also be opened from the File menu by selection 'Open'.) You
can either import new data sets from one of the three supported formats,
or use one of the already imported data sets. For this tutorial we will
use the example data set provided with the tool. See [Importing Data](/projects/fragmentation-analyzer#importing-data) for details on how to import data. For now, select 'example data set' in the list of
available data sets and click on 'Load Data'.
 
The tool will now load the data set. Note that depending on the
size of the data set this can take some time. When finished a dialog
verifying that the data has been loaded will be shown and the drop
down menus in the left part of the screen will be updated with the
data from the loaded data set.

[Go to top of page](#contents)
 
### Selecting Search Parameters
To perform a search select the properties of the identifications
you are searching for in the lists. For example: instrument as ESI-QUAD-TOF,
N-term as NH2, C-term as COOH and charge as 2. The numbers behind the
terms are the total number of occurrences of that particular term in
the data set. Note that these numbers are for the whole data set and
not for the subset of the data set that you are currently selecting.
So even though all your selections have a high occurrence number, this
does not automatically result in identifications matching all your
selections. Leave the modification selection empty for now.

[Go to top of page](#contents)
 
### General Search
There are two search options available: general search or modification
search. We will first look at general search which basically returns
all identifications matching all the selected parameters. Click on
the 'Search' button in the lower left corner to start the search.
(Again note that depending on the size of the data set the process
might take some time completing.)

[Go to top of page](#contents)
 
### Search Results
When the search is completed a dialog presenting the main findings
will be shown, number of matches etc, and the results will be
inserted into the 'Search Results' table at the upper right part
of the screen. The results are sorted on the number of occurrences
of each identification, such that the most frequent are at the top
of the list.

[Go to top of page](#contents)

### Individual Spectra
Select a subset of the identifications by clicking in the rightmost
column of the table. Then select an analysis type in the  'Select Analysis Type'
drop down menu. First try 'List Individual Identifications'. Then
click the 'Analyze / Plot' button to the right of the drop down menu.
The list of individual spectra is then shown in the 'Individual Spectra'
table in the middle of the right part of the screen.

[Go to top of page](#contents)
 
### Analyze/Plot
Select a couple of the items in this table and again select an
analysis type in the 'Select Analysis Type' drop down menu for
the 'Individual Spectra' table, for example 'View Spectra'. Then
click the 'Analyze / Plot' button for the 'Individual Spectra' table.
The 'Search Results' and 'Individual Spectra' section will then
close and the 'Plot / Analyses' section will be expanded showing
the just created plot(s). The closed sections can easily be opened
again by clicking on the section header. Clicking ones more will
again close the section. Make sure that the 'Plot / Analyses' section
is visible before continuing.

[Go to top of page](#contents)

### Resizing Plots
In the plots section each plot is located in its own separate
frame. The frames can be resized and maximized individually. To
maximize a plot click on the plots maximize button in the upper
right corner (or double click on the title bar).

[Go to top of page](#contents)
 
### Plot Types
Currently nine different analysis types are supported:
 * Spectra Visualization - visualize the MS/MS spectra with fragment ion annotation, zooming and manual de-novo-sequencing.
 * Intensity Box Plots - analyze intensity variation for a set of identification of the same peptide.
 * Mass Error Scatter Plots - visualize the mass error spread in a set of selected identifications/spectra.
 * Mass Error Bubble Plots - same as Mass Error Scatter Plots but with peak intensities added.
 * Mass Error Box Plot - analyze the variation in mass errors.
 * Fragment Ion Probability Plot - analyze the probability of observing specific fragment ions.
 * Fragment Ion Heat Map - compare fragmentations using heat maps of correlation data.
 * Intensity Correlation - detect how the intensity correlates with the spread in intensity.
 * Intensity Meta Plots - further analyze the variations in intensity.

#### Heat Maps

The fragment ion heat maps compare fragmentation patterns across different peptide sequences. The input is the fragmentation patterns of a list of peptides and the output is a heat map comparing these against each other (one-by-one) using either Spearman or Pearson correlation (selected in the Preferences dialog, on the Edit menu).

Note that only the sequence range common to all sequences (starting from the N-term) is used. This is why one gets the "Peptides with different lengths ..." dialog. It is also possible to select a subset of this range as well. When this is done four heat maps are created.

Two plots for the b-ions and two for the y-ions are created. The only difference between the two types is that the one labeled "Significant" only uses two colors for a simpler view. A 99% significance level is used to decide if the comparison of two peptides is "equal enough" (colored red), or not "equal enough" (colored green).

While in the two other plots this cut-off is not used and the color simply represents the correlation between the two (from light green - low correlation, to light red - high correlation).

The last column and row in the table represents the average.

[Go to top of page](#contents)
        
### Plot Options
For the scatter and bubble plots two additional options are available.
First, the results can either be combined into one plot, or each
selected row can result in one plot. Chosen by selecting either
'Single' or 'Combine' in the drop down menu next to the 'Select
Analysis Type' menus. Second, is the option of using absolute
(Dalton) or relative (ppm) distance measurement when plotting.
Again selected in a drop down menu next to the 'Select
Analysis Type' menus.
 
The size of the bubbles (the scaling factor) can be altered by
selecting 'Preferences' on the 'Edit' menu. Note that any changes
only affect future plots. Existing plots are not updated.

[Go to top of page](#contents)
 
### Plot Tool Bars
Each plotting type also has a separate tool bar menu, which
accessed by right clicking on the title bar of the plot's frame.
The tool bars provides additional options for refining the
data shown, by turning on or off the different data series.
 
The non-spectrum plots also have an additional set of options
that can be accessed by right clicking on the plot itself.
These options include zooming, export/save plot amongst others.
 
[Go to top of page](#contents)

### Spectrum Plot Options
To zoom in a spectrum plot click and hold the left mouse
button where you want to start the zoom, and then drag in
the direction you want to zoom, marking the area to be
zoomed. Note that all the spectra plots are linked, so
zooming in one will result in zooming for all spectra. To
do manual de-novo-sequencing click on one peak. The distance
and amino acids matching this distance (if any) will then
be shown. To add the sequencing, click on the second peak.
Repeat the process to sequence more peaks. An added sequence
is removed by holding down the Ctrl button when clicking on
the sequence. To "store" a sequence, hold down the Alt button
and click on the sequence, the sequence turns red. To
remove such "stored" sequences, hold down Ctrl and Alt and
click in the sequence.

[Go to top of page](#contents)
 
### Remove All Plots
To remove all the plots in one operation, right click on the
title bar of one of the plots and select the 'Remove All' option
from the appearing popup menu.

[Go to top of page](#contents)

### Modification Search
While the general search simply finds all identifications matching
the selected parameters, the modification search is a little more
advanced. Use the same parameters as for the general search example
(instrument as ESI-QUAD-TOF, N-term as NH2, C-term as COOH and charge
as 2) but this time select `<Mox>` in the Alt 1 modification
parameters drop down menu, select 'Modification Search' and click
the 'Search Button'.

[Go to top of page](#contents)

### Identification/Sequence Pairs
For modification searches you are trying to find identification pairs
where one of them are modified with the selected modification and
the other is unmodified. You therefore have to select the minimum
number of such pairs required before a pair is used. Generally
you want as many matches as possible, e.g., 30+, but the data set
used in this tutorial is not big enough for that, so reduce the
number to 2.

[Go to top of page](#contents)
 
### Intensity Box Plots
When the search completes you will get one match. Select this
match, select the 'Intensity Box Plot' analysis type and create
the plot. The created plot presents the difference in relative
intensity between the different fragment ion types, for both
the modified and the unmodified identifications.

[Go to top of page](#contents)
 
### Normalization
In order to be able to compare the identifications coming from
spectra with varying total intensity total intensity normalization
is used to normalize the intensity of the used fragment ions
before the comparison is made.

[Go to top of page](#contents)