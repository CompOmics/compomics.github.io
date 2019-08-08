---
title: PeptideMapperCLI
layout: default
permalink: /projects/compomics-utilities/wiki/PeptideMapperCLI
tags: wiki, compomics-utilities
project: compomics-utilities
github_project: https://github.com/compomics/compomics-utilities
---

# PeptideMapperCLI
# PeptideMapperCLI - PeptideMapper Command Line Interface #

[PeptideMapper](https://github.com/compomics/compomics-utilities/wiki/PeptideMapper) can be used to map sequences and sequence tags to a database of protein sequences. This wiki page describes its command line usage.

  * [Command Line](#command-line)
  * [Supported Formats](#supported-formats)
  * [Example](#example)

---

## Command Line ##

[PeptideMapper](https://github.com/compomics/compomics-utilities/wiki/PeptideMapper) is distributed in the compomics-utilities package. PeptideMapperCLI can be run from the utilities jar file as detailed below.

```java
java -cp utilities-X.Y.Z.jar com.compomics.util.experiment.identification.protein_inference.executable.PeptideMapping -[p|t] <InputFasta> <InputList> <OutputResultList> [<UtilitiesParameterFile>]
```

Please replace _X.Y.Z_ by the version used, _e.g._ 4.7.2.

### Options ###

| Option                 | Value        | Description                                                                    |
| ---------------------- |:------------:| ------------------------------------------------------------------------------ |
| p\|t                   | p or t       | Type of mapping, _p_ for peptide sequences, _t_ for sequence tags. (Mandatory) |
| InputFasta             | Path to File | Path to a FASTA file containing the protein sequences. (Mandatory)             |
| InputList              | Path to File | Path to a file containing the input sequences or tags.                         |
| OutputResultList       | Path to File | Path to a file where to store the result of the mapping.                       |
| UtilitiesParameterFile | Path to File | Path to a file containing the identification parameters.                       |

## Supported Formats ##

### Protein Sequence database ###
PeptideMapper supports protein sequence databases in the [FASTA format](http://en.wikipedia.org/wiki/FASTA_format). In a FASTA file each sequence is represented by a header and the sequence itself. The header contains information about the protein, e.g., protein accession number, database and species. However, the format of the header varies from database to database. [PeptideMapper](https://github.com/compomics/compomics-utilities/wiki/PeptideMapper) supports the most encountered databases like UniProt, Ensembl, NextProt, NCBI and IPI, plus a long list of other databases. For home made databases we recommend our [generic FASTA format](https://github.com/compomics/searchgui/wiki/DatabaseHelp#non-standard-fasta).

### Peptide Sequences ###

Peptide sequences should be provided in a text file, one sequence per line.

```
QAERYDDMASAMK
NEPLSNEER
ANQIEYYFVS
...
```

### Sequence Tags ###

Sequence tags should be provided in a text file, one tag per line, with the tag components separated by a comma.

```
211.521,LLQ,358.521
421.115,GAEM,97.555
85.455,YS,854.265
502.596,SGLTR,142.503
...
```

### Parameters File ###

The parameters file should be in the json format. Parameters files can be generated using the [IdentificationParametersCLI](https://github.com/compomics/compomics-utilities/wiki/IdentificationParametersCLI).

## Example ##

Example to map a peptide list to a FASTA file:

```java
java -cp utilities-X.Y.Z.jar com.compomics.util.experiment.identification.protein_inference.executable.PeptideMapping -p exampleFiles/PeptideMapping/yeast.fasta exampleFiles/PeptideMapping/yeast-pep-1k.csv result-file.csv
```