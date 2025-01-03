---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 1](../) - Week 04

W04: In week 4, we start the transition from running someone else's code to writing our own. First, you'll connect remotely to the Pi and take a first look at Python on the Pi. We'll then disable the Yahboom code and start writing our own GPIO code.

**Announcements**
> Week 05 Session 2 ~~(next week)~~ **(MOVED TO WEEK06)**: End of Sprint Project 1 is completed on your own. No Zoom session that day. Open the Week 05 link, complete the required coding, and submit your work by end of Session 1. The class will review Project 1 coding the following week.
> #### Requirements:
> 1. Access your remote desktop.
> 2. Open and use VS Code to write and run code.
> 3. Refer to prior code examples. Copy code and duplicate patterns. 
> 4. Reference documents and class notes to determine GPIO pins.
> 5. Take a screen capture of your code window.
> 6. Zip your code along with screen capture and submit to Moodle.
> 7. All Sprint 1 technical debt must be submit by the end of Week 05. No late credit is available after.

**Session 1**

- Build Validation review - issues? Does everything work?
  - [Build Validation 1](../../lessons/13/BuildValidationPart1.pdf){:target='_blank'}?
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

- End of Sprint Project 1/Assessment moved to Week 06

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
  - Submit the resulting week04.zip file to the Moodle assignment link.


---

### Assignments
- **W04** Assignments - Zip assignment files specified in the following activities and submit to the link below
  - **ColorLED.py**
  - **blink.py**
  - **beep.py**
  - **blink_beep.py**
