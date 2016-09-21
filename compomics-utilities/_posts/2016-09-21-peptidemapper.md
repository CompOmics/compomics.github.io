---
name: PeptideMapper
project: compomics-utilities
layout: default
permalink: /compomics-utilities/wiki/peptidemapper.html
github_project: https://github.com/compomics/compomics-utilities
---

# PeptideMapper - Efficient Amino Acid Sequence Mapping #

PeptideMapper is a lightweight and efficient application for the mapping of amino acid sequences onto protein databases in the [FASTA format](https://en.wikipedia.org/wiki/FASTA_format). It takes advantage of the latest advances in string pattern matching to create a self-contained index that can be rapidly queried.

We have implemented queries for peptide sequences as well as sequence tags (alternating series of amino acids and mass gaps as produced by _de novo_ sequencing algorithms).

PeptideMapper can be used standalone in command line or integrated as a dependency in other applications.

For command line options and format specifications, please refer to [PeptideShakerCLI](/compomics-utilities/wiki/peptidemappercli.html). For use as a dependency, please refer to [Usage As Dependency](/compomics-utilities/wiki/usage-as-dependency.html).

  * [Methods](#methods)
  * [Performance](#performance)
  * [Troubleshooting](#troubleshooting)
  * [References](#references)

## Methods ##

### Database Index Creation ###

The first step is to prepare the protein sequences by creating one string with the
pattern: _/protein<sub>1</sub>/protein<sub>2</sub>/…/protein<sub>n</sub>/_ where _protein<sub>i</sub>_ is the i<sup>th</sup> protein sequence in the given database and '/' a separation character preventing
the mapping of peptides on two consecutive proteins. Accordingly, we
compute the suffix array (SA) [\[1\]](#references) of the complete
proteome using [divsufsort](https://github.com/y-256/libdivsufsort), chosen for its [performance](https://github.com/y-256/libdivsufsort/blob/wiki/SACA_Benchmarks.md). Subsequently, the Burrows and Wheeler
transform (BWT) [\[2\]](#references) is computed and stored in a wavelet tree (WT) data
structure [\[3\]](#references) for fast rank queries.

Only the 22 amino acid characters, the four characters for amino acid combinations and '/' complete
the alphabet _&Epsilon;_ for the WT. To save memory, the WT is constructed according to
a corresponding entropy-coded tree [\[4\]](#references) built from the number
of occurrences of every character. Additionally, the accession
numbers extracted from the header are stored for every protein.

We implemented an efficient
function querying all character occurrences within a substring in _O_(_&sigma;_)
where _&sigma;_=|_&Epsilon;_|. The SA is necessary to retrieve the starting positions of
the mapped peptides within a protein. To save memory, we sample the SA
and can retrieve the missing entries by using the last-to-front (LF)-mapping
function [\[5\]](#references) on the BWT.

For both peptide and
sequence tag mapping, we utilize the backward search [\[5\]](#references) which finds all occurrences of a pattern _P_ in a text _T_ in _O_(_p_) where _p_ = |_P_|.

### Peptide Mapping ###

To manage ambiguous amino acids and amino acids with indistinguishable mass, we first
split peptides into their constituent amino acids and create a set of possible amino acids at each
position. _E.g._, ATDWIRK => {A,X}{T,X}{D,B,X}{W,X}{I,L,J,X}{R,X}{K,X}. Theoretically, for this short peptide, we would need to map all possible 384 combinations, but using a dynamic programming
approach we omit mapping of combinations containing prefixes we
previously discarded.

The result is a set of ranges within the suffix array
indicating matches that can be back calculated to the actual positions in
the corresponding proteins. Having the position, we retrieve the accession
number that completes all necessary data for further processing.

### Sequence Tag Mapping ###

_Sequence Tags_ are defined as alternating series of masses and sequences of amino acids. They can be inferred from spectra using sequence tag algorithms or _de novo_ sequencing tools. A simple example is a tag of the following pattern _m<sub>1</sub>-s-m<sub>2</sub>_, where _m<sub>i</sub>_ is a mass and _s_ a partial peptide sequence. Having mapped _s_ as described previously, we try to map the mass _m<sub>1</sub>_. Therefore, we extend _s_ with all possible
preceding sequences in the database creating a set of sequences _s'_. 

For every sequence in _s'_, we store a nominal mass based on the individual amino acid masses and fixed modifications provided. We compute alternative possible masses based on the variable modifications. A sequence in _s'_ is kept when reaching _m<sub>1</sub>_ making a new set of sequences _s"_, and discarded if the nominal mass exceeds _m<sub>1</sub>_ plus a given tolerance mass. Subsequently, we extend every sequence in _s"_ with its possible following amino acids as done previously until reaching _m<sub>2</sub>_. Since this extension is conducted in the opposite direction, we also compute an index for the reversed protein sequences. Having extended _s_ to all sequences matching the tag, all proteins
it appears in as well as the corresponding starting positions are returned.

## Performance ##

For the following benchmark tests, we are using an Intel(R) Xeon(R) 2.80 GHz quad core desktop computer with 16 GB RAM. Note that only one core is used for the performance tests, since the task of mapping independent peptides against a sequence database can be heavily parallelized, the computation time can almost be divided by the number of cores used.

### Protein Sequences Databases and Benchmark Datasets ###

Yeast (May 2016):

  * size: 6,721 Proteins, 3,025,143 residues, 0 _X_ residues
  * fixed modifications: none
  * variable modifications: none
  * fragment tolerance: 0.02 Da

Mouse (May 2016):

  * size: 16,813 Proteins, 9,474,758 residues, 79 _X_ residues
  * fixed modifications: Carbamidomethylation of C
  * variable modifications: none
  * fragment tolerance: 0.02 Da

Human (July 2015):

  * size: 20,207 Proteins, 11,326,153 residues, 670 _X_ residues
  * fixed modifications: Carbamidomethylation of C, Oxidation of M
  * variable modifications: none
  * fragment tolerance: 0.02 Da

Proteogenomics (March 2015) [\[6\]](#references):

  * size: 83,721 Proteins, 13,851,427 residues, 0 _X_ residues
  * fixed modifications: Carbamidomethylation of C, Oxidation of M, Acetylation of K
  * variable modifications: Acetylation of peptide N-term, Pyrolidone from Q, Pyrolidone from E
  * fragment tolerance: 0.5 Da

Metaproteomics (January 2013) [\[7\]](#references):

  * size 55,152 Proteins, 100,955,085 residues, 2,561,698 _X_ residues
  * fixed modifications: Carbamidomethylation of C
  * variable modifications: Oxidation of M, Pyrolidone from Q, Acetylation of peptide N-term
  * fragment tolerance: 0.2 Da

All UniProt proteomes concatenated (July 2016):

 * size: 551,705 Proteins, 197,114,987 residues, 8,027 _X_ residues
 * fixed modifications: Carbamidomethylation of C, Oxidation of M
 * variable modifications: Acetylation of K
 * fragment tolerance: 0.02 Da

For every database listed above, benchmark data sets D = {D1, D2, D3, D4} of different sizes (|D1| = 1,000, |D2| = 10,000, |D3| = 100,000, |D4| = 1,000,000) were created by extracting peptides and tags at random positions in the database. 

### Results - Index Creation ###

| Database      | time [s] | size [MB] |
| ------------- |:------:| :-----:|
| Yeast | 2.55 | 7.02 |
| Mouse | 6.575 | 22.02 |
| Human | 7.49 | 26.33 |
| Proteogenomics | 8.81 | 32.38 |
| Metagenomics | 58.35 | 238.7 |
| All Proteomes | 122.08 | 458.1 |

### Results - Peptide Sequences Mapping Time ###

| Database      | D1 [s] | D2 [s] | D3 [s] | D4 [s] |
| ------------- |:------:| :-----:| :-----:| :-----:|
| Yeast | 0.041 | 0.206 | 1.385 | 12.018 | 7.028 |
| Mouse | 0.057 |0.313 | 2.291 |19.49 |
| Human | 0.056 | 0.403 | 2.297 | 21.35 |
| Proteogenomics | 0.058 | 0.262 | 2.094 | 17.71 |
| Metaproteomics | 0.224 | 1.547 | 13.49 | 134.5 |
| All Proteomes | 0.119 | 0.643 | 6.270 | 62.20 |

### Results - Sequence Tags Mapping Time ###

| Database      | D1 [s] | D2 [s] | D3 [s] | D4 [s] |
| ------------- |:------:| :-----:| :-----:| :-----:|
| Yeast | 0.096 | 0.59 | 3.863 | 33.596 |
| Mouse | 0.167 | 1.196 | 9.910 | 97.106 |
| Human | 0.178 | 1.352 | 11.67 | 114.4 |
| Proteogenomics | 0.297 | 1.546 | 12.16 | 119.1 |
| Metaproteomics | 3.978 | 36.48 | 324.4 | 3154 |
| All Proteomes | 1.417 | 12.85 | 112.8 | 1145.0 |

## Troubleshooting ##

Should you encounter any issue with the usage of PeptideMapper, please create a new entry in the [issue tracker](/compomics-utilities/issues.html).

## References ##

[1] [Manber and Myers, _1st Annual ACM-SIAM Symposium on Discrete Algorithms_, 1990](http://epubs.siam.org/doi/abs/10.1137/0222058)<br>
[2] [Burrows and Wheeler, _Technical report, Digital Equipment
Corporation_, 1994](http://www.hpl.hp.com/techreports/Compaq-DEC/SRC-RR-124.pdf)<br>
[3] [Grossi et al., _Proceedings of the Fourteenth Annual_
_ACM-SIAM Symposium on Discrete Algorithms_, 2003](http://dl.acm.org/citation.cfm?id=644108.644250)<br>
[4] [Huffman, _Proceedings of the Institute of Radio Engineers_, 1952](https://www.ic.tu-berlin.de/fileadmin/fg121/Source-Coding_WS12/selected-readings/10_04051119.pdf)<br>
[5] [Ferragina and Manzini, _Proceedings of the 41st Annual Symposium on Foundations of Computer Science_, 2000](https://people.unipmn.it/manzini/papers/focs00draft.pdf)<br>
[6] [Tanca et al, _PLoS ONE_, 2013](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0082981)<br>
[7] [Crappé et al, _Nucleic Acids Research_, 2014](http://nar.oxfordjournals.org/content/43/5/e29.long)<br>