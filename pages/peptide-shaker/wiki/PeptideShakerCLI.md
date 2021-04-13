---
title: "PeptideShakerCLI"
layout: default
permalink: "/projects/peptide-shaker/wiki/PeptideShakerCLI"
tags: wiki, peptide-shaker
project: "peptide-shaker"
github_project: "https://github.com/compomics/peptide-shaker"
---

# PeptideShakerCLI

# PeptideShaker Command Line Interface #

The PeptideShaker command line interface can be used to process identification files and output identification results in various formats.

There are six main sections to this page:

  * [A) PeptideShakerCLI](#a---peptideshakercli) - data processing
  * [B) ReportCLI](#b---reportcli) - identification results exports
  * [C) FollowUpCLI](#c---followupcli) - export for follow up analysis
  * [D) MzidCLI](#d---mzidcli) - export as mzIdentML
  * [E) PathSettingsCLI](#e---pathsettingscli) - set the paths to use
  * [F) General](#f---general) - general command line help

Note that ReportCLI, FollowUpCLI, MzidCLI and PathSettingsCLI options can also be appended directly to PeptideShakerCLI command lines.

All command line options have the same overall structure and only differ in the features and parameters available.

Identification parameters for use in PeptideShakerCLI can be provided as a file. Identification parameter files are in the [json](https://en.wikipedia.org/wiki/JSON) format and can be created in the graphical user interface, using the [IdentificationParametersCLI](/projects/compomics-utilities/wiki/IdentificationParametersCLI), or using third party tools. Alternatively, the parameters can be passed directly to PeptideShakerCLI by using the command line arguments of the [IdentificationParametersCLI](/projects/compomics-utilities/wiki/IdentificationParametersCLI).

Temporary folders used in the processing can be set via [PathSettingsCLI](#pathsettingscli). Note that PeptideShaker back-end relies on a database allowing only a single open connection at a time. It is thus important to use a single instance of PeptideShakerCLI at a time. In distributed setups, we recommend keeping a clean copy of PeptideShaker, and distribute it to the different workers prior to execution.

---

## A - PeptideShakerCLI ##

**Standard command line**

```java
java -cp PeptideShaker-X.Y.Z.jar eu.isas.peptideshaker.cmd.PeptideShakerCLI [parameters]
```

**Mandatory parameters**

```
-reference                 The reference/name for the project.

-fasta_file (*)            The complete path to the FASTA file.

-identification_files      Identification files in a comma separated list, as compressed zip file, 
                           or an entire folder. Example: "c:\file1.omx, c:\file1.mzid, c:\file1.t.xml".

-spectrum_files (*)        The spectrum files (mgf or mzML format) in a comma separated list or an 
                           entire folder. Example: "c:\file1.mgf, c:\file2.mzml".

-id_params (*)             The identification parameters file (.par). 
                           Generated using the GUI or via IdentificationParametersCLI.
                           Example: "c:\search_parameters.par". 
                           Alternatively, IdentificationParametersCLI parameters can be passed directly.

(*) Not mandatory if these files are part of a zip file input with the identification files.
```

**Optional output parameters**

```
-out                       PeptideShaker output file (.psdb). If the file already exists 
                           it will be silently overwritten. Example: "c:\ps_output.psdb".

-zip                       Exports the entire project as a zip file in the file specified.

-output_mgf                When using zipped output, exports mgf file(s) out of the zip file 
                           into the same folder in addition. 0: no, 1: yes, default is '0'.
```

**Optional processing parameters**

```
-threads                   The number of threads to use. Defaults to the number of available CPUs.

-gui                       Use a dialog to display the progress (1: true, 0: false, default is '0').
```

**PeptideShakerCLI Example**

PeptideShakerCLI example where _X_, _Y_ and _Z_ have to be replaced by the actual version of PeptideShaker and _my folder_ by the folder containing the desired files:

```java
java -cp PeptideShaker-X.Y.Z.jar eu.isas.peptideshaker.cmd.PeptideShakerCLI 
-reference myReference -fasta_file "C:\my folder\my_data.fasta"
-identification_files "C:\my folder" -spectrum_files "C:\my folder" 
-id_params "C:\my folder\my_search_params.par" 
-out "C:\my folder\myCpsFile.psdb"
```

_Note that for readability the command is here split over multiple lines. When used the command should of course be a single line._

[Go to top of page](#peptideshakercli)

---

## B - ReportCLI ##

**Standard command line**

```java
java -cp PeptideShaker-X.Y.Z.jar eu.isas.peptideshaker.cmd.ReportCLI [parameters]
```

**Mandatory parameters**

```
-in                        PeptideShaker project (.psdb or zip file)

-out_reports               Output folder for report files. (Existing files will be overwritten.)
```

**Optional report options**

```
-reports                   Comma separated list of types of report to export. 
                           0: Certificate of Analysis, 
                           1: Default Hierarchical Report, 
                           2: Default PSM Phosphorylation Report, 
                           3: Default PSM Report, 
                           4: Default PSM Report with non-validated matches, 
                           5: Default Peptide Phosphorylation Report, 
                           6: Default Peptide Report, 
                           7: Default Peptide Report with non-validated matches, 
                           8: Default Protein Phosphorylation Report, 
                           9: Default Protein Report, 
                           10: Default Protein Report with non-validated matches, 
                           11: Extended PSM Report, 
                           12-n: Your own custom reports.

-report_prefix             Prefix added to the report file name.

-documentation             Comma separated list of types of report documentation to export. 
                           0: Certificate of Analysis, 
                           1: Default Hierarchical Report, 
                           2: Default PSM Phosphorylation Report, 
                           3: Default PSM Report, 
                           4: Default PSM Report with non-validated matches, 
                           5: Default Peptide Phosphorylation Report, 
                           6: Default Peptide Report, 
                           7: Default Peptide Report with non-validated matches, 
                           8: Default Protein Phosphorylation Report, 
                           9: Default Protein Report, 
                           10: Default Protein Report with non-validated matches, 
                           11: Extended PSM Report, 
                           12-n: Your own custom reports.
                           
-gzip                      Indicates whether the report should be compressed.
                           0: no, 1: yes, default is 0.
```

To add custom reports see Export > Identification Features > Reports in PeptideShaker.

**ReportCLI Example**

ReportCLI example where _X_, _Y_ and _Z_ have to be replaced by the actual version of PeptideShaker:

```java
java -cp PeptideShaker-X.Y.Z.jar eu.isas.peptideshaker.cmd.ReportCLI 
-in "C:\my folder\myCpsFile.psdb" -out_reports "C:\my folder" -reports "0, 3" -report_prefix "my_" -gzip 0
```

[Go to top of page](#peptideshakercli)

---

## C - FollowUpCLI ##

**Standard command line**

```java
java -cp PeptideShaker-X.Y.Z.jar eu.isas.peptideshaker.cmd.FollowUpCLI [parameters]
```

**Mandatory parameters**

```
-in                        PeptideShaker project (.psdb or zip file)
```

**Optional recalibration parameters**

```
-recalibration_folder      Output folder for the recalibrated files. (Existing files will be overwritten.)

-recalibration_mode        Recalibration type. 
                           0: precursor and fragment ions (default), 
                           1: precursor only, 
                           2: fragment ions only.
```

**Optional spectrum export parameters**

```
-spectrum_folder           Output folder for the spectra. (Existing files will be overwritten.)

-psm_type                  Type of PSMs. 
                           0: Spectra of Non-Validated PSMs (default),  
                           1: Spectra of Non-Validated Peptides, 
                           2: Spectra of Non-Validated Proteins, 
                           3: Spectra of Validated PSMs, 
                           4: Spectra of Validated PSMs of Validated Peptides, 
                           5: Spectra of validated PSMs of Validated Peptides of Validated Proteins.
```

**Optional Progenesis export parameters**

```
-progenesis_file           Output file for identification results in Progenesis LC-MS compatible format. 
                           (Existing files will be overwritten.)

-progenesis_type           Type of hits to export to Progenesis. 
                           0: Validated PSMs of Validated Peptides of Validated Proteins.
                           1: Validated PSMs of Validated Peptides, 
                           2: Validated PSMs,
                           3: Validated PSMs containing confidently localized PTMs.

-progenesis_ptms           Comma separated list of PTMs to include in reports of Type 3.
```

**Optional protein accessions export parameters**

```
-accessions_file           Output file to export the protein accessions in text format. 
                           (Existing files will be overwritten.)

-accessions_type           When exporting accessions, select a category of proteins. 
                           0: Main Accession of Validated Protein Groups (default),
                           1: All Accessions of Validated Protein Groups, 
                           2: Non-Validated Accessions.
```

**Optional protein sequences (in FASTA format) export parameters**

```
-sequences_file            File where to export the protein details in fasta format. 
                           (Existing files will be overwritten.)

-sequences_type            When exporting protein details, select a category of proteins. 
                           0: Main Accession of Validated Protein Groups (default), 
                           1: All Accessions of Validated Protein Groups, 
                           2: Non-Validated Accessions.
```

**Optional inclusion list generation parameters**

```
-inclusion_list_file       Output file for an inclusion list of validated hits. 
                           (Existing files will be overwritten.)

-inclusion_list_format     Format for the inclusion list. 
                           0: Thermo (default), 
                           1: ABI, 
                           2: Bruker, 
                           3: MassLynx.

-inclusion_list_peptide_filters     
                           Peptide filters to be used for the inclusion list export (comma separated). 
                           0: Miscleaved Peptides, 
                           1: Reactive Peptides, 
                           2: Degenerated Peptides.

-inclusion_list_protein_filters     
                           Protein inference filters to be used for the inclusion list export (comma separated). 
                           1: Related Proteins, 
                           2: Related and Unrelated Proteins, 
                           3: Unrelated Proteins.

-inclusion_list_rt_window  Retention time window for the inclusion list export (in seconds).
```

**Optional proteoforms parameters**

```
-proteoforms_file      Output file for the proteoforms. (Existing file will be overwritten.)
```

**FollowUpCLI Example**

FollowUpCLI example where _X_, _Y_ and _Z_ have to be replaced by the actual version of PeptideShaker and _my folder_ by the folder containing the desired files:

```java
java -cp PeptideShaker-X.Y.Z.jar eu.isas.peptideshaker.cmd.FollowUpCLI -in "C:\my folder\myCpsFile.psdb" -spectrum_folder "C:\my folder" -psm_type 0
```

[Go to top of page](#peptideshakercli)

---

## D - MzidCLI ##

**Standard command line**

```java
java -cp PeptideShaker-X.Y.Z.jar eu.isas.peptideshaker.cmd.MzidCLI [parameters]
```

**Mandatory parameters**

```
-in                        PeptideShaker project (.psdb or zip file)

-output_file               Output file.

-contact_first_name        Contact first name.

-contact_last_name         Contact last name.

-contact_email             Contact e-mail.

-contact_address           Contact address.

-organization_name         Organization name.

-organization_email        Organization e-mail.

-organization_address      Organization address.
```

**Optional parameters:**

```
-gzip                      Indicates whether the mzIdentML file should be compressed.
                           0: no, 1: yes, default is 0.

-contact_url               Contact URL.

-organization_url          Organization URL.   

-include_sequences         Include the protein sequences. 
                           1: true, 0: false, default is '0'.

-mzid_version              The version of the mzIdentML scheme to use. 
                           0: v1.1, 1: v1.2, default is '0'.
```

[Go to top of page](#peptideshakercli)

---

## E - PathSettingsCLI ##

**Standard command line**

```java
java -cp PeptideShaker-X.Y.Z.jar eu.isas.peptideshaker.cmd.PathSettingsCLI [parameters]
```

**Generic temporary folder**

```
-temp_folder               A folder for temporary file storage. Use only if 
                           you encounter problems with the default configuration.

-log                       Folder where the log files are written.

-use_log_folder            Use the log folder. 0: write to standard output, 
                           1: use the log folder. Default: 1.
```

**Specific path setting**

```
-peptideshaker_matches_directory    
                           Folder where identification matches are temporarily 
                           saved to reduce the memory footprint.

-peptideshaker_user_preferences     
                           Folder containing the PeptideShaker user preferences file.

-peptideshaker_exports     Folder containing the user custom exports file.

-utilities_user_preferences         
                           Folder containing the compomics utilities user preferences file.

-ptm_configuration         Folder containing the PTM user preferences file.

-fasta_indexes             Folder containing the indexes of the protein sequences databases.

-gene_mapping              Folder containing the gene mapping files.

-pride_annotation          Folder containing the PRIDE annotation preferences.
```

[Go to top of page](#peptideshakercli)

---

## F - General ##

**Comma Separated Lists**

When using comma separated lists as input please pay attention to the quotes required. Surround the full content of the option in quotes and not the individual items:

```java
-spectrum_files "C:\..\file_1.mgf, C:\..\file_2.mgf"
```

**Absolute Paths**

In general it is recommended to use absolute paths.

**Memory Settings**

Remember that big datasets require more than the default memory provided to the Java virtual machine, so for larger dataset please increase the maximum memory setting. Example, for a maximum of 2GB of memory:

```java
java -Xmx2048M -cp PeptideShaker-X.Y.Z.jar eu.isas.peptideshaker.cmd.PeptideShakerCLI [parameters]
```

See also: [JavaTroubleShooting](/projects/compomics-utilities/wiki/JavaTroubleShooting).

**Opening PeptideShaker Projects**

To open a PeptideShaker project (cps file or zipped cps file) from the command line (for display in PeptideShaker) use the following command:

```java
java -jar PeptideShaker-X.Y.Z.jar -cps "C:\my folder\myCpsFile.psdb"
```

To open a zipped PeptideShaker project via a URL from the command line (for display in PeptideShaker) use the following command:

```java
java -jar PeptideShaker-X.Y.Z.jar -zipUrl "http://my_url/PS.zip" -zipUrlFolder C:\my folder\"
```

**Opening a PX Accession for Reshaking**

To open a PX accession directly in the Reshake mode use:

```java
java -jar PeptideShaker-X.Y.Z.jar -pxAccession "yourPxAccesion"
```

To open private data use:

```java
java -jar PeptideShaker-X.Y.Z.jar -pxAccession "yourPxAccesion" -pxAccessionPrivate
```

**Help**

If you experience any problems with the command line or have any suggestion please contact us via the [PeptideShaker issue tracker](https://github.com/compomics/peptide-shaker/issues).

[Go to top of page](#peptideshakercli)