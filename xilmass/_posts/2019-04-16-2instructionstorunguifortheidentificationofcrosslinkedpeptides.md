---
name: 2InstructionstorunGUIfortheidentificationofcrosslinkedpeptides
project: xilmass
layout: default
permalink: /projects/xilmass/wiki/2instructionstorunguifortheidentificationofcrosslinkedpeptides.html
github_project: https://github.com/compomics/xilmass
---

Xilmass GUI has seven panels, which allows users to easily to give their settings. <br> Note that *a user must provide the parameters indicated by an asterisk*. 

 * [Input/Output](#inputoutput)
 * [Cross-linking](#cross-linking)
 * [In-silico digestion](#in-silico-digestion)
 * [Modifications](#modifications)
 * [Scoring](#scoring)
 * [Spectrum preprocessing](#spectrum-preprocessing)
 * [Multithreading and validation](#multithreading-and-validation )


## Input/Output

`Select the FASTA database`: Provide the full path to the FASTA file that contains the protein sequences that are cross linked. Please make sure that your database is in the right format (See [here] (https://github.com/compomics/xilmass/wiki/5.-Database)). 

`Select the contaminants FASTA database`: Provide the full path to the FASTA file that contains contaminant protein sequences (OPTIONAL). If this information is provided, contaminant proteins are in silico digested and scored but such contaminant derived spectra will not be included in the final identification list. If you **dont give** any contaminant database, please make sure **this entry is empty**. 

`Select the cross-linked and mono-linked peptides search database`: Provide the full path of the search database that contains cross-linked and, if selected for monolinked peptides searching, mono-linked peptides. Requires only a folder. For running the first time, it is recommended to introduce an empty folder. 

If it is the first time to search Xilmass against your database of interest, Xilmass will generate both a search database file and a folder for indexing. The search database is constructed based on your selected parameters on **Cross-linking** panel. 

If you previously searched your database, Xilmass tries to locate previously indexed database on the given folder. 

The search database contains cross-linked peptides, and if selected, also mono-linked peptides. Details about the search database can be found [here] (https://github.com/compomics/xilmass/wiki/5.-Database)). Briefly, the search database has very similar to a fasta format but a modified version of fasta. The first-time constructed search database will have the name of the FASTA database and "cx" with an extension of the cross-linked peptide database (*".fastacp"*).

`Select the spectra files directory`: Provide the full path to the folder that contains the mgf files (MS/MS spectra). Currently supporting mgf files. 

`Select the output file directory`: Provide the full path of the folder with the Xilmass result files for each give mgf file. An mgf name is written for the title of each of these Xilmass output files. When Xilmass executes searching, there will be also one file which contains all XPSMs (allXPSMs_list.txt), one file file which contains the validated XPSMs (validatedXPSMs_list.txt), and one file which contains the search settings (settings.txt)


![Input-Output](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/xilmass/GUI/2.1.Start.PNG)




## Cross-linking

`Select the cross-linker*`: A cross-linker name, currently supporting for DSS (d0/d12), BS3(d0/d4), EDC and GA. 

`Select the labeling type of a cross-linker¨*`: `heavy` is for the usage of a only heavy labeled cross-linker; `light` is for the usage of a light labeled cross-linker and `both` is for the usage of both a heavy and light labeled cross-linker.

`Consider side reactions (only for N-hydroxysuccinimide cross-linkers, such as DSS and BS3) for`: This option enables to assume that serine, threonine and/or tyrosine as a linkable for only N-hydroxysuccinimide cross-linkers, such as DSS and BS3.

`Select the cross-linking type*`: `intra` shows intra-protein cross linking; `inter` shows inter-protein cross-linking; and `both` shows inter- and intra-protein cross linking.

`Mono-linking*`: This option enables including searches also for mono-linked peptides (recommended).

`Minimum peptide length*`: A minimum length of each peptide allowed in a cross linked-peptide

`Maximum total length of cross-linked peptides*`: A maximum length of a pair of cross-linked peptides allowed in a cross linked-peptide

`Intra-linking`: This option allows to include searches also for intra-peptides (cross linking of the same peptides within the same protein)


![Cross-linking](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/xilmass/GUI/2.1.XL.PNG)



## In-silico digestion

`Select the enzyme used for the in-silico digestion*:` Select an enzyme from the provided list.

`Allowed number of miscleavages*:` Provide number of allowed miscleaveges

`Minimum peptide mass considered for cross-linked combinations*:` The minimum mass of one putative peptide in order to include cross-linked peptide combinations

`Maximum peptide mass considered for cross-linked combinations*:` The maximum mass of one putative peptide in order to include cross-linked peptide combinations

![In-silico digestion](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/xilmass/GUI/2.1.Digestion.PNG)


## Modifications

`Select the fixed modifications*:` Select fixed modifications from the given modification list. 

`Select the variable modifications*:` Select variable modifications from the given modification list. 

`Maximum number of variable modifications per peptide*:` Provide a number of maximum allowed variable modifications per peptide. 


![Modifications](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/xilmass/GUI/2.1.Mods.PNG)


## Scoring

`Select the neutral losses to consider*:` This option allows including peaks for neutral losses while scoring. The first option is no neutral losses are taken into account. The second option introduces only singly charged water losses for D/E/S/T and ammonia losses for K/N/Q/R in the presence of the parent ions, as implemented in [Andromeda](http://pubs.acs.org/doi/abs/10.1021/pr101065j). The last option is to introduce all water and ammonia losses are considered (both singly and doubly charged).

`Select the fragmentation mode*:` Select one of the enlisted fragmentation modes, which as HCD (b and y ions also a2); CID (b and y ions), ETD (c and z ions). 

`Select the number of peptide tolerance windows*:` Provide the total number of peptide tolerance windows.

`Peptide mass tolerance window 1:` The first opened peptide tolerance window in either PPM or Da. `Base` is the center of this peptide tolerance mass window. For example, if its `Value `is 2Da with its `Base` of 1.5Da will open a window with values of -0.5Da to 3.5Da. Note that the unit of this base is always Dalton.

`Peptide mass tolerance window 2:` The second opened peptide tolerance window in either PPM or Da. `Base` is the center of this peptide tolerance mass window.

`Peptide mass tolerance window 3:` The third opened peptide tolerance window in either PPM or Da. `Base` is the center of this peptide tolerance mass window.

`Peptide mass tolerance window 4:` The fourth opened-peptide tolerance window in either PPM or Da. `Base` is the center of this peptide tolerance mass window.

`Peptide mass tolerance window 5:` The fifth opened peptide tolerance window in either PPM or Da. `Base` is the center of this peptide tolerance mass window.

`Fragment mass tolerance*:` Provide the fragment mass tolerance value (in Dalton)

`Minimum number matched peaks for cross-linked peptides*:` Number of minimum required theoretical peaks along peptide-bonds from each peptide in order to keep this cross-linked peptides to spectrum matches.

`Peak matching`: This option allows finding either all matched theoretical peaks within a tolerance or only the closest theoretical peak within a tolerance.

`MS1 mass differences reporting unit*:` Select the unit to report MS1 differences on the final list.


![Scoring](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/xilmass/GUI/2.1.Scoring.PNG)


## Spectrum preprocessing

`Spectrum scoring mass window value*:` Provide the mass value to divide spectrum into windows/bins during scoring	

`Minumum number of filtered peaks per window*:` Provide the minimum number of filtered peaks per mass window during scoring - Inclusive 

`Maximum number of filtered peaks per window*:` Provide the maximum number of filtered peaks per mass window during scoring - Inclusive

`Lower precursor mass bound for selecting the C13 peak over the C12 peak*:` Provide the minimum precursor mass (Da) that C13 peak might be selected over C12 (the point on which we start observing C13 peak selection above this given precursor mass).

`Deisotope precision`: Provide the allowed tolerance between the C12 peak and the C12 with one C13 fragment peak (in Da).

`Deconvulate precision`: Provide the precision value to select if a singly charged and its deconvoluted peak exist within this precision value (in Da).


![Spectrum preprocessing](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/xilmass/GUI/2.1.SpectrumProcessing.PNG)


## Multithreading and validation

`Number of threads`: Provide the number of cores for multithreading 

`Write separate Percolator input files*`: Enables writing separate Percolator input files. Currently, being tested and not fully-function yet


`FDR calculation*:` Select either `improved` or `global`. `improved` splits the XL sites lists into two groups and computes FDR for each sub-XL sites according to the given values of `Inter-protein improved FDR value*` and `Intra-protein improved FDR value*`. In case of the selection of `global`, FDR is being computed with all XL sites, according to user given value of `Global FDR value*`

![Multithreading and validation](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/xilmass/GUI/2.1.MultithreadingValidation.PNG)