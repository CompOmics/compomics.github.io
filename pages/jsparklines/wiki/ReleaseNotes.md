---
title: "ReleaseNotes"
layout: default
permalink: "/projects/jsparklines/wiki/ReleaseNotes"
tags: wiki, jsparklines
project: "jsparklines"
github_project: "https://github.com/CompOmics/jsparklines"
---

# Release Notes

----

**Changes in JSparklines 1.1.2 (March 1. 2023):**

* BUG FIX: Fixed an issue with unwanted shadows in the box plots.

----

**Changes in JSparklines 1.1.1 (February 26. 2023):**

* BUG FIX: Fixed an issue with unwanted shadows in some of the bar charts.

----

**Changes in JSparklines 1.1.0 (November 5. 2022):**

* LIBRARY UPDATE: Updated jfreechart to version 1.5.3 (requiring Java 11 or newer).

----

**Changes in JSparklines 1.0.12 (January 26. 2020):**

* FEATURE IMPROVEMENT: Moved the code to Java 8.
* FEATURE IMPROVEMENT: Made the JavaDoc compiler work on Java 9 and newer.

----

**Changes in JSparklines 1.0.11 (July 18. 2019):**

* FEATURE IMPROVEMENT: Added an empty default constructor to the XYDataPoint class (needed by PeptideShaker).

----

**Changes in JSparklines 1.0.10 (June 18. 2019):**

* FEATURE IMPROVEMENT: The font colors for the ChromosomeTableCellRenderer are no longer hardcoded
* BUG FIX: Fixed a bug in the JSparklinesMultiIntervalChartTableCellRenderer where the reference line could not be hidden.

----

**Changes in JSparklines 1.0.9 (March 31. 2017):**

* FEATURE IMPROVEMENT: Minor JavaDoc corrections.

----

**Changes in JSparklines 1.0.8 (March 15. 2016):**

 * NEW FEATURE: Added a table cell renderer displaying JSparklinesDataSeries as heat maps where the double values are used for the color coding.

----

**Changes in JSparklines 1.0.7 (February 5. 2016):**

 * FEATURE IMPROVEMENT: Made the chromosome class more generic, now any string can be used as input.

----

**Changes in JSparklines 1.0.6 (September 12. 2015):**

 * FEATURE IMPROVEMENT: Added a method for returning the data sorting type for ArrayListDataPoints objects.

----

**Changes in JSparklines 1.0.5 (July 15. 2015):**

 * FEATURE IMPROVEMENT: The compareTo method for JSparklinesDataset now uses the summed absolute values and also checks against NaN values.

----

**Changes in JSparklines 1.0.4 (September 8. 2014):**

 * BUG FIX: Fixed a bug in the NimbusCheckBoxRenderer.

----

**Changes in JSparklines 1.0.3 (September 6. 2014):**

 * FEATURE IMPROVEMENT: Added checks for incorrect input, e.g., if the lower range is set higher than the upper range.
 * FEATURE IMPROVEMENT: Improved the way the list of supported object types for the renderers is listed in the JavaDoc.
 * FEATURE IMPROVEMENT: JavaDoc as HTML is now deployed as part of 'mvn deploy'.
 * FEATURE IMPROVEMENT: Added Unit tests for the data package.

 * BUG FIX: Fixed bugs where Byte objects were not correctly supported in some of the renderers.

----

