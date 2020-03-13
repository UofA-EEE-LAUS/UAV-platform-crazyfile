# Use Guide
============

author: Zhihan Xu

This is the user guide for python script control to achieve certain functions. All the funtions need to be used under [python library](https://github.com/bitcraze/crazyflie-lib-python) environment.

## [crazyflie python library installation](https://github.com/bitcraze/crazyflie-lib-python)

cflib is an API written in Python that is used to communicate with the Crazyflie
and Crazyflie 2.0 quadcopters. It is intended to be used by client software to
communicate with and control a Crazyflie quadcopter. For instance the [cfclient][cfclient] Crazyflie PC client uses the cflib.

### Developing for the cfclient
* [Fork the cflib](https://help.github.com/articles/fork-a-repo/)
* [Clone the cflib](https://help.github.com/articles/cloning-a-repository/), `git clone git@github.com:YOUR-USERNAME/crazyflie-lib-python.git`
* [Install the cflib in editable mode](http://pip-python3.readthedocs.org/en/latest/reference/pip_install.html?highlight=editable#editable-installs), `pip install -e path/to/cflib` 


* [Uninstall the cflib if you don't want it any more](http://pip-python3.readthedocs.org/en/latest/reference/pip_uninstall.html), `pip uninstall cflib`

Note: If you are developing for the [cfclient][cfclient] you must use python3. On Ubuntu (16.04, 18.08) use `pip3` instead of `pip`.


## multiranger_pointcloud.py
* put the py file under python library folder. Normally put it at crazyflie-lib-python/examples/
* This function needs both flow deck and multiranger-deck to work. 
* It is modified from original multiranger_pointcloud.py. 
* It will scan the surrounding area and draw it on the ui axies, it could also show the position of the crazyflie if you want to. After disconnection, it will save the image.

## wallfollowing.py
* put the py file under python library folder. Normally put it at crazyflie-lib-python/examples/
* This function needs both flow deck and multiranger-deck to function. 
* It is modified from multiranger_push.py. 
* The crazyflie will move forward, after it sees the obsticle, it will move back and forward until you remove the obsticle. 

## swarm.py
* put the py file under python library folder. Normally put it at crazyflie-lib-python/examples/swarm
* This funtion needs flow deck to function. 
* One crazyflie will fly in circle while the other one rotating in the middle.
* Crazyflies need to be written into different addresses, the method is indicated below.

## initial_position.py
* put the py file under python library folder. Normally put it at crazyflie-lib-python/examples/
* This function needs flow deck to function.
* It is modified from initial_position.py. 
* It will draw a UoFA logo. It could also fly by giving xyz corrdinates if you uncommented [line 127 to line 134](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/blob/380ad4ca1a0bd42ae11431eedf27d36eab3a2678/formation-control/initial_position.py#L127-L134) and commented the [line 17 to line 43](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/blob/380ad4ca1a0bd42ae11431eedf27d36eab3a2678/formation-control/initial_position.py#L17-L43). All the coordinates are calculated by kalman filter from informatin gathered by flow deck.

## About URI 
Uniform Resource Identifier (URI)
All communication links are identified using an URI build up of the following: InterfaceType://InterfaceId/InterfaceChannel/InterfaceSpeed

Currently only radio and debug interfaces are used but there's ideas for more like udp, serial, usb, etc…Here are some examples:

Radio interface, USB dongle number 0, radio channel 10 and radio speed 250 Kbit/s: radio://0/10/250K
Debug interface, id 0, channel 1: debug://0/1

The default one is E7E7E7E7E7. 

### You could change the URI by following these steps:
* 1.Unplug your Crazyradio
* 2.Start the Crazyflie
* 3.Connect the Crazyflie with USB cable
* 4.Start the client
* 5.You should now have something like "usb://0" in the URI selector in the top left corner
* 6.Click connect
* 7.Open the Configure 2.0 dialog
* 8.Change the address
* 9.Click write
* 10.Close the configure dialog
* 11.Restart the Crazyflie
* 12.Reconnect by clicking Connect
* 13.Reopen the Config dialog
### If you have the new address, the procedure to connect using the radio should be:
* 1.Close the client
* 2.Disconnect the USB cable
* 3.Plug in the radio again
* 4.Start the client
* 5.Enter your new address in the Address field
* 6.Click Scan
