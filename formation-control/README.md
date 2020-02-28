Use Guide
============

author: Zhihan Xu

This is the user guide for python script control to achieve certain functions. All the funtions need to be used under python library environment.

## multiranger_pointcloud.py

This function needs both flow deck and multiranger-deck to function. It is modified from original multiranger_pointcloud.py. It will scan the surrounding area and draw it on the ui axies, it could also show the position of the crazyflie if you want to. After disconnection, it will save the image.

## wallfollowing.py

This function needs both flow deck and multiranger-deck to function. It is modified from multiranger_push.py. The crazyflie will move forward, after it sees the obsticle, it will move back and forward until you remove the obsticle. 

## swarm.py

This funtion needs flow deck to function. One crazyflie will fly in circle while the other one rotating in the middle.

## initial_position.py

This function needs flow deck to function, It is modified from initial_position.py. It will draw a UoFA logo. It could also fly by giving xyz corrdinates. All the coordinates are calculated by kalman filter from informatin gathered by flow deck.
