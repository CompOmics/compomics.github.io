---
name: 1StepbystepHowtorunXilmass
project: xilmass
layout: default
permalink: /xilmass/wiki/1stepbystephowtorunxilmass.html
github_project: https://github.com/compomics/xilmass
---

Xilmass is open-source and freely available under the permissive Apache2 license and works on Windows, Linux and OS-X operating systems. Xilmass is implemented in Java with [Apache-Lucene] (http://lucene.apache.org/) for the database indexing. Therefore, you have to make sure that [JDK] (http://www.oracle.com/technetwork/java/javase/downloads/index.html) is already installed on your computer environment. The current program works as a standalone version which can be run by following the steps described underneath. 


**1-** Update the configuration file (xLink.properties) according to your search settings. Detailed information on the different parameters can be found on [here] (https://github.com/compomics/xilmass/wiki/1.1.-Xilmass-parameters).
 
**2-** Make sure that your database contains both target and decoy sequences. Note that you can use [DBToolKit] (/dbtoolkit.html) to generate your decoy database. The header of every decoys must contain either `REVERSED` or `SHUFFLED` next to the accession number position.

**IMPORTANT**: If your decoy headers contain `_REVERSED` or `_SHUFFLED` next to the accession number, the underscore `_` from this header will be removed.

**3-** In order to run Xilmass execute the following line on the command prompt
<java –jar xilmass.X.Y.Z.jar> 
Note that X.Y.Z stands for version number. Currently avaliable Xilmass is `xilmass.0.2.jar`

After running Xilmass, there will be a fastacp file on the given cxDBName. This search database is composed  of all possible generated cross-linked peptides. The details on the presentation of this cross-linked peptide database can be found on [here](https://github.com/compomics/xilmass/wiki/2.-Database-entries)
