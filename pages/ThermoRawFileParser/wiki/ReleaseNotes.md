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