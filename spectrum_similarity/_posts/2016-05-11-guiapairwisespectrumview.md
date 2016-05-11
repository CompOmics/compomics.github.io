---
name: GUIapairwisespectrumview
project: spectrum_similarity
layout: default
permalink: /spectrum_similarity/wiki/guiapairwisespectrumview.html
github_project: https://github.com/compomics/spectrum_similarity
---

This GUI enables the manual inspection of how spectra actually look alike and can be downloaded [here](http://genesis.ugent.be/maven2/com/compomics/spectrum_similarity_pairwise_GUI/0.1/spectrum_similarity_pairwise_GUI-0.1.zip).


**1-Start the application:** GUI can be started by running a command prompt in a folder that contains spectrum_similarity_pairwise_GUI-X.Y.Z.jar (X.Y.Z shows the current version number). On the command prompt, the following line needs to be executed:


> java -jar spectrum_similarity_pairwise_GUI-0.1.jar


![startup](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/pairwise/step1_startup.PNG)


**2-Introduce the files:**

The required inputs 
- Two folders containing spectra that are compared (specA and specB, and must be mgf files) 
- A text file containing calculated scores
- Indices of spectrum titles from these two spectra folders in a given text file

![files](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/pairwise/step2_initial.PNG)


**3-Create:** Click on the `CREATE` button to start visualizing pairwise spectra.

 ![after create](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/pairwise/Step2-starting.PNG)


A pairwise spectra can be inspected either as bubble spectra (see above) or mirrored spectra (see below).


![mirror spectra](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/pairwise/Step3-mirror.PNG)



**FILTERING:** Each visualization can be also inspected by applying noise filtering. Clicking the `NoiseFilter` button applies an adaptive noise filtering from [pride-asa-pipeline](/pride-asa-pipeline.html). The resulted remaining percentage can be automatically given.


![NoiseFilterSpecA](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/pairwise/Step4-NoiseFilteringSpecA.PNG)



Alternatively, the sliding bar allows the removal of low-intense peaks corresponding to the remaining percentage of peaks in a given spectrum. 


![FilteringPercentageSpecB](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/pairwise/Step5-FilteringPercentageSpecB.PNG)


Note that column colors and spectrum colors in visualization match. 