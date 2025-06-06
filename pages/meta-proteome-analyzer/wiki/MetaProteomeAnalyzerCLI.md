---
title: "MetaProteomeAnalyzerCLI"
layout: default
permalink: "/projects/meta-proteome-analyzer/wiki/MetaProteomeAnalyzerCLI"
tags: wiki, meta-proteome-analyzer
project: "meta-proteome-analyzer"
github_project: "https://github.com/CompOmics/meta-proteome-analyzer"
---

# MetaProteomeAnalyzerCLI

# MPA Command Line Interface #

The command line interface (CLI) for the MetaProteomeAnalyzer (MPA), referred to as MetaProteomeAnalyzerCLI, can be used to execute the MPA software in a command line setting, for example for the use on a Linux server or as part of another software pipeline/workflow.

MetaProteomeAnalyzerCLI takes one or multiple spectrum files as input and uses X!Tandem, Comet and MS-GF+ algorithms to perform database searching according to the given search parameters. In addition, MPA features several post-processing steps, such as FDR estimation, protein hit grouping (so-called metaprotein generation), taxonomic and functional analysis.

Please note that MS/MS spectra must be provided in Mascot Generic File (MGF) and protein sequence databases in FASTA format.

**Java command line execution:**

```java
java -cp mpa-portable-X.Y.Z.jar de.mpa.cli.CmdLineInterface [parameters]
```

**Mandatory parameters:**

```
-spectrum_files          Spectrum files (MGF format), comma separated list for multiple files. Example: "file1.mgf, file2.mgf".
-database                FASTA database file against which is searched.
-missed_cleav            The number of maximum allowed missed cleavages.
-prec_tol                The precursor tolerance (in Dalton, e.g. 0.5Da or PPM, e.g. 10ppm).
-frag_tol                The fragment ion tolerance (in Dalton, e.g. 0.5Da).
-output_folder           The output folder for exporting the processed results.

```

**Optional parameters:**

```
-xtandem                Turn database search algorithm X!Tandem on or off (1: on, 0: off, default is '1').
-comet                  Turn database search algorithm Comet on or off (1: on, 0: off, default is '0').
-msgf                   Turn database search algorithm MS-GF+ on or off (1: on, 0: off, default is '0'). 
-generate_metaproteins  Turn meta-protein generation (aka. protein grouping) on or off (1: on, 0: off, default is '1').
-peptide_rule           The peptide rule chosen for meta-protein generation (-1: off, 0: share-one-peptide, 1: shared-peptide-subset, default is '0').
-cluster_rule           The sequence cluster rule chosen for meta-protein generation (-1: off, 0: UniRef100, 1: UniRef90, 2: UniRef50, default is '-1').
-taxonomy_rule          The taxonomy rule chosen for meta-protein generation (-1: off, 0: on superkingdom or lower, 1: on kingdom or lower, 2: on phylum or lower, 3: on class or lower, 4: on order or lower, 5: on family or lower, 6: on genus or lower, 7: on species or lower, 8: on subspecies, default is '-1').
-iterative_search       Turn iterative (aka. two-step) searching on or off (-1: off, 0: Protein-based, 1: Taxon-based, default is '-1')
-fragment_method        The fragmentation method chosen for the MS instrument (1: CID, 2: HCD, 3: ETD, default is '1' - CID).
-peptide_index          Turn peptide indexing (of FASTA database) on or off (1: on, 0: off, default is '1').
-fdr_threshold          The applied FDR threshold for filtering the results (default is 0.05 == 5% FDR).
-threads                The number of threads to use for the processing (default is the number of cores available).
```


**Conda command line execution:**

```
mpa-portable de.mpa.cli.CmdLineInterface [parameters]
```

Please note that MPA Portable must have been previously installed as conda package using the bioconda channel:

```
conda install mpa-portable -c bioconda 
```

[Go to top of page](#metaproteomeanalyzercli)

---

## Comma Separated List ##

When using comma separated lists as input for the mgf files please pay attention to the quotes required. Surround the full content of the option in quotes and not the individual items:

```java
-spectrum_files "C:\..\file_1.mgf, C:\..\file_2.mgf" [other parameters]

```

[Go to top of page](#metaproteomeanalyzercli)

---

## Examples ##

Here is a minimum working example for the Windows operating system. _X_, _Y_ and _Z_ have to be replaced by the actual version of MetaProteomeAnalyzer (portable) software and _my folder_ by the folder containing the desired files:

```java
java -cp mpa-portable-X.Y.Z.jar de.mpa.cli.CmdLineInterface 
-spectrum_files C:\my_folder\spectrum_file.mgf 
-database C:\my_folder\uniprot_sprot.fasta
-missed_cleav 1 
-prec_tol 10ppm 
-frag_tol 0.5Da
-output_folder C:\my_folder\output

```

_For sake of readability, the input parameters are split over multiple lines. When using the command line, however, all parameters should be included as single line._

Here is an extended example for the Linux operating system featuring all optional parameters explicitely.
In this setup, X!Tandem, Comet and MS-GF+ are employed (using 8 threads) for protein identification, iterative searching is turned off, an FDR threshold of 1% is applied and proteins are grouped based on the meta-protein rule of requiring a single shared peptide. Both taxonomy and cluster rule are turned off.
```java
java -cp mpa-portable-X.Y.Z.jar de.mpa.cli.CmdLineInterface 
-spectrum_files /home/my_folder/spectrum_file.mgf 
-database /home/my_folder/uniprot_sprot.fasta
-missed_cleav 1 
-prec_tol 10ppm 
-frag_tol 0.5Da
-xtandem 1 
-comet 1 
-msgf 1 
-iterative_search 0 
-fdr_threshold 0.01 
-generate_metaproteins 1 
-peptide_rule 0 
-cluster_rule -1 
-taxonomy_rule -1 
-threads 8
-output_folder /home/my_folder/output/

```

[Go to top of page](#metaproteomeanalyzercli)