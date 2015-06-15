# Compomics Documentation Website

---

This repository contains the compomics.github.io site, which collates documentation from all Compomics projects on Github. The site is built automatically as the result of a Jenkins build triggered by a Github webhook. This runs a Groovy postbuild script (see [https://gist.github.com/iain8/d6cd41e4e2ef920c50af](here)) which passes the project name and required urls to the shell script `generate-docs.sh`, which retrieves the readme and wiki files and adds the necessary front-matter for Jekyll to parse them.