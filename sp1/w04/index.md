---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 1](../) - Week 04

W04: In week 4, we start the transition from running someone else's code to writing our own. First, you'll connect remotely to the Pi and take a first look at Python on the Pi. 
In session 2, we'll introduce Project 1. This is a written report evaluating your experience with the piRover so far. You complete a team activity to prepare, but the report is not due until Week 05.

**Session 1**
- Build Validation review - issues?
- Current requirements
    - VNC remote connection - either Ethernet or Wi-Fi
    - RPI configuration completed - new password, yahboomtank as hostname
    - RPi connected to Wi-Fi (use of ping command to test)
    - Browser shortcuts on the Pi - Moodle, - OneDrive or Google Drive
    - Issues? - see [this document](../../lessons/15/ConfiguringTheRaspberryPi.pdf){:target="_blank"} for assistance.
    - RPi updated and VS Code installed
    - Note: The following code takes signicant time to complete. This code block was provided last week and you were directed to run on your own due to long delay.

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

- Python in VS Code - first look
  - ColorLED.py
  - Guessing Game

```bash 
wget https://k2controls.github.io/piRover01/lessons/19/game_test.py

```
 
**Session 2**
  
- [Disabling Yahboom BluetoothURL](../../lessons/21/DisablingYahboomBluetooth.pdf){:target='_blank'}

- [Blinkwith VS Code](../../lessons/22/piRoverBlink.pdf){:target='_blank'}
  - beep code
  - game-buzzer-beep mash-up

```bash 
wget https://k2controls.github.io/piRover01/lessons/22/blink.py
```

- Saving piRover code to your cloud storage
 
- Project 1: [Yahboom Evaluation](../../projects/P01/P01piRoverYahboomEval.pdf) (due Week 5)

<!--
- [piRover Yahboom Evaluation - Preparation](../../lessons/23/piRoverYahboomEvalPrep.docx)
-->

---

### Assignments
- **W04** Assignments - Zip assignment files specified in the following activities and submit to the link below
  - **guessing_game.py**
  - **blink.py**
  - **beep.py**
- Include a short video clip of "blink" if you did not complete the lab check in class.