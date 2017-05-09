---
name: JavaTroubleShooting
project: compomics-utilities
layout: default
permalink: /projects/compomics-utilities/wiki/javatroubleshooting.html
github_project: https://github.com/compomics/compomics-utilities
---

# Java Troubleshooting #

The aim of this wiki page is to provide help with common Java related issues that one can encounter when using software from the CompOmics group. If you have a Java related question that is not answered below please let us know _via_ our [Issue Tracker](https://github.com/compomics/compomics-utilities/issues).

1. [Installing Java](#installing-java)
2. [Memory Issues](#memory-issues)
3. [32 bit or 64 bit](#32-bit-or-64-bit)
4. [Tool Does Not Start](#tool-does-not-start)
5. [Text and Icons Are Too Small](#text-and-icons-are-too-small)
6. [More Help](#more-help)

## Installing Java ##

  * Do you have Java installed? Download the latest version of Java  [here](http://java.sun.com/javase/downloads/index.jsp). (You only need the JRE version (and not the JDK version) to run CompOmics tools.) [64 bit is always recommended!](#32-bit-vs-64-bit)

---

## Memory Issues ##

  * **Memory Issues I** - Big datasets can require a lot of memory. If the software fails on a big project, and the software mentions that it ran out of memory, try to give the program more memory. This can be done by selecting `Java Options` on the `Edit` menu in most tools. Set the memory limit in MB, e.g., `4000` for a maximum of appr. 4 GB of memory. _Please note that on a 32-bit operating system you cannot increase this value beyond 2000 (and usually the maximum limit is lower than this)._

  * **Memory Issues II** - Using more than 2 GB of memory requires 64 bit Java. Downloaded from the same location as the 32 bit version: [Java](http://java.sun.com/javase/downloads/index.jsp). _Note that 64 bit Java only works on 64 bit operating systems!_

---

## 32 bit or 64 bit ##

  * **Java 32 bit vs. 64 bit** - Java comes in two versions: 32 bit and 64 bit. The 32 bit version is limited to using a maximum of around 2 GB of memory. For bigger datasets this is not always enough. Most newer machines support the 64 bit version, and it is always recommended to use Java 64 bit if possible.

  * **Multiple Installations** - If you have both 32 and 64 bit versions of Java the operating system can get confused about which version to use when running Java tools. For Windows the CompOmics tools try to default to the 64 bit version of Java. You can override this option by setting your own Java Home, by creating a file called `JavaHome.txt` in the `resources\conf` folder of the tool, with the path to the bin folder of the Java installation, e.g., `C:\Program Files\Java\jdk1.7.0_21\bin\`. If the folder does not exist (or it does not contain the required files), the default Java version will be used.

---

## Tool Does Not Start ##

  * **Does Not Start I** - Do you have Java installed? Download the latest version of Java  [here](http://java.sun.com/javase/downloads/index.jsp) and try again. (You only need the JRE version (and not the JDK version) to run CompOmics tools.) [64 bit is always recommended!](#32-bit-vs-64-bit)

  * **Does Not Start II** - Have you unzipped the zip file? You need to unzip the file before double clicking the jar file. If you get the message "A Java Exception has occurred", you are most likely trying to run the tool from within the zip file. Unzip the file and try again.

  * **Does Not Start III** - Is the tool installed in a path containing special characters, i.e. `[`, `%`, æ, ø, å, etc? If so, move the whole folder to a different location or rename the folder(s) causing the problem and try again. (Note that on Linux, most tools have to be run from paths not containing spaces as well).

  * **Does Not Start IV** - Is the tool installed in the _Program Files_ folder? If the tool is located in the _Program Files_ folder you need to run the tool with administrator right. It is simpler and better practice to move the tool to another folder.

  * **Does Not Start V** - Do you have read/write right to the folder where the tool is installed? Is the folder synced or mapped? The tool needs to write to its own folder, make sure that it is allowed to. Please also avoid synced and mapped folders like on client machines or dropbox folders as your computer might stall trying to sync while the tool is running.

  * **Does Not Start VI** - If the tool fails during start-up many of our tools generate a file called `startup.log` in the tool's `resources\conf` folder. Here you can find detailed information about why the program was not able to start.

  * **Unidentified Developer** - If you run Java applications on a Mac you can get the warning _"Application" can't be opened because it is from an unidentified developer_. To escape this warning control-click on the file icon and then select "Open." This will give you the option of opening it regardless of its unidentified source. This only has to be done once for each version of the application.

---

## Text and Icons Are Too Small ##

If you have a very high resolution screen the text and icons in your Java tools may be too small to read clearly. This is due to a known issue in Java itself where the information is not rescaled. A proper fix will hopefully be introduced in an upcoming release of Java.

1) The first thing you can try is to increase your DPI scaling factor (see your computer help for how to to this). If set high enough this usually solves the problem.

2) An even simpler solution is to use an external monitor with a "normal" resolution.

3) If none of the above works, there is a third option available for **_advanced Windows users only_**, which includes editing the manifest of the Java executables. 

**Note: This fix is for advanced users only, and is done at your own risk!**

1) Download an exe decompiler/editor. (For example the free Resource Hacker: http://angusj.com/resourcehacker/)

2) Edit the applicable java.exe and javaw.exe files (make sure to pick the right ones; you may have multiple JDK and JRE installations!)

3) Go to the Manifest section in the exe, and edit the manifest file. It will have a section like this:

```
<asmv3:application>
   <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">
      <dpiAware>true</dpiAware>
   </asmv3:windowsSettings>
</asmv3:application>
```

Change the value of the `<dpiAware>true</dpiAware>` tag to `false`.

4) Recompile the manifest (green 'Play' button in Resource Hacker).

5) Save the altered exe file (Resource Hacker automatically creates a backup called `[filename]_original.exe`; in other tools, make sure that you make a backup of the original yourself!).

6) Reboot the computer (if your exe was run before, Windows caches the exe file in memory, which prevent sit from re-reading the updated manifest. A restart fixes this.)

7) You should now have a JVM that renders Java applications in normal size, albeit a bit fuzzier.

Note that you would have to repeat this fix whenever you update your Java version.

---

## More Help ##

  * **Problem Not Solved? Or Problem Not In List?** Contact the developers by setting up an issue describing the problem at the given tool's web page (available via the Issues tab).