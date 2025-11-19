---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 3](../) - Week 13

W13:  We'll continue with GPIO implmentation producing servo and switch code. 

**Schedule (Revised)**

- Week 13
  - Session 1
    - piRover_Buzzer - review
    - piRover_Servo
    - piRover_switch.py 
  - Session 2
    - piRover_keyboard.py - review and extensions
    - P03 Part 1 assigned
- Week 14
  - Session 1
    - *No Zoom class session*
    - P03 Part 1 - work on your own.
    - **P03 Part 1 Due** - end of the day on Wednesday, Nov 26
  - Session 2
    - *No class - Holiday break*
- Week 15
  - Session 1
    - Bluetooth module, messaging, and integration
  - Session 2
    - Analog inputs and operations
    - piRover_phone_app.py
- Week 16
  - Session 1
    - piRover_phone_app.py
      - testing and extensions
      - shut down
      - start up
      - Enabling at Startup
  - Session 2
    - *No Zoom class session*
    - **P03 Part 2 Due** - end of the day on Wednesday, Dec 10
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
|servo          | Done     | in progress      |
|switch         | Done    | used for 'arm'      |


  - piRover_servo.py
    - [P03.Servo.pdf](P03.Servo.pdf){:target='_blank'}
  - piRover_switch.py 
  - test_arm_rover.py.py
  
    
**Session 2**

- piRover_keyboard testing 
  - all functional except LED

- Assigned: [P03 Part 1](P03.piRoverKeyboard.docx)
  - Requirements - Table 1
    - Table 1 defines required actions
    - Table 1 identifies your keyboard interface design
    - Table 1 indicates test results for fakes
    - Table 1 indicates test results for finals
  - Review and test Buzzer, Drive, and Servo
    - Verify and identify any issues
  - LED functionality
    - Extend piRover_led_fake as required
    - Implement piRover_led as required
    - Test, verify, and identify any issues
  - Assessment
    - Review the grading rubric on the final page
    - Zip your final weekP03 code and add your completed P03.piRoverKeyboard document as either a .docx or .pdf file
    - Verify you zip file contains all required files
    - Submit to the course link by the deadline below. No late work is accepted
      - ***Due Date:*** P03 Part 1 - Wednesday, Nov 26 end of the day



---

### Assignments
- **W13** Assignments 
  - *No submission required*
  - **BUT** you must test your ability to zip and submit.
    - PRACTICE - Zip your weekP03 folder and submit. Be sure to add your updated P03.piRoverKeyboard document.
    - **weekP03.zip**
      - piRover_buzzer_fake.py
      - piRover_buzzer.py *(with pwm)*
      - piRover_drive_fake.py
      - piRover_drive.py  *(all drive and speed function)*
      - piRover_keyboard.py *(must implement all functions in table 1)*
      - piRover_led_fake.py
      - piRover_servo_fake.py
      - piRover_servo.py *(left, right, center, set_position)*
    - **P03.piRoverKeyboard.docx** *(.docx or .pdf)*
