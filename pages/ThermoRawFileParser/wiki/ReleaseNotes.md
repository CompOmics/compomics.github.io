---
title: "ReleaseNotes"
layout: default
permalink: "/projects/ThermoRawFileParser/wiki/ReleaseNotes"
tags: wiki, ThermoRawFileParser
project: "ThermoRawFileParser"
github_project: "https://github.com/compomics/ThermoRawFileParser"
---

# ReleaseNotes

---

**Changes in ThermoRawFileParser 1.4.0 (June 10. 2022):**

* Precursor intensity was added to mzML files
> Precursor intensity is now included in mzML output, the output should be fairly similar to ProteoWizard. However, the intensity value should be used with caution, see [Issue 125](/projects/ThermoRawFileParser/issues/125) and cited issues.
* Support for all possible MS levels
> All MS levels are included in the output, previously only up to MS3; mapping precursor scans using new method [Issue 126](/projects/ThermoRawFileParser/issues/126)
* `-x` switch has reversed its meaning
> When `-x` is defined reference and exception data will be excluded from the output, by default they will be included. Similar to Proteowizard.
* Plain mzML (non-indexed) is forced when using `-s` and mzML format
> When using output to STDOUT and mzML format, the format will be always non-indexed [Issue 118](/projects/ThermoRawFileParser/issues/118)
* Updated ontology terms for ionization methods (HUPO PSI-MS version 4.1.79)
> Added / updated ionization methods, [Issue 128](/projects/ThermoRawFileParser/issues/128) Thank you, @[abdelq](https://github.com/abdelq)
* Switch to include noise and baseline data (`-N`)
> With the new switch `-N|noiseData` noise and baseline data can be included in mzML output [Issue 130](/projects/ThermoRawFileParser/issues/130) Thank you, @[GeorgWa](https://github.com/GeorgWa)
* Spectral points are sorted by mass
> [Issue 117](/projects/ThermoRawFileParser/issues/117)
* Metadata, format, and logging switches recognize both numeric and string values of parameters
> It is possible to use both text representation (case-insensitive) and numeric representation for switches, i.e. `-f mzml` and `-f 1` are the same [Issue 121](/projects/ThermoRawFileParser/issues/121)

---

**Changes in ThermoRawFileParser 1.3.4 (April 20. 2021):**

* Disable peak picking for specified MS levels
* Rollback of ThermoRawFileParser CV term until downstream tools update their PSI-MS CV

---

**Changes in ThermoRawFileParser 1.3.3 (April 01. 2021):**

* Removed BOM prefix in indexed mzML output
* Addition of MS:1000576 (no compression) CV term when no compression is used
* Same metadata output for both TEXT and JSON formats
* FAIMS compensation voltage output
* Thermo libraries upgrade to 5.0.0.71
* `-s, --stdout` option addition for writing to standard out (mostly for Windows)

---

**Changes in ThermoRawFileParser 1.3.2 (Oct 02. 2020):**

* Flag -x include reference and exception peaks
* SPS masses are included as precursors in mzML
* Ignore all not .raw files when processing folder
* Updates in instrument and detector mapping to PSI-MS CV terms

---

**Changes in ThermoRawFileParser 1.3.1 (Sep 08. 2020):**

* Select MS levels to be written to the file (`-L|--msLevel` command line argument)
* Write precursor scan number in the TITLE of MGF file (`-P|--mgfPrecursor` command line argument)
* Correct version of the assembly
* Correct typo in `-a` flag description

---

**Changes in ThermoRawFileParser 1.3.0 (Aug 26. 2020):**

* Able to extract additional detector data - UV, PDA, pressure chromatograms, PDA spectra (new command line argument `-a|--allDetectors`)
* Fix instrument mapping and adding new instruments (Exploris series, ID-X etc)
* Update PSI-MS ontology version
* Fix empty output directory bug

---

**Changes in ThermoRawFileParser 1.2.3 (May 4. 2020):**

* Default centroiding of segmented scan data
* Thermo libraries upgrade
---

**Changes in ThermoRawFileParser 1.2.2 (Mar 2. 2020):**

* Minor change in biocontainer docker file
---

**Changes in ThermoRawFileParser 1.2.1 (Feb 14. 2020):**

* Bug fixes
* Additional XIC input validation
---

**Changes in ThermoRawFileParser 1.2.0 (Feb 6. 2020):**

* Addition xic and query subcommands (beta)
* Minor bug fixes
---

**Changes in ThermoRawFileParser 1.1.11 (Sep 25. 2019):**

* Addition of more Thermo instrument models
---

**Changes in ThermoRawFileParser 1.1.10 (Aug 23. 2019):**

* input directory argument addition
* silent logging mode
* metadata output file argument addition
* error handling improvements
---

**Changes in ThermoRawFileParser 1.1.9 (Jul 2. 2019):**

* no zlib compression flag addition for the binary data in the mzML output
---

**Changes in ThermoRawFileParser 1.1.8 (Jun 18. 2019):**

* addition of a progress indicator
* in MGF output: if no charge is found, no `CHARGE` header instead of `CHARGE=0+`

---

**Changes in ThermoRawFileParser 1.1.7 (Jun 4. 2019):**

* reports the monoisotopic mass as precursor mass when available
* fixed MS3 precursor scan not found
* fixed wrong scan type annotation (centroid/profile) in mzML output
* log file appender is commented out
* addition of --version argument
* updated thermo library to version to 5.0.0.6
* added extra log statement with the number of scans being processed
* fixed max and min charge bug in json metadata output

----