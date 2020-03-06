<p>
<img src="https://img.shields.io/github/repo-size/UofA-EEE-LAUS/UAV-platform-crazyfile" alt="repo size">
<img src="https://img.shields.io/badge/platform-MacOS 10.15.3-blue" alt="platform">
<img src="https://img.shields.io/badge/platform-XUbuntu 2018.04-blue" alt="platform">
<p>

# UAV-platform-crazyfile

  <img src="https://upload.wikimedia.org/wikipedia/en/thumb/c/ca/University-of-Adelaide-Logo.svg/220px-University-of-Adelaide-Logo.svg.png" alt="uni logo">
 
**University of Adelaide Summer Research Internship 2019**

group member: 
*Zhihan Xu*
               *Ruoshi Sun*
              *Ziming Wang*
                 
            
              

====================================

## [crazyflie Setup](https://www.bitcraze.io/getting-started-with-the-crazyflie-2-0/#unpacking-the-crazyflie)

Setup crazyflie

### 1. Unpacking the Crazyflie

The Crazyflie 2.X box contains the following items. Make sure that you have all of them before you start assembling.

#### package contents

1 x Crazyflie 2.X control board with all components mounted
5 x CW propellers
5 x CCW propellers
6 x Motor mounts
1 x LiPo battery (240mAh)
5 x Coreless DC motors
2 x Short expansion connector pins (1×10, 2mm spacing, 8 mm long)
2 x Long expansion connector pins (1×10, 2mm spacing, 14 mm long)
1 x Battery holder expansion board
1 x USB cable (only with the Crazyflie 2.1)


### 2. Testing
The Crazyflie 2.X is tested extensively when produced, but to make sure nothing has happened during shipping/storage you should run the tests before starting the assembly. Power on the Crazyflie 2.X using a USB source (either computer or charger) and check the results of the test below. Note that it’s important to hold the Crazyflie 2.X steady during the test and away from strong magnetic sources.

#### self-test
Before you start assembling anything, run the power on self-test by connecting the Crazyflie 2.X to a uUSB power source. The LEDs M1 and M4 will indicate the result of the test. If the M4 LED blinks GREEN five times fast, then the test has passed.

#### self-test fails
If the self-test fails, then the M1 LED blinks 5 times fast RED, then pauses and does it again. 

### 3.Assembling
Assembling your Crazyflie 2.X will probably take less than 10 minutes, but there are a few pitfalls. So make sure to follow the instructions below!

#### twisting the wires
Start by twisting the wires of the four motors. This will reduce electronic noise and make the wires fit better in the motor mount “hooks”.

#### mount the motors
Push the four motors into the motor mounts. You will need some force to insert them. If it is difficult doing it as in the video try putting the motor can towards a table edge and press on the mount, however don’t press on the motor axis while inserting them as it might damage the motor. The motor should be inserted all the way to the stop in the mount.

#### attach the twisted wire
Attach the twisted wire into the two small “hooks” that are underneath the motor mount.

#### insert the motor
Insert the motor mounts on the Crazyflie 2.X wings. They are press fit and might need a small amount of force. Make sure they go all the way to the stop. It’s not important which motor you put where. After it’s been inserted, connect the motor connectors to the Crazyflie 2.X.

#### attach the propellers
Now it’s time to attach the propellers.

Note: There are two kinds of propellers, the clock wise (CW) and counter clock wise (CCW) propellers, each kind has their own bag in the box. Notice the shape of the tips, the sharper corner is on back side of the rotation direction. The CW propellers are also usually marked with an “A”, “A1” or “A2”, while the CCW propellers are marked with “B”, “B1” or “B2” (the number is irrelevant).

Also make sure that the correct side is facing up, the top side should be convex.

Here’s a detailed view of where to attach CW and CCW propellers.
![image](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/raw/master/images/cf2_props.png)

#### attach the rubber pad
The rubber pad should be attached to the Crazyflie 2.X between the expansion headers. This will create friction, keep the battery from slipping out and also protect the electronics.

