Use Guide
============

author: Zhihan Xu

This is the user guide for changing the firmware to achieve certain autonomous functions.

## sequence.c

This function is implemented as a deck. It need to be put in src/deck/drivers/src.  Change the makefile and config.mk [accordingly](https://wiki.bitcraze.io/doc:crazyflie:api:firmware:deck:howto). This funciton has the samilar function as the flowsequenceSync.py in python library. The crazyflie will start to fly after 3 seconds the power button is pressed.

## push.c

This function is implemented as a deck. It need to be put in src/deck/drivers/src.  Change the makefile and config.mk [accordingly](https://wiki.bitcraze.io/doc:crazyflie:api:firmware:deck:howto). This funciton has the samilar function as the multiranger_push.py in python library. The crazyflie will start to hover after you unlock the UAV by putting hands on top of it and remove after a while.

## Stop-at-obsticle

This stop-at-obsticle works as a deck. The function works during all the running time, which was written in high-level-command. Put the stop-at-obsticle.c at the deck/drivers/src. Change the crtp_commander_high_level files accordingly. In order to control the crazyflie while this funciton is running, the python control need to use the high-level control as well. simple.py is an example to control the crazyflie to move forward for 1 meter.
