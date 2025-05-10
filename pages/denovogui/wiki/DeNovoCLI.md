---
title: "DeNovoCLI"
layout: default
permalink: "/projects/denovogui/wiki/DeNovoCLI"
tags: wiki, denovogui
project: "denovogui"
github_project: "https://github.com/CompOmics/denovogui"
---

# DeNovoCLI

# DeNovoGUI Command Line Interface #

The command line interface to DeNovoGUI, referred to as DeNovoCLI, makes is easy to use DeNovoGUI in a command line setting, for example as part of a bigger software pipeline.

DeNovoCLI takes a set of spectrum files as input and uses the [PepNovo+](http://proteomics.ucsd.edu/Software/PepNovo.html),  [DirecTag](http://fenchurch.mc.vanderbilt.edu/bumbershoot/directag/), [pNovo+](http://pfind.ict.ac.cn/software/pNovo/) (beta) and [Novor](http://rapidnovor.com) algorithms to de novo sequence each spectrum according to the given search parameters.

Note that the spectra must be provided in the Mascot Generic File (mgf) format.

The recommended way to generate an identification parameters file is via the DeNovoGUI graphical user interface. But the file can also be created using the [IdentificationParametersCLI](/projects/denovogui/wiki/IdentificationParametersCLI). The folders used in the processing can be set via [PathSettingsCLI](#pathsettingscli).

**General command line:**

```java
java -cp DeNovoGUI-X.Y.Z.jar com.compomics.denovogui.cmd.DeNovoCLI [parameters]
```

**Mandatory parameters:**

```
-spectrum_files          Spectrum files (mgf format), comma separated list or an entire folder.
                         Example: "file1.mgf, file2.mgf".

-output_folder           The output folder.

-id_params               A search parameters file. Generated from the GUI 
                         or using the IdentificationParametersCLI.
```

**Optional common parameters:**

```
-pepnovo                Turn the PepNovo+ sequencing on or off. 
                        (1: on, 0: off, default is '1')

-directag               Turn the DirecTag sequencing on or off. 
                        (1: on, 0: off, default is '1')

-pnovo                  Turn the pNovo+ sequencing on or off.
                        (1: on, 0: off, default is '0') 

-novor                  Turn the Novor sequencing on or off.
                        (1: on, 0: off, default is '0') 
```

**Optional advanced parameters:**

```
-pep_novo_folder        The folder where PepNovo+ is installed. 
                        Defaults to the version provided with DeNovoGUI.

-directag_folder        The folder where DirecTag is installed. 
                        Defaults to the version provided with DeNovoGUI.

-pnovo_folder           The folder where pNovo+ is installed. 
                        Defaults to the version provided with DeNovoGUI.

-novor_folder           The folder where Novor is installed. 
                        Defaults to the version provided with DeNovoGUI.

-threads                The number of threads to use for the processing. 
                        Default is the number of cores available.
```

[Go to top of page](#denovocli)

---

## PathSettingsCLI ##

**Standard command line**

```java
java -cp DeNovoGUI-X.Y.Z.jar com.compomics.denovogui.cmd.PathSettingsCLI [parameters]
```

**Generic temporary folder**

```
-temp_folder               A folder for temporary file storage. Use only if 
                           you encounter problems with the default configuration.

-log                       Folder where to write the log files.
```

**Specific path setting**

```
-denovogui_matches_directory  
                           Folder where identification matches are temporarily saved to reduce the memory footprint.

-utilities_user_preferences
                           Folder containing the compomics utilities user preferences file.

-ptm_configuration         Folder containing the PTM user preferences file.

-fasta_indexes             Folder containing the indexes of the protein sequences databases.

-gene_mapping              Folder containing the gene mapping files.

-pride_annotation          Folder containing the PRIDE annotation preferences.
```

[Go to top of page](#denovocli)

---

## Comma Separated List ##

When using comma separated lists as input for the mgf files or the PTMs, please pay attention to the quotes required. Surround the full content of the option in quotes and not the individual items:

```java
-spectrum_files "C:\..\file_1.mgf, C:\..\file_2.mgf"

-variable_mods "oxidation of m, phosphorylation of s"
```

[Go to top of page](#denovocli)

---

## Examples ##

Here is an example for Windows using a search parameters file. _X_, _Y_ and _Z_ have to be replaced by the actual version of DeNovoGUI and _my folder_ by the folder containing the desired files:

```java
java -cp DeNovoGUI-X.Y.Z.jar com.compomics.denovogui.cmd.DeNovoCLI 
-spectrum_files "C:/my_folder" 
-output_folder "C:/my_folder/output"
-search_params "C:/my_folder/DeNovoGUI.parameters" 
```

_Note that for readability the commands are here split over multiple lines. When used the commands should of course be single lines._

[Go to top of page](#denovocli)

---

## Help ##

If you experience any problems with the command line or have any suggestion please contact us via the [DeNovoGUI mailing list](https://groups.google.com/group/denovogui).

[Go to top of page](#denovocli)