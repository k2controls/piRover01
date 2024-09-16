---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 1](../) - Week 04

W04: In week 4, we start the transition from running someone else's code to writing our own. First, you'll connect remotely to the Pi and take a first look at Python on the Pi. We'll then disable the Yahboom code and start writing our own GPIO code.

**Session 1**

- [Connecting Remotely](../../lessons/11/CreatingARemoteConnection.pdf){:target="_blank"}
  - Connect to your remote desktop
    - Option 1: Ethernet - connection is peer-to-peer
      - *piRover.local* is the VNC server name
    - Option 2: Network/Wi-Fi connection 
      - Raspberry Pi and your workstation share the same network
      - *piRover* is the VNC server name
      - NMC network does not support
      - But we have set up *nmc_makers* open access point in the makerspace. 
      - Enter the pass code for your Wi-Fi access point (AP). Again, the nmc_makers AP is open. No pass code is required
    - Use a smartphone hotspot? This may be the best option if it is available to you. Once you have connected the Pi, you can view the connection on your phone. The IP address is normally available.
    - Hover or Wi-Fi icon in menu bar - your IP address is displayed
    - Test Internet connectivity in a terminal window
      - ping 8.8.8.8    (ctrl+C to exit)
      - ping google.com (ctrl+C to exit)

  - **Use must be remotely connected this week!**
    - Access assistance in the makerspace. See the tools section for tech schedule.

- The remote desktop
  - Menu
  - Browser
  - File Explorer
  - Terminal emulator
  - Power issues
  - Updates?
  - Networking/Wi-Fi

- Browser shortcuts
  - Moodle
  - Google Drive

- An introduction to the Linux command line.
 - [Introduction to Linux and Basic Linux Commands for Beginners](https://www.youtube.com/watch?v=IVquJh3DXUA&ab_channel=sakitech){:target="_blank"}  by sakitech
  - [Linux Essentials Tutorials: A Beginner’s first 100 commands](https://factorpad.com/tech/linux-essentials/index.html) by FactorPad

- RAM 155 workspace on the Pi
  - create piRover directory
  - create week04 directory

- A first look at Python
  - Download Yahboom Python examples - See Tools section
  - Extract Yahboom examples to home directory (~)
  - Demo - running Python from terminal prompt

  
- A first look at Visual Studio Code
  - Copy ColorLED.py to week04 folder
  - Run. Issues?
  - VS code investigation0
 
**Session 2**

<!-- - Python in VS Code - first look/review
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

- Saving piRover code to your cloud storage -->
 
---

### Assignments
- **W04** Assignments - Zip assignment files specified in the following activities and submit to the link below
  - **ColorLED.py**
  - **blink.py**
  - **beep.py**
  - **blink_beep.py**
  - Include a short video clip of "blink_beep.py". Show your VS Code window with code. (Zoom video with screen share is preferred.)
  