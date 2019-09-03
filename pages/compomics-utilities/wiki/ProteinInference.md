---
title: "ProteinInference"
layout: default
permalink: "/projects/compomics-utilities/wiki/ProteinInference"
tags: wiki, compomics-utilities
project: "compomics-utilities"
github_project: "https://github.com/compomics/compomics-utilities"
---

# Protein Inference #

This page describes what **protein inference** is, why it is so complicated, and how protein inference is handled in bioinformatic tools.

## What is protein inference? ##

Shotgun proteomics relies on the identification of proteins via peptides obtained from digestion of complex mixtures. The **protein inference** is the task of inferring a set of proteins from identified peptide sequences.

## Why is it so complicated? ##

### Shared peptides ###

The peptide-centric approach is by design flawed by the presence of _shared peptides_ also named _degenerated peptides_ whose sequence is shared between different proteins. When such peptides are encountered, it is common practice to group the matching proteins into **ambiguity groups**, see [Nesvizhskii and Aebersold](http://www.mcponline.org/cgi/pmidlookup?view=long&pmid=16009968) for a detailed formalism of this so-called **protein inference problem**.

How shared peptides influence the scoring of protein matches is left to the appreciation of the bioinformatician - and strongly impacts the list of proteins validated at a desired quality level. For more details on identification results validation see [Nesvizhskii](http://www.ncbi.nlm.nih.gov/pubmed/?term=20816881) and the Chapter 1.5 of our [free tutorials for peptide and protein identification](http://compomics.com/bioinformatics-for-proteomics/).
Consequently, which proteins are actually retained in the end strongly varies between tools. Indeed, there is room for variability between a **minimal set** of proteins where one protein per ambiguity group is selected and a **maximal set** where every possible accession is retained as reviewed [here](http://www.expert-reviews.com/doi/abs/10.1586/epr.12.51?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%3dpubmed) for example.

As a result, different software will give you different proteins from the same peptide list. Various tools are available for this task, integrated in a larger environment like the [Trans-Proteomic Pipeline (TPP)](http://tools.proteomecenter.org/wiki/index.php?title=Software:TPP) or [OpenMS](http://open-ms.sourceforge.net/), integrated in a software like  [MassSieve](http://www.ncbi.nlm.nih.gov/staff/slottad/MassSieve/), [MaxQuant](http://www.maxquant.org/) or [PeptideShaker](https://code.google.com/p/peptide-shaker/), or standalone like [IDPicker](http://fenchurch.mc.vanderbilt.edu/software.php).

Practical examples can be found in the Chapter 1.4 of our [free tutorials for peptide and protein identification](http://compomics.com/bioinformatics-for-proteomics/).

### Technical implementation ###

Search engines provide their own peptide to protein mapping. However, the mapping can be different between search engines or for a single search engine across runs as reviewed [here](http://www.sciencedirect.com/science/article/pii/S1570963913002562). For this reason, it is mandatory to remap every peptide to every protein when working with identification results. Remapping peptides to proteins can be very slow on large databases: for every run the software has to search thousands of peptides in the FASTA file.

Also, this task is complicated by the presence of Xs (which can be any amino-acid), combination of amino-acids like B or J and indistinguishable amino-acids like I and L: the software then has to test every possibility and false peptide to protein matches might occur. An extreme example where protein inference breaks down is proteins containing series of Xs (like [UniProtKB/Swiss-Prot Mucin-3A](http://www.uniprot.org/uniprot/Q02505) at the time of writing) which can basically map to any peptide.

Peptide to protein mapping is implemented in online resources like in the [Protein Information Resource](http://proteininformationresource.org/peptide.shtml) and in software packages like [OpenMS](http://open-ms.sourceforge.net/). In this package, the mapping is done via [PeptideMapper](/projects/compomics-utilities/wiki/peptidemapper). PeptideMapper also presents the particularity to map partial sequences similarly to [DirecTag](http://www.ncbi.nlm.nih.gov/pubmed/18630943). It is used in [PeptideShaker](http://compomics.github.io/projects/peptide-shaker.html) and [DeNovoGUI](http://compomics.github.io/projects/denovogui.html). For more information please refer to the [PeptideMapper wiki page](/projects/compomics-utilities/wiki/peptidemapper).

For the sake of speed and quality, it is thus crucial that the protein database used contains as few sequences as possible with as low ambiguity as possible - while maintaining the best coverage of the proteins in the sample including potential contaminants.