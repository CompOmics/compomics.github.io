---
title: DatabaseHelp
layout: default
permalink: /projects/searchgui/wiki/DatabaseHelp
tags: wiki, searchgui
project: searchgui
github_project: https://github.com/compomics/searchgui
---

# DatabaseHelp
# Database Help [ ](# )

 * [Introduction](#introduction)
 * [FASTA Format](#fasta-format)
 * [Non Standard FASTA](#non-standard-fasta)
 * [UniProt Databases](#uniprot-databases)
 * [IPI Databases](#ipi-databases)
 * [Decoy Sequences](#decoy-sequences)
 * [Mascot Users](#mascot-users)
 * [PeptideShaker](#peptideshaker)

## Introduction

Besides the spectra themselves, the sequence database to search in is the most important input of the search. If a sequence is not in the database the corresponding peptide/protein cannot be identified. 

On the other hand, adding sequences of proteins that cannot occur in your experiment will increase the rate of false identifications. It is therefore essential to use the correct sequence database.

[Go to top of page](# )

----

## FASTA Format

The standard format for sequence databases is called [FASTA](http://en.wikipedia.org/wiki/FASTA_format). [SearchGUI](http://searchgui.googlecode.com) therefore requires that the sequences are stored in this format. A FASTA file will usually end with .fasta, but .fast and .fas is also used.

In a FASTA file each sequence is represented by a header and the sequence itself. The header contains information about the protein, _e.g._, protein accession number, database and species. However, the format of the header varies from database to database. [SearchGUI](http://searchgui.googlecode.com) supports the most encountered databases like UniProt, Ensembl, NextProt, NCBI and IPI, plus a long list of other databases.

_It is strongly recommended to use one of the standard databases, and of these [UniProt](http://www.uniprot.org) is the preferred option._

## Non Standard FASTA

Non-standard home made sequence databases with non-standard headers can also be used, but the downstream usage may be limited, e.g., in [PeptideShaker](http://compomics.github.io/projects/peptide-shaker.html). 

Databases that do not match the standard header formats of the common databases (like UniProt, NCBInr etc) can be added using a generic header format (supported from [SearchGUI](http://compomics.github.io/projects/searchgui.html) version 1.7.3 and [PeptideShaker](http://compomics.github.io/projects/peptide-shaker.html) version 0.14.6 onwards):

```
>generic[your tag]|[protein accession]|[protein description]

or 

>generic[your tag]|[protein accession]
```

Note that `[your tag]` can be empty.

Examples:

```
>generic_contig-535081|AC:123132|Hypothetical protein
>generic|AC:123132|Hypothetical protein
>generic|AC:123132
```

`AC:123132` will then be used as the protein accession number and `Hypothetical protein` as the protein description (if provided).

If you have a sequence database that cannot be parsed, please let us know be setting up an [issue](https://github.com/compomics/searchgui/issues) at the SearchGUI home page</a>.

To parse databases with generic FASTA headers in Mascot we recommend the following Mascot database parse rules:

```
accession: ">generic[your tag]|\([^|]*\)|(.*)"
description: ">generic[your tag]|[^|]*|\(.*\)"
```

Replace or remove the `[your tag]` part depending on if you have a user defined tag or not.

[Go to top of page](# )

----

## UniProt Databases

As mentioned above it is strongly recommended to use sequence databases based on [SwissProt/UniProt](http://www.uniprot.org). This ensures that you get reviewed, maintained and well-annotated sequences that can easily be linked to a long list of other resources.

To get the SwissProt/UniProt sequence database for your species go to [www.uniprot.org](http://www.uniprot.org) and type _organism:'name of your species'_ into the Query field at the top, e.g., _organism:"homo sapiens"_. 

Next select one of the three provided options: _show only reviewed entries (UniProtKB/Swiss-Prot), show unreviewed entries (UniProtKB/TrEMBL), or show only entries from a complete proteome set_. Which option to chose depends on the properties of your experiment and on how well-annotated your given species is. (See [http://www.uniprot.org/faq/7(www.uniprot.org/faq/7) for details.)

Next click on the Download link in the upper right corner, and under the FASTA header select and download either _Canonical sequence data in FASTA format_ or _Canonical and isoform sequence data in FASTA format_. Again the choice depends on the properties of your experiment. (See [http://www.uniprot.org/faq/30](www.uniprot.org/faq/30) for details.)

Note that the presence of isoforms makes the downstream protein inference task more complex. It is generally advised to use a simple database and subsequently improve the complexity if needed.

You now have a [UniProt](http://www.uniprot.org) sequence database containing only sequences from your species that can be used as input to a [SearchGUI](http://compomics.github.io/projects/searchgui.html) search.

For more details on UniProt databases see [http://www.uniprot.org/faq/](www.uniprot.org/faq).

[Go to top of page](# )

----

## IPI Databases

Sequence databases based on the [International Protein Index (IPI)](http://www.ebi.ac.uk/IPI/IPIhelp.html) used to be a very common in proteomics. However, this format has been discontinued and ought to be replaced by corresponding [SwissProt/UniProt](http://www.uniprot.org) databases as explained above.

For more information on why IPI was discontinued see the [IPI home page](http://www.ebi.ac.uk/IPI/IPIhelp.html). 

[Go to top of page](# )

----

## Decoy Sequences

In order to conduct an unbiased validation of the identification results, it is possible to append non-existing sequences (so-called decoy sequences)  to your protein sequences (target sequences). Decoy sequences must fulfill two necessary and sufficient conditions: (1) similarity: the similarity between target and decoy sequences will ensure that false positives occur in equal amounts in both target and decoy sequences; (2) orthogonality: the absence of shared peptides between target and decoy sequences will allow the distinction of target and decoy hits.
After searching this concatenated target/decoy database, results can hence be thresholded to a desired level of quality.
For this task, we recommend the use of [PeptideShaker](http://compomics.github.io/projects/peptide-shaker.html).

There are various ways of creating the decoy sequences, the most popular being reversed versions of the actual sequences. Adding decoy sequences is easily done by clicking the _Decoy_ button next to the database file text field. Reversed versions of every sequence in the original sequences database will then be added to the FASTA file.

[Go to top of page](# )

----

## Mascot Users

_Using Mascot's [Automatic Decoy Search](http://www.matrixscience.com/help/decoy_help.html#AUTO) is not compatible with [PeptideShaker](http://compomics.github.io/projects/peptide-shaker.html)!_ 

The reason for this is that Mascot decoy sequences are not present in the FASTA file. Moreover, when combining results from different search engines it is vital that the database and decoys used are identical, something that cannot be guaranteed when using Mascot's [Automatic Decoy Search](http://www.matrixscience.com/help/decoy_help.html#AUTO). 

To combine Mascot results with your OMSSA and X!Tandem results you therefore have to use the same target-decoy database as the one used in the [SearchGUI](http://compomics.github.io/projects/searchgui.html) search and **not** select the decoy option when performing the Mascot search.  

Finally, to ensure compatibility between search engines, be sure to use the exact same database for all algorithms.

[Go to top of page](# )

----

## PeptideShaker

Note that for your search results to be compatible with [PeptideShaker](http://compomics.github.io/projects/peptide-shaker.html), decoy sequences have to be added as explained in the [Decoy Sequences(#decoy-sequences) section above. 

_Search results from [SearchGUI](http://compomics.github.io/projects/searchgui.html) can be opened in [PeptideShaker](http://peptide-shaker.googlecode.com) even when decoys are not added, but it will then not be possible to statistically validate the identifications!_

[Go to top of page](# )

----