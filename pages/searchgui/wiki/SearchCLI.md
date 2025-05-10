---
title: "SearchCLI"
layout: default
permalink: "/projects/searchgui/wiki/SearchCLI"
tags: wiki, searchgui
project: "searchgui"
github_project: "https://github.com/CompOmics/searchgui"
---

# SearchCLI [ ](# )

## SearchGUI Command Line Interface

The command line interface to SearchGUI, referred to as SearchCLI, makes it possible to run all search engines and _de novo_ algorithms supported by SearchGUI using a single command line.

SearchCLI searches spectrum files according to search parameters using [X! Tandem](http://www.thegpm.org/tandem), [MyriMatch](http://forge.fenchurch.mc.vanderbilt.edu/scm/viewvc.php/*checkout*/trunk/doc/index.html?root=myrimatch), [MS Amanda](http://ms.imp.ac.at/?goto=msamanda), [MS-GF+](https://github.com/MSGFPlus/msgfplus), [OMSSA](http://www.ncbi.nlm.nih.gov/pubmed/15473683), [Comet](http://comet-ms.sourceforge.net/), [Tide](http://cruxtoolkit.sourceforge.net), [Andromeda](http://www.andromeda-search.org), [MetaMorpheus](https://github.com/smith-chem-wisc/MetaMorpheus), [Sage](https://github.com/lazear/sage), [Novor](http://rapidnovor.com) and [DirecTag](http://fenchurch.mc.vanderbilt.edu/bumbershoot/directag/).

Identification parameters for use in SearchCLI can be provided as a file. Identification parameter files are in the [json](https://en.wikipedia.org/wiki/JSON) format and can be created in the graphical user interface, using the [IdentificationParametersCLI](/projects/compomics-utilities/wiki/IdentificationParametersCLI), or using third party tools. Alternatively, the parameters can be passed directly to SearchCLI by using the command line arguments of the [IdentificationParametersCLI](/projects/compomics-utilities/wiki/IdentificationParametersCLI).

We recommend [redirecting temporary folders and logs](#pathsettingscli) when running SearchGUI on the command line. Please note that the search engines use indexes and temporary files stored locally in their folders. It is thus important to use a single instance of SearchCLI at a time. In distributed setups, we recommend keeping a clean copy of SearchGUI, and distribute it to the different workers prior to execution.

### General command line

```java
java -cp SearchGUI-X.Y.Z.jar eu.isas.searchgui.cmd.SearchCLI [parameters]
```

### Mandatory parameters

```java
-spectrum_files         Spectrum files (mgf or mzml), comma separated list or an entire folder.
                        Example: "c:\file1.mgf, c:\file2.mzml".

-fasta_file             The complete path to the FASTA file.

-output_folder          The output folder, example: "c:\output_folder".

-id_params              The identification parameters file (.par). 
                        Generated using the GUI or via IdentificationParametersCLI.
                        Example: "c:\search_parameters.par". 
                        Alternatively, IdentificationParametersCLI parameters can be passed directly.
```

### Optional common parameters

```java
-xtandem                Turn the X!Tandem search on or off. 
                        (1: on, 0: off, default is '0')

-myrimatch              Turn the MyriMatch search on or off. 
                        (1: on, 0: off, default is '0')

-ms_amanda              Turn the MS Amanda search on or off. 
                        (1: on, 0: off, default is '0')

-msgf                   Turn the MS-GF+ search on or off. 
                        (1: on, 0: off, default is '0')

-omssa                  Turn the OMSSA search on or off. 
                        (1: on, 0: off, default is '0')

-comet                  Turn the Comet search on or off. 
                        (1: on, 0: off, default is '0')

-tide                   Turn the Tide search on or off. 
                        (1: on, 0: off, default is '0')

-andromeda              Turn the Andromeda search on or off. 
                        (1: on, 0: off, default is '0')

-meta_morpheus          Turn the MetaMorpheus search on or off. 
                        (1: on, 0: off, default is '0')

-sage                   Turn the Sage search on or off. 
                        (1: on, 0: off, default is '0')

-novor                  Turn the Novor sequencing on or off. 
                        (1: on, 0: off, default is '0')

-directag               Turn the DirecTag sequencing on or off. 
                        (1: on, 0: off, default is '0')
```


### Optional advanced parameters

```java
-xtandem_folder         The folder where X!Tandem is installed, defaults                        
                        to the provided version for the given OS.

-myrimatch_folder       The folder where MyriMatch is installed, defaults                        
                        to the provided version for the given OS.

-ms_amanda_folder       The folder where MS Amanda is installed, defaults                        
                        to the provided version for the given OS.

-msgf_folder            The folder where MS-GF+ is installed.

-omssa_folder           The folder where OMSSA is installed, defaults                        
                        to the provided version for the given OS.

-comet_folder           The folder where Comet is installed, defaults                        
                        to the provided version for the given OS.

-tide_folder            The folder where Tide is installed, defaults                        
                        to the provided version for the given OS.

-tide_index_file        The file where the Tide index should be stored. 
                        If this option is provided and the index is found,
                        the creation of the index will be skipped. If this 
                        option is not provided, the index will always be
                        created and stored either in the Tide or the temp 
                        folder.

-andromeda_folder       The folder where Andromeda is installed, defaults                        
                        to the provided version for the given OS.

-meta_morpheus_folder   The folder where MetaMorpheus is installed, defaults                        
                        to the provided version for the given OS.

-sage_folder            The folder where Sage is installed, defaults                        
                        to the provided version for the given OS.

-novor_folder           The folder where Novor is installed, defaults                        
                        to the provided version for the given OS.

-directag_folder        The folder where DirecTag is installed, defaults                        
                        to the provided version for the given OS.

-makeblastdb_folder     The folder where makeblastdb is installed, defaults                        
                        to the provided version for the given OS.

-mgf_check_size         Turn the mgf size check on or off. 
                        0: off, 1: on, default is '0'.

-mgf_splitting          The maximum mgf file size in MB before 
                        splitting an mgf. Default is '1000'.
                        (See also MGF Splitting below.)

-mgf_spectrum_count     The maximum number of spectra per mgf file 
                        when splitting. Default is '25000'.

-correct_titles         Correct for duplicate spectrum titles. 
                        (0: no correction, 1: rename spectra, 
                         2: delete spectra, default is '1').

-missing_titles         Add missing spectrum titles. (From v1.19.0)
                        (0: no correction, 1: add missing spectrum titles, default is '0').

-threads                The number of threads to use for the processing. 
                        Default is the number of cores available.

-ref_mass               Reference mass for the conversion of the fragment ion tolerance 
                        from ppm to Dalton. Default is '2000'.
```

### Optional output compression parameters

```java
-output_default_name    Optional output default name, default is 'searchgui_out'.

-output_gzip            Gzip result files (0: no, 1: yes, default is '1').

-output_option          Optional result file compression:
                        0: Single zip file,
                        1: One zip file per mgf,
                        2: One zip file per algorithm,
                        3: No zipping,
                        default is '0'.

-output_data            Include mgf and FASTA in the zipped output 
                        (0: no, 1: yes, default is '0').

-output_date            Include date in zipped output name 
                        (0: no, 1: yes, default is '0').

-rename_xtandem         Turn the renaming of the X! Tandem files on/off.
                        0: off, 1: on, default is '1'.

-target_decoy_tag       The tag added after adding decoy sequences to a FASTA file. 
                        Default is '_concatenated_target_decoy'.
```

[Go to top of page](# )

----

## PathSettingsCLI

### Standard command line

```java
java -cp SearchGUI-X.Y.Z.jar eu.isas.searchgui.cmd.PathSettingsCLI [parameters]
```

### Generic temporary folder

```java
-temp_folder               A folder for temporary file storage. Use only if 
                           you encounter problems with the default configuration.

-log                       Folder where the log files are written.

-use_log_folder            Use the log folder. 0: write logs and errors to standard output, 
                           1: use the log folder. Default: 1.
```

### Specific path setting

```java
-search_engine_temp        Folder where search engine temporary files are stored.
                           (Note: does not work for Andromeda!)

-utilities_user_preferences         
                           Folder containing the compomics utilities user preferences file.

-ptm_configuration         Folder containing the PTM user preferences file.

-fasta_indexes             Folder containing the indexes of the protein sequences databases.

-gene_mapping              Folder containing the gene mapping files.

-pride_annotation          Folder containing the PRIDE annotation preferences.
```

[Go to top of page](# )

----

## Comma Separated List

When using comma separated lists as input for the mgf files please pay attention to the quotes required. Surround the full content of the option in quotes and not the individual items:

```java
-spectrum_files "C:\..\file_1.mgf, C:\..\file_2.mgf"
```

[Go to top of page](# )

----

## MGF Splitting

If the provided MGF files become too big it can result in memory issues for the search engines, e.g., OMSSA often struggles with files bigger than 1GB. SearchGUI therefore provides an option to split the MGF files. This option should only be used if you are experiencing memory issues with the search engines, as it is always best to search the complete MGF files in a single search. However, if a tool such as [PeptideShaker](http://compomics.github.io/projects/peptide-shaker.html) is used to combine the search results afterwards, the effects of the splitting should be minimal.

The list of MGF files used in the search (after splitting) is always listed in the file output_folder\searchGUI_input.txt. Please refer to this file when forwarding the SearchGUI search results to [PeptideShaker](http://compomics.github.io/projects/peptide-shaker.html).

## Examples

Here is an example for Windows using a search parameters file. _X_, _Y_ and _Z_ have to be replaced by the actual version of SearchGUI and _my folder_ by the folder containing the desired files:

```java
java -cp SearchGUI-X.Y.Z.jar eu.isas.searchgui.cmd.SearchCLI 
-spectrum_files "C:/my_folder" 
-output_folder "C:/my_folder/output"
-id_params "C:/my_folder/SearchGUI.parameters" 
```

_Note that for readability the commands are here split over multiple lines. When used the commands should of course be single lines._

[Go to top of page](# )

----

## FASTA File Handling

SearchGUI also has a separate FastaCLI command line for manipulating FASTA files.

### General command line

```java
java -cp SearchGUI-X.Y.Z.jar eu.isas.searchgui.cmd.FastaCLI [parameters]
```

### Mandatory parameters

```java
-in                     The FASTA file.
```

### Optional parameters

```java
-decoy	                Create a concatenated target/decoy database.

-decoy_suffix           Target decoy suffix, defaults to _concatenated_target_decoy.fasta.
```

### Generic temporary folder

```java
-temp_folder               A folder for temporary file storage. Use only if 
                           you encounter problems with the default configuration.

-log                       Folder where the log files are written.

-use_log_folder            Use the log folder. 0: write logs and errors to standard output, 
                           1: use the log folder. Default: 1.
```

The PathSettingsCLI options can also be used directly as options to FastaCLI. 

[Go to top of page](# )

----

## Help

If you experience any problems with the command line or have any suggestion please contact us via the [SearchGUI issue tracker](https://github.com/compomics/searchgui/issues).

[Go to top of page](# )