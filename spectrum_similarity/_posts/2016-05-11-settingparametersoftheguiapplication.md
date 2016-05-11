---
name: SettingparametersoftheGUIapplication
project: spectrum_similarity
layout: default
permalink: /spectrum_similarity/wiki/settingparametersoftheguiapplication.html
github_project: https://github.com/compomics/spectrum_similarity
---

## Input & Output
`Select the spectra directory` is the path that contains spectra (currently supporting mgf files).

`Select the comparison spectra directory` is the path that contains spectra in the comparison data set (currently supporting mgf files).

`Select the output directory` is the path where output text file is stored. 

## Pipeline parameters
`Compare spectra regardless of charge` enables the comparison of spectra with the same precursor charge. If this option is not checked, a spectrum is compared to another one ignoring the precursor charge.

`Precursor tolerance` enables the comparison of spectra within this precursor tolerance (in ppm) against a spectrum of the comparison data set. If this value is set to 0.0, the precursor tolerance option is ignored, and any spectrum is compared.

`Fragment tolerance` enables the matching peaks of both spectra within this given fragment tolerance (in Da).

`Consider only the 5 neighbour slice` enables the comparison of the spectra coming from the closer slices on gel runs. The slice name must be part of the file name of a given mgf spectra, separated by "_". the index of the slice number of the mgf file must be given on `File name slice index`. For example, *ni_hq_Goat_taenia_hydatigena_rt_1.mgf* shows that the mgf comes from *slice number 1* and the *slice index* is *6*, note that indexing starts from 0. 


### Preprocessing 

`Preprocessing order` enables to change the order for preprocesing. Either noise filtering follows to a peak transformation or peak transformation follows to noise filtering.

`Transformation` enables intensity transformation of peaks. Currently, there are three options avaliable: none, log2 or square root transformation of peak intensities.

`Noise filter` enables noise filtering by removing peaks. Currently, there are three options avaliable: none, [pride-asap](/pride-asa-pipeline.html)-adaptive noise filtering, topN intense peak selection and discarding peaks with less than x% of precursor intensity

`Number of peaks cutoff` is required for `topN intense peak selection` a number of peaks with top intensity to keep in a spectrum.

`Peak intensity cutoff (%)` is required for `discarding peaks with less than x% of the precursor intensity`: the percentage value of the precursor intensity in order to keep any peak larger than this percentaged value.

`Remove precursor ion peak` enables removing peaks derived from the precursor peak.

## Other
`Number of threads` is required for multi-threaded spectrum comparison.
