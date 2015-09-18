---
name: 22RunExecution
project: pladipus
layout: default
permalink: /pladipus/wiki/22runexecution.html
github_project: https://github.com/compomics/pladipus
---

## Execution mode

* The execution mode is command line only and has several switches

### Drawing jobs from the queue
  
To pull a single task: `java -jar Pladipus-execution-X.Y.Z.jar -pull`

To pull tasks continuously: `java -jar Pladipus-execution-X.Y.Z.jar -auto_pull`

### Posting jobs to the queue

Jobs can be posted to pladipus using the following command : 

`java -jar Pladipus-execution-X.Y.Z.jar -push -template [template.xml] -job_config [config.tsv] -u [username] -p [password]`

----