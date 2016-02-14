---
name: SettingparametersoftheGUIforthecomparisonofcumulativebinomialderivedscoringfunction
project: spectrum_similarity
layout: default
permalink: /spectrum_similarity/wiki/settingparametersoftheguiforthecomparisonofcumulativebinomialderivedscoringfunction.html
github_project: https://github.com/compomics/spectrum_similarity
---

## Input & Output
`Select the spectra directory` is a path that contains spectra (currently supporting mgf files) 

`Select the comparison spectra directory` is a path that contains spectra in the comparison data set (currently supporting mgf files) 

`Select the output directory` is a path where output text file is stored. 

## Pipeline parameters
`Compare spectra regardless of charge` enables the comparison of spectra with the same precursor charge. If this option is not checked, a spectrum is compared to another one with ignoring precursor charge.

`Precursor tolerence` enables the comparison of spectra within this precursor tolerance (in ppm) against a spectrum on the comparison data set. If this value is set to 0.0, precursor tolerance option is ignored, and any spectrum is compared.

`Fragment tolerence` enables the matching peaks on both spectra within this given fragment tolerance (in Da).

`Consider only the 5 neighbour slice` enables the comparison of the spectra coming from the closer slices on gel runs. The slice name must be existed on the file name of given mgf spectra, separated by "_". Index of slice number on mgf file must be entered on `File name slice index`. For example, `ni_hq_Goat_taenia_hydatigena_rt_1.mgf` shows that the mgf comes from the slice number of 1 and the slice index is 6, note that indexing starts from 0. 


### Preprocessing 

`Preprocessing order` enables the order for preprocesing. Either noise filtering follows to a peak transformation or peak transformation follows to noise filtering.

`Transformaton` enables intensity transformation of peaks. Currently, there are three options avaliable: none, log2 or square root transformation of peak intensities.

`Noise filter` enables noise filtering, removing peaks. Currently, there are three options avaliable: none, [pride-asap](/pride-asa-pipeline.html) -adaptive noise filtering, topN intense peak selection and discarding peaks with less than x% of precursor intensity

`Number of peaks cutoff` is required for `topN intense peak selection` a number of peaks with top intensity to keep on spectrum.

`Peak intensity cutoff (%)` is required for `discarding peaks with less than x% of precursor intensity`: the percentage value of precursor intensity in order to keep any peaks with bigger than this percentaged value.

`Remove precursor ion peak` enables removing peaks derived from precursor peak.

## Other
`Number of threads` is required for multi-threaded spectrum comparison.
