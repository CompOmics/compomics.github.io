---
name: PeptideMapper
project: compomics-utilities
layout: default
permalink: /compomics-utilities/wiki/peptidemapper.html
github_project: https://github.com/compomics/compomics-utilities
---

# PeptideMapper


# Efficient Amino Acid Sequence Mapping #

PeptideMapper is a lightweight and efficient application for the mapping of amino acid sequences onto protein databases. It takes advantage of the latest advances in string pattern matching to create a self-contained index that can be rapidly queried. We implemented queries for peptide sequences as well as sequence tags, alternating series of amino acids and mass gaps as produced by _de novo_ sequencing algorithms. PeptideMapper can be used standalone in command line or integrated as dependency to other applications. For command line options, please refer to the [PeptideMapperCLI wiki page] (/compomics-utilities/wiki/peptidemappercli.html).

  * [Methods](#methods)
  * [Performance](#performance)
  * [Troubleshooting](#troubleshooting)

---

## Methods ##

### Database Index Creation ###
The first step is to prepare the proteome by creating one string with the
pattern: /protein1/protein2/…/proteinn/ where proteini is the ith protein
seqence in the given database and / a separation character preventing
the mapping of peptides on two consecutive proteins. Accordingly, we
compute the suffix array (SA) (Manber and Myers, 1990) of the complete
proteome using divsufsort1, which is to date the fastest suffix array
construction algorithm. Subsequently, the Burrows and Wheeler (1994)
transform (BWT) is computed and stored in a wavelet tree (WT) data
structure (Grossi et al., 2003) for fast rank queries. Only the 22 amino
acid characters, the four characters for amino acid groups and ’/’ complete
the alphabet  for the WT. To save memory, the WT is built according to
a corresponding entropy-coded tree (Huffman, 1952) built of the number
of occurrences of every character. Additionally, the UniProt accession
numbers are stored for every protein. We implemented an efficient
function querying all character occurrences within a substring in O()
where  = jj. The SA is necessary to retrieve the starting positions of
the mapped peptides within a protein. To save memory, we sample the SA
and can retrieve the missing entries by using the last-to-front (LF)-mapping
function (Ferragina and Manzini, 2000) on the BWT. For both peptide and
sequence tag mapping, we utilize the backward search (Ferragina and
Manzini, 2000) which finds all occurrences of pattern P in text T inO(p)
where p = jPj.

### Peptide Mapping ###
To manage ambiguous AAs and AAs with indistinguishable mass, we first
split peptides into their AAs and create a set of possible AAs at each
position, e.g., ATDWIRK ! fA; Xg; fT; Xg; fD; B; Xg; fW; Xg; fI; L;
J; Xg; fR; Xg; fK; Xg. Theoretically, for this small example, we should
map all possible 384 combinations, but with a dynamic programming
approach we omit mapping of combinations containing prefixes we
previously discarded. The result is a set of ranges within the suffix array
indicating matches which can be back calculated to the actual positions in
the corresponding proteins. Having the position, we retrieve the accession
number that completes all necessary data for further post-processing.

### SequenceTag Mapping ###
When starting to map a mass against a proteome, a combinatorial explosion
would occur. Therefore, it is reasonable to start the mapping with the
peptide sequence as described in the previous paragraph. For this example,
a tag has the following patternm1􀀀s􀀀m2. Having mapped sequence s,
we try to map the tag mass m1. Therefore, we extend s with all possible
predecessors of s according to the proteome receiving a set of s0. For
every s0 we are storing the current mass. This provides an easy inclusion
of modified AAs with alternated masses. When some s0 has reached m1
after several iterations of extension, s0 will be kept or discarded if the
current mass exceeds m1 plus a given tolerance mass. Since we have to
extend s0 in the opposite direction for m2, we also compute an index for
the reversed proteome. Having extended s0 so that it fits the tag, all proteins
it appears in as well as the corresponding starting positions are inferred.


## Performance ##

For the following benchmark, we are using an Intel(R) Xeon(R) 2.80GHz quad core desktop computer with 16GB RAM. Remark that only one core is used for the performance tests, since the task of mapping independent peptides against a proteome is embarrassingly parallel where the computation time can almost be devided by the number of used cores.

### Datasets and Properties ###

Yeast (May 2016):
  * size: 6721 Proteins, 3025143 residues, 0 X residues containing
  * fixed modifications:
  * variable modifications:
  * fragment tolerance: 0.02Da

Mouse (May 2016):
  * size: 16813 Proteins, 9474758 residues, 79 X residues containing
  * fixed modifications: Cabamidomethylation of C
  * variable modifications:
  * fragment tolerance: 0.02Da

Human (July 2015):
  * size: 20207 Proteins, 11326153 residues, 670 X residues containing
  * fixed modifications: Cabamidomethylation of C, Oxydation of M
  * variable modifications:
  * fragment tolerance: 0.02Da

Metaproteomics (January 2013) [1]:
  * size 55152 Proteins, 100955085 residues, 2561698 X residues containing
  * fixed modifications: Carbamidomethylation of C
  * variable modifications: Oxidation of M, Pyrolidone from Q, Acetylation of peptide N-term
  * fragment tolerance: 0.2Da

Proteogenomics (March 2015) [2]:
  * size: 83721 Proteins, 13851427 residues, 0 X residues containing
  * fixed modifications: Cabamidomethylation of C, Oxydation of M, Acetylation of K
  * variable modifications: Acetylation of peptide N-term, Pyrolidone from Q, Pyrolidone from E
  * fragment tolerance: 0.5Da

All UniProt proteomes (July 2016):
  * size: 551705 Proteins, 197114987 residues, 8027 X residues containing
  * fixed modifications: Cabamidomethylation of C, Oxydation of M
  * variable modifications: Acetylation of K
  * fragment tolerance: 0.02Da


### Results - index creation ###
| Data sets peptides      | time [s] | size [MB] |
| ------------- |:------:| :-----:|
| Yeast | 2.55 | 7.02 |
| Mouse | 6.575 | 22.02 |
| Human | 7.49 | 26.33 |
| Metagenomics | 58.35 | 238.7 |
| Proteogenomics | 8.81 | 32.38 |
| All Proteomes | 122.08 | 458.1 |

### Results - mapping ###
We took pepitde and sequence tag sets D = {D1, D2, D3, D4} of several sizes (|D1| = 1000, |D2| = 10000, |D3| = 100000, |D4| = 1000000) into account and measured the computation time in seconds.

| Data sets peptides      | D1 [s] | D2 [s] | D3 [s] | D4 [s] |
| ------------- |:------:| :-----:| :-----:| :-----:|
| Yeast | 0.041 | 0.206 | 1.385 | 12.018 | 7.028 |
| Mouse | 0.057 |0.313 | 2.291 |19.49 |
| Human | 0.056 | 0.403 | 2.297 | 21.35 |
| Metaproteomics | 0.224 | 1.547 | 13.49 | 134.5 |
| Proteogenomics | 0.058 | 0.262 | 2.094 | 17.71 |
| All Proteomes | 0.119 | 0.643 | 6.270 | 62.20 |

| Data sets tags      | D1 [s] | D2 [s] | D3 [s] | D4 [s] |
| ------------- |:------:| :-----:| :-----:| :-----:|
| Yeast | 0.096 | 0.59 | 3.863 | 33.596 |
| Mouse | 0.167 | 1.196 | 9.910 | 97.106 |
| Human | 0.178 | 1.352 | 11.67 | 114.4 |
| Metaproteomics | 3.978 | 36.48 | 324.4 | 3154 |
| Proteogenomics | 0.297 | 1.546 | 12.16 | 119.1 |
| All Proteomes | 1.417 | 12.85 | 112.8 | 1145.0 |

[1] [Tanca et al: PLoS ONE. 2013.](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0082981)<br>
[2] [Crappé et al: Nucleic Acids Research. 2014.](http://nar.oxfordjournals.org/content/43/5/e29.long)


## Troubleshooting ##

Should you encounter any issue with the usage of PeptideMapper, please create a new entry in the [issue tracker] (/compomics-utilities/issues.html).