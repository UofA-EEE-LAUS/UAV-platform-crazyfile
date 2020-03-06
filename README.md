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

### Assembling
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


platform Mac or virtual machine

## For MAC Platform





For our project, we will use both [flow deck](https://www.bitcraze.io/flow-deck/) and [multiranger deck](https://www.bitcraze.io/multi-ranger-deck/).


## formation-control

Some simple python control script to control the crazyflie.

## firmware-change

Some firmware change in c language to achieve some automous functions.

## simple-gui

Modified simple gui to control the crazyflie.

## modelling

V-rep model of the crazyflies.
