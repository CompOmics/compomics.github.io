---
name: Standalonehowtorunaprobabilisticbasedscoringfunctiontocomparetwogivenspectradatasets
project: spectrum_similarity
layout: default
permalink: /spectrum_similarity/wiki/standalonehowtorunaprobabilisticbasedscoringfunctiontocomparetwogivenspectradatasets.html
github_project: https://github.com/compomics/spectrum_similarity
---

The stand-alone tool can be started by running a command prompt on a folder that contains scoring_pipeline-X.Y.Z.jar (X.Y.Z shows the current version number). On the command prompt, the following line needs to be executed:

> java -cp scoring_pipeline-1.0.jar main.ScorePipeline
 
Parameters must be introduced on MS2Similarity.properties. Parameters are explained [here](https://github.com/compomics/spectrum_similarity/wiki/Setting-parameters-for-the-stand-alone-application-%28MS2Similarity.properties%29)