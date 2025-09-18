---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 1](../) - Week 04

W04: In week 4, we start the transition from running someone else's code to writing our own. First, you'll connect remotely to the Pi and take a first look at Python on the Pi. We'll then disable the Yahboom code and start writing our own GPIO code.


**Session 1**

- Build Validation **review** - issues? Does everything work?
  - [Build Validation 1](../../lessons/13/BuildValidationPart1.pdf){:target='_blank'}?
  - [Build Validation - Part 2](../../lessons/13/BuildValidationPart2.pdf){:target='_blank'}?
  
- Remote connections 
  - Status? All connected?

- Remote Desktop Review
  - piRover Browser
  - Google Drive
- Visual Studio Code - more introduction
  - the piRover workspace

  ```console
  cd piRover
  code .
  ```

  - Add week04 directory

  - ColorLED.py - copy from week03
  - Demo - running Python from terminal prompt

- A first look at Visual Studio Code
  - Copy ColorLED.py to week04 folder
  - Run. Issues?
  - VS code investigation
  - Using the "debugger"
    - Run with debugging - F5
    - set breakpoints
    - single step code execution 

- Removing the Yahboom code conflict
  - [Disabling Yahboom Bluetooth](../../lessons/21/DisablingYahboomBluetooth.pdf){:target='_blank'} 
  
**Session 2**

<!-- - End of Sprint - Week 05 is next week
  - Technical Debt
  - Retrospection
  - P01 assessment durring Session 2
    - No Zoom Class Session
    - Open P01, complete coding, create video, and post -->

- Python coding using Visual Studio Code
  - Open VS Code using the terminal prompt
  
  ```console
  cd piRover
  code .
  ```

  - Review of ColorLED.py (see session 1)
    - VS code investigation
      - Review Activity Bar - Explorer
      - Review Activity Bar - Run and Debug
    - Run code using toolbar or F5
      - creating a launch.json file

- Review: Removing the Yahboom code conflict
  - See session 1
  - No 4 beeps at boot or servo action
  - ColorLED.py code runs without issues
    - modify delays - e.g. 3 seconds
    - set breakpoint and single-step
    - "comment-out" code using Ctrl + /

- [RPi.GPIO library](https://sourceforge.net/projects/raspberry-gpio-python/){:target='_blank'}
  - This resource is installed on Raspberry OS by default.

- [Yahboom Expansion Board Manual](../../hardware_kit/expansionBoardManual.pdf){:target='_blank'}

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
