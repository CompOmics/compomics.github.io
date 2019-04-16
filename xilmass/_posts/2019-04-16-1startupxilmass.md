---
name: 1StartupXilmass
project: xilmass
layout: default
permalink: /projects/xilmass/wiki/1startupxilmass.html
github_project: https://github.com/compomics/xilmass
---

To start using Xilmass, unzip the downloaded file from [here](https://github.com/compomics/xilmass/blob/master/README.md).
<br> </br>

Xilmass can start identifying by **double clicking** over the  xilmass-X.Y.Z.jar (X.Y.Z shows the current version number).  

If that is not the case, please run a command prompt on a folder that contains xilmass-X.Y.Z.jar with following step. 

On the command prompt: 

**to run the a graphical user-interface (GUI) version for the identification of cross-linked peptides in your sample:**

> java -jar Xilmass-X.Y.Z.jar

![GUI-to-identify](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/xilmass/1.1.GUI-to-identify-start-up.PNG)

Follow the instruction [here](https://github.com/compomics/xilmass/wiki/2.-Instructions-to-run-GUI-for-the-identifications-of-cross-linked-peptides). 


### Further options to run Xilmass
Xilmass can be run as a command line which can be easily plug in your pipeline. Moreover, Xilmass can be also performed to visualize how experimental spectrum is annotated by Xilmass. 

To achieve this, please run a command prompt on a folder that contains xilmass-X.Y.Z.jar with following step. 

On the command prompt: 
 
 
**to run the command-line (CLI) version for the identification of cross-linked peptides in your sample:**

> java -jar Xilmass-X.Y.Z.jar -c

![CLI-to-identify](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/xilmass/1.1.CLI-to-identify-start-up.PNG)

Follow the instruction [here] (https://github.com/compomics/xilmass/wiki/3.-Instructions-to-run-CLI-for-the-identification-of-cross-linked-peptides). 
<br> </br>
Please make sure that [resources/xLink.properties] (https://github.com/compomics/xilmass/wiki/3.1.-Xilmass-parameters-CLI) have the right settings.

<br> </br>
<br> </br>
**to run GUI to inspect identified peptide-to-spectrum matches by Xilmass:**

> java -jar Xilmass-X.Y.Z.jar -r

![GUI-to-inspect](https://dl.dropboxusercontent.com/u/10018463/github_wiki_pages/xilmass/1.1.GUI-to-inspect-ids.PNG)

Follow the instruction [here] (https://github.com/compomics/xilmass/wiki/4.-Visualizing-the-Xilmass-peptides-to-spectrum-matches). 
<br> </br>



<br> </br>
<br> </br>
**Furthermore, there are other parameters with following functionalities:**
> java -jar Xilmass-X.Y.Z.jar -h

to provide information for the available commands.  
<br> </br>