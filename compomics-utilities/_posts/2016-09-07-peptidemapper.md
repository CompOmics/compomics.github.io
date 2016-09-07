---
name: PeptideMapper
project: compomics-utilities
layout: default
permalink: /compomics-utilities/wiki/peptidemapper.html
github_project: https://github.com/compomics/compomics-utilities
---

For the following benchmark, we are using an Intel(R) Xeon(R) 2.80GHz quad core desktop computer with 16GB RAM. Remark that only one core is used for the performance tests, since the task of mapping independent peptides against a proteome is embarrassingly parallel where the computation time can almost be devided by the number of used cores.

## Datasets and Properties ##

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


## Results - index creating ##
| Data sets peptides      | time [s] | size [MB] |
| ------------- |:------:| :-----:|
| Yeast | 2.55 | 7.02 |
| Mouse | 6.575 | 22.02 |
| Human | 7.49 | 26.33 |
| Metagenomics | 58.35 | 238.7 |
| Proteogenomics | 8.81 | 32.38 |
| All Proteomes | 122.08 | 458.1 |

## Results - mapping ##
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