---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 3](../) - Week 12

W12: This week's focus is Pulse Width Modulation. This type of output provides an output pulse with the ability to control the duration of the pulse. This creates an analog value that can be used to dim an LED or control motor speed. 


**Session 1**
- [Project 02 - User Move](../../projects/P02/P02UserMove.pdf){:target='_blank'}  (solution/review)
- Review - Pulse Width Modulation (PWM) Introduction and Motor Speed Control
- Sprint 3 Plan
  - Step 1 Keyboard interface
  - Step 2 Fake modules and integration
  - Step 3 Module implementations and integration
  - Step 4 Bluetooth interface replaces keyboard
- Partner Activity - [Keyboard Interface Design](../../lessons/32/KeyboardInterfaceDesign.docx)
    - Submit a Keyboard Interface document (.docx or .pdf) that specifies your vision for a keyboard interface for all piRover functions available on the smartphone Control interface.
    - Include additional moves [shown here](../../lessons/32/tank_drive_images.pdf){:target='_blank'}
    - Include speed control - set speed?
- With your partner, create piRover_keyboard.py as directed in the activity document using the [https://replit.com/](https://replit.com/){:target='_blank'} resource.
  - You will need to create an account.
  - The instructor will demonstrate sample code.
  
**Session 2**
- [Project 02 - User Move](../../projects/P02/P02UserMove.pdf){:target='_blank'}  (solution/review)
- Review - Keyboard Interface Design (.docx or .pdf)
- Open the piRover solution on your Pi and create the final weekP03 directory. This folder will contain project code for the remainder of the semester.
- Copy your piRover_keyboard.py code from the last session into your piRover solution. Revise and extend based on the class discussion.
  - extend to include speed value input.
- Create/connect piRover_drive_fake.py
  - test fake implementation
  - see assignment requirements below

---

### Assignments
- **W12** Assignments - Zip assignment files specified in the following activities and submit to the link below
    - **Keyboard interface document**- must have completed table with all rover functions identified and keystrokes assigned
    - **piRover_keyboard.py** 
      - must have selection structure (if/elif/else) that supports rover functions identified in interface document
      - piRover_drive_fake is integrated with drive messages produced by fake rather than in main keyboard file
    - **piRover_drive_fake.py**
      - includes function stubs for all drive operations including set_speed()