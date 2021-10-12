---
title: "IdentificationParametersCLI"
layout: default
permalink: "/projects/denovogui/wiki/IdentificationParametersCLI"
tags: wiki, denovogui
project: "denovogui"
github_project: "https://github.com/compomics/denovogui"
---

# IdentificationParametersCLI

# Identification Parameters Command Line Interface #

IdentificationParametersCLI can be used to create or edit an identification parameter file via the command line for use in [DeNovoGUI](http://compomics.github.io/projects/denovogui.html). Identification parameter files are in the [json](https://en.wikipedia.org/wiki/JSON) format and can also be created in the graphical user interface or using third party tools. Alternatively, the parameters can be created and edited directly in the command lines of [DeNovoGUI](http://compomics.github.io/projects/denovogui.html).

Note that most of the advanced settings and algorithm specific parameters listed below are for expert usage only. Changes from the default settings should be done with care.

  * [General command line](#general-command-line)
  * [General parameters](#general-parameters)
  * [Spectrum matching parameters](#spectrum-matching-parameters)
  * [Algorithm specific parameters](#general-parameters)
    * [PepNovo advanced parameters](#pepnovo-advanced-parameters)
    * [DirecTag advanced parameters](#directag-advanced-parameters)
    * [pNovo advanced parameters](#pnovo-advanced-parameters)
    * [Novor advanced parameters](#novor-advanced-parameters)
  * [Comma Separated List](#comma-separated-list)
  * [Help](#help)

---

## General command line ##

```java
java -cp DeNovoGUI-X.Y.Z.jar 
com.compomics.denovogui.cmd.IdentificationParametersCLI [parameters]
```

## General parameters ##

```
-out                      The destination Identification Parameters file (.par).

-id_params                An identification parameters file to modify (optional).

-mods                     Lists the available modifications.
                          "Name (Description)" is given for every modification.
                          Use the name for the setting of parameters.
```

## Spectrum matching parameters ##

```
-prec_tol                 Precursor ion mass tolerance, default is '10'.

-prec_ppm                 Precursor ion tolerance unit: ppm (1) or Da (0), default is '1'. 
                          (NB: Not supported for DeNovoGUI as here only Dalton is used.)

-frag_tol                 Fragment ion mass tolerance, default is '0.5'.

-frag_ppm                 Fragment ion tolerance unit: ppm (1) or Da (0), default is '0'. 
                          (NB: Not supported for DeNovoGUI as here only Dalton is used.)

-fixed_mods               Fixed modifications as comma separated list,
                          e.g., "Oxidation of M, Phosphorylation of S"
                          Note: case sensitive.

-variable_mods            Variable modifications as comma separated list,
                          e.g., "Oxidation of M, Phosphorylation of S"
                          Note: case sensitive.
```

## Algortithm Specific parameters ##

The following parameters allow controlling specific identification algorithms specifically.

## PepNovo advanced parameters ##

```
-pepnovo_hitlist_length   PepNovo+ number of de novo solutions [0-2000], default is '10'.

-pepnovo_estimate_charge  PepNovo+ estimate precursor charge option.
                          1: true, 0: false, default is '1'.

-pepnovo_correct_prec_mass
                          PepNovo+ correct precursor mass option.
                          1: true, 0: false, default is '1'.

-pepnovo_discard_spectra  PepNovo+ discard low quality spectra optoin.
                          1: true, 0: false, default is '1'.

-pepnovo_fragmentation_model
                          PepNovo+ fragmentation model, default is 'CID_IT_TRYP'.

-pepnovo_generate_blast   PepNovo+ generate a BLAST query.
                          1: true, 0: false, default is '0'.
```

## DirecTag advanced parameters ##

```
-directag_tic_cutoff      DirecTag TIC cutoff in percent, default is '85'.

-directag_max_peak_count  DirecTag max peak count, default is '400'.

-directag_intensity_classes
                          DirecTag number of intensity classses, default is '3'.

-directag_adjust_precursor
                          DirecTag adjust precursor, 1: true, 0: false, default is '0'.

-directag_min_adjustment  DirecTag minimum precursor adjustment, default is '-2.5'.

-directag_max_adjustment  DirecTag maximum precursor adjustment, default is '2.5'.

-directag_adjustment_step DirecTag precursor adjustment step, default is '0.1'.

-directag_charge_states   DirecTag number of charge states considered, default is '3'.

-directag_output_suffix   DirecTag output suffic, default is no suffix.

-directag_ms_charge_state DirecTag use charge state from M spectrum, 1: true, 0: false, default is '0'.

-directag_duplicate_spectra
                          DirecTag duplicate spectra per charge, 1: true, 0: false, default is '1'.

-directag_deisotoping     DirecTag deisotoping mode, default is '0', 0: no deisotoping, 
                          1: precursor only, 2: precursor and candidate.

-directag_isotope_tolerance
                          DirecTag isotope mz tolerance, default is '0.25'.

-directag_complement_tolerance
                          DirecTag complement mz tolerance, default is '0.5'.

-directag_tag_length      DirecTag tag length, default is '3'.

-directag_max_var_mods    DirecTag maximum variable modifications per sequence, default is '2'.

-directag_max_tag_count   DirecTag maximum tag count, default is '20'.

-directag_intensity_weight
                          DirecTag intensity score weight, default is '1.0'.

-directag_fidelity_weight DirecTag fidelity score weight, default is '1.0'.

-directag_complement_weight
                          DirecTag complement_score_weight, default is '1.0'.
```

## pNovo advanced parameters ##

```
-pnovo_num_peptides       pNovo+ number of peptides per spectrum, default is '10'.

-pnovo_lower_prec         pNovo+ minimum precursor mass, default is '300'.

-pnovo_upper_prec         pNovo+ maximum precursor mass, default is '5000'.

-pnovo_activation         pNovo+ actication type (HCD, CID or EDT), default is 'HCD'.
```

## Novor advanced parameters ##

```
-novor_fragmentation      Novor fragmentation method, CID or HCD, default is 'HCD'.

-novor_mass_analyzer      Novor mass analyzer, Trap, TOF, or FT, default is 'FT'.
```

---

## Comma Separated List ##

When using comma separated lists as input for the the PTMs, please pay attention to the quotes required. Surround the full content of the option in quotes and not the individual items:

```java
-variable_mods "Oxidation of M, Phosphorylation of S"
```

---

## Help ##

If you experience any problems with the command lines or have any suggestion please contact us via the [DeNovoGUI mailing list](http://groups.google.com/group/denovogui).