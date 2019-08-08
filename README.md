# compomics.github.io
Overview and documentation of CompOmics GitHub repositories.

## Run website locally
- Install Jekyll requirements
- Install webpage dependencies: `bundle install`
- Run Jekyll web server: `bundle exec jekyll serve`
- The website is now hosted at http://localhost:4000

## Create pages for GitHub repositories
The entire pages folder can be generated automatically by `generate_docs.py`.
This script can be configured trough a YAML config file or the command line
interface (run `python generate_docs.py -h`). See `requirements.txt` for the
required Python packages.

### Folder structure
Requires the following folder structure for projects:
```
pages/
|-- sample_project/
    |-- sample_project.md
    |-- wiki/
        |-- sample_wikipage.md
        |-- sample_wikipage2.md
```
where every GitHub repository has one folder with in its root the README file
and a subfolder containing all wiki pages of that repository.


### Jekyll file headers
The project markdown files need to contain the following items in their header:

#### README file
```
---
name: "simple"
description: "A simple tool"
layout: default
tags: project_home, simple
permalink: /projects/simple
project: simple
github_project: "https://github.com/compomics/simple"
---
```

#### Wiki page
```
---
name: docs
title: docs
layout: default
permalink: "/projects/simple/wiki/docs"
tags: wiki, simple
project: simple
github_project: https://github.com/compomics/simple
---
```

# Created with
- Jekyll template [Boostrap 4 Github Pages](https://nicolas-van.github.io/bootstrap-4-github-pages/).
- Bootstrap 4
- Font Awesome 4.7.0
- ...