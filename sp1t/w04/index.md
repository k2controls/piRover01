---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 1](../) - Week 04

W04: In week 4, we start the transition from running someone else's code to writing our own. First, you'll connect remotely to the Pi and take a first look at Python on the Pi. We'll then disable the Yahboom code and start writing our own GPIO code.

**Announcements**
1. Week 05 Session 1 (next week): End of Sprint Project 1 is completed on your own. No Zoom session that day. Open the Week 05 link, complete the required coding, and submit your work by end of Session 1. The class will review and revise during Session 2.
2. We're looking to hire new NMC Makerspace lab technicians this semester. You'll need to be enrolled at NMC at least through next school year. Email me if you are interested.


**Session 1**

- Build Validation review - issues? Does everything work?
  
- Remote connections - Status? 
  - Connecting via phone Hotspot
    - ![hotspot connect](./hotspot_connect.jpg)
  
- Next week - Week 5 end of sprint
- Tuesday - Project 1, on your own
  - Access remote desktop
  - Create project 1 Python file
  - Enter code by extending week04 code
  - Zip and submit by class end
- Thursday - Project 1 review and revise
  - Resubmit Project 1 at end of week

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

- Visual Studio Code - installation
  - Linux commands to update and then install Visual Studio Code (Not required at this time.)

```bash  
sudo apt update
sudo apt upgrade
sudo apt install code

```

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

**Session 2**

- [Blink with VS Code](../../lessons/22/piRoverBlink.pdf){:target='_blank'}

```bash 
wget https://k2controls.github.io/piRover01/lessons/22/blink.py
```
- Create beep.py and test
- Create blink_beep.py and test

- Saving piRover code to your cloud storage


---

### Assignments
- **W04** Assignments - Zip assignment files specified in the following activities and submit to the link below
  - **blink.py**
  - **beep.py**
  - **blink_beep.py**
  - Include a short video clip of "blink_beep.py". Show your VS Code window with code. (Zoom video with screen share is preferred.)
  