---
layout: default
---
## piRover Builds by K2 - Course 1:Python

### [piRover01](../../) - [Sprint 1](../) - Week 03

W03 - During this week you verify the function of your piRover by downloading, installing, and running Yahboom Robot software on your mobile device. You'll also get your first introduction to Linux and Python.

**Session 1**

- No Class Session - KEK at a conference
- Own your own  
  - **Activity: Build Validation - Part 2**
  - Review today's video and practice connecting remotely to your Pi Desktop.
   

**Session 2**

- Complete build validation 2. Review "Creating a Remote Connect" and verify you can connect remotely and do have Internet access on your piRover.
- [Build Validation - Part 1](../../lessons/13/BuildValidationPart1.docx)
  - **Video:** [Build Validation - Overview](https://youtu.be/RanVP2aGpzg){:target="_blank"}
- [Build Validation - Part 2](../../lessons/13/BuildValidationPart2.docx)
  - **Video:** [Build Validation - Line Follower](https://youtu.be/k2n6r7ibBpA){:target="_blank"}
  - **Video:** [Build Validation - Servo LEDs](https://youtu.be/Qzsm5Gdbr1w){:target="_blank"}
  - **Video:** [Build Validation - Sonar Tracking](https://youtu.be/oyVOCAg20fM){:target="_blank"}
  - **Video:** [Build Validation - Camera    ](https://youtu.be/4QIFle79sMI){:target="_blank"} 

- [Connecting Remotely](../../lessons/11/CreatingARemoteConnection.pdf){:target="_blank"}
  1. Connect to your remote desktop
    - Option 1: Ethernet - connection is peer-to-peer
      - yahboomtank.local is the VNC server name
    - Option 2: Network/Wi-Fi connection (not at NMC) 
      - Raspberry Pi and your workstation share the same network
      - yahboomtank is the VNC server name
  2. Use localhost (or 192.168.50.1) in Pi's browser to configure Wi-Fi client 
    - User=Admin, Password=yahboom
    - Enter the pass code for your Wi-Fi access point (AP)
    - Hover or Wi-Fi icon in menu bar
    - wlan0 shows an IP address
    - Test in a terminal window
      - ping 8.8.8.8    (ctrl+C to exit)
      - ping google.com (ctrl+C to exit)

- **Assigned** - Create a Zoom video verifying your remote desktop and Internet connection
  - Start Zoom in your "My Personal Meeting"
  - Record your session either locally or to the cloud
  - Share your Desktop selecting the VNC window
  - Hover over the Wi-Fi icon to show the wlan0 IP address
  - Use the browser or the ping command to verify your connection to the Internet

<!-- - The following resource is provided if there are issues with DNS settings
- [Setting DNS](https://pimylifeup.com/raspberry-pi-dns-settings/){:target="_blank"}  -->

- Freeing up space
  - Expand the file system to use the entire 32G SD card
    - Open a terminal window
    - Enter "sudo fdisk -l"
    - Note the size of the Linux partition
    - Enter "sudo raspi-config"
    - Navigate to "Advanced Options" and press Enter
    - Select "Expand Filesystem"
    - Exit by pressing Escape
    - Enter "reboot"
    - When the desktop connection returns, enter "sudo fdisk -l" again. Note the change.


  - Remove unused files
    - Open Downloads - delete openCV
    - Empty Trash
    - Remove LibreOfficepace using the following commands 
  
```bash
sudo apt-get remove --purge libreoffice*
sudo apt-get clean
sudo apt-get autoremove

```   

---

### Assignments
- **W03** Assignments - Zip assignment files specified in the following activities and submit to the link below
    - **Activity: Build Validation - Part 2**
    - **Zoom video** showing remote desktop and Internet connectivity. See above.
      - Add your mp4 file to this week's zip file
      - or paste the URL to your cloud recording in the text area