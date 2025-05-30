---
title: "DatabaseUpdates"
layout: default
permalink: "/projects/ms-lims/wiki/DatabaseUpdates"
tags: wiki, ms-lims
project: "ms-lims"
github_project: "https://github.com/CompOmics/ms-lims"
---

# Database updates

**Save the ms-lims update scripts as .cdf and apply them by using the ConfigurationGUI in the ms-lims menu.**

### 7.2 to 7.5 (2010-08-30)

  * Create a new scan table to persist spectrum retention time.
  * Alter the spectrum table to add two variables for the mass-to-charge ratio and the charge value
  * Populate these fields and the new scan table with all existing data.

[conversion_72_75.cdf](https://github.com/compomics/ms-lims/blob/master/rdbms/conversion/7.2_to_7.5/conversion_72_75.cdf)

----

### 7.1 to 7.2 (2010-07-01)

  * Update the package names for all StorageEngines.
  * Create a table for quantiation_groups for n:n mappings between identifications and quantitations.
  * Create a table spectrum_file table for BLOB dumps of the actual MS/MS spectra.
  * Move all BLOB entries from spectrumfile to spectrum.
  * Rename spectrumfile into spectrum.

[conversion_71_72.cdf](https://github.com/compomics/ms-lims/blob/master/rdbms/conversion/7.1_to_7.2/conversion_71_72.cdf)

----

### 7.0 to 7.1 (2010-03-01)

  * Addition of two new columns: highest_peak_in_spectrum and total_spectrum_intensity
  * Automatic population of these two columns
  * Set both highest_peak_in_spectrum and total_spectrum_intensity to 'not null' status with a default of '0.0'.

[conversion_70_71.cdf](https://github.com/compomics/ms-lims/blob/master/rdbms/conversion/7.0_to_7.1/conversion_70_71.cdf)
