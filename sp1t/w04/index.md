---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 1](../) - Week 04

W04: In week 4, we start the transition from running someone else's code to writing our own. First, you'll connect remotely to the Pi and take a first look at Python on the Pi. We'll then disable the Yahboom code and start writing our own GPIO code.



**Session 1**

- Build Validation review - issues? Does everything work?
  - [Build Validation 1](../../lessons/13/BuildValidationPart1.pdf){:target='_blank'}?
  - [Build Validation - Part 2](../../lessons/13/BuildValidationPart2.pdf){:target='_blank'}?
  
- Remote connections 
  - Status? 9 of 11 connected

- Remote Desktop Review
  - piRover Browser
    - Google Drive
    - Moodle (elearn.nmc.edu)


- Linux - basic commands

| Command | Operation |
|---------|-----------|
| ls      |Displays information about files in the current directory. |
| pwd     |Displays the current working directory.|
| mkdir   |Creates a directory.|
| cd      |To navigate between different folders.|
| rmdir   |Removes empty directories from the directory lists.|
| cp      |Moves files from one directory to another.|
| mv      |Rename and Replace the files|
| rm      |Delete files|

- RAM 155 workspace on the Pi
  - create piRover directory
  - create week04 directory
  
- A first look at Python
  - ColorLED.py
  - Demo - running Python from terminal prompt
  - Error! - Yahboom code is written in Python2, we're using Python3

- A first look at Visual Studio Code
  - Copy ColorLED.py to week04 folder
  - Run. Issues?
  - VS code investigation  
  
**Session 2**

<!-- - End of Sprint Project 1/Assessment moved to Week 06

- Python coding using Visual Studio Code
  - Open VS Code using the terminal prompt
  
  ```console
  cd piRover
  code .
  ```

  - Review of ColorLED.py (see week04 assignments)
    - VS code investigation
    - Run code using toolbar or F5

- Removing the Yahboom code conflict
  - [Disabling Yahboom Bluetooth](../../lessons/21/DisablingYahboomBluetooth.pdf){:target='_blank'}

- Single stepping using the debugger

- [RPi.GPIO library](https://sourceforge.net/projects/raspberry-gpio-python/){:target='_blank'}
  - This resource is installed on Raspian OS by default.

- [Blink with VS Code](../../lessons/22/piRoverBlink.pdf){:target='_blank'}

```bash 
wget https://k2controls.github.io/piRover01/lessons/22/blink.py
```
- Create beep.py and test
- Create blink_beep.py and test

- Saving piRover code to your cloud storage
  - Copy files listed in Assignments to week04 in your Google Drive.
  - Download the week04 folder to your workstation.
  - Submit the resulting week04.zip file to the Moodle assignment link. -->


---

### Assignments
- **W04** Assignments - Zip assignment files specified in the following activities and submit to the link below
  - **ColorLED.py**
  - **blink.py**
  - **beep.py**
  - **blink_beep.py**
