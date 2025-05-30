---
title: "Manual"
layout: default
permalink: "/projects/pride-asa-pipeline/wiki/Manual"
tags: wiki, pride-asa-pipeline
project: "pride-asa-pipeline"
github_project: "https://github.com/CompOmics/pride-asa-pipeline"
---

# Manual

  * [In a nutshell](#in-a-netshell)
  * [Configuration](#configuration)
  * [Output](#output)
  * [Command line mode](#command-line-mode)
  * [GUI mode](#gui-mode)
  * [Use pride-asap as Maven dependency](#use-pride-asap-as-maven-dependency)

## In a nutshell
For a given experiment, identifications and spectra are retrieved from the PRIDE public MySQL database or a PRIDE xml file and processed into three categories, with `Δm` the mass difference between the experimental and theoretical precursor mass:

  * _unmodified_: `Δm` is smaller than the systematic mass error.
  * _modified_: `Δm` can be fitted to a combination of modification masses, so the precursor carries likely one or more PTMs.   
  * _unexplained_: `Δm` is significant but can’t be explained by a modification combination.  

Before the evaluation of the mass difference `Δm`, a systematic mass error and error window are calculated per charge state in a recalibration step. If not enough identifications were found for a given charge state, a default systematic mass error and the annotated instrument precursor mass error are used instead.    

The peptide sequences are then matched to the corresponding spectra after adaptive noise filtering, and a score is derived for each peptide-to-spectrum match. In this step, the instrument fragment mass error is taken as the fragment ion mass deviation. The final output of the tool consists of the complete list of annotated identifications and spectra, and the list of modifications used to explain the observed precursor mass deviations in that experiment.

## Configuration
The pipeline configuration files can be found in the _resources_ folder. These files can be edited by the user if necessary. If no files are found in the _resources_ directory, default values will be used instead. Note that the pipeline can be configured in GUI mode (_Edit_ -> _Configuration_) as well. 

### pride_asa_pipeline.properties
Most of the parameter values in this file should be left to their default values. The settings that the user might need the change are listed below

  * `results_path`: the path on the file system where the pipeline result files will be stored.
  * `spectrumannotator.include_pride_modifications`: include the modifications in found in PRIDE for a given experiment. Note that setting this parameter to `true` can increase the processing time. The modifications defined in the pipeline ([pride_asap_modifications.xml](#pride_asap_modificationsxml)) are always taken into account.  
  * `modification.use_monoisotopic_mass`: use the monoisotopic or the average mass for the PTMs.
  * `pipeline.considered_charge_states`: the considered charge states for a precursor.
  * `massrecalibrator.maximum_systematic_mass_error`: the threshold systematic mass error value. The systematic mass errors (per charge state) as result of a recalibration step are checked against this value.
  * `massrecalibrator.mass_delta_threshold`: only identifications with a lower `Δm` are taken into account for the recalibration step.  
  * `massrecalibrator.minimum_peptide_count`: the minimum number of identifications per charge state used for the recalibration. Else the analyzer instrument default values are used.

### pride_asap_modifications.xml
This XML file contains the modifications used to explain a possible difference between the experimental and theoretical precursor mass. It can be edited or replaced (_Edit_ -> _Modifications_ in GUI mode) by a modifications result file. The accompanying XML schema can be found in the [here](http://genesis.ugent.be/uvpublicdata/pride-asa-pipeline/modifications.xsd). 

As mentioned before, this fixed set of pipeline modifications can be complemented with modifications found in PRIDE for the experiment of interest. In [GUI mode](#gui-mode), a dialog is shown if one or more PRIDE modifications have a similar mass compared to the pipeline PTMs.
## Output
The pipeline produces two result files. The first one (_\<experiment accession\>_.txt) contains the fragment ion annotations for each identified spectrum. The second one (_\<experiment accession\>_\_mods.txt) contains the subset of modifications that could actually explain a precursor mass deviation. These files can be imported (back) into the GUI for further analysis. Please note that for the moment, result files from processed PRIDE xml experiments can be imported, but the identifications details can't be explored.

In case of an unexpected error, the log file (pride-asa-pipeline.log) can be found in the _user_ root folder.

## Command line mode
Execute the following command in the folder where the pipeline _.jar_ file is located:

```
java -jar pride-asa-pipeline-<version>.jar [-a <accession> | -f <experiment_accessions_file_path> | -p <pride_xml_file_path> | -s <pride_xml_paths_file_path>] [-u] [-h]
```

Using argument `-a` followed by a PRIDE experiment accession annotates one experiment, whereas `-f` followed by the path of a _.txt_ file containing one or more experiment accessions (line separated) annotates multiple experiments sequentially. `-p` annotates the PRIDE xml file specified in the following path, while `-s` followed by the path of a _.txt_ file containing one or more PRIDE XML file paths (line separated) annotates multiple experiments sequentially. Arguments `-h` and `-u` give more information about the available command line parameters.

## GUI mode
Run the pipeline in GUI mode by double clicking the _.jar_ file. The GUI consists of three parts, described in the following.

### Pipeline panel

*Experiment selection*

On the main panel, an experiment can be selected from the publicly available PRIDE experiments. If the experiment contains no useful identifications, a message is shown. While processing a given experiment, two dialogs might pop up:

  * Systematic mass error dialog: one or more systematic mass errors exceed the threshold value. The user can decide to proceed or not.
  * Conflicting modifications dialog: The conflicting PRIDE modifications are shown on the left, the pipeline modifications and non-conflicting PRIDE modifications on the right. The user can include or exclude PRIDE modifications in this dialog. The pipeline modifications can be edited in the [modifications dialog](#modifications-dialog). Note that the pipeline can handle equal mass modifications, although they increase the processing time significantly. 

A PRIDE xml file can be ran through the pipeline in the _PRIDE XML_ tab. 

In the _Pipeline Result File_ tab, a result file from an already processed experiment can be loaded.

*Pipeline result*

In the _Summary_ tab, some descriptive graphs are shown.In the _Identifications_ tab, all identifications are listed. Clicking on an identifaction shows the annotated spectrum.

### Configuration dialog
The pipeline settings described in the [Configuration section](#configuration) can be viewed and modified in this dialog. The user is able to restore the default settings by clicking the _reset_ button. Saving the current settings will write the parameter values to the `pride_asa_pipeline.properties` file in the _resources_ folder.

### Modifications dialog
In this dialog, the user can add, modify and delete modifications. As mentioned before, a modifications XML file can be imported as well. In case of validation error against the schema, an error dialog will be shown.

## Use pride-asap as Maven dependency
Include the following dependency

```
    <dependency>
        <groupId>com.compomics</groupId>
        <artifactId>pride-asa-pipeline</artifactId>
        <version>X.Y.Z</version>
    </dependency>
```

and the following repositories in your _pom.xml_ file:

```
    <repositories>                   
        <repository>
            <id>genesis-maven2-repo</id>
            <name>Genesis maven2 repository</name>
            <url>http://genesis.UGent.be/maven2</url>
            <layout>default</layout>
        </repository>
        <repository>
            <id>genesis-maven-repo</id>
            <name>Genesis maven repository</name>
            <url>http://genesis.UGent.be/maven</url>
            <layout>default</layout>
        </repository>                
    </repositories>
```

This project uses the _Spring_ framework for depency injection, so the _application context_ needs to be loaded, e.g.:

```
import com.compomics.pride_asa_pipeline.spring.ApplicationContextProvider;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import com.compomics.pride_asa_pipeline.logic.PrideSpectrumAnnotator;

//set the default application context
ApplicationContextProvider.getInstance().setDefaultApplicationContext();
ApplicationContext applicationContext = ApplicationContextProvider.getInstance().getApplicationContext();

DbSpectrumAnnotator dbSpectrumAnnotator = applicationContext.getBean("dbSpectrumAnnotator", DbSpectrumAnnotator.class);
//annotate the first PRIDE experiment
dbSpectrumAnnotator.annotate("1"); 
```

The two _Spring_ configuration files (`springXMLConfig.xml` and `guiSpringXMLConfig.xml`) can be found in the `scr\main\resources` folder.