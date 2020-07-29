---
title: "fasta2speclib"
layout: default
permalink: "/projects/ms2pip_c/wiki/fasta2speclib"
tags: wiki, ms2pip_c
project: "ms2pip_c"
github_project: "https://github.com/compomics/ms2pip_c"
---

# fasta2speclib: generate MS²PIP-predicted spectral libraries

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Command line interface](#command-line-interface)
  - [Configuration file](#configuration-file)
  - [Modifications](#modifications)
  - [Example configuration file](#example-configuration-file)

---

## Introduction
The *fasta2speclib* pipeline allows you to generate an MS²PIP-predicted spectral
library, starting from a FASTA file. Multiple parameters to adjust the
comprehensiveness of the spectral library can be set in a JSON config file, such
as digestion enzyme, precursor charges, modifications... The pipeline also
allows you to easily create a predicted decoy spectral library (currently by
reversing digested peptide sequences). All information on the usage of
*fasta2speclib* and its parameters is listed below.

*fasta2speclib* can now add [DeepLC](/projects/DeepLC)-predicted
retention times to its spectral libraries! Just set `add_retention_time` to `true`
in the configuration file.

If you use *fasta2speclib* and MS²PIP
 for your research please cite:
>Gabriels, R., Martens, L., Degroeve, S. **Updated MS²PIP web server
delivers fast and accurate MS² peak intensity prediction for multiple
fragmentation methods, instruments and labeling techniques.** *Nucleic Acids
Research* (2019)  
[doi: 10.1093/nar/gkz299](https://doi.org/10.1093/nar/gkz299)

*fasta2speclib* was first described in:
>Van Puyvelde, B.\*, Willems, S.\*, Gabriels, R.\*, Daled, S., De Clerck, L.,
Staes, A., Impens, F., Deforce, D., Martens, L., Degroeve, S., Dhaenens, M.§.
**Removing the Hidden Data Dependency of DIA with Predicted Spectral
Libraries.** *Proteomics* (2020)  
[doi: 10.1002/pmic.201900306](https://doi.org/10.1002/pmic.201900306)

---

## Installation
fasta2speclib is installed alongside MS²PIP. See the
[MS²PIP README page](/projects/ms2pip_c#installation)
for installation instructions.

---

## Usage
### Command line interface
```
usage: fasta2speclib [-h] [-o OUTPUT_FILENAME] [-c CONFIG_FILENAME]
                     fasta_filename

Create an MS2PIP-predicted spectral library, starting from a fasta file.

positional arguments:
  fasta_filename      Path to the fasta file containing protein sequences

optional arguments:
  -h, --help          show this help message and exit
  -o OUTPUT_FILENAME  Name for output file(s) (if not given, derived from
                      input file)
  -c CONFIG_FILENAME  Name of configuration json file (default:
                      fasta2speclib_config.json)
```

### Configuration file
All *fasta2speclib* settings need to be set in a JSON config file (by default
`fasta2speclib_config.json`). It contains the following options:

Name | Description | Possible values | Default value | Data type
--- | --- | --- | --- | ---
`output_filetype` | Output file formats for spectral library | `msp`, `mgf`, `spectronaut`, `bibliospec` (also for Skyline) and/or `hdf` | `["msp"]` | array of strings
`charges` | Precusor charges to include | positive integer | `[2, 3]` | array of numbers
`min_peplen` | Minimum length of peptides to include | positive integer | `8` | number
`max_peplen` | Maximum length of peptides to include | positive integer | `30` | number
`missed_cleavages` | Number of missed cleavages to include | positive integer | `2` | number
`modifications` | Modifications to include. See below for more information | *see below* | modifications object | object
`ms2pip_model` | MS2PIP model to use for predictions | *see MS2PIPc documentation* | `"HCD"` | string
`decoy` | Also create decoy spectral library by reversing peptide sequences | `true`, `false` | `true` | boolean
`add_retention_time` | Add retention times using [DeepLC](/projects/DeepLC) | `true`, `false` | `true` | boolean
`elude_model_file` | If not null, predict retention times with this ELUDE model* | `path/to/model.file` or `null` | `null` | string or null
`peprec_filter` | If not null, do not predict spectra for peptides present in this peprec | `path/to/peprec.file` or `null` | `null` | string or null
`batch_size` | To reduce memory consumption, the (still unmodified) peptides to predict are split-up into batches. A higher batch size is slightly faster, but requires more RAM. | positive integer | `5000` | number 
`num_cpu` | Number of processes for multithreading | positive integer | `24` | number

*\* For this functionality, ELUDE needs to be installed and callable with the
command `elude`.*

### Modifications
Modified versions of peptides can be included in the predicted spectral library.
For this, an array of modification objects needs to be entered into the JSON
config file. Every modification needs the following parameters:

Name | Description | Type
--- | --- | ---
`name` | Name of the modifications, as it will appear in the output files. Using the PSI-MS modification names is recommended. | string
`unimod_accession` | UniMod accession number (required for ELUDE RT predictions). | number
`mass_shift` | Mass shift the modification introduces. | number
`amino_acid` | Amino acid on which the modification occurs. If the modification does not occur on a specific amino acid (e.g. N-terminal acetylation), this can be set to `null`. | string or null
`n_term` | If the modification only occurs on the N-terminus, set to `true`. This can be combined with a specifically set amino_acid (e.g. Glu->pyro-Glu only occurs on N-terminal glutamic acid). | boolean
`fixed` | Set to `true` if only the modified version of the peptide should be present in the spectral library (e.g. for Carbamidomethyl). | boolean

Please take the following into account:
- As is the case in the MS²PIP configuration, if a modification occurs on
multiple specific modifications (such as phosphorylation), a separate entry is
required, each with a unique name (e.g. PhosphoS, PhosphoT, and PhosphoY) for
every amino acid.
- If no modifications should be included in the spectral library, the
modifications object is an empty array (`[]`).
- C-terminal modifications are not yet supported!
- N-terminal modifications WITH specific first AA do not yet prevent other
modifications to be added on that first AA. This means that the function will,
for instance, combine Glu->pyro-Glu (combination of N-term and normal PTM) with
other PTMS for Glu on the first AA, while this is not possible in reality!

### Example configuration file
```json
{
    "output_filetype":["msp", "mgf", "bibliospec", "spectronaut", "hdf"],
    "charges":[2, 3],
    "min_peplen":8,
    "max_peplen":30,
    "missed_cleavages":2,
    "modifications":[
        {"name":"Glu->pyro-Glu", "unimod_accession":27, "mass_shift":-18.0153, "amino_acid":"E", "n_term":true, "fixed":false},
        {"name":"Gln->pyro-Glu", "unimod_accession":28, "mass_shift":-17.0305, "amino_acid":"Q", "n_term":true, "fixed":false},
        {"name":"Acetyl", "unimod_accession":1, "mass_shift":42.01057, "amino_acid":null, "n_term":true, "fixed":false},
        {"name":"Oxidation", "unimod_accession":35, "mass_shift":15.9994, "amino_acid":"M", "n_term":false, "fixed":false},
        {"name":"Carbamidomethyl", "unimod_accession":4, "mass_shift":57.0513, "amino_acid":"C", "n_term":false, "fixed":true}
    ],
    "ms2pip_model":"HCD",
    "decoy":true,
    "add_retention_time":true,
    "elude_model_file":null,
    "rt_predictions_file":null,
    "peprec_filter":null,
    "save_peprec":false,
    "batch_size":10000,
    "num_cpu":24
}
```