#### attach headers
There are two types of headers in the box, long and short ones. Find the two short ones and insert them into the expansion connector.

#### attach the battery
Place the battery between the headers inserted into the expansion connector and insert the battery holder board onto the headers. Watch out for the pins that can be a bit sharp when inserting it. The friction should hold the battery in place so tighten it until it does.

Now connect the battery and you are finished with the assembly. The battery wires can preferably be bent and placed underneath the PCB to be out of the way.

#### power on!
The assembly is finished, now it’s time to power it on! Note that the power button is a push button, not a sliding button. During the power-on self-test all the propellers will spin in sequence. Make sure they all spin, if they don’t then check the motor connections.

### Start up sequence
When the Crazyflie 2.X is powered on it will automatically go through a short sequence of events to get ready for flight.

*Run self tests - the Crazyflie 2.X checks that the hardware is OK*
*Calibrate sensors - the Crazyflie 2.X reads its sensors to get base values. It must be absolutely still to do this, so it’s best to put it on a level surface for a second.*
*Ready to fly!*

### Understanding LEDs
You also need to understand what the LEDs mean.

Power on and all is good: The blue LEDs (2 and 3) are fully lit and the front right LED (1) is blinking red twice every second.
Power on and all is good but sensors are not yet calibrated: The blue LEDs (2 and 3) are fully lit and the front right LED (1) is blinking red with 2 seconds interval. Put the Crazyflie 2.X on a level surface and keep it absolutely still to calibrate.
Radio connected: The front left LED (4) is flickering in red and/or green.
Battery low: The front right LED (1) is fully lit in red. It’s time to land and re-charge the battery.
Charging: The back left blue LED (3) is blinking while the right back blue LED (4) is lit.
Boot loader mode: The blue LEDs (2 and 3) at the back are blinking approximately once every second.
Self test fail: The right front LED (1) is repeatedly blinking five short red pulses with a longer pause between groups.

![image](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/raw/master/images/frontCF.png)

## Installing on a computer
When using a computer to fly the Crazyflie, you also need a standard gamepad (more information) for maneuvering and a Crazyradio PA for communication.


### For MAC Platform
On OS X it is possible to run the client from source code. With this option you are required to clone the source code from Git and install a few software packages. 

#### Using the official python distribution

The easiest to get the client running on Mac if you do not already have Homebrew installed is to use the official Python distribution.
If you are using Homebrew look at the next section.
If you are using Anaconda/Conda, the procedure should be very similar but you can skip the python installation.

 1) Download and install python from [python.org](https://python.org)
 2) [Download sdl2](https://www.libsdl.org/download-2.0.php) for Mac OSX and copy SDL2.framework into /Lirary/Frameworks
 3) Open a console and install the client with ```python3 -m pip install cfclient[qt5] pysdl2```. This will install the latest release.

You can now launch the client with ```python3 -m cfclient.gui```

If you want to develop and modify the client, you can clone this repos, uninstall cfclient with ```python3 -m pip uninstall cfclient``` and install it in development mode by navigating into the repos root folder and installing the client in edit mode: ```python3 -m pip install -e .```.

