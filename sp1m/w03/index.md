---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 1](../) - Week 03

W03 - During this week you verify the function of your piRover by downloading, installing, and running Yahboom Robot software on your mobile device. You'll also get your first introduction to Linux and Python.

**Session 1**
- Build updates. Issues?

- Startup - a review
  - Smartphone app testing
- [Build Validation - Part 1](../../lessons/13/BuildValidationPart1.docx)
  - **Video:** [Build Validation - Overview](https://youtu.be/RanVP2aGpzg){:target="_blank"}
- [Build Validation - Part 2](../../lessons/13/BuildValidationPart2.docx)
  - **Video:** [Build Validation - Line Follower](https://youtu.be/k2n6r7ibBpA){:target="_blank"}
  - **Video:** [Build Validation - Servo LEDs](https://youtu.be/Qzsm5Gdbr1w){:target="_blank"}
  - **Video:** [Build Validation - Sonar Tracking](https://youtu.be/oyVOCAg20fM){:target="_blank"}
  - **Video:** [Build Validation - Camera    ](https://youtu.be/4QIFle79sMI){:target="_blank"}
- [Test and Deploy (Hybrid Robotics)](../../lessons/12/TestAndDeploy.docx)   
- [Connecting Remotely](../../lessons/11/CreatingARemoteConnection.pdf){:target="_blank"}

- The following resource is provided if there are issues with DNS settings
- [Setting DNS](https://pimylifeup.com/raspberry-pi-dns-settings/){:target="_blank"}


    
**Session 2**
    
- Review - [Connecting Remotely](../../lessons/11/CreatingARemoteConnection.pdf){:target="_blank"}
  - Ethernet connection is peer-to-peer, so yahboomtank.local
  - Network/Wi-Fi connection (not at NMC) - yahboomtank
  - Use localhost in browser to configure Wi-Fi client User=Admin, Password=yahboom


- The following resource is provided if there are issues with DNS settings
- [Setting DNS](https://pimylifeup.com/raspberry-pi-dns-settings/){:target="_blank"} 


- Free up space on SD cards
  - Open Downloads - delete openCV
  - Empty Trash
  - Remove LibreOfficepace
  
```bash
sudo apt-get remove --purge libreoffice*
sudo apt-get clean
sudo apt-get autoremove

```   

- [Linux Command - investigation](../../lessons/16/LinuxInvestigation.pdf){:target="_blank"}
- [Introduction to Linux](https://training.linuxfoundation.org/training/introduction-to-linux/){:target="_blank"} (optional resource)

 

  
---

### Assignments
- **W03** Assignments - Zip assignment files specified in the following activities and submit to the link below
    - **Activity: Build Validation - Part 1**
    - **Activity: Build Validation - Part 2**