# Replication Repository for "Programmer Visual Attention During Context-Aware Code Summarization" under major revision at TSE

This replication package has two parts, first the replication protocol to conduct the itrace study, and second the replication protcol for scripts to analyze the data

## Part I - Replication procedure for the itrace study:
Tested for OS: Microsoft Windows 10 pro 10.0.19045

### Phase I: itrace Setup
#### Step 1: Download Eclipse IDE for Java Developers

https://www.eclipse.org/downloads/packages/release/2023-06/r

Version: 2023-06 (4.28.0)

#### Step 2: Download and install the following itrace tools:
https://www.i-trace.org/main/pages/downloads.html

- Core - v0.2.0
- Plugin - v0.2.0 
- Toolkit - v0.2.2

#### Step 3: Download the following zip file containing the 5 projects which have been cleaned, processed, and xml catalogued

https://drive.google.com/file/d/1-klGiDbqCbIgnEwpwnu0-rT1z-9LOmcK/view?usp=share_link

#### Step 4: Create a new project in Eclipse called "itrace", change from package explorer to project explorer

This step is crucial, package explorer does not show .java files and class structure is not well-suited to the experimental design.

Add the project folders downloaded above to the src folder of this newly created project.

#### Step 5: Remove the main src folder from build path, then add only the following folders to build path by navitating to them in the project explorer

Right-click itrace>src and select Build Path> Remove from Build Path. Then, for each of the following paths, navigate in project explorer and right click, then select Build Path>Use as Source Folder.

- src>srcimage>scrimage-core>src>main>java
- src>mallet>src
- src>mltk>src>main>java
- src>openaudible>src>main>java
- src>freecol>src

These folders contain <project>.txt files, where <project> is a placeholder for name of the project. Now, you can populate call graphs by selecting method name for any method and right click, then select open call hierarchy.


#### Step 6: Creating random files

For each participant we randomize the order of projects they do (except scrimage is always the first project), as well randomize the order of methods they process except the first method. To generate these files you can use randoms/randomize.py. 

```
python3 randomize.py --path=.\P21
```

Change the name of the target folder "P21" to the Participant ID to create randomized project.txt files for that participant.

### Phase 2: Prep before each session

#### Step 1: Open the itrace core, in the tab Session Setup, set the path to save this session date, the participant ID and Task as project name.

#### Step 2: In iTrace tracking tab, select tobii eye tracker device and turn on the screen recording as well as the Deja-Vu Replay options. Note, DejaVu is part of the itrace core application and will produce an out.csv file in the session directory specified above. This file can be used by the core to do a DejaVu replay of all participant actions during the session including mouse,keyboard, and eye tracking recordings.

#### Step 3: Open the itrace plugin in Eclipse and connect to core.

#### Step 4: Right click these folders depending on the project:

- src>srcimage>scrimage-core>src>main>java>com>sksamuel
- src>mallet>src>cc>mallet
- src>mltk>src>main>java>mltk
- src>openaudible>src>main>java>org>openaudible
- src>freecol>src>net>sf>freecol

and "Go Into" to limit the view of the participant to that project only.

### Phase 3: Session execution procedure

#### Step 0: Walk the participants through Step 1-5 if it is their first time as a mock before starting the study.

#### Step 1: Show the participant StudyInstructions.md and the txt file to make sure they understand the task

#### Step 2: Calibrate with Tobii Eye-Tracker Manager

#### Step 3: Calibrate with itrace-core

#### Step 4: Instruct the participant to start and stop tracking after every summary written

#### Step 5: Recalibrate halfway through the study, i.e., after method 4.

## Part II - Data Processing

Our study involved 10 participants, each of whome processed 5 sessions of 1-1.5 hours. Participant ID is offset by 2 because P1 and P2 could not continue with the study beyond the pilot session. Therefore P3 is Participant 1 in the paper, P4 is participant 2..... P12 is participant 10.

Data after extraction and processing for fixations can be found at:
https://drive.google.com/file/d/1Z6o9RmHAktPTVVDDm2wrGxRVy0EtolRa/view?usp=share_link

Note: This data is aquired by post-processing using itrace toolkit using the parameters discussed in the TSE paper. Raw data is for eye movements and screen recordings if over 300 GB in size and may be obtained on request by emailing the authors. Lab director - Collin McMillan (cmc@nd.edu).

The following guide is for post-processing on fixation data for results in the paper:-

### To extract fixations from each session
```
python3 extractfixations.py 
```
This script walks all the database files for each session and compiles one file with all relevant data called "fixations.pkl" (provided in the dataset)

### To filter data to only include tokens from java code

``` 
python3 java_fixations.py
```

### The following scripts are used to compute fixation count, duration, regression, lines visited and methods visited for RQs 1:

```
python3 fixation_count.py

python3 fixation_duration.py

python3 line_count.py

python3 method_count.py

python3 regressions.py

```

### The following scripts are used to correlate quality ratings from the summary csv with fixation count, duration, regression, lines visited and methods visited for RQ 2:

```
python3 fcount_quality.py

python3 fduration_quality.py

python3 lcount_quality.py

python3 mcount_quality.py

python3 regression_quality.py
```

### To extract contextual information for RQ 3 in the paper
```
python3 extract_context.py

python3 contextfixation.py
```

Note: the graphs in the paper were generated using excel and google sheets, these scripts will not be able to generate graphs for you, rather they can generate data for Tables and CSV files for further analysis.
