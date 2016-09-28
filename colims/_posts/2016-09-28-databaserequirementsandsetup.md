---
name: DatabaseRequirementsAndSetup
project: colims
layout: default
permalink: /colims/wiki/databaserequirementsandsetup.html
github_project: https://github.com/compomics/colims
---

# Database requirements and setup 
 
  * [Introduction](#introduction)
  * [System requirements](#system-requirements)
  * [Database](#database)

## Introduction

Before using colims for the first time, some one-time installation steps have to be executed. The following paragraphs will guide you through this procedure.

## System requirements

As a single-user setup, colims can run on any modern laptop or desktop PC. Furthermore, since it is written in Java, it can run on any platform that supports a Java Virtual Machine version 1.7.0 or above (Windows, Linux, and Mac OS-X). However, if colims is to be used as a shared system between many different users, it will be more practical to set up a central database on a dedicated server that multiple users can access simultaneously. This task can easily be handled by any modern desktop machine with sufficient storage space.  

## Database

### Requirements
Colims uses a relational database as data repository. The system is able to run on both [MySQL](http://dev.mysql.com/) 5.x and [MariaDB](https://mariadb.org/en/) - two freely downloadable and commonly used data management solutions. After installation, please increase the maximum allowed package size in the *.ini* file (e.g. `max_allowed_packet=256M` or higher). [PostgreSQL](http://dev.mysql.com/) is supported as well, although we haven't tested it extensively.

### Schema
Once the database server is installed, the schema with the colims tables, fields and relationships can be created.

  1. connect to the database server (with the database command line tool or a database client like [MySQL Workbench](http://www.mysql.com/products/workbench/) or [SQuirreL SQL](http://www.squirrelsql.org/))
  2. create a new schema in the connected server and set it as the default schema
  3. MySQL or MariaDB: run the [MySQL setup script](http://genesis.ugent.be/colims/colims_db_setup.sql). PostgreSQL: run the [setup script](http://genesis.ugent.be/colims/colims_db_setup_postgres.sql PostgreQL). The script creates the necessary tables, indexes, keys and inserts some default records into the database.

In principle, colims is designed to be able to run on other SQL databases as well, but some SQL syntax and code adjustments may be necessary. Let us know and we'll try to help you as much as possible.

### Results - Peptide Sequences Mapping Time ###


| Database      | D1 [s] | D2 [s] | D3 [s] | D4 [s] |
| ------------- |:------:| :-----:| :-----:| :-----:|
| Yeast | 0.041 | 0.206 | 1.385 | 12.018 |
| Mouse | 0.057 |0.313 | 2.291 |19.49 |
| Human | 0.056 | 0.403 | 2.297 | 21.35 |
| Proteogenomics | 0.058 | 0.262 | 2.094 | 17.71 |
| Metaproteomics | 0.224 | 1.547 | 13.49 | 134.5 |
| All Proteomes | 0.119 | 0.643 | 6.270 | 62.20 |


testing