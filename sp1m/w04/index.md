---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 1](../) - Week 04

W04: In week 4, we start the transition from running someone else's code to writing our own. First, you'll connect remotely to the Pi and take a first look at Python on the Pi. We'll then disable the Yahboom code and start writing our own GPIO code.

**Session 1**
- Build Validation review - issues?
- Current requirements
    - VNC remote connection - either Ethernet or Wi-Fi
    - RPI configuration completed - new password, yahboomtank as hostname
    - RPi connected to Wi-Fi (use of ping command to test)
    - Browser shortcuts on the Pi - Moodle, - OneDrive or Google Drive
    - Issues? - see [this document](../../lessons/15/ConfiguringTheRaspberryPi.pdf){:target="_blank"} for assistance.
- Next Stpes
    - Update RPi packages 
    - Install Visual Studio Code
    - Note: The following code takes signicant time to complete. 

```bash  
sudo apt update
sudo apt upgrade
sudo apt install code

```

- [Visual Studio Code - Getting Started](../../lessons/19/VisualStudioCodeGettingStarted.pdf){:target="_blank"}
  - Add Python extension

- [RPi.GPIO library](https://sourceforge.net/projects/raspberry-gpio-python/){:target='_blank'}
  - This resource is installed on Raspian OS by default.
  -VS Code Intellisense for GPIO
    -Remove Pylance
    -Add JEDI

 - [Disabling Yahboom Bluetooth](../../lessons/21/DisablingYahboomBluetooth.pdf){:target='_blank'}


- Python in VS Code - first look
  - ColorLED.py

 
**Session 2**

- Python in VS Code - first look/review
  - disabling Yahboom Bluetooth (see Session 1 link)
  - ColorLED.py

- [RPi.GPIO library](https://sourceforge.net/projects/raspberry-gpio-python/){:target='_blank'}
  - This resource is installed on Raspian OS by default.
  -VS Code Intellisense for GPIO
    -Remove Pylance
    -Add JEDI

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

- Saving piRover code to your cloud storage
 
---

### Assignments
- **W04** Assignments - Zip assignment files specified in the following activities and submit to the link below
  - **blink.py**
  - **beep.py**
  - **blink_beep.py**
  - Include a short video clip of "blink_beep.py". Show your VS Code window with code. (Zoom video with screen share is preferred.)
  