---
name: ReleaseNotes
project: thermorawfileparser
layout: default
permalink: /projects/thermorawfileparser/wiki/releasenotes.html
github_project: https://github.com/compomics/ThermoRawFileParser
---

# ReleaseNotes

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