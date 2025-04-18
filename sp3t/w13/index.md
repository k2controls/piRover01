---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 3](../) - Week 13

W13:  We'll continue with GPIO implmentation producing servo and switch code. The first part of P03 assessment is assigned.

**Schedule**
- Week 13
  - Session 1
    - Servo implementation
    - Switch implementation and testing
    - Arming the rover
  - Session 2
    - *No class session* - P03 working session
    - **P03 Part 1 due** - Due by Monday deadline - piRover_keyboard with Rover functions
- Week 14
  - Session 1
    - Bluetooth module, messaging, and integration
  - Session 2
    - Analog inputs and operations
    - P03 piRover_phone_app.py assigned
- Week 15
  - Session 1
    - No class session - P03 Part 2 working session
  - Session 2
    - No class session
    - **P03 Part 2 due**
    - Debt
    - Retro

**Session 1**

- weekP03 status

| Requirement   | Status  | Comment             |
|---------------|-------- |---------------------|
|Planning doc   | Done    | revise?             |
|pRover_keyboard| Done    | analog ins included |
|buzzer_fake    | Done    | add beep N times?   |
|drive_fake     | Done    | speed func added    |
|led_fake       | Done    | RGB, red,green,blue |
|servo_fake     | Done    |                     |
|buzzer         | Done    | done including PWM  |
|drive          | Done    | done - turn, speed  |
|led            | **TODO**    | implement GPIO      |
|servo          | IP      | in progress      |
|switch         | TODO    | used for 'arm'      |


  - piRover_servo.py
    - [P03.Servo.pdf](P03.Servo.pdf){:target='_blank'}
  - piRover_switch.py 
  - test_arm_rover.py.py
  - piRover_keyboard testing - all functional except LED
  - [P03 Part 1 assessment](P03.piRoverKeyboard.docx)
    
**Session 2**
- No class today. 
  - Working session for P03 Part1. 
  - KEK will be on Zoom at start of class for any questions.
  - piRover_led.py (on your own)
  - Submit functional piRover_keyboard solution
  - Include completed P03.piRoverKeyboard document. Key map (table 1) must match your solution file.
  - Be sure to double-check your zip file to be sure all is included. See list in Assignment section below.


---

### Assignments
- **W13** Assignments - Zip your weekP03 folder and submit. Be sure to add your updated P03.piRoverKeyboard document.
  - **weekP03.zip**
    - piRover_buzzer_fake.py
    - piRover_buzzer.py *(with pwm)*
    - piRover_drive_fake.py
    - piRover_drive.py  *(all drive and speed function)*
    - piRover_keyboard.py *(must implement all functions in table 1)*
    - piRover_led_fake.py
    - piRover_led.py *(this implementation is on your own)*
    - piRover_servo_fake.py
    - piRover_servo.py *(left, right, center, set_position)*
    - piRover_switch.py
    - test_arm_rover.py *(in class)*
    - **P03.piRoverKeyboard.docx** *(.docx or .pdf)*
