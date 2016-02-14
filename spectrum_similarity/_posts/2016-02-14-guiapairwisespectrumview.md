---
name: GUIApairwisespectrumview
project: spectrum_similarity
layout: default
permalink: /spectrum_similarity/wiki/guiapairwisespectrumview.html
github_project: https://github.com/compomics/spectrum_similarity
---

This GUI enables the manual inspection how spectra actually look alike with corresponding to similarity score and can be downloaded [here](http://genesis.ugent.be/maven2/com/compomics/spectrum_similarity_pairwise_GUI/0.1/spectrum_similarity_pairwise_GUI-0.1.zip).

The required inputs 
- Two folders containing spectra that are compared (specA and specB, and must be mgf files) 
- A text file containing calculated scores
- Indices of spectrum titles from these two spectra folders on a given text file. 

After introducing these inputs, a pairwise spectra can be inspected by either bubble spectra or mirrored spectra, with allowing filtering either based on percentage remaining peaks or adaptive noise filtering from [pride-asa-pipeline](/pride-asa-pipeline.html) ive noise filtering from pride-asa-pipeline 