**Changes in JSparklines 1.0.2 (September 3. 2014):**

 * FEATURE IMPROVEMENT: Updated and unified the JavaDoc, and made it available here  [http://genesis.ugent.be/maven2/no/uib/jsparklines/javadoc/](http://genesis.ugent.be/maven2/no/uib/jsparklines/javadoc/).

----

**Changes in JSparklines 1.0.1 (July 29. 2014):**

 * FEATURE IMPROVEMENT: Changed the annotation of multiple indexes in JSparklinesMultiIntervalChartTableCellRenderer from "x2" to "2x", etc.
 * BUG FIX: Fixed an issue in the way non supported object types did not have the correct background color in JSparklinesMultiIntervalChartTableCellRenderer.

----

**Changes in JSparklines 1.0.0 (July 27. 2014):**

 * FEATURE IMPROVEMENT: Changed the look and feel to Nimbus for the demos and removed the gradient background color.

----

**Changes in JSparklines 0.8.0 (July 22. 2014):**

 * FEATURE IMPROVEMENT: JSparklinesErrorBarChartTableCellRenderer: Added support for indicating significance.
 * FEATURE IMPROVEMENT: JSparklinesErrorBarChartTableCellRenderer: Added support for displaying the mean value and the chart.

----

**Changes in JSparklines 0.7.0 (July 10. 2014):**

 * FEATURE IMPROVEMENT: Added the option to use gradient color coding also when all values are positive. (The first color of the gradient is used for values close to the min value, while the third color of the gradient is used for values close to the max value. The middle gradient color is used for the halfway point between the min and max values.)
 * FEATURE IMPROVEMENT: Added support for gradient color in the JSparklinesErrorBarChartTableCellRenderer.
 * FEATURE IMPROVEMENT: Made it possible to set the width of the error bar in the JSparklinesErrorBarChartTableCellRenderer.
 * BUG FIX: Fixed a bug in the gradient color coding where the colors too quickly ended up as too dark.

----

**Changes in JSparklines 0.6.7 (May 12. 2014):**

 * FEATURE IMPROVEMENT: Added the option to control the sorting in the ArrrayListDataPoints class: first numbers, sum or sum except last number.

----

**Changes in JSparklines 0.6.6 (April 25. 2014):**

 * FEATURE IMPROVEMENT: Extended the options for which value to display in the table for the JSparklinesArrayListBarChartTableCellRenderer (firstNumberOnly, sumOfNumbers, sumExceptLastNumber).
 * FEATURE IMPROVEMENT: The tooltip in JSparklinesArrayListBarChartTableCellRenderer now uses the same number formatting as the value displayed in the table.

----

**Changes in JSparklines 0.6.5 (February 1. 2014):**
 * FEATURE IMPROVEMENT: Added a new ArrrayListDataPoints object for use in the JSparklinesArrayListBarChartTableCellRenderer, such that the array list can now be sorted based on the sum of the values in the lists. Note that ArrrayListDataPoints is now the only supported type for JSparklinesArrayListBarChartTableCellRenderer.

----

**Changes in JSparklines 0.6.4 (December 11. 2013):**
 * NEW FEATURE: Added a new JSparklinesArrayListBarChartTableCellRenderer, identical to JSparklinesTwoValueBarChartTableCellRenderer but supporting more than just two values.
 * BUG FIX: Fixed typos in some method names in JSparklinesTwoValueBarChartTableCellRenderer.

----

**Changes in JSparklines 0.6.3 (October 9. 2013):**
 * FEATURE IMPROVEMENT: Made many of the classes in the no.uib.jsparklines.data package serializable.

----

**Changes in JSparklines 0.6.2 (July 11. 2013):**
 * NEW FEATURE: Added a new integer to icon table cell renderer.
 * NEW FEATURE: Added a first draft of a ChromosomeTableCellRenderer.
 * FEATURE IMPROVEMENT: The cell renderers now support string objects.
 * BUG FIX: Fixed issues detected using FindBugs, plus corrected JavaDoc typos.

----

**Changes in JSparklines 0.5.45 (January 20. 2013):**
 * NEW FEATURE: Added a log scaling option to the JSparklinesBarChartTableCellRenderer.
 * FEATURE IMPROVEMENT: Added getter methods for the max/min values for JSparklinesBarChartTableCellRenderer and JSparklinesTwoValueBarChartTableCellRenderer.
 * FEATURE IMPROVEMENT: Added getter and setter methods for the color and tooltip maps for JSparklinesIntegerColorTableCellRenderer.
 * FEATURE IMPROVEMENT: Fixed an issue in JSparklinesIntervalChartTableCellRenderer where empty intervals (min = max) resulted in an exception being thrown. Now only intervals where the min value is larger than the max value throw an exception.
 * FEATURE IMPROVEMENT: Added a toString method to the StartIndexes object listing the indexes.

Download Count: 73

----

**Changes in JSparklines 0.5.41 (October 14. 2012):**
 * NEW FEATURE: Added a new JSparklinesMultiIntervalChartTableCellRenderer making it possible to show multiple markers in the same interval chart.
 * NEW FEATURE: Added a ChartPanel table cell renderer making it possible to put any chart panel into a cell.
 * NEW FEATURE: Added a line border when the heat map option in JSparklinesBarChartTableCellRenderer is used, making it easier to see which rows/cells that are selected.
 * NEW FEATURE: Added experimental JXTable support in JSparklinesBarChartTableCellRenderer.
 * BUG FIX: Fixed an issue in JSparklinesMultiIntervalChartTableCellRenderer that could result in an ArrayOutOfBoundsException if a single value (or no values) were provided instead of the expected multiple values.
 * FEATURE IMPROVEMENT: Maven 3 is now fully supported.

Download Count: 20

----

**Changes in JSparklines 0.5.35 (March 2. 2012):**
 * Made it possible to hide the reference line when using the proteinSequence plot type in the JSparklinesTableCellRenderer.
 *  Added a new JSparklinesTwoValueBarChartTableCellRenderer that displays an XYDataPoint as a two colored stacked bar chart.
 * Added the option of adding a fill color to the JSparklinesTwoValueBarChartTableCellRenderer.
 * Made it possible to add a reference line in the middle of the plots for the JSparklinesIntervalChartTableCellRenderer.
 * Fixed some bugs in the JSparklinesIntervalChartTableCellRenderer for when integer values was used, resulting in a casting exceptions.
 * Removed the hard coded white Nimbus selected foreground color for JSparklinesIntervalChartTableCellRenderer.
 * Added a pie chart version to the JSparklinesMultiLabelTableCellRenderer.

Download Count: 54

----

**Changes in JSparklines 0.5.30 (December 29. 2011):**
 * Extended the TrueFalseIconRenderer with icon and tooltip for null values.
 *Extended the JSparklinesBarChartTableCellRenderer with the option of adding a value and a boolean value (a ValueAndBooleanDataPoint object) used for the significance color coding.
 * Added a new jsparkline type: multi labels, where 1-4 labels can be colored coded and displayed in the same cell.
 * Fixed a bug in the JSparklinesIntervalChartTableCellRenderer where a color object was sometimes set to null resulting in strange side effects.
 * In the JSparklinesIntervalChartTableCellRenderer if the float or double value equals -1 it is now shown as N/A.
 * Added a CellHighlighterRenderer that makes it possible to highlight cells ending with a given string.
 * Removed that hardcoded selected cell chart color (white) for the Nimbus look and feel for JSparklinesBarChartTableCellRenderer and JSparklinesErrorBarChartTableCellRenderer.
 * Minor JavaDoc corrections.
 * Added a new stackedBarChartIntegerWithUpperRange option to JSparklinesTableCellRenderer.
 * JSparklinesDataset now implements Comparable.

Download Count: 5

----

**Changes in JSparklines 0.5.22 (October 28. 2011):**
 * Added a simple Color cell renderer displaying the color as a box instead of having to fill the whole cell.
 * In JSparklinesIntervalChartTableCellRenderer the tooltip values are now shown as integers if the input values are integers, and the input type used is XYDataPoint or XYDataPoint[].
 * Fixed a bug in HtmlLinksRenderer that resulted in a null pointer if the cell contained a null object.
 * Added toString methods to all JSparklines data types.

Download Count: 10

----

**Changes in JSparklines 0.5.18 (August 13. 2011):**
 * Added a new protein sequence plotting type to the JSparklinesTableCellRenderer.
 * Added a new area difference cell renderer that displays the information using one color for positive values and one color for negative values.
 * Made it possible to override the default background color in the JSparklinesTableCellRenderer.
 * Made it possible to set the decimal format for the JSparklinesBarChartTableCellRenderer when showing the numbers and the bar.

Download Count: 15

----

**Changes in JSparklines 0.5.15 (July 18. 2011):**
 * Added a simple renderer that makes it possible to use different HTML tag colors for selected vs not selected rows. For example the default blue font color can be used for the not selected rows, while a white font color can be used for the selected rows.
 * Added the possibility of adding tooltips based on the integer value to the JSparklinesIntegerColorTableCellRenderer.
 * Added a new constructor to the JSparklinesIntervalChartTableCellRenderer making it possible to now use XYDataPoint values in the cells. The X value is then assumed to be the lower range of the interval and the Y values is assumed to be the upper range.
 * Added the possibility of adding tooltips to the TrueFalseIconRenderer.
 * Added a new renderer displaying bar charts with error bars.
 * Fixed a minor Nimbus GUI bug.
 * Made it possible to use a list of XYDataPoints as input to the JSparklinesIntervalChartTableCellRenderer.

Download Count: 2

----

**Changes in JSparklines 0.5.8 (April 19. 2011):**
 * Added a new interval marker cell renderer. Similar to bar charts, but instead of a bar, only an interval around the top of the bar is shown.

Download Count: 10

----

**Changes in JSparklines 0.5.7 (April 7. 2011):**
 * Added a new table cell render displaying integers as color coded equal sized bar charts.
 * Fixed a minor bug with the background color for the NimbusCheckBoxRenderer.

Download Count: 5

----

**Changes in JSparklines 0.5.5 (March 18. 2011):**
 * Added a cell renderer for check boxes when using Nimbus with alternating row colors. This is needed to get the correct background color due to a bug in Nimbus.
 * Fixed a bug in the horizontal text alignment in the label when showing both the number and the sparkline.

Download Count: 3

----

**Changes in JSparklines 0.5.3 (March 3. 2011):**
 * Fixed some issues related to alternating row color coding.

Download Count: 1

----

**Changes in JSparklines 0.5.2 (March 2. 2011):**
 * Fixed various issues related to background color coding when using JSparklines in tables using the Nimbus look and feel with alternating row colors and bar charts. 
 * Improved the formatting of the numbers when displaying both the values and the bar charts.

Download Count: 2

----

**Changes in JSparklines 0.5.1 (March 1. 2011):**
 * Found and fixed a casting bug in JSparklinesBarChartTableCellRenderer that occurred when using XYDataPoint objects.

Download Count: 1

----

**Changes in JSparklines 0.5.0 (February 19. 2011):**
 * Made it possible to display the numbers _and_ the bar charts.
 * Added gradient color coding options to the bar charts.
 * Added a heat map table cell renderer.
 * Made it possible to use different lines styles in line plots.

Download Count: 6

----

**Changes in JSparklines 0.4.0 (February 10. 2011):**
 * Added an additional data type to the JSparklinesBarChartTableCellRenderer, XYDataPoint, making it possible to use significance color coding in addition to the up/down regulated colors.
 * Added default bar chart colors and additional constructors.
 * Added a bar chart renderer for statistical bar charts, similar to BarChartColorRenderer.

Download Count: 2

----

**Changes in JSparklines 0.3.0 (January 15. 2011):**
 * Added support for scatter and bubble plots. 
 * Removed unnecessary padding to the left and right of the plots.
 * Minor JavaDoc updates and code cleanups.

Download Count: 3

----

**Changes in JSparklines 0.2.0 (January 10. 2011):**
 * Added pie charts, stacked bar charts, stacked bar charts as percent, area charts, box plots, and up/down charts to the list of supported charts.
 * Each JSparklinesDataSeries is now given a label by the user, which are then used in the tooltip for the plot.
 * Reference lines and areas can now be added to the charts.

Download Count: 2

----

**Changes in JSparklines 0.1.2 (January 1. 2011):**
 * Null values are now supported in the JSparklinesBarChartTableCellRenderer. Also made it possible to set minimum chart value to display and when to use more than 2 decimals for the tooltips.

Download Count: 2

----

**Changes in JSparklines 0.1.1 (December 28. 2010):**
 * Added constructors making it possible to set the line chart line width. Changed the default line width from 20 to 5.

Download Count: 1

----

**Changes in JSparklines 0.1.0 (December 27. 2010):**
 *  The first public release of JSparklines!

Download Count: 1

----