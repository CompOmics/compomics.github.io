---
name: IdentificationParametersCLI
project: compomics-utilities
layout: default
permalink: /projects/compomics-utilities/wiki/identificationparameterscli.html
github_project: https://github.com/compomics/compomics-utilities
---

# IdentificationParametersCLI

# Identification Parameters Command Line Interface #

IdentificationParametersCLI can be used to create or edit an identification parameter file via command line, for use in tools like [SearchGUI](http://compomics.github.io/projects/searchgui.html), [PeptideMapper](/projects/compomics-utilities/wiki/peptidemapper.html), [DeNovoGUI](http://compomics.github.io/projects/denovogui.html) and [PeptideShaker](http://compomics.github.io/projects/peptide-shaker.html). Identification parameter files are in the [json](https://en.wikipedia.org/wiki/JSON) format and can also be created in the graphical user interface or using third party tools. Alternatively, the parameters can be created and edited directly in the command lines of [CompOmics-utilities](http://compomics.github.io/projects/compomics-utilities.html), [SearchGUI](http://compomics.github.io/projects/searchgui.html) and [PeptideShaker](http://compomics.github.io/projects/peptide-shaker.html).

Note that most of the advanced settings and algorithm specific parameters listed below are for expert usage only. Changes from the default settings should be done with care.

  * [General command lines](#general-command-lines)
  * [General parameters](#general-parameters)
  * [Spectrum matching parameters](#spectrum-matching-parameters)
  * [Advanced parameters](#advanced-parameters)
    * [Spectrum Annotation](#spectrum-annotation)
    * [Sequence Matching](#sequence-matching)
    * [Import Filters](#import-filters)
    * [PTM Localization](#ptm-localization)
    * [Gene Annotation](#gene-annotation)
    * [Protein Inference](#protein-inference)
    * [Validation Levels](#validation-levels)
    * [Fraction Analysis](#fraction-analysis)
  * [Algorithm specific parameters](#general-parameters)
    * [XTandem advanced parameters](#xtandem-advanced-parameters)
    * [MS-GF advanced parameters](#ms-gf-advanced-parameters)
    * [MS Amanda advanced parameters](#ms-amanda-advanced-parameters)
    * [OMSSA advanced parameters](#omssa-advanced-parameters)
    * [MyriMatch advanced parameters](#myrimatch-advanced-parameters)
    * [Comet advanced parameters](#comet-advanced-parameters)
    * [Tide advanced parameters](#tide-advanced-parameters)
    * [Andromeda advanced parameters](#andromeda-advanced-parameters)
    * [PepNovo advanced parameters](#pepnovo-advanced-parameters)
    * [DirecTag advanced parameters](#directag-advanced-parameters)
    * [pNovo advanced parameters](#pnovo-advanced-parameters)
    * [Novor advanced parameters](#novor-advanced-parameters)
  * [Comma Separated List](#comma-separated-list)
  * [Help](#help)

---

## General command lines ##

```java
java -cp utilities-X.Y.Z.jar 
com.compomics.cli.identification_parameters.IdentificationParametersCLI[parameters]
```

```java
java -cp SearchGUI-X.Y.Z.jar 
eu.isas.searchgui.cmd.IdentificationParametersCLI [parameters]
```

```java
java -cp PeptideShaker-X.Y.Z.jar 
eu.isas.peptideshaker.cmd.IdentificationParametersCLI [parameters]
```

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
-db                       The sequence database in FASTA format.

-prec_tol                 Precursor ion mass tolerance, default is '10'.

-prec_ppm                 Precursor ion tolerance unit: ppm (1) or Da (0), default is '1'. 
                          (NB: Not supported for DeNovoGUI as here only Dalton is used.)

-frag_tol                 Fragment ion mass tolerance, default is '0.5'.

-frag_ppm                 Fragment ion tolerance unit: ppm (1) or Da (0), default is '0'. 
                          (NB: Not supported for DeNovoGUI as here only Dalton is used.)

-digestion                The type of digestion to consider: 
                          0: Enzyme, 1: Unspecific or 2: Whole Protein. Default is 0.

-enzyme                   Enzyme, default is 'Trypsin'. 
                          Available enzymes are listed in the GUI.
                          Note: case sensitive.

-specificity              Specificity of the enzyme: 
                          0: Specific, 1: Semi-Specific, 2: N-term Specific or 3: C-term Specific
                          If more than one enzyme was used, please provide the missed cleavages for 
                          every enzyme in the same order as comma separated list with quotes, e.g. "0, 1"

-mc                       Number of allowed missed cleavages, default is '2'.

-fixed_mods               Fixed modifications as comma separated list,
                          e.g., "Oxidation of M, Phosphorylation of S"
                          Note: case sensitive.

-variable_mods            Variable modifications as comma separated list,
                          e.g., "Oxidation of M, Phosphorylation of S"
                          Note: case sensitive.

-min_charge               Minimal charge to search for, default is '2'.

-max_charge               Maximal charge to search for, default is '4'.

-fi                       Type of forward ion searched, default is 'b'.

-ri                       Type of rewind ion searched, default is 'y'.

-min_isotope              Minimum precursor isotope, default is '0'.

-max_isotope              Maximum precursor isotope, default is '1'.
```

## Advanced Parameters ##

The following parameters allow controlling the identification workflow in details. If not set, these settings will be inferred from the [Spectrum matching parameters](#spectrum-matching-parameters).

## Spectrum Annotation ##

```
-annotation_level         The intensity percentile to consider for annotation.
                          e.g. 0.75 means that the 25% most intense peaks will be annotated.
                          Default is 0.75.

-annotation_mz_tolerance  The m/z tolerance to annotate peaks, default is equal to the search settings MS2 tolerance.

-annotation_high_resolution    
                          If true the most accurate peak will be selected within the m/z tolerance.
                          1: true, 0: false, default is '1'.

```

## Sequence Matching ##

```
-sequence_index_type      The protein database index type. Default is 0.
                          0: FM-Index
                          1: Tree

-sequence_matching_type   The peptide to protein sequence matching type. Default is 2.
                          0: Character Sequence
                          1: Amino Acids
                          2: Indistinguishable Amino Acids

-sequence_matching_x      The maximal share of Xs in a sequence, 0.25 means 25% of Xs, default is 0.25.

```

## Import Filters ##

```
-import_peptide_length_min     
                          The minimal peptide length to consider when importing identification files, default is 8.

-import_peptide_length_max     
                          The maximal peptide length to consider when importing identification files, default is 30.

-import_missed_cleavages_min
                          The minimal number if missed cleavages to consider when importing identification files, default is no filter.

-import_missed_cleavages_max
                          The maximal number if missed cleavages to consider when importing identification files, default is no filter.

-import_precurosor_mz     The maximal precursor precursor deviation to allow when importing identification files, the precursor tolerance by default.

-import_precurosor_mz_ppm Maximal precursor ion deviation unit: ppm (1) or Da (0), default is '1'.

-exclude_unknown_ptms     If true peptides presenting unrecognized PTMs will be excluded.
                          1: true, 0: false, default is '1'.

```

## PTM Localization ##

```
-ptm_score                The PTM probabilistic score to use for PTM localization, default is 1.
                          0: A-score
                          1: PhosphoRS
                          2: None

-ptm_threshold            The threshold to use for the PTM scores. Automatic mode will be used if not set.
                          Default is automatic threshold.

-score_neutral_losses     Include neutral losses in spectrum annotation of the PTM score.
                          1: true, 0: false, default is '0'.

-ptm_sequence_matching_type    
                          The PTM to peptide sequence matching type. Default is 1.
                          0: Character Sequence
                          1: Amino Acids
                          2: Indistinguishable Amino Acids

-ptm_alignment            Align peptide ambiguously localized PTMs on confident sites.
                          1: true, 0: false, default is '1'.

```

## Gene Annotation ##

```
-useGeneMapping           If true gene mappings will be used and saved along with the project.
                          1: true, 0: false, default is '1'
                          Note: UniProt databases only.

-updateGeneMapping        If true gene mappings will be updated automatically from Ensembl.
                          1: true, 0: false, default is '1'
                          Note: UniProt databases only.

```

## Protein Inference ##

```
-db_pi                    The sequence database to use for protein inference in FASTA format.

-simplify_groups          Simplify protein groups.
                          1: true, 0: false, default is '1'.

-simplify_score           Simplify protein groups based on the PeptideShaker target/decoy score.
                          1: true, 0: false, default is '1'.

-simplify_enzymaticity    Simplify protein groups based on the peptide enzymaticity.
                          1: true, 0: false, default is '1'.

-simplify_evidence        Simplify protein groups based on the UniProt protein evidence.
                          1: true, 0: false, default is '1'.

-simplify_uncharacterized Simplify protein groups based on the protein characterization.
                          1: true, 0: false, default is '1'.

```

## Validation Levels ##

```
-psm_fdr                  FDR at the PSM level in percent, default is 1.

-peptide_fdr              FDR at the peptide level in percent, default is 1.

-protein_fdr              FDR at the protein level in percent, default is 1.

-group_psms               Group PSMs by charge for scoring and validation.
                          1: yes, 0: no, default is 1.

-group_peptides           Group peptides by modification status for scoring and validation.
                          1: yes, 0: no, default is 1.

-merge_subgroups          Merge small PSM and peptide groups for scoring and validation.
                          1: yes, 0: no, default is 1.

```

## Fraction Analysis ##

```
-protein_fraction_mw_confidence
                          Minimum confidence required for a protein in the fraction MW plot (default 95%: '95.0').

```

## Algortithm Specific parameters ##

The following parameters allow controlling specific identification algorithms specifically.

## XTandem advanced parameters ##

```
-xtandem_dynamic_range    X!Tandem 'spectrum, dynamic range' option, default is '100'.

-xtandem_npeaks           X!Tandem 'spectrum, total peaks' option, default is '50'.

-xtandem_min_frag_mz      X!Tandem 'spectrum, minimum fragment mz' option, default is '200'.

-xtandem_min_peaks        X!Tandem 'spectrum, minimum peaks' option, default is '15'.

-xtandem_noise_suppr      X!Tandem 'spectrum, use noise suppression' option.
                          1: true, 0: false, default is '0'.

-xtandem_min_prec_mass    X!Tandem 'spectrum, minimum parent m+h' option, default is '500'.

-xtandem_quick_acetyl     X!Tandem 'protein, quick acetyl' option.
                          1: true, 0: false, default is '1'.

-xtandem_quick_pyro       X!Tandem 'protein, quick pyrolidone' option.
                          1: true, 0: false, default is '1'.

-xtandem_stp_bias         X!Tandem 'protein, stP bias' option.
                          1: true, 0: false, default is '0'.

-xtandem_refine           X!Tandem 'refine' option.
                          1: true, 0: false, default is '1'.

-xtandem_refine_evalue    X!Tandem 'refine, maximum valid expectation value' option, default is '0.01'.

-xtandem_refine_unc       X!Tandem 'refine, unanticipated cleavage' option.
                          1: true, 0: false, default is '1'.

-xtandem_refine_semi      X!Tandem 'refine, cleavage semi' option.
                          1: true, 0: false, default is '0'.

-xtandem_refine_pot       X!Tandem 'refine, use potential modifications for full refinement' option. 
                          1: true, 0: false, default is '0'.

-xtandem_refine_p_mut     X!Tandem 'refine, point mutations' option.
                          1: true, 0: false, default is '0'.

-xtandem_refine_snaps     X!Tandem 'refine, saps' option.
                          1: true, 0: false, default is '1'.

-xtandem_refine_spec_synt X!Tandem 'refine, spectrum synthesis' option.
                          1: true, 0: false, default is '1'.

-xtandem_evalue           X!Tandem 'output, maximum valid expectation value' option, default is '0.01'.

-xtandem_output_results   X!Tandem 'output, results' option (all|valid|stochastic), default is 'all'.

-xtandem_output_proteins  X!Tandem 'output, proteins' option.
                          1: true, 0: false, default is '0'.

-xtandem_output_sequences X!Tandem 'output, sequences' option.
                          1: true, 0: false, default is '0'.

-xtandem_output_spectra   X!Tandem 'output, spectra' option.
                          1: true, 0: false, default is '0'.

-xtandem_skyline_path     X!Tandem 'spectrum, skyline path' option.
```

## MyriMatch advanced parameters ##

```
-myrimatch_min_pep_length MyriMatch minumum peptide length, default is '8'.

-myrimatch_max_pep_length MyriMatch maximum peptide length, default is '30'.

-myrimatch_min_prec_mass  MyriMatch minumum precursor mass, default is '0.0'.

-myrimatch_max_prec_mass  MyriMatch maximum precursor mass, default is '10000.0'.

-myrimatch_num_matches    MyriMatch maximum number of spectrum matches, default is '10'.

-myrimatch_num_ptms       MyriMatch max number of PTMs per peptide, default is '2'.

-myrimatch_fragmentation  MyriMatch fragmentation method, 
                          cid (b, y), etd (c, z*) 
                          or manual (a comma-separated list of [abcxyz] 
                          or z* (z+1), e.g. manual:b,y,z).

-myrimatch_termini        MyriMatch number of enzymatic termini, 
                          0: non-tryptic
                          1: semi-tryptic 
                          2: fully-tryptic
                          default is '2'.

-myrimatch_plus_three     MyriMatch smart plus three option, 
                          1: true, 0: false, default is '1'.

-myrimatch_xcorr          MyriMatch xcorr option.
                          1: true, 0: false, default is '0'.

-myrimatch_tic_cutoff     MyriMatch TIC cutoff percentage, default is '0.98'.

-myrimatch_intensity_classes
                          MyriMatch number of intensity classes, default is '3'.

-myrimatch_class_multiplier
                          MyriMatch class multiplier option, default is '2'.

-myrimatch_num_batches    MyriMatch number of batches option, default is '50'.

-myrimatch_max_peak       MyriMatch max peak count option, default is '100'.
```

## MS Amanda advanced parameters ##

```
-ms_amanda_decoy          MS Amanda generate decoys option.
                          0: false, 1: true, default is '0'.

-ms_amanda_instrument     MS Amanda instrument id option. Available enzymes are listed in the GUI. 
                          (Note: case sensitive.).

-ms_amanda_max_rank       MS Amanda maximum rank, default is '5'.

-ms_amanda_mono           MS Amanda use monoisotopic mass values.
                          0: false, 1: true, default is '1'.

-ms_low_mem_mode          MS Amanda use low memory mode option.
                          0: false, 1: true, default is '1'.
```

## MS-GF advanced parameters ##

```
-msgf_decoy               MS-GF+ search decoys option, 1: true, 0: false, default is '0'.

-msgf_instrument          MS-GF+ instrument id option, 
                          0: Low-res LCQ/LTQ, 
                          1: Orbitrap/FTICR, 2: TOF, 3: Q-Exactive (Default).

-msgf_fragmentation       MS-GF+ fragmentation id option, 
                          0: As written in the spectrum or CID if no info, 
                          1: CID, 2: ETD, 3: HCD, 4: UVPD.
                          Default is '3'.

-msgf_protocol            MS-GF+ protocol id option.
                          0: Automatic (Default)
                          1: Phosphorylation
                          2: iTRAQ
                          3: iTRAQPhospho
                          4: TMT
                          5: Standard

-msgf_min_pep_length      MS-GF+ minumum peptide length, default is '8'.

-msgf_max_pep_length      MS-GF+ maximum peptide length, default is '30'.

-msgf_num_matches         MS-GF+ maximum number of spectrum matches, default is '10'.

-msgf_additional          MS-GF+ additional features.
                          0: output basic scores only (Default)
                          1: output additional features

-msgf_termini             MS-GF+ number of tolerable termini.
                          0: non-tryptic
                          1: semi-tryptic
                          2: fully-tryptic
                          Default is '2'.

-msgf_num_ptms            MS-GF+ max number of PTMs per peptide, default is '2'.

-msgf_num_tasks           MS-GF+ number of tasks as an integer.
                          Default: internally calculated based on inputs.
```

## OMSSA advanced parameters ##

```
-omssa_memory             OMSSA map sequences in memory option.
                          1: true, 0: false, default is '1'.

-omssa_neutron            Mass after which OMSSA should consider neutron exact mass, default is '1446.94'.

-omssa_low_intensity      OMSSA low intensity cutoff as percentage of the most intense peak, default is '0.0'.

-omssa_high_intensity     OMSSA high intensity cutoff as percentage of the most intense peak, default is '0.2'.

-omssa_intensity_incr     OMSSA intensity increment, default is '0.0005'.

-omssa_single_window_wd   OMSSA single charge window width in Da, integer, default is '27'.

-omssa_double_window_wd   OMSSA double charge window width in Da, integer, default is '14'.

-omssa_single_window_pk   OMSSA single charge window number of peaks, integer, default is '2'.

-omssa_double_window_pk   OMSSA double charge window number of peaks, integer, default is '2'.

-omssa_min_ann_int_pks    OMSSA minimum number of annotated peaks among the most intense ones, integer, 
                          default is '6'.

-omssa_min_annotated_peaks
                          OMSSA minimum number of annotated peaks, integer, default is '2'.

-omssa_min_peaks          OMSSA minimum number of peaks, integer, default is '4'.

-omssa_methionine         OMSSA N-terminal methionine cleavage option.
                          1: true, 0: false, default is '1'.

-omssa_max_ladders        OMSSA maximum number of m/z ladders, integer, default is '128'.

-omssa_max_frag_charge    OMSSA maximum fragment charge, integer, default is '2'.

-omssa_fraction           OMSSA fraction of peaks to estimate charge 1, default is '0.95'.

-omssa_plus_one           OMSSA estimate plus one charge algorithmically option. 
                          1: true, 0: false, default is '1'.

-omssa_charge             OMSSA fragment charge option, 1: plus, 0: minus, default is '1'.

-omssa_prec_per_spectrum  OMSSA minimum number of precursors per spectrum, integer, default is '1'.

-omssa_forward            OMSSA include first forward ion (b1) in search.
                          1: true, 0: false, default is '0'.

-omssa_rewind             OMSSA search rewind (C-terminal) ions option.
                          1: true, 0: false, default is '1'.

-omssa_max_frag_series    OMSSA maximum fragment per series option, integer, default is '100'.

-omssa_corr               OMSSA use correlation correction score option.
                          1: true, 0: false, default is '1'.

-omssa_consecutive_p      OMSSA consecutive ion probability, default is '0.5'.

-omssa_it_sequence_evalue
                          OMSSA e-value cutoff to consider a sequence in the iterative search 0.0 means all.
                          Default is '0.0'.

-omssa_it_spectrum_evalue
                          OMSSA e-value cutoff to consider a spectrum in the iterative search 0.0 means all.
                          Default is '0.01'.

-omssa_it_replace_evalue  OMSSA e-value cutoff to replace a hit in the iterative search 0.0 means keep best.
                          Default is '0.0'.

-omssa_remove_prec        OMSSA remove precursor option, 1: true, 0: false, default is '1'.

-omssa_scale_prec         OMSSA scale precursor mass option.
                          1: true, 0: false, default is '0'.

-omssa_estimate_charge    OMSSA estimate precursor charge option.
                          1: true, 0: false, default is '1'.

-omssa_max_evalue         OMSSA maximal evalue considered, default is '100'.

-omssa_hitlist_length     OMSSA hitlist length.
                          0 means all, default is '0'.

-omssa_hitlist_charge     OMSSA number of hits per spectrum per charge, default is '30'.

-omssa_min_pep_length     OMSSA minumum peptide length (semi-tryptic or no enzyme searches only).

-omssa_max_pep_length     OMSSA maximum peptide length (OMSSA semi-tryptic or no enzyme searches only).

-omssa_format             OMSSA output format.
                          0: omx, 1: csv, default is 'omx'.

```

## Comet advanced parameters ##

```
-comet_num_matches        Comet maximum number of spectrum matches, default is '10'.

-comet_num_ptms           Comet max number of variable PTMs per peptide, default is '10'.

-comet_req_ptms           Comet require at least one variable PTM per peptide.
                          1: true, 0: false, default is '0'.

-comet_min_peaks          Comet min number of peaks for a spectrum, default is '10'.

-comet_min_peak_int       Comet min peak intensity, default is '0.0'.

-comet_remove_prec        Comet remove precursor.
                          0: off, 1: on, 2: as expected for ETD/ECD spectra.
                          default is '0'.

-comet_remove_prec_tol    Comet remove precursor tolerance, default is '1.5'.

-comet_clear_mz_range_lower
                          Comet clear mz range lower, default is '0.0'.

-comet_clear_mz_range_upper
                          Comet clear mz range upper, default is '0.0'.

-comet_enzyme_type        Comet enzyme type.
                          1: semi-specific
                          2: full-enzyme 
                          8: unspecific N-term
                          9: unspecific C-term
                          Default is '2'.

-comet_isotope_correction Comet isotope correction.
                          0: off
                          1: 0, +1 
                          2: 0, +1, +2
                          3: 0, +1, +2, +3
                          4: -8, -4, 0, +4, +8
                          5: -1, 0, +1, +2, +3
                          Default is '3'.

-comet_min_prec_mass      Comet minimum precursor mass, default is '0.0'.

-comet_max_prec_mass      Comet maximum precursor mass, default is '10000.0'.

-comet_max_frag_charge    Comet maximum fragment charge [1-5], default is '3'.

-comet_remove_meth        Comet remove methionine.
                          1: true, 0: false, default is '0'.

-comet_batch_size         Comet batch size, '0' means load and search all spectra at once, 
                          default is '0'.

-comet_theoretical_fragment_ions
                          Comet theoretical_fragment_ions option, default is '1'.

-comet_frag_bin_offset    Comet fragment bin offset, default is '0.0'.
```

## Tide advanced parameters ##

```
-tide_num_ptms            Tide max number of PTMs per peptide, default is no limit.

-tide_num_ptms_per_type   Tide max number of PTMs of each type per peptide, default is '2'.

-tide_min_pep_length      Tide minumum peptide length, default is '8'.

-tide_max_pep_length      Tide maximum peptide length, default is '30'.

-tide_min_prec_mass       Tide minumum precursor mass, default is '200.0'.

-tide_max_prec_mass       Tide maximum precursor mass, default is '7200.0'.

-tide_decoy_format        Tide decoy fomat (none|shuffle|peptide-reverse|protein-reverse), default is 'none'.

-tide_keep_terminals      Tide keep terminal amino acids when creating decoys (N|C|NC|none), default is 'NC'.

-tide_dedoy_seed          Tide decoy seed, default is '1'.

-tide_output_folder       Tide output folder (relative to the Tide working folder), default is 'crux-output'.

-tide_print_peptides      Tide print peptides.
                          1: true, 0: false, default is '0'.

-tide_verbosity           Tide progress display verbosity (0|10|20|30|40|50|60), default is '30'.

-tide_monoisotopic        Tide monoisotopic precursor.
                          1: true, 0: false, default is '1'.

-tide_clip_n_term         Tide clip n term methionine.
                          1: true, 0: false, default is '0'.

-tide_digestion_type      Tide digetion type (full-digest or partial-digest), default is 'full-digest'.

-tide_compute_sp          Tide compute sp score.
                          1: true, 0: false, default is '0'.

-tide_max_psms            Tide maximum number of spectrum matches spectrum, default is '10'.

-tide_compute_p           Tide compute exact p-values.
                          1: true, 0: false, default is '0'.

-tide_min_spectrum_mz     Tide minimum spectrum mz, default is '0.0'.

-tide_max_spectrum_mz     Tide maximum spectrum mz, default is no limit.

-tide_min_spectrum_peaks  Tide min spectrum peaks, default is '20'.

-tide_spectrum_charges    Tide spectrum charges (1|2|3|all), default is 'all'.

-tide_remove_prec         Tide remove precursor.
                          1: true, 0: false, default is '0'.

-tide_remove_prec_tol     Tide remove precursor tolerance, default is '1.5'.

-tide_progress_indicator  Tide progress indicator frequency, default is '1000'.

-tide_use_flanking        Tide use flanking peaks.
                          1: true, 0: false, default is '0'.

-tide_use_neutral_losses  Tide use neutral losses peaks.
                          1: true, 0: false, default is '0'.

-tide_mz_bin_width        Tide mz bin width, default is '0.02'.

-tide_mz_bin_offset       Tide mz bin offset, default is '0.0'.

-tide_concat              Tide concatenate target and decoy results.
                          1: true, 0: false, default is '0'.

-tide_store_spectra       Tide file name in with to store the binary spectra, default is null, i.e., not set.

-tide_export_text         Tide export text file.
                          1: true, 0: false, default is '1'.

-tide_export_sqt          Tide export SQT file.
                          1: true, 0: false, default is '0'.

-tide_export_pepxml       Tide export pepxml.
                          1: true, 0: false, default is '0'.

-tide_export_mzid         Tide export mzid.
                          1: true, 0: false, default is '0'.

-tide_export_pin          Tide export Percolator input file.
                          1: true, 0: false, default is '0'.

-tide_remove_temp         Tide remove temp folders when the search is done.
                          1: true, 0: false, default is '1'.
```

## Andromeda advanced parameters ##

```
-andromeda_max_pep_mass   Andromeda maximum peptide mass, default is '4600.0'.

-andromeda_max_comb       Andromeda maximum combinations, default is '250'.

-andromeda_top_peaks      Andromeda number of top peaks, default is '8'.

-andromeda_top_peaks_window  
                          Andromeda top peaks window width, default is '100'.

-andromeda_incl_water     Andromeda account for water losses.
                          1: true, 0: false, default is '1'.

-andromeda_incl_ammonia   Andromeda account for ammonina losses.
                          1: true, 0: false, default is '1'.

-andromeda_neutral_losses Andromeda neutral losses are sequence dependent.
                          1: true, 0: false, default is '1'.

-andromeda_fragment_all   Andromeda fragment all option.
                          1: true, 0: false, default is '0'.

-andromeda_emp_correction Andromeda emperical correction.
                          1: true, 0: false, default is '1'.

-andromeda_higher_charge  Andromeda higher charge option.
                          1: true, 0: false, default is '1'.

-andromeda_frag_method    Andromeda fragmentation method.
                          HCD, CID or EDT, default is 'CID'.

-andromeda_max_mods       Andromeda maximum number of modifications, default is '5'.

-andromeda_min_pep_length Andromeda minimum peptide length when using no enzyme, default is '8'.

-andromeda_max_pep_length Andromeda maximum peptide length when using no enzyme, default is '25'.

-andromeda_equal_il       Andromeda whether I and L should be considered indistinguishable.
                          1: true, 0: false, default is '0'.

-andromeda_max_psms       Andromeda maximum number of spectrum matches spectrum, default is '10'.
```

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

If you experience any problems with the command lines or have any suggestion please contact us via the [PeptideShaker mailing list](https://groups.google.com/group/peptide-shaker).