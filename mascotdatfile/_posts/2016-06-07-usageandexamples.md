---
name: UsageAndExamples
project: mascotdatfile
layout: default
permalink: /mascotdatfile/wiki/usageandexamples.html
github_project: https://github.com/compomics/mascotdatfile
---

# Usage And Examples

 * [Introduction](#introduction)
 * [How to parse the peptide hits](#how-to-parse-the-peptide-hits)
 * [Using MascotDatfile as a Maven dependency](#using-mascotdatfile-as-a-maven-dependency)
 * [Example code](#example-code)

----

## Introduction

This library was developed as a tool for the large scale analysis of all data inside one or more complex [Mascot](http://www.matrixscience.com/) MS/MS datfiles for a variety of purposes.

The main functionality consists of retrieving a Mascot datfile from multiple sources (a harddisk, database or MascotServer URL) and transforming into a functional object model.

A MascotDatfile instance captures all the data from PeptideHits and Queries into easy accessible objects. Standard methods are integrated into the objects to analyse small details like:

  * threshold calculation of an MS/MS spectrum versus ionscore of a peptide identification
  * sequence coverage of a peptide identification in a MS/MS spectrum
  * processing of modified aminoacid residues on peptide identifications
  * processing of MS/MS spectra
  * etc ..

*In summary, this library makes the raw data inside Mascot datfiles easily accessible for research purposes.*

The library was written by Kenny Helsens (kenny.helsens@UGent.be) and you can contact the author for any questions concerning this library. 

Also feel free to contact the developers if you have suggestions/enhancements/comments to library.

[Go to top of page](#usage-and-examples)

----

## How to parse the peptide hits

`com.compomics.mascotdatfile.research.script.PeptideHitParser`

### Print usage by running the JAR without parameters

```
$ java -jar mascotdatfile-3.2.11.jar
	SimpleParser arguments:	 <alpha> <output> <input 1> [<input 2> <input 3> ... <input n>]
		
	Input Structure:
	<alpha> 	 alpha=0.05 reports peptide hits above 95% probability threshold
	<output> 	 output file
	<input> 	 one or more MascotDatfile input files

	Output structure:
	<MascotDatfile> <query number> <spectrum title> <charge state> <peptide> <peptide+PTM> <ionscore> <rank>
```

### Example usage
```
$ java -jar mascotdatfile-3.2.11.jar 0.05 /tmp/test_peptidehitparser.txt /tmp/mascot/results/directory/F004071.dat

	Processing /tmp/mascot/results/directory/F004071.dat
	Successfully parsed 77 PSMs from 56 (1000) Queries above alpha 0.05
```

### Example output
```
	F004071.dat;3;51008_1.6.1mox_9087_210.mgf;3+;PAQEVYR;Ace-PAQ<Dam>EVYR-COOH;6.66;1;
	F004071.dat;3;51008_1.6.1mox_9087_210.mgf;3+;PAQEVYR;PAQEVYR-COOH;6.66;2;
```

### Note
If you want to include -ALL- the PeptideHits, then set alpha to '100000000' which will produce a negative confidence threshold. As the IonScore is by definition positive, all PeptideHits will be included.

[Go to top of page](#usage-and-examples)

----

## Using MascotDatfile as a Maven dependency
MascotDatfile is hosted at our public maven repository.
Add the following code into your `pom.xml` file:

**Repository**
```
    <repositories>
        <!-- Compomics Genesis Maven 2 repository -->
        <repository>
            <id>genesis-maven2-repository</id>
            <name>Genesis maven2 repository</name>
            <url>http://genesis.UGent.be/maven2</url>
            <layout>default</layout>
        </repository>
    
        <!-- EBI Maven 2 repository -->
        <repository>
            <id>ebi-repo</id>
            <name>The EBI Maven2 repository</name>
            <url>http://www.ebi.ac.uk/~maven/m2repo</url>
            <layout>default</layout>
        </repository>
    </repositories>
```

**Dependency**
```
    <dependencies>
        <dependency>
            <groupId>com.compomics</groupId>
            <artifactId>mascotdatfile</artifactId>
            <version>X.Y.Z</version>
            <type>jar</type>
        </dependency>
    </dependencies>
```

Update the version number (X.Y.Z) to latest released version.

Note that the [repository](http://genesis.ugent.be/maven2/com/compomics/mascotdatfile/) can be manually accessed to download the *src* or *javadocs*.

[Go to top of page](#usage-and-examples)

----

## Example code

```
public class ExampleWiki1 {
    public ExampleWiki1(String aFileName) {

        String file = aFileName;

        // Define the separator
        char separator = ',';

        // Ready to go!
        MascotDatfileInf iMascotDatfile = null;

        // log the status.
        System.out.println("Processing " + file);

        // Create a new MascotDatfile instance for each filename in the Input array.
        iMascotDatfile = MascotDatfileFactory.create(file, MascotDatfileType.MEMORY);

        // Fetch the QueryToPeptideMap. This indexes all queries.
        // From 1 to n number of spectra in the corresponding datfile.

        QueryToPeptideMapInf lQueryToPeptideMap = iMascotDatfile.getQueryToPeptideMap();
        // Also explore other methods on the QueryToPeptideMap!!!

        ArrayList list = null;

        // This Vector retrieves the best PeptideHit for each Query.
        // The Vector is zero based.
        // ex: Vector[0] contains the peptidehit of Query 1, etc.
        Vector lBestPeptideHits = lQueryToPeptideMap.getAllPeptideHitsAboveIdentityThreshold();

        // A - Iterate over all ProteinIDs
        Iterator iter = iMascotDatfile.getProteinMap().getProteinIDIterator();
        ProteinID lProteinID = null;
        while (iter.hasNext()) {
            String item = "";

            String lAccession = iter.next().toString();
            lProteinID = iMascotDatfile.getProteinMap().getProteinID(lAccession);

            // Collect information for current protein.
            item = "PROTEIN" + separator
                    + lAccession + separator
                    + lProteinID.getQueryNumbers().length + separator
                    + lProteinID.getDescription();

            // Print to system outputstream
            System.out.println(item);
        }

        // B - Iterate over all PeptideHits.
        for (int j = 0; j < lBestPeptideHits.size(); j++) {
            PeptideHit lPeptideHit = (PeptideHit) lBestPeptideHits.elementAt(j);
            // CSV output array.

            if (lPeptideHit != null) {
                // 1. MS/MS Spectrum filename.
                // 2. Modified PeptideSequence
                // 3. IonScore
                // 4. 95% Identity Threshold
                // 5. Number of ProteinHits
                // 6a. Protein i accession
                // 6b. Protein i description
                // etc. for n proteins.

                // As a Peptide can come from multiple proteins, it can have multiple proteinhits.
                ArrayList lProteins = lPeptideHit.getProteinHits();

                for (int k = 0; k < lProteins.size(); k++) {
                    list = new ArrayList();

                    ProteinHit lProteinHit = (ProteinHit) lProteins.get(k);
                    String lAccession = lProteinHit.getAccession();
                    // The protein description come from another part of the Mascot Result file.
                    // The ProteinMap also keeps track how many peptides refer to a Protein, mind that protein inference is not regarded at all!
                    // 6a.
                    list.add(lAccession);
                    list.add("PEPTIDE");

                    // 1.
                    list.add(((Query) iMascotDatfile.getQueryList().get(j)).getFilename());

                    // 2.
                    list.add(lPeptideHit.getModifiedSequence());

                    // 3.
                    list.add(lPeptideHit.getIonsScore());

                    // 4.
                    list.add(lPeptideHit.calculateIdentityThreshold(0.05));

                    String lResult = "";
                    for (Object item : list) {
                        lResult = lResult + item + separator;
                    }

                    System.out.println(lResult);

                }
            }
        }
        iMascotDatfile.finish();

    }

    public static void main(String[] args) {
        new ExampleWiki1("/home/myfolder/mydatfile.dat");
    }
}
```

[Go to top of page](#usage-and-examples)