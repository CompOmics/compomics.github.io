---
name: 22SettingparametersofthestandaloneapplicationMS2Similarityproperties
project: spectrum_similarity
layout: default
permalink: /projects/spectrum_similarity/wiki/22settingparametersofthestandaloneapplicationms2similarityproperties.html
github_project: https://github.com/compomics/spectrum_similarity
---

## Input parameters

`spectra.folder` is the path that contains spectra (currently supporting mgf files) 

`spectra.to.compare.folder` is the path that contains spectra in the comparison data set (currently supporting mgf files) 

`output.folder` is the path where output text file is stored. 


## Calculation parameters
`is.charged.based` enables the comparison of spectra with the same precursor charge. If this option is not checked, a spectrum is compared to another one ignoring the precursor charge. (`is.charged.based=true` on, `is.charged.based=false` off)

`precursor.tolerance` enables the comparison of spectra within this precursor tolerance (in ppm) against a spectrum of the comparison data set. If this value is set to `precursor.tolerance=0`, precursor tolerance option is ignored, and any spectrum is compared.

`fragment.tolerance` enables the matching peaks on both spectra within this given fragment tolerance (in Da).

`calculate.only5` enables the comparison of the spectra coming from the closer slices on gel runs. The slice name must be part of the file name of a given mgf spectra, and separated by "_". The index of the slice number of the mgf file must be given on `slice.index`. For example, `ni_hq_Goat_taenia_hydatigena_rt_1.mgf` shows that the mgf comes from the slice number 1 and the slice index is 6, note that indexing starts from 0 (`calculate.only5=true` on, `calculate.only5=false` off).

##Preprocessing parameters

`transformation` enables intensity transformation of peaks. Currently, there are three options avaliable: `transformation=0`: none, `transformation=1`: log2 or `transformation=2`: square root transformation of peak intensities. Must be one of these three integer values!

`noise.filtering` enables noise filtering, by removing peaks. Currently, there are three options avaliable: `noise.filtering=0`: none, `noise.filtering=1`: [pride-asap](/projects/pride-asa-pipeline.html)-adaptive noise filtering, `noise.filtering=2`: topN intense peak selection and `noise.filtering=3`: discarding peaks with less than x% of the precursor intensity. Must be one of these four integer values!

`topN` is required for `noise.filtering=2`. A number of peaks with top intensity to keep in a spectrum. Must be an integer value!

`percent` is required for `noise.filtering=3`. The percentage value of precursor intensity in order to keep any peaks with bigger than this percentaged value. Must be a double value between 0-100!

`precursor.peak.removal` enables removing peaks derived from the precursor peak (`precursor.peak.removal=true` on, `precursor.peak.removal=false` off).

`isNFTR` enables the order for preprocesing. Either noise filtering follows to a peak transformation (`isNFTR=true`) or peak transformation follows to noise filtering (`isNFTR=false`).

## Other
`thread.numbers` is required for multi-threaded spectrum comparison. Shows the number of threads.