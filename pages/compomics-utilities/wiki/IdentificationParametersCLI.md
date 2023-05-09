---
title: "IdentificationParametersCLI"
layout: default
permalink: "/projects/compomics-utilities/wiki/IdentificationParametersCLI"
tags: wiki, compomics-utilities
project: "compomics-utilities"
github_project: "https://github.com/compomics/compomics-utilities"
---

# IdentificationParametersCLI

# Identification Parameters Command Line Interface #

IdentificationParametersCLI can be used to create or edit an identification parameter file via command line, for use in tools like [SearchGUI](http://compomics.github.io/projects/searchgui.html), [PeptideMapper](/projects/compomics-utilities/wiki/PeptideMapper) and [PeptideShaker](http://compomics.github.io/projects/peptide-shaker.html). Identification parameter files are in the [json](https://en.wikipedia.org/wiki/JSON) format and can also be created in the graphical user interface or using third party tools. Alternatively, the parameters can be created and edited directly in the command lines of [CompOmics-utilities](http://compomics.github.io/projects/compomics-utilities.html), [SearchGUI](http://compomics.github.io/projects/searchgui.html) and [PeptideShaker](http://compomics.github.io/projects/peptide-shaker.html).

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
    * [Database Processing](#database-processing)
  * [Algorithm specific parameters](#general-parameters)
    * [XTandem advanced parameters](#xtandem-advanced-parameters)
    * [MS-GF advanced parameters](#ms-gf-advanced-parameters)
    * [MS Amanda advanced parameters](#ms-amanda-advanced-parameters)
    * [OMSSA advanced parameters](#omssa-advanced-parameters)
    * [MyriMatch advanced parameters](#myrimatch-advanced-parameters)
    * [Comet advanced parameters](#comet-advanced-parameters)
    * [Tide advanced parameters](#tide-advanced-parameters)
    * [Andromeda advanced parameters](#andromeda-advanced-parameters)
    * [MetaMorpheus advanced parameters](#metamorpheus-advanced-parameters)
    * [Sage advanced parameters](#sage-advanced-parameters)
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
com.compomics.cli.identification_parameters.IdentificationParametersCLI [parameters]
```

```java
java -cp SearchGUI-X.Y.Z.jar 
eu.isas.searchgui.cmd.IdentificationParametersCLI [parameters]
```

```java
java -cp PeptideShaker-X.Y.Z.jar 
eu.isas.peptideshaker.cmd.IdentificationParametersCLI [parameters]
```

## General parameters ##

```
-out                      The destination Identification Parameters file (.par).

-id_params                An identification parameters file to modify (optional).

-mods                     Lists the available modifications.

-enzymes                  Lists the available enzymes.
```

## Spectrum matching parameters ##

```
-prec_tol                 Precursor ion mass tolerance, default is '10'.

-prec_ppm                 Precursor ion tolerance unit: ppm (1) or Da (0), default is '1'.

-frag_tol                 Fragment ion mass tolerance, default is '0.5'.

-frag_ppm                 Fragment ion tolerance unit: ppm (1) or Da (0), default is '1'.

-digestion                The type of digestion to consider: 
                          0: Enzyme, 1: Unspecific or 2: Whole Protein. Default is 0.

-enzyme                   Enzyme, default is 'Trypsin'. Note: case sensitive.

-specificity              Specificity of the enzyme: 
                          0: Specific, 1: Semi-Specific, 2: N-term Specific or 3: C-term Specific
                          If more than one enzyme was used, please provide the missed cleavages for 
                          every enzyme in the same order as comma separated list with quotes, e.g. "0, 1"

-mc                       Number of allowed missed cleavages, default is '2'.
                          If more than one enzyme was used, please provide the missed cleavages for every 
                          enzyme in the same order as comma separated list with quotes, e.g. "2, 1".

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
-annotation_level         The intensity threshold to consider for annotation.
                          e.g. using percentiles, 0.75 means that the 25% most intense peaks will be annotated.
                          Default is 0.75.
                          
-annotation_level_type    The type of the intensity threshold.
                          percentile: Percentile of the intensities, snp: Signal to noise probability.
                          Default is percentile.

-annotation_mz_tolerance  The m/z tolerance to annotate peaks. 
                          Default: equal to the search settings MS2 tolerance.

-annotation_high_resolution    
                          If true the most accurate peak will be selected within the m/z tolerance.
                          1: true, 0: false, default is '1'.

```

## Sequence Matching ##

```
-sequence_matching_type   The peptide to protein sequence matching type. Default is 2.
                          0: Character Sequence
                          1: Amino Acids
                          2: Indistinguishable Amino Acids

-sequence_matching_x      The maximal share of Xs in a sequence, 0.25 means 25% of Xs, default is 0.25.

-sequence_matching_enzymatic_tags
                          Tags should only be mapped to enzymatic peptides. 1: true, 0: false. Default is 0.

-sequence_matching_max_ptms_per_tag
                          The maximum number of PTMs per peptide when mapping tags, default is 3.

-sequence_matching_min_amino_acid_score
                          The minimum amino acid score when mapping tags, default is 30.

-sequence_matching_min_tag_length
                          The minimum tag length when mapping tags, default is 3.
```

## Import Filters ##

```
-import_peptide_length_min     
                          The minimal peptide length to consider when importing identification files, default is 8.

-import_peptide_length_max     
                          The maximal peptide length to consider when importing identification files, default is 30.

-import_missed_cleavages_min
                          The minimal number of missed cleavages to consider when importing identification files, 
                          default is no filter.

-import_missed_cleavages_max
                          The maximal number of missed cleavages to consider when importing identification files, 
                          default is no filter.

-import_precursor_mz      The maximal precursor precursor deviation to allow when importing identification files, 
                          the precursor tolerance by default.

-import_precursor_mz_ppm  Maximal precursor ion deviation unit: ppm (1) or Da (0), default is '1'.

-exclude_unknown_ptms     If true peptides presenting unrecognized PTMs will be excluded.
                          1: true, 0: false, default is '1'.
```

## PTM Localization ##

```
-ptm_score                The PTM probabilistic score to use for modification localization, default is 1.
                          0: A-score
                          1: PhosphoRS
                          2: None

-ptm_threshold            The threshold to use for the modification localization score. 
                          Default is 95. 

-score_neutral_losses     Include neutral losses in spectrum annotation of the PTM score.
                          1: true, 0: false, default is '0'.

-ptm_sequence_matching_type    
                          The modification to peptide sequence matching type. Default is 1.
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
-simplify_groups          Simplify protein groups.
                          1: true, 0: false, default is '1'.
                          
-simplify_evidence        Simplify protein groups based on the UniProt protein evidence.
                          1: true, 0: false, default is '1'.

-simplify_confidence      Simplify protein groups based on the peptide confidence.
                          1: true, 0: false, default is '1'.

-simplify_confidence_threshold      
                          Peptide confidence threshold below which a peptide is considered absent, default is 0.05.

-simplify_enzymaticity    Simplify protein groups based on the peptide enzymaticity.
                          1: true, 0: false, default is '1'.

-simplify_variant         Simplify protein groups based on the variant matching
                          1: true, 0: false, default is '1'.

-pi_modifications         Account for modifications when mapping peptides to proteins.
                          1: true, 0: false, default is '1'.

```

## Validation Levels ##

```
-psm_fdr                  FDR at the PSM level in percent, default is 1.

-peptide_fdr              FDR at the peptide level in percent, default is 1.

-protein_fdr              FDR at the protein level in percent, default is 1.

```

## Fraction Analysis ##

```
-protein_fraction_mw_confidence
                          Minimum confidence required for a protein in the fraction MW plot (default 95%: '95.0').

```

## Database Processing ##

```
-fasta_target_decoy       FASTA file should be processed as target-decoy. 1: true, 0: false, default is '1'.

-fasta_decoy_tag          The flag for decoy proteins in the accession. Default is '-REVERSED'.

-fasta_decoy_type         Decoy type. 0: prefix, 1: suffix, default is '1'.

-fasta_decoy_file_tag     The tag added after adding decoy sequences to a FASTA file. Default is 
                          '_concatenated_target_decoy'.

```

## Algortithm Specific parameters ##

The following parameters allow controlling specific identification algorithms specifically.

## XTandem advanced parameters ##

```
-xtandem_dynamic_range    X!Tandem 'spectrum, dynamic range' option, default is '100'.

-xtandem_npeaks           X!Tandem 'spectrum, total peaks' option, default is '50'.

-xtandem_min_frag_mz      X!Tandem 'spectrum, minimum fragment mz' option, default is '200'.

-xtandem_min_peaks        X!Tandem 'spectrum, minimum peaks' option, default is '5'.

-xtandem_noise_suppr      X!Tandem 'spectrum, use noise suppression' option.
                          1: true, 0: false, default is '0'.

-xtandem_min_prec_mass    X!Tandem 'spectrum, minimum parent m+h' option, default is '500'.

-xtandem_parent_isotope_correction
                          X!Tandem 'spectrum, parent monoisotopic mass isotope error. 
                          1: true, 0: false, default is '1'.

-xtandem_quick_acetyl     X!Tandem 'protein, quick acetyl' option.
                          1: true, 0: false, default is '1'.

-xtandem_quick_pyro       X!Tandem 'protein, quick pyrolidone' option.
                          1: true, 0: false, default is '1'.

-xtandem_stp_bias         X!Tandem 'protein, stP bias' option.
                          1: true, 0: false, default is '0'.

-xtandem_ptm_complexity   X!Tandem 'protein, ptm complexity' option, default is '6.0'.

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

-xtandem_refine_snaps     X!Tandem 'refine, sNAps' option.
                          1: true, 0: false, default is '1'.

-xtandem_refine_spec_synt X!Tandem 'refine, spectrum synthesis' option.
                          1: true, 0: false, default is '1'.

-xtandem_evalue           X!Tandem 'output, maximum valid expectation value' option, default is '0.01'.

-xtandem_output_results   X!Tandem 'output, results' option (all|valid|stochastic), default is 'all'.

-xtandem_output_proteins  X!Tandem 'output, proteins' option.
                          1: true, 0: false, default is '1'.

-xtandem_output_sequences X!Tandem 'output, sequences' option.
                          1: true, 0: false, default is '0'.

-xtandem_output_spectra   X!Tandem 'output, spectra' option.
                          1: true, 0: false, default is '1'.

-xtandem_output_histograms   
                          X!Tandem 'output, histograms' option.
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

-myrimatch_output         MyriMatch output format option, mzIdentML or pepXML, default is 'mzIdentML'.

```

## MS Amanda advanced parameters ##

```
-ms_amanda_decoy          MS Amanda generate decoys option.
                          0: false, 1: true, default is '0'.

-ms_amanda_decoy_ranking  MS Amanda decoys ranking options, 0: shared rank, 1: rank target and decoy 
                          separately, default is '1'.

-ms_amanda_instrument     MS Amanda instrument id option. Available enzymes are listed in the GUI. 
                          (Note: case sensitive.).

-ms_amanda_max_rank       MS Amanda maximum rank, default is '5'.

-ms_amanda_mono           MS Amanda use monoisotopic mass values.
                          0: false, 1: true, default is '1'.

-ms_low_mem_mode          MS Amanda use low memory mode option.
                          0: false, 1: true, default is '1'.

-ms_amanda_perform_deisotoping
                          MS Amanda perform deisotoping. 
                          0: false, 1: true, default is '1'.

-ms_amanda_max_mod        MS Amanda maximum number of occurrences of a specific modification on 
                          a peptide (0-10), default is '3'.
                          
-ms_amanda_max_var_mod.   MS Amanda maximum number of variable modifications per peptide (0-10). 
                          default is '4'
                          
-ms_amanda_max_mod_sites  MS Amanda maximum number of potential modification sites per modification 
                          per peptide (0-20), default is '6'.
                          
-ms_amanda_max_neutraul_losses
                          MS Amanda maximum number of water and ammonia losses per peptide (0-5), 
                          default is '1'.
                          
-ms_amanda_max_neutral_losses_mod
                          MS Amanda maximum number identical modification specific losses per 
                          peptide (0-5), default is '2'.
                          
-ms_amanda_min_pep_length MS Amanda minimum peptide length. Default is '8'.

-ms_amanda_max_pep_length MS Amanda maximum peptide length. Default is '30'.
                          
-ms_amanda_loaded_proteins
                          MS Amanda maximum number of proteins loaded into memory (1000-500000). 
                          default is '100000'
                          
-ms_amanda_loaded_spectra MS Amanda maximum number of spectra loaded into memory (1000-500000). 
                          default is '2000'
                          
-ms_amanda_output         MS Amanda output format option, csv or mzIdentML.
                          default is 'csv'.

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
-omssa_low_intensity      OMSSA low intensity cutoff as percentage of the most intense peak, default is '0.0'.

-omssa_high_intensity     OMSSA high intensity cutoff as percentage of the most intense peak, default is '0.2'.

-omssa_intensity_incr     OMSSA intensity increment, default is '0.0005'.

-omssa_min_peaks          OMSSA minimum number of peaks, integer, default is '4'.

-omssa_remove_prec        OMSSA eliminate charge reduced precursors in spectra option, 
                          1: true, 0: false, default is '0'.

-omssa_estimate_charge    OMSSA estimate precursor charge option.
                          1: Use range, 0: Believe input file, default is '1'.

-omssa_plus_one           OMSSA estimate plus one charge algorithmically option. 
                          1: true, 0: false, default is '1'.

-omssa_fraction           OMSSA fraction of precursor m/z for charge one estimation, default is '0.95'.

-omssa_prec_per_spectrum  OMSSA minimum number of precursors per spectrum, integer, default is '1'.

-omssa_scale_prec         OMSSA scale precursor mass option.
                          1: true, 0: false, default is '1'.

-omssa_memory             OMSSA map sequences in memory option.
                          1: true, 0: false, default is '1'.

-omssa_methionine         OMSSA N-terminal methionine cleavage option.
                          1: true, 0: false, default is '1'.

-omssa_neutron            Mass after which OMSSA should consider neutron exact mass, default is '1446.94'.

-omssa_single_window_wd   OMSSA single charge window width in Da, integer, default is '27'.

-omssa_double_window_wd   OMSSA double charge window width in Da, integer, default is '14'.

-omssa_single_window_pk   OMSSA single charge window number of peaks, integer, default is '2'.

-omssa_double_window_pk   OMSSA double charge window number of peaks, integer, default is '2'.

-omssa_min_ann_int_pks    OMSSA minimum number of annotated peaks among the most intense ones, integer, 
                          default is '6'.

-omssa_min_annotated_peaks
                          OMSSA minimum number of annotated peaks, integer, default is '2'.

-omssa_max_ladders        OMSSA maximum number of m/z ladders, integer, default is '128'.

-omssa_max_frag_charge    OMSSA maximum fragment charge, integer, default is '2'.

-omssa_charge             OMSSA fragment charge option, 1: plus, 0: minus, default is '1'.

-omssa_forward            OMSSA include first forward ion (b1) in search.
                          1: true, 0: false, default is '0'.

-omssa_rewind             OMSSA search rewind (C-terminal) ions option.
                          1: true, 0: false, default is '1'.

-omssa_max_frag_series    OMSSA maximum fragment per series option, integer, default is '100'.

-omssa_corr               OMSSA use correlation correction score option.
                          1: true, 0: false, default is '1'.

-omssa_consecutive_p      OMSSA consecutive ion probability, default is '0.5'.

-omssa_hitlist_charge     OMSSA number of hits per spectrum per charge, default is '30'.

-omssa_it_sequence_evalue
                          OMSSA e-value cutoff to consider a sequence in the iterative search 0.0 means all.
                          Default is '0.0'.

-omssa_it_spectrum_evalue
                          OMSSA e-value cutoff to consider a spectrum in the iterative search 0.0 means all.
                          Default is '0.01'.

-omssa_it_replace_evalue  OMSSA e-value cutoff to replace a hit in the iterative search 0.0 means keep best.
                          Default is '0.0'.
                          
-omssa_min_pep_length     OMSSA minumum peptide length (semi-tryptic or no enzyme searches only).

-omssa_max_pep_length     OMSSA maximum peptide length (OMSSA semi-tryptic or no enzyme searches only).

-omssa_max_evalue         OMSSA maximal evalue considered, default is '100'.

-omssa_hitlist_length     OMSSA hitlist length.
                          0 means all, default is '0'.

-omssa_format             OMSSA output format.
                          0: omx, 1: csv, 2: pepXML, default is 'omx'.

```

## Comet advanced parameters ##

```
-comet_num_matches        Comet maximum number of spectrum matches, default is '10'.

-comet_num_ptms           Comet max number of variable PTMs per peptide, default is '10'.

-comet_req_ptms           Comet require at least one variable PTM per peptide.
                          1: true, 0: false, default is '0'.

-comet_min_peaks          Comet min number of peaks for a spectrum, default is '10'.

-comet_min_peak_int       Comet min peak intensity, default is '0.0'.

-comet_remove_prec        Comet remove precursor peaks:
                          0: off, 
                          1: all peaks around the precursor m/z, 
                          2: all charge reduced precursor peaks, 
                          3: precursor phosphate neutral loss peaks.
                          Default is '0'.

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
                          Default is '3'.

-comet_min_prec_mass      Comet minimum precursor mass, default is '0.0'.

-comet_max_prec_mass      Comet maximum precursor mass, default is '10000.0'.

-comet_min_pep_length     Comet minimum peptide length, default is '8'.

-comet_max_pep_length     Comet maximum peptide length, default is '30'.

-comet_max_frag_charge    Comet maximum fragment charge [1-5], default is '3'.

-comet_remove_meth        Comet remove methionine.
                          1: true, 0: false, default is '0'.

-comet_batch_size         Comet batch size, '0' means load and search all spectra at once, 
                          default is '0'.

-comet_theoretical_fragment_ions
                          Comet theoretical_fragment_ions option, default is '1'.

-comet_frag_bin_offset    Comet fragment bin offset, default is '0.0'.

-comet_num_matches        Comet maximum number of spectrum matches, default is '10'.

-comet_output             Comet output type, PepXML, SQT, TXT, Percolator or mzIdentML, default is 'PepXML'.
```

## Tide advanced parameters ##

```
-tide_min_pep_length      Tide minumum peptide length, default is '8'.

-tide_max_pep_length      Tide maximum peptide length, default is '30'.

-tide_min_prec_mass       Tide minumum precursor mass, default is '200.0'.

-tide_max_prec_mass       Tide maximum precursor mass, default is '7200.0'.

-tide_monoisotopic        Tide monoisotopic precursor.
                          1: true, 0: false, default is '1'.

-tide_clip_n_term         Tide clip n term methionine.
                          1: true, 0: false, default is '0'.

-tide_min_ptms            Tide min number of PTMs per peptide, default is '0'.

-tide_max_ptms            Tide max number of PTMs per peptide, default is '255'.

-tide_num_ptms_per_type   Tide max number of PTMs of each type per peptide, default is '2'.

-tide_digestion_type      Tide digetion type (full-digest or partial-digest), default is 'full-digest'.

-tide_print_peptides      Tide print peptides.
                          1: true, 0: false, default is '0'.

-tide_decoy_format        Tide decoy fomat (none|shuffle|peptide-reverse|protein-reverse), default is 'none'.

-tide_keep_terminals      Tide keep terminal amino acids when creating decoys (N|C|NC|none), default is 'NC'.

-tide_dedoy_seed          Tide decoy seed, default is '1'.

-tide_remove_temp         Tide remove temp folders when the search is done.
                          1: true, 0: false, default is '1'.

-tide_compute_p           Tide compute exact p-values.
                          1: true, 0: false, default is '0'.

-tide_compute_sp          Tide compute sp score.
                          1: true, 0: false, default is '0'.

-tide_min_spectrum_mz     Tide minimum spectrum mz, default is '0.0'.

-tide_max_spectrum_mz     Tide maximum spectrum mz, default is no limit.

-tide_min_spectrum_peaks  Tide min spectrum peaks, default is '20'.

-tide_spectrum_charges    Tide spectrum charges (1|2|3|all), default is 'all'.

-tide_remove_prec         Tide remove precursor.
                          1: true, 0: false, default is '0'.

-tide_remove_prec_tol     Tide remove precursor tolerance, default is '1.5'.

-tide_use_flanking        Tide use flanking peaks.
                          1: true, 0: false, default is '0'.

-tide_use_neutral_losses  Tide use neutral losses peaks.
                          1: true, 0: false, default is '0'.

-tide_mz_bin_width        Tide mz bin width, default is '0.02'.

-tide_mz_bin_offset       Tide mz bin offset, default is '0.0'.

-tide_max_psms            Tide maximum number of spectrum matches spectrum, default is '10'.

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

-tide_output_folder       Tide output folder (relative to the Tide working folder), default is 'crux-output'.

-tide_verbosity           Tide progress display verbosity (0|10|20|30|40|50|60), default is '30'.

-tide_progress_indicator  Tide progress indicator frequency, default is '1000'.

-tide_concat              Tide concatenate target and decoy results.
                          1: true, 0: false, default is '0'.

-tide_store_spectra       Tide file name in with to store the binary spectra, default is null, i.e., not set.
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

-andromeda_max_pep_length Andromeda maximum peptide length when using no enzyme, default is '30'.

-andromeda_equal_il       Andromeda whether I and L should be considered indistinguishable.
                          1: true, 0: false, default is '0'.

-andromeda_max_psms       Andromeda maximum number of spectrum matches spectrum, default is '10'.
```

## MetaMorpheus advanced parameters ##

```
-meta_morpheus_min_pep_length
                          MetaMorpheus minimum peptide length, default is '8'.

-meta_morpheus_max_pep_length
                          MetaMorpheus maximum peptide length, default is '30'.

-meta_morpheus_search_type
                          MetaMorpheus search type, Classic, Modern or NonSpecific, default is 'Classic'.

-meta_morpheus_num_partitions
                          MetaMorpheus number of partitions when indexing, default is '1'.

-meta_morpheus_dissociation_type
                          MetaMorpheus dissociation type, HCD, CID, ECD or ETD, default is 'HCD'.

-meta_morpheus_max_mods_for_peptide
                          MetaMorpheus maximum modifications per peptide, default is '2'.

-meta_morpheus_meth       MetaMorpheus initiator methionine behavior: 
                          Undefined, Retain, Cleave or Variable, default is 'Variable'.

-meta_morpheus_score_cutoff
                          MetaMorpheus score cutoff, default is '5.0'.

-meta_morpheus_use_delta_score
                          MetaMorpheus use delta score, 1: true, 0: false, default is '0'.

-meta_morpheus_frag_term  MetaMorpheus fragmentation terminus, Both, N or C, default is 'Both'.

-meta_morpheus_max_frag_size
                          MetaMorpheus maximum fragmentation size, default is '30000'.

-meta_morpheus_min_internal_fragment_length
                          MetaMorpheus minimum allowed internal fragment length, default is '0'.

-meta_morpheus_mass_diff_acceptor_type
                          MetaMorpheus mass difference acceptor type, Exact, OneMM, TwoMM, ThreeMM, 
                          PlusOrMinusThreeMM, ModOpen or Open, default is 'OneMM'.

-meta_morpheus_write_mzid MetaMorpheus write mzid, 1: true, 0: false, default is '1'.

-meta_morpheus_write_pepxml
                          MetaMorpheus write pepxml, 1: true, 0: false, default is '0'.

-meta_morpheus_use_provided_prec
                          MetaMorpheus use provided precursor info, 1: true, 0: false, default is '1'.

-meta_morpheus_do_prec_deconv
                          MetaMorpheus do precursor deconvolution, 1: true, 0: false, default is '1'.

-meta_morpheus_deconv_int_ratio
                          MetaMorpheus deconvolution intensity ratio, default is '3.0'.

-meta_morpheus_deconv_mass_tol
                          MetaMorpheus deoconvolution mass tolerance, default is '4.0'.

-meta_morpheus_deconv_mass_tol_type
                          MetaMorpheus deoconvolution mass tolerance type, PPM or Absolute, default is 'PPM'.

-meta_morpheus_trim_ms1   MetaMorpheus trim MS1 peaks, 1: true, 0: false, default is '0'.

-meta_morpheus_trim_msms  MetaMorpheus trim MSMS peaks, 1: true, 0: false, default is '1'.

-meta_morpheus_num_peaks_per_window
                          MetaMorpheus number of peaks per window, default is '200'.

-meta_morpheus_min_allowed_int_ratio_to_base_peak
                          MetaMorpheus minium allowed intensity ratio to base peak, default is '0.01'.

-meta_morpheus_window_with_thompson
                          MetaMorpheus window width in Thompson.

-meta_morpheus_num_windows
                          MetaMorpheus number of windows.

-meta_morpheus_norm_across_all_windows
                          MetaMorpheus normalize peaks across all windows, 1: true, 0: false, default is '0'.

-meta_morpheus_mod_peptides_are_different
                          MetaMorpheus modified peptides are different, 1: true, 0: false, default is '0'.

-meta_morpheus_no_one_hit_wonders
                          MetaMorpheus exclude one hit wonders, 1: true, 0: false, default is '0'.

-meta_morpheus_search_target
                          MetaMorpheus search target sequences, 1: true, 0: false, default is '1'.

-meta_morpheus_decoy_type MetaMorpheus decoy type, None, Reverse or Slide, default is 'None'.

-meta_morpheus_max_mod_isoforms
                          MetaMorpheus maximum modified isoforms, default is '1024'.

-meta_morpheus_min_variant_depth
                          MetaMorpheus minimum variant depth, default is '1'.

-meta_morpheus_max_hetrozygous_var
                          MetaMorpheus maximum hetrozygous variants, default is '4'.

-meta_morpheus_gptm       MetaMorpheus run G-PTM, 1: true, 0: false, default is '0'.

-meta_morpheus_gptm_categories
                          MetaMorpheus G-PTM categories to include in the G-PTM search:
                          Common, Common_Biological, Common_Artifact, Metal, Glyco,
                          Less_Common, Labeling, Nucleotide_Substitution_One, 
                          Nucleotide_Substitution_TwoPlus, Other.
```

## Sage advanced parameters ##

```
-sage_bucket_size         Sage bucket size, number of fragments in each 
                          internal mass bucket, default is '32768'.

-sage_min_pep_length      Sage minimum peptide length, default is '8'.

-sage_max_pep_length      Sage maximum peptide length, default is '30'.

-sage_min_frag_mz         Sage minimum fragment mz, default is '200.0'.

-sage_max_frag_mz         Sage maximum fragment mz, default is '2000.0'.

-sage_min_pep_mass        Sage minimum peptide mass, default is '600.0'.

-sage_max_pep_mass        Sage maximum peptide mass, default is '5000.0'.

-sage_min_ion_index       Sage minimum ion index for the preliminary search, 
                          default is '2', i.e. skip b1/b2/y1/y2 ions.

-sage_max_var_mods        Sage maximum number of variable modifications, default is '2'.

-sage_generate_decoys     Sage generate decoys, default is 'true'.

-sage_tmt                 Sage TMT: Tmt6, Tmt10, Tmt11, Tmt16, or Tmt18.

-sage_tmt_level           Sage TMT level: MS-level to perform TMT quantification on, default is '3'.

-sage_tmt_sn              Sage use signal/noise instead of intensity for TMT quant, default is 'false'.

-sage_lfq                 Sage LFQ: default is 'false'.

-sage_lfq_peak_scoring    Sage LFQ peak scoring: Hybrid, RetentionTime or SpectralAngle. Default is 'Hybrid'.

-sage_lfq_intergration    Sage LFQ integration: Sum or Max. Default is 'Sum'.

-sage_lfq_spectral_angle  Sage LFQ spectral angle, default is '0.7'.

-sage_lfq_ppm_tolerance   Sage LFQ ppm tolerance, default is '0.5'.

-sage_deisotope           Sage deisotope, perform deisotoping and charge state deconvolution, 
                          default is 'false'.

-sage_chimera             Sage search for chimeric/co-fragmenting PSMs, default is 'false'.

-sage_wide_window         Sage ignore `precursor_tol` and search spectra in wide-window/dynamic 
                          precursor tolerance mode, default is 'false'.

-sage_predict_rt          Sage use of retention time prediction model as an feature for LDA, 
                          default is 'true'.

-sage_min_peaks           Sage min number of peaks for a spectrum, default is '15'.

-sage_max_peaks           Sage max number of peaks for a spectrum, default is '150'.

-sage_min_matched_peaks   Sage minimum matched peaks, default is '4'

-sage_max_frag_charge     Sage maximum fragment charge, default is 'null'.

-sage_num_psms            Sage number of PSMs to report for each spectra. 
                          Recommend setting to 1, higher values might disrupt LDA, default is '1'.

-sage_batch_size          Sage batch size, default is the number of CPUs/2.
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


## DirecTag advanced parameters ##

```

-directag_tag_length      DirecTag tag length, default is '4'.

-directag_max_var_mods    DirecTag maximum variable modifications per sequence, default is '2'.

-directag_charge_states   DirecTag number of charge states considered, default is '3'.

-directag_duplicate_spectra
                          DirecTag duplicate spectra per charge, 1: true, 0: false, default is '1'.

-directag_isotope_tolerance
                          DirecTag isotope mz tolerance, default is '0.25'.

-directag_deisotoping     DirecTag deisotoping mode, default is '0', 0: no deisotoping, 
                          1: precursor only, 2: precursor and candidate.

-directag_intensity_classes
                          DirecTag number of intensity classses, default is '3'.

-directag_output_suffix   DirecTag output suffic, default is no suffix.

-directag_max_peak_count  DirecTag max peak count, default is '100'.

-directag_max_tag_count   DirecTag maximum tag count, default is '10'.

-directag_tic_cutoff      DirecTag TIC cutoff in percent, default is '100'.

-directag_complement_tolerance
                          DirecTag complement mz tolerance, default is '0.1'.

-directag_adjustment_step DirecTag precursor adjustment step, default is '0.1'.

-directag_min_adjustment  DirecTag minimum precursor adjustment, default is '-0.5'.

-directag_max_adjustment  DirecTag maximum precursor adjustment, default is '1.5'.

-directag_intensity_weight
                          DirecTag intensity score weight, default is '1.0'.

-directag_fidelity_weight DirecTag fidelity score weight, default is '1.0'.

-directag_complement_weight
                          DirecTag complement_score_weight, default is '1.0'.
                          
-directag_adjust_precursor
                          DirecTag adjust precursor, 1: true, 0: false, default is '0'.

-directag_ms_charge_state DirecTag use charge state from M spectrum, 1: true, 0: false, default is '1'.
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