
"""
A script to fly 5 Crazyflies in formation. One stays in the center and the
other four fly aound it in a circle. Mainly intended to be used with the
Flow deck.
The starting positions are vital and should be oriented like this

     >

^    +    v

     <

The distance from the center to the perimeter of the circle is around 0.5 m

"""
import math
import time
import logging
import sys
import time

import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils.multiranger import Multiranger

# Change uris according to your setup
URI0 = 'radio://0/80/2M/E7E7E7E701'
URI1 = 'radio://0/80/2M/E7E7E7E702'


# d: diameter of circle
# z: altituce
params0 = {'d': 0.6, 'z': 0.3}
params1 = {'d': 0.0, 'z': 0.5}



uris = {
    URI0,
    URI1,
    
}

params = {
    URI0: [params0],
    URI1: [params1],
    
}


def reset_estimator(scf):
    cf = scf.cf
    cf.param.set_value('kalman.resetEstimation', '1')
    time.sleep(0.1)
    cf.param.set_value('kalman.resetEstimation', '0')
    time.sleep(2)


def poshold(cf, t, z):
    steps = t * 10

    for r in range(steps):
        cf.commander.send_hover_setpoint(0, 0, 0, z)
        time.sleep(0.1)


def run_sequence(scf, params):
    cf = scf.cf

    # Number of setpoints sent per second
    fs = 4
    fsi = 1.0 / fs

    # Compensation for unknown error :-(
    comp = 1.3

    # Base altitude in meters
    base = 0.15

    d = params['d']
    z = params['z']

    poshold(cf, 2, base)

    ramp = fs * 2
    for r in range(ramp):
        cf.commander.send_hover_setpoint(0, 0, 0, base + r * (z - base) / ramp)
        time.sleep(fsi)

    poshold(cf, 2, z)

    for _ in range(2):
        # The time for one revolution
        circle_time = 8

        steps = circle_time * fs
        for _ in range(steps):
            cf.commander.send_hover_setpoint(d * comp * math.pi / circle_time,
                                             0, 360.0 / circle_time, z)
            time.sleep(fsi)

    poshold(cf, 2, z)

    for r in range(ramp):
        cf.commander.send_hover_setpoint(0, 0, 0,
                                         base + (ramp - r) * (z - base) / ramp)
        time.sleep(fsi)

    poshold(cf, 1, base)

    cf.commander.send_stop_setpoint()
 
def is_close(range):
    MIN_DISTANCE = 0.2  # m

    if range is None:
        return False
    else:
        return range < MIN_DISTANCE

def push(scf):
    cf=scf.cf
    with MotionCommander(scf) as motion_commander:
            with Multiranger(scf) as multiranger:
                keep_flying = True

                while keep_flying:
                    VELOCITY = 0.3
                    velocity_x = 0.0
                    velocity_y = 0.0

                    if is_close(multiranger.front):
                        velocity_x -= VELOCITY
                    if is_close(multiranger.back):
                        velocity_x += VELOCITY

                    if is_close(multiranger.left):
                        velocity_y -= VELOCITY
                    if is_close(multiranger.right):
                        velocity_y += VELOCITY

                    if is_close(multiranger.up):
                        keep_flying = False

                    motion_commander.start_linear_motion(
                        velocity_x, velocity_y, 0)

                    time.sleep(0.1)

            print('Demo terminated!')

if __name__ == '__main__':
    cflib.crtp.init_drivers(enable_debug_driver=False)

    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        swarm.parallel(reset_estimator)
        swarm.parallel(push)
