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

- [RPi.GPIO library](https://sourceforge.net/projects/raspberry-gpio-python/)
    - This resource is installed on Raspian OS by default.
    -VS Code Intellisense for GPIO
        -Remove Pylance
        -Add JEDI

- Python in VS Code - first look
  - ColorLED.py
  - Guessing Game

```bash 
wget https://k2controls.github.io/piRover01/lessons/19/game_test.py

wget https://k2controls.github.io/piRover01/lessons/19/blink.py
```

- [Disabling Yahboom Bluetooth](../../lessons/21/DisablingYahboomBluetooth.pdf){:target="_blank"}

 
**Session 2**
  
<!--

    - Disabling Yahboom BluetoothURL[label](../../lessons/21/DisablingYahboomBluetooth.pdf)
        -beep code
        -game-buzzer-beep mash-up
    - Project 1: [Yahboom Evaluation](../../projects/P01/P01piRoverYahboomEval.pdf) (due Week 5)
    - [piRover Yahboom Evaluation - Preparation](../../lessons/23/piRoverYahboomEvalPrep.docx)

-->

---

### Assignments
- **W04** Assignments - Zip assignment files specified in the following activities and submit to the link below
    - **VS_code.jpg** (screen capture of VS Code on the Pi with Guessing Game code)
    - **guessing_game.py**
    - **blink.py**
  
<!--
- Additional items were submitted during class session
    - piRover Yahboom Evaluation Prep
--> 