#### Using homebrew
**IMPORTANT NOTE**: The following will use
[Homebrew](http://brew.sh/) and its own Python distribution. If
you have a lot of other 3rd party python stuff already running on your system
they might or might not be affected by this.

1. Install homebrew

    See [the Homebrew site](https://brew.sh/)

1. Install the brew bottles needed
    ```
    brew install python3 sdl sdl2 sdl_image sdl_mixer sdl_ttf libusb portmidi pyqt5
    ```

1. Install the client

    * If you only want to use the client to fly the Crazyflie and don't care about coding
    ```
    pip3 install cfclient
    ```

    * If you want to develop the client and play with the source code. From the source folder run
    ```
    pip3 install -e .
    ```
    If you want to develop on cflib as well, install cflib from <https://github.com/bitcraze/crazyflie-lib-python>

1. You now have all the dependencies needed to run the client. The client can now be started from any location by:
    ```
    cfclient
    ```

### For VM Platform

#### install VirtualBox
Before downloading the virtual machine you must have VirtualBox or some other virtualization application installed on your computer. VirtualBox is a cross-platform virtualization application that imports and runs our preconfigured virtual machine.
[Download and install Oracle VirtualBox.](https://www.virtualbox.org/)

#### download the Bitcraze virtual machine
Once you have installed VirtualBox you can download the virtual machine from the [Bitcraze VM release page.](https://github.com/bitcraze/bitcraze-vm/releases/)

#### installing the virtual machine
After downloading the virtual machine, double click it. VirtualBox is now going to start, and ask you to import the virtual machine. Click import.

#### start the virtual machine
Now it’s time to start the Bitcraze virtual machine. in VirtualBox, highlight the Bitcraze VM and start it.

#### update source code
In the virtual machine double click the “update all projects” icon on the desktop. This pulls down the latest source code from GitHub for all projects.
![image](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/raw/master/images/update-all-projects-icon.png)

### configure USB on the virtual machine

#### Windows
Install the Crazyradio Windows USB driver.
In the bottom right corner click the USB icon and choose “Bitcraze Crazyradio PA USB dongle”.
![image](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/raw/master/images/SwPic5Final.png)

Now choose your game controller in the same list.

#### OS X
In the bottom right corner click the USB icon, then click “USB settings”.
![image](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/raw/master/images/SwPic2.1Final.png)

Click the USB filter “+” icon.
![image](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/raw/master/images/SwPic3Final.png)

Choose your game controller from the list. Click OK.
![image](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/raw/master/images/SwPic4Final.png)

Now click the USB icon again and choose the “Bitcraze Crazyradio PA USB dongle”.
![image](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/raw/master/images/SwPic5Final_os.png)

Now choose your game controller in the same list.

### start the Crazyflie client
Double click the “Crazyflie client” icon on the VM desktop
![image](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/raw/master/images/cf-client-icon.png)

## latest firmware flash by client
### download latest firmware
*Open the web browser and go to https://github.com/bitcraze/crazyflie-release/releases. If you are on the VM, open the browser in the VM.
download the zip file named crazyflie-xxx.zip from the latest release.*
Note: You must have the zip file, some browsers automatically unzip after download.

### update firmware in the Crazyflie
*Turn the Crazyflie off.
Start the Crazyflie in bootloader mode by pressing the power button for 3 seconds. Both the blue LEDs will blink.
Go back to the Crazyflie client and click the Connect -> Bootloader menu.*
![image](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/raw/master/images/update_firmware.png)
*Click the “Initiate bootloader cold boot” button. After a few seconds the status should read “Connected to bootloader”.
Click the “Browse” button and go to home/bitcraze/Downloads and select the zip file you downloaded earlier.
Click the “Program” button. The progress bar will go from 0% to 100% twice, as the firmware for the two processors is uploaded to the Crazyflie.
Click the “Restart in firmware mode” button. The Crazyflie reboots and is now updated.
Close the bootloader window.*

### connect to the Crazyflie
*In the Crazyflie client click the “Scan” button in top left corner. The radio settings for you Crazyflie is displayed in the drop-down list.
Choose your Crazyflie from the drop-down list.*
![image](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/raw/master/images/connect_to_the_crazyflie.png)
*Click the “Connect” button.*
Now that you have connected your Crazyflie to your client, telemetry data is continuously sent from the copter to the client. When you move the Crazyflie around you will see the flight data being updated in realtime, as well as battery status and the link quality.

## Fly!



## For our project, we will use both [flow deck](https://www.bitcraze.io/flow-deck/) and [multiranger deck](https://www.bitcraze.io/multi-ranger-deck/).


## formation-control

Some simple python control script to control the crazyflie.

## firmware-change

Some firmware change in c language to achieve some automous functions.

## simple-gui

Modified simple gui to control the crazyflie.

## modelling

V-rep model of the crazyflies.
