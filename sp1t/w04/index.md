---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 1](../) - Week 04

W04: In week 4, we start the transition from running someone else's code to writing our own. First, you'll connect remotely to the Pi and take a first look at Python on the Pi. We'll then disable the Yahboom code and start writing our own GPIO code.

<!-- **Announcements**
1. Week 05 Session 1 (next week): End of Sprint Project 1 is completed on your own. No Zoom session that day. Open the Week 05 link, complete the required coding, and submit your work by end of Session 1. The class will review and revise during Session 2. -->

**Session 1**

- Build Validation review - issues? Does everything work?
  - Build Validation 1?
  - Build Validation 2?
  
- Remote connections - Status? 
  - via Ethernet (connect to piRover.local)
  - have your home Wi-Fi connected?
    - no Ethernet cable required
    - connect to piRover
  - Smartphone Hotspot is also a good option
    - The IP address of your piRover is visible
    - ![hotspot connect](./hotspot_connect.jpg)
    - Connect via VNC using the IP address rather than piRover
  - Connecting via nmc_makerspace
    - new nmc_makerspace Wi-Fi access point
    - workstations can connect to nmc_makersapce
    - connect your rover using direct connection (Monitor, Keyboard, Mouse)
    - Or, new SD card is configured to automatically connect to nmc_makerspace AP.

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
  
 A first look at Python
  - Download Yahboom Python examples - See Tools section
  - Extract Yahboom examples to home directory (~)
  - Demo - running Python from terminal prompt
  - Yahboom code is written in Python2, we're using Python3

- A first look at Visual Studio Code
  - Copy ColorLED.py to week04 folder
  - Run. Issues?
  - VS code investigation  
  
**Session 2**
<!-- 
- Python in VS Code - first look/review
  - ColorLED.py

- [Disabling Yahboom Bluetooth](../../lessons/21/DisablingYahboomBluetooth.pdf){:target='_blank'}

- [RPi.GPIO library](https://sourceforge.net/projects/raspberry-gpio-python/){:target='_blank'}
  - This resource is installed on Raspian OS by default.
  - VS Code Intellisense for GPIO
    - Remove Pylance
    - Add JEDI

- Guessing Game and debugger use

```bash 
wget https://k2controls.github.io/piRover01/lessons/19/game_test.py

```

- [Blink with VS Code](../../lessons/22/piRoverBlink.pdf){:target='_blank'}

```bash 
wget https://k2controls.github.io/piRover01/lessons/22/blink.py
```
- Create beep.py and test
- Create blink_beep.py and test

- Saving piRover code to your cloud storage -->


---

### Assignments
- **W04** Assignments - Zip assignment files specified in the following activities and submit to the link below
  - **ColorLED.py**
  - **blink.py**
  - **beep.py**
  - **blink_beep.py**
