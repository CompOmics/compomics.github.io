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