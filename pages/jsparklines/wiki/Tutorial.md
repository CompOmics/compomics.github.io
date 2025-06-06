---
title: "Tutorial"
layout: default
permalink: "/projects/jsparklines/wiki/Tutorial"
tags: wiki, jsparklines
project: "jsparklines"
github_project: "https://github.com/CompOmics/jsparklines"
---

# Tutorial [ ](# )

----

Using **JSparklines** is very easy and only requires a couple of lines of code. Below you will find simple code examples of how to use **JSparklines** in your project.

 * [Demos](#demos)
 * [Single Values](#single-values)
 * [Multiple Values](#multiple-values)
 * [Multiple Data Series](#multiple-data-series)
 * [2D and 3D Data Series](#2d-and-3d-data-series)
 * [Reference Lines and Areas](#reference-lines-and-areas)
 * [Heat Maps](#heat-maps)

 * [Maven Dependency](#maven-dependency)

For the complete source code see the **JSparklines** [Demos](#demos) found with the source code. See also the [http://genesis.ugent.be/maven2/no/uib/jsparklines/javadoc](JavaDoc).

----

## Demos

To run the main demo, double click the file `jsparklines-X.Y.Z.jar`, or use: `java -jar jsparklines-X.Y.Z.jar`.

**Note:** Remember to first unzip the downloaded zip file before trying to run the demos.

[Go to top of page](# )

----


## Single Values

When displaying single numeric values in a column the simplest option is to use the JSparklinesBarChartTableCellRenderer. This renderer can be used on any table column containing most numeric objects as follows:

```java
singleValuesJTable.getColumn("Fold Change").setCellRenderer(
    new JSparklinesBarChartTableCellRenderer(
        PlotOrientation.HORIZONTAL,             // orientation of the plot
        -5.0,                                   // lower range for the plot
        5.0,                                    // upper range for the plot
        negativeColor,                          // color to use for the negative values
        positiveColor));                        // color to use for the positive values
```


If the column only contains positive numbers it becomes even simpler:

```java
singleValuesJTable.getColumn("Coverage").setCellRenderer(
    new JSparklinesBarChartTableCellRenderer(
        PlotOrientation.HORIZONTAL,             // orientation of the plot
        100.0,                                  // upper range for the plot
        positiveColor));                        // color to use for the positive values
```

This effectively sets the lower range to zero.

**Using Color Gradients**

Turn on color gradient:

```java
((JSparklinesBarChartTableCellRenderer) singleValuesJTable.getColumn(
    "Peptides").getCellRenderer()).setGradientColoring(ColorGradient.BlueWhiteGreen, false);
```

Turn off color gradient:

```java
((JSparklinesBarChartTableCellRenderer) singleValuesJTable.getColumn(
    "Peptides").getCellRenderer()).setGradientColoring(null, false);
```

**Show Numbers and Chart**

```java
((JSparklinesBarChartTableCellRenderer) singleValuesJTable.getColumn(
    "Peptides").getCellRenderer()).showNumberAndChart(true, 40);
```


**Notes:**

 * **Note** that when using **JSparklines** in this way the underlying values can be edited as normal by double clicking the cell to edit.
 * **Note** that it is possible to change the maximum and minimum values later by using the setMaxValue(...) and setMinValue(...) methods in the renderer.
 * **Note** that the underlying values can be shown by using the showNumbers(...) method.

[Go to top of page](# )

----

## Multiple Values

When displaying multiple values in a single plot one has to use the JSparklinesTableCellRenderer. In this case the values to be plotted first has to be added to a JSparklineDataset, and this object then added to the table cell.

```java
// add the data points to display to an arraylist
ArrayList<Double> dataA = new ArrayList<Double>();

dataA.add(new Double(2.4));
dataA.add(new Double(4.1));
...
dataA.add(new Double(1.3));

// create a JSparklineDataSeries 
JSparklinesDataSeries sparklineDataseriesA = new JSparklinesDataSeries(
    dataA, Color.DARK_GRAY, "Dataset A");

// add the data series to JSparklineDataset
ArrayList<JSparklinesDataSeries> sparkLineDataSeriesAll = new ArrayList<JSparklinesDataSeries>();
sparkLineDataSeriesAll.add(sparklineDataseriesA);

JSparklinesDataset dataset = new JSparklinesDataset(sparkLineDataSeriesAll);

// add the data to the table
((DefaultTableModel) multipleValuesJTable.getModel()).addRow(new Object[]{"Protein " + (j + 1), dataset});

// set the JSparklines renderer
multipleValuesJTable.getColumn("Change").setCellRenderer(
    new JSparklinesTableCellRenderer(
        JSparklinesTableCellRenderer.PlotType.lineChart,   // plot type
        PlotOrientation.VERTICAL,                          // plot orientation
        0.0,                                               // lower plot range
        maxValue));                                        // upper plot range
```

**Notes:**

 * **Note** that cells with **JSparklines** with multiple values are NOT editable, so please set columns using **JSparklines** non-editable.
 * **Note** that the chart type, the maximum and minimum values, the line width for line charts etc can be change later by using the methods setPlotType(...), setMaxValue(...), setMinValue(...), setLineWidth(...), etc, methods in JSparklinesTableCellRenderer.
 * **Note** To change the plotting type simply change the JSparklinesTableCellRenderer.PlotType value.

[Go to top of page](# )

----

## Multiple Data Series

Displaying more than one data series is also very simple with **JSparklines**. Simply add multiple JSparklineDataSeries to the JSparklineDataset:

```java
// add the data points for the first data series
ArrayList<Double> dataA = new ArrayList<Double>();

dataA.add(new Double(2.4));
dataA.add(new Double(4.1));
...
dataA.add(new Double(1.3));

// create a JSparklineDataSeries 
JSparklinesDataSeries sparklineDataseriesA = new JSparklinesDataSeries(dataA, Color.RED, "Dataset A");


// add the data points for the second data series
ArrayList<Double> dataB = new ArrayList<Double>();

dataB.add(new Double(2.4));
dataB.add(new Double(4.1));
...
dataB.add(new Double(1.3));

// create a JSparklineDataSeries 
JSparklinesDataSeries sparklineDataseriesB = new JSparklinesDataSeries(dataB, Color.BLUE, "Dataset B");


// add the data series to JSparklineDataset
ArrayList<JSparklinesDataSeries> sparkLineDataSeriesAll = new ArrayList<JSparklinesDataSeries>();
sparkLineDataSeriesAll.add(sparklineDataseriesA);
sparkLineDataSeriesAll.add(sparklineDataseriesB);

JSparklinesDataset dataset = new JSparklinesDataset(sparkLineDataSeriesAll);


// add the data to the table
((DefaultTableModel) multipleDataSeriesJTable.getModel()).addRow(new Object[]{"Protein " + (j + 1), dataset});


// set the JSparklines renderer
multipleDataSeriesJTable.getColumn("Change").setCellRenderer(
    new JSparklinesTableCellRenderer(
        JSparklinesTableCellRenderer.PlotType.barChart,    // plot type
        PlotOrientation.VERTICAL,                          // plot orientation
        0.0,                                               // lower plot range
        maxValue));                                        // upper plot range
```

**Notes:**

 * **Note** that cells with **JSparklines** with multiple values are NOT editable, so please set columns using **JSparklines** non-editable.
 * **Note** that the chart type, the maximum and minimum values, the line width for line charts etc can be change later by using the methods setPlotType(...), setMaxValue(...), setMinValue(...), setLineWidth(...), etc, in JSparklinesTableCellRenderer.

[Go to top of page](# )

----

### 2D and 3D Data Series

When plotting 2D or 3D data use the JSparklines3dTableCellRenderer instead of the standard JSparklinesTableCellRenderer, and the JSparklines3dDataset instead of the JSparklinesDataset.

```java
// add the 2D/3D data points to display to an arraylist
ArrayList<XYZDataPoint> dataA = new ArrayList<XYZDataPoint>();

dataA.add(new XYZDataPoint(2.4, 3.4, 2.7));
dataA.add(new XYZDataPoint(5.8, 2.7, 8.2));
...
dataA.add(new XYZDataPoint(6.2, 6.3, 1.1));

// create a JSparkline3dDataSeries
JSparklines3dDataSeries sparkline3dDataseriesA = new JSparklines3dDataSeries(
    dataA, Color.DARK_GRAY, "Dataset A");

// add the data series to JSparkline3dDataset
ArrayList<JSparklines3dDataSeries> sparkLine3dDataSeriesAll = new ArrayList<JSparklines3dDataSeries>();
sparkLine3dDataSeriesAll.add(sparkline3dDataseriesA);

JSparklines3dDataset dataset = new JSparklines3dDataset(sparkLine3dDataSeriesAll);

// add the data to the table
((DefaultTableModel) 3dValuesJTable.getModel()).addRow(new Object[]{"Protein " + (j + 1), dataset});

// set the JSparklines 3D renderer
3dValuesJTable.getColumn("Spread").setCellRenderer(new JSparklines3dTableCellRenderer(
    JSparklines3dTableCellRenderer.PlotType.bubblePlot, // plot type
    -10d,                                               // x lower
    100d,                                               // x upper
    -10d,                                               // y lower
    110d));                                             // y upper
```

**Notes:**

 * **Note** that cells with **JSparklines** with 2D/3D values are NOT editable, so please set columns using **JSparklines** non-editable.
 * **Note** that the chart type, the maximum and minimum values, etc can be change later by using the methods setPlotType(...), setMaxXValue(...), setMinXValue(...), etc, in JSparklines3dTableCellRenderer.

[Go to top of page](# )

----

## Reference Lines and Areas

Often it can be helpful to add reference lines or areas to the charts to make them easier to compare. In **JSparklines** this is very easy:

```java

    // get the JSparklines cell renderer
    JSparklinesTableCellRenderer tempRenderer = ((JSparklinesTableCellRenderer) multipleValuesJTable.getColumn(
    "My Column").getCellRenderer());
    
    // add the reference
    tempRenderer.addReferenceArea(
        "My Reference",               // the reference label
        4,                            // the start value
        6,                            // the end value
        Color.LIGHT_GRAY,             // the color to use
        0.5f);                        // the alpha level

    // repaint the chart
    myJTable.revalidate();
    myJTable.repaint();

```

Removing the reference is equally straightforward:

```java
    // get the JSparklines cell renderer
    JSparklinesTableCellRenderer tempRenderer = ((JSparklinesTableCellRenderer) multipleValuesJTable.getColumn(
    "My Column").getCellRenderer());

    // remove the reference
    tempRenderer.removeReferenceArea("My Reference");
```

To add a line reference instead if an area reference, simply use the addReferenceLine(...) method instead.

**Note:** For 2D/3D plots use addXAxisReferenceLine(...), removeXAxisReferenceLine(...), etc, to add or remove reference lines and areas.

[Go to top of page](# )

----

## Heat Maps

There are two ways to create heat maps using **JSparklines**, either by using the JSparklinesBarChartTableCellRenderer and use the showAsHeatMap method, or by using the JSparklinesBubbleHeatMapTableCellRenderer. In both cases the numbers are added to the Java table as normal, and the renderer is then used for all columns in the table.

Various color gradient options are available.

Heat map using JSparklinesBarChartTableCellRenderer:

```java
for (int i = 0; i < heatmapJTable.getColumnCount(); i++) {
    heatmapJTable.getColumn(
        heatmapJTable.getColumnName(i)).setCellRenderer(
            new JSparklinesBarChartTableCellRenderer(
                PlotOrientation.HORIZONTAL, 
                -100d, 100d));
    ((JSparklinesBarChartTableCellRenderer) heatmapJTable.getColumn(
        heatmapJTable.getColumnName(i)).getCellRenderer()).showAsHeatMap(
        ColorGradient.RedBlackGreen);
}
```

Heat map using JSparklinesBubbleHeatMapTableCellRenderer:

```java
for (int i = 0; i < heatmapJTable.getColumnCount(); i++) {
    heatmapJTable.getColumn(
        heatmapJTable.getColumnName(i)).setCellRenderer(
            new JSparklinesBubbleHeatMapTableCellRenderer(
            100d, ColorGradient.RedBlackGreen));
}
```

Setting the background color for the heat maps:

Black:

```java
heatmapJTable.setGridColor(Color.BLACK);
heatmapJTable.setBackground(Color.BLACK);
heatmapJTable.setOpaque(true);
heatmapJTable.setForeground(Color.WHITE);
```

White:

```java
heatmapJTable.setGridColor(Color.WHITE);
heatmapJTable.setBackground(Color.WHITE);
heatmapJTable.setOpaque(true);
heatmapJTable.setForeground(Color.BLACK);
```

Change the color gradient:

```java
for (int i = 0; i < heatmapJTable.getColumnCount(); i++) {
    ((JSparklinesBarChartTableCellRenderer) heatmapJTable.getColumn(
        heatmapJTable.getColumnName(i)).getCellRenderer()).
            setGradientColoring(colorGradient);
}
```

Same for the JSparklinesBubbleHeatMapTableCellRenderer.

For a complete demo of how to use the heat maps see the `JSparklinesHeatMapDemo` class in the `no.uib.jsparklines` package.

[Go to top of page](# )

----

## Maven Dependency 

**JSparklines** is available for use in Maven projects:

```java
<dependency>
    <groupId>no.uib</groupId>
    <artifactId>jsparklines</artifactId>
    <version>X.Y.Z</version>
</dependency>
```
```java
<repository>
    <id>genesis-maven2-repository</id>
    <name>Genesis maven2 repository</name>
    <url>https://genesis.UGent.be/maven2</url>
</repository>
```

Update the version number to latest released version.

[Go to top of page](# )

----