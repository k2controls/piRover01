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
      - buzzer, drive, led, servo
    - Implement piRover_Drive
  - Session 2
    - piRover_buzzer
    - buzzer test with toggle
- Week 13
  - Session 1
    - Servo implementation
    - Switch implementation and testing
  - Session 2
    - **P03 Part 1 due** - piRover_keyboard with Rover functions
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

- Review piRover_keyboard.py
- Review/test fake implementation
- add piRover_buzzer_fake.py
- add piRover_servo_fake.py
- add piRover_LED_fake.py
- test keyboard with fakes
- GPIO implementations
  - piRover_buzzer.py
  - piRover_drive.py

    
**Session 2**

- weekP03 status

| Requirement   | Status  | Comment             |
|---------------|-------- |---------------------|
|Planning doc   | Done    | revise?             |
|pRover_keyboard| Done    | analog ins included |
|buzzer_fake    | Done    | add beep N times?   |
|drive_fake     | Done    | speed func added    |
|led_fake       | Done    | RGB, red,green,blue |
|servo_fake     | Done    |                     |
|buzzer         | TODO    | implement GPIO      |
|drive          | TODO    | implement GPIO      |
|led            | TODO    | implement GPIO      |
|servo          | TODO    | implement GPIO      |
|switch         | Opt     | Optional            |


- GPIO implementations
  - Drive
    - drive_init()
    - add left, right, speed
    - test
  - Buzzer
    - buzzer_init()
    - beep - use pwm for continuous beeping
    - add buzzer_beeps(beep_count):
  - Servo as time permits
  
---

### Assignments
- **W12** Assignments - Zip assignment files specified in the following activities and submit to the link below
    - **piRover_keyboard.py**
    - **piRover_buzzer_fake.py**
    - **piRover_buzzer.py**
    - **piRover_drive_fake.py**
    - **piRover_drive.py**
    - **piRover_led_fake.py** (must include red, green, and blue support)
    - **piRover_servo_fake.py**

