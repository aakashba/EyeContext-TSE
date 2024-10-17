# Replication Repository for "Programmer Visual Attention During Context-Aware Code Summarization" under major revision at TSE

This replication package has two parts, first the replication protocol to conduct the itrace study, and second the replication protcol for scripts to analyze the data

## Part I - Replication procedure for the itrace study:
Tested for OS: Microsoft Windows 10 pro 10.0.19045

### Step 1: Download Eclipse IDE for Java Developers

https://www.eclipse.org/downloads/packages/release/2023-06/r

Version: 2023-06 (4.28.0)

### Step 2: Download and install the following itrace tools:
https://www.i-trace.org/main/pages/downloads.html

- Core - v0.2.0
- Plugin - v0.2.0 
- Toolkit - v0.2.2

### Step 3: Download the following zip file containing the 5 projects which have been cleaned, processed, and xml catalogued

https://drive.google.com/file/d/1-klGiDbqCbIgnEwpwnu0-rT1z-9LOmcK/view?usp=share_link

### Step 4: Create a new project in Eclipse called "itrace", change from package explorer to project explorer

This step is crucial, package explorer does not show .java files and class structure is not well-suited to the experimental design.

Add the project folders downloaded above to the src folder of this newly created project.

### Step 5: Remove the main src folder from build path, then add only the following folders to build path by navitating to them in the project explorer

Right-click itrace>src and select Build Path> Remove from Build Path. Then, for each of the following paths, navigate in project explorer and right click, then select Build Path>Use as Source Folder.

- src>srcimage>scrimage-core>src>main>java
- src>mallet>src
- src>mltk>src>main>java
- src>openaudible>src>main>java
- src>freecol>src

These folders contain <project>.txt files, where <project> is a placeholder for name of the project. Now, you can populate call graphs by selecting method name for any method and right click, then select open call hierarchy.


### Creating random files

For each participant we randomize the order of projects they do (except scrimage is always the first project), as well randomize the order of methods they process except the first method. To generate these files you can use randoms/randomize.py. 

```
python3 randomize.py --path=.\P21
```

Change the name of the target folder "P21" to the Participant ID to create randomized project.txt files for that participant.

### Before each session

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

# Experimental Procedure

## Step 0: Walk the participants through Step 1-5 if it is their first time as a mock before starting the study.

## Step 1: Show the participant StudyInstructions.md and the txt file to make sure they understand the task

## Step 2: Calibrate with Tobii Eye-Tracker Manager

## Step 3: Calibrate with itrace-core

## Step 4: Instruct the participant to start and stop tracking after every summary written

## Step 5: Recalibrate halfway through the study, i.e., after method 4.

