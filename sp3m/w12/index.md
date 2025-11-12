---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 3](../) - Week 12

W12: You'll review and extend the main keyboard interface using fakes. You'll then create an piRoverDrive module that implements the required drive operations. Finally, you'll wire this piRoverDrive module to the keyboard drive interface.

**Schedule**
- Week 12
  - Session 1 (today)
    - Fakes and keyboard testing
    - Complete piRover_led_fake.py on your own.
  - Session 2
    - Implement piRover_Drive
    - Implement piRover_Buzzer
- Week 13
  - Session 1
    - piRover_Buzzer
    - piRover_Servo
  - Session 2
    - piRover_keyboard.py - review and extensions
    - piRover_switch.py 
    - test_piRover_armed.py

- Week 14
  - Session 1
    - P03 Part 1 due - piRover_keyboard
  - Session 2
    - No class - Holiday break
- Week 15
  - Session 1
    - Bluetooth module and messaging
  - Session 2
    - piRover_phone_app.py
- Week 16
  - Session 1
    - piRover_phone_app.py
      - testing and extensions
      - shut down
      - start up
      - Enabling at Startup
  - Session 2
    - No class session
    - P03 Part 2 due
    - Debt
    - Retro

**Session 1**    

- Review piRover_keyboard.py
- Review/test fake implementation
- add piRover_buzzer_fake.py
- add piRover_servo_fake.py
- add piRover_LED_fake.py
- test keyboard with fakes


    
**Session 2**

- weekP03 status

| Requirement   | Status  | Comment             |
|---------------|-------- |---------------------|
|Planning doc   | Done    | revise?             |
|pRover_keyboard| Done    | analog ins included |
|buzzer_fake    | Done    |   |
|drive_fake     | Done    | speed func added    |
|led_fake       | Done    | red,green,blue with dim |
|servo_fake     | Done    |                     |
|buzzer         | TODO    | implement GPIO      |
|drive          | TODO    | implement GPIO      |
|led            | TODO    | implement GPIO      |
|servo          | TODO    | implement GPIO      |
|switch         | Opt     | Optional            |

- GPIO implementations
  - piRover_buzzer.py
  - piRover_drive.py

- GPIO implementations - Drive
  - drive_init()
  - add left, right, speed
  - test
- GPIO implementations - Buzzer
    - buzzer_init()
    - beep - use pwm for continuous beeping
    - add buzzer_beeps(beep_count):
- GPIO implementations - Servo as time permits
  
---

### Assignments
- **W12** Assignments - Zip assignment files specified in the following activities and submit to the link below
    - **piRover_keyboard.py** (must include all input from planning doc)
    - **piRover_buzzer_fake.py**
    - **piRover_buzzer.py**
    - **piRover_drive_fake.py**
    - **piRover_drive.py**
    - **piRover_led_fake.py** (must include red, green, and blue support)
    - **piRover_servo_fake.py**