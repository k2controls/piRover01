---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 1](../) - Week 04

W04: In week 4, we start the transition from running someone else's code to writing our own. First, you'll connect remotely to the Pi and take a first look at Python on the Pi. We'll then disable the Yahboom code and start writing our own GPIO code.

**Session 1**

- Build Validation review - issues? Does everything work?
    
- Status? 
  - open issues?
  - plans to resolve?
  - Impact on Validation assignment - none
  - Connecting via phone Hotspot
    - ![hotspot connect](./hotspot_connect.jpg)

- Linux - basic commands - review and practice

- [Python - Investigation](../../lessons/17/PythonInvestigation.pdf){:target="_blank"}
  - [Python3 for Robotics](https://www.theconstructsim.com/robotigniteacademy_learnros/ros-courses-library/python-robotics/){:target="_blank"} - optional, on-your-own
  - Python.org - Documentation - Beginner's Guide
  - [Python Fiddle](http://pythonfiddle.com/)

- Visual Studio Code - installation
  - Linux commands to update and then install Visual Studio Code

```bash  
sudo apt update
sudo apt upgrade
sudo apt install code

```



**Session 2**



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

- Saving piRover code to your cloud storage

---

### Assignments
- **W04** Assignments - Zip assignment files specified in the following activities and submit to the link below
  - **blink.py**
  - **beep.py**
  - **blink_beep.py**
  - Include a short video clip of "blink_beep.py". Show your VS Code window with code. (Zoom video with screen share is preferred.)
  