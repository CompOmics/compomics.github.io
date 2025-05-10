---
title: "MzIdentML Import"
layout: default
permalink: "/projects/meta-proteome-analyzer/wiki/MzIdentML-Import"
tags: wiki, meta-proteome-analyzer
project: "meta-proteome-analyzer"
github_project: "https://github.com/CompOmics/meta-proteome-analyzer"
---

# MzIdentML Import #
For compatibility with existing proteomic database search tools, the import of results files stored in the mzIdentML standard data format (Version 1.2) is possible in the MPA Portable application. This feature is particularly useful for analyzing/reprocessing protein result data that have been generated using external tools or for data obtained from the public domain PRIDE database.
The following tools already support the mzIdentML format (MPA is not listed there yet...):
http://www.psidev.info/tools-implementing-mzidentml

**Project Creation and MzIdentML File Import:**

For the actual file import, an MPA project needs to be created first (in the Project tab). It is then required to navigate to the menu called "Import" at the top and click on the menu item "MzIdentML File" (see screenshot below).

![Import MzIdentML](https://github.com/compomics/meta-proteome-analyzer/blob/master/docu/ImportMzIdentML.png)

This will allow to import database search engine results in mzIdentML format and the respective result data. **Please note** that further protein analysis steps (e.g. grouping of proteins to meta-proteins) can be performed under the "View Results" tab. After the importing of mzIdentML data, the "Results" button should be clickable (see screenshot below).

![Import MzIdentML 2](https://github.com/compomics/meta-proteome-analyzer/blob/master/docu/ImportMzIdentML_2.png)

