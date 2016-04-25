---
name: 11Xilmassparameters
project: xilmass
layout: default
permalink: /xilmass/wiki/11xilmassparameters.html
github_project: https://github.com/compomics/xilmass
---

**Inputs files related parameters are as follows:**

`givenDBName`: full path to the FASTA file that contains the protein sequences that are cross linked.

`contaminantDBName`: full path to the FASTA file that contains contaminant protein sequences (OPTIONAL). If this information is provided, contaminant proteins are in silico digested and scored. Such contaminant derived spectra will not be included in the final identification list.

`cxDBName`: full path of the search database that contain cross-linked and mono-linked peptides. Required only a name (and no file extension). .

`mgfs`: full path to the folder that contains the mgf files (MS/MS spectra)
resultFolder: full path to the folder with the Xilmass result files for each mgf. An mgf name is written in the title of each of these Xilmass output file.

`resultFolder`: Full path of the folder with the Xilmass result files for each mgf. An mgf name is written in the title of each of these Xilmass output files.

`tdfile`: The validated list of target hits with a given FDR.

`allXPSMoutput`: A list of merged XPSMs 



**Cross-linking experiment related parameters are as follows:**

`crossLinkerName`: A cross-linker name, currently supporting for DSS (d0/d12), BS3(d0/d4), EDC and GA. 

`isLabeled`: T: usage of a heavy labeled cross-linker; F: usage of a light labeled cross-linker; B: usage of both a heavy and light labeled cross-linker

`crossLinkedProteinTypes`: intra: intra-protein cross linking; inter: inter-protein; both: inter- and intra-protein cross linking (case insensitive)

`isConsideredSideReactionSerine`: Whether side reactions are considered (T) or not (F). Enabling this option assumps Serine (S) residue as linkeable for only N-hydroxysuccinimide cross-linkers, such as DSS and BS3

`isConsideredSideReactionThreonine`: Whether side reactions are considered (T) or not (F). Enabling this option assumps Threonine (T) residue as linkeable for only N-hydroxysuccinimide cross-linkers, such as DSS and BS3

`isConsideredSideReactionTyrosine`: Whether side reactions are considered (T) or not (F). Enabling this option assumps Tyrosine(Y) residue as linkeable for only N-hydroxysuccinimide cross-linkers, such as DSS and BS3

`searcForAlsoMonoLink`: T: includes to search also for mono-linked peptides; F: excludes to search for monolinked peptides

`minLen`: minimum length of each peptide allowed in a cross linked-peptide

`maxLenCombined`: maximum total length allowed for a cross-linked peptide

`allowIntraPeptide`: T: includes to search also for intra-peptides (cross linked of the same peptides within the same protein); F: excludes to search for any intra peptide

  



**In silico digestion related parameters are as follows:**

`enzymeName`: enzyme name (the entire list of enzymes can be found on resources/ enzymes.txt)

`miscleavaged`: number of allowed miscleavages 

`lowerMass`: minimum mass of one tryptic peptide in order to include cross-linked peptide combinations

`higherMass`: maximum mass of one tryptic peptide in order to include cross-linked peptide combinations




**Peptide modifications related parameters are as follows:**

`fixedModification`: list of fixed PTM names. Each PTM must be introduced via semi-colon (case insensitive)

`variableModification`: list of variable PTM names. Each PTM must be introduced via semi-colon (case insensitive)

`maxModsPerPeptide`: number of maximum allowed variable modifications per peptide. 




**Scoring related parameters are as following:**

`fragMode`: Fragmentation modes are as follows: HCD (b and y ions also a2); CID (b and y ions), ETD (c and z ions). 

`peptide_tol_total`: Total number of peptide_tol windows. Make sure to give the right value, peptide_tol_total=1 will only identify peptide_tol_1 even if there are other mass-windows given.

`peptide_tol1`: The first opened-peptide_tol window in either PPM or Da according to is_peptide_tol1.

`is_peptide_tol1_PPM`: Unit of the first opened-peptide_tol window is either PPM (T) or Da (F)

`peptide_tol1_base`: Center of peptide_tol1 mass window. For example, peptide_tol1 as 2Da with peptide_tol_base as 1.5Da will open a window with values of -0.5Da to 3.5Da. Note that the unit of this base is always Dalton.


`peptide_tol2`: The second opened-peptide_tol_window

`is_peptide_tol2_PPM`: The unit of the second opened-peptide_tol_window

`peptide_tol2_base`: Center of peptide_tol2 mass window


`peptide_tol3`: The third opened-peptide_tol_window

`is_peptide_tol3_PPM`: The unit of the third opened-peptide_tol_window

`peptide_tol3_base`: Center of peptide_tol3 mass window.


`peptide_tol4`: The fourth opened-peptide_tol_window

`is_peptide_tol4_PPM`: The unit of the fourth opened-peptide_tol_window

`peptide_tol4_base`: Center of peptide_tol4 mass window.


`peptide_tol5`: The fifth opened-peptide_tol_window

`is_peptide_tol5_PPM`: The unit of the fifth opened-peptide_tol_window

`peptide_tol5_base`: Center of peptide_tol5 mass window.



`msms_tol`: Fragment mass tolerance (in Dalton)

`report_in_ppm`: Reporting MS1 differences in either PPM(T) or Da (F).

`minRequiredPeaks`: Number of minimum required theoretical peaks along peptide-bonds from each peptide. 



**Spectrum processing related parameters are as follows:**

`massWindow`: mass value to divide spectrum into windows during scoring	

`minimumFiltedPeaksNumberForEachWindow`: minimum number of filtered peaks per mass window during scoring - Inclusive (Default=1)

`maximumFiltedPeaksNumberForEachWindow`: Set maximum number of filtered peaks per mass window during scoring - Inclusive(Default=10)


`minPrecMassIsotopicPeakSelected`: minimum precursor mass (Da) that C13 peak might be selected over C12 (we start observing C13 peak selection above this given precursor mass).

`deisotopePrecision`: Allowed tolerance between the C12 peak and the C12 with one C13 fragment peak (in Da).

`deconvulatePrecision`: The precision to select if a singly charged and its deconvoluted peak exist within this precision value (in Da).



**Multi-threading and validation related parameters are as follows:**

`threadNumbers`: number of cores for multithreading 

`isPercolatorAsked`: T: Write separate Percolator input files; F: Do not write Percolator input files (Still not fully-functional and tested)

`isSPLITFDR`: T: splits the XL sites lists into two groups and computes FDR for each sub-XL sites with the following 

`fdrInterPro` and `fdrIntraPro` parameters. F: computes FDR from all XL sites without splitting with using `fdr` option

`fdrInterPro`: A double value to compute FDR from only inter-protein XL site containing XPSMs by splitting XPSMs into two group as inter-protein and intra-protein XL sites lists. 

`fdrIntraPro`: A double value to compute FDR from only intra-protein XL site containing XPSMs by splitting XPSMs into two group as inter-protein and intra-protein XL sites lists.

`fdr`: A double value to compute FDR with all XL sites; this is only function if isSPLITFDR is set to F.
