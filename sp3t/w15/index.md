---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 3](../) - Week 15

W15: You will complete P03 Part 2 this week by adding a Bluetooth service that enables smartphone functionality for the piRover. The instructor will discuss the requirements for Part 2 and introduce bluetooth concepts and coding.

**Schedule**
- Week 15
  - Session 1
    - Bluetooth module, messaging, and integration
  - Session 2
    - Analog inputs and operations
    - piRover_phone.py
- Week 16
  - Session 1
    - piRover_phone.py
      - testing and extensions
      - shut down
      - start up
      - Enabling at Startup
  - Session 2
    - *No Zoom class session*
    - **P03 Part 2 Due** - end of the day on Thursday, Dec 11
    - Debt
    - Retro


**Session 1**

- Review of P03 Part 1 - keyboard solution
  - PWM freq of 1000?
  - pin numbers for LEDs?
  - capturing analog values from user
  - LED solution

- Bluetooth introduction
  - Add [piRover_bluetooth.py](piRover_bluetooth.py)

```console

wget https://k2controls.github.io/piRover01/sp3t/w15/piRover_bluetooth.py

```

- test_bluetooth.py (instructor demo)
- add piRover_phone.py
    
**Session 2**

- P03 Part 2 due Thursday, Dec 11
  - Zoom video demonstrating smartphone functionality
  - [P03 Part 2](P03.piRoverPhone_part2.pdf){:target='_blank'} requirements
- Bluetooth module and messaging
  - piRover_bluetooth.py module added in session 1
  - piRover_phone.py introduction
    - follow in class example
    - refer to keyboard solution
    - complete on your own.
  - analog inputs 
    - speed - constrain to 0 to 100
    - dim - contrain to 0 to 100
    - dim - see note on issue with toggle after dim
- Enable multiple key presses
  - add last_command_id
  - Exit app with two successive LED_ON presses (L)
  - Enable "latched" forward, backward, left, right
    - sink "STOP" when basic motion is last command
    - Keep stop on key up for alt moves
- Arm Rover using controller board start button
- Indicate disarm (done) using long beep

---

### Assignments
- Final P03 Part 2 in progress
  - Submit Zoom video link to course link by Thursday deadline
