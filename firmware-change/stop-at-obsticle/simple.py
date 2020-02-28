import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.mem import MemoryElement
from cflib.crazyflie.mem import Poly4D
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger

# URI to the Crazyflie to connect to
#uri = 'radio://0/120/2M/E7E7E7E707'
uri = 'radio://0/80/2M'

# The trajectory to fly
# See https://github.com/whoenig/uav_trajectories for a tool to generate
# trajectories



def reset_estimator(cf):
    cf.param.set_value('kalman.resetEstimation', '1')
    time.sleep(0.1)
    cf.param.set_value('kalman.resetEstimation', '0')
    time.sleep(2)

def activate_high_level_commander(cf):
    cf.param.set_value('commander.enHighLevel', '1')


def activate_mellinger_controller(cf):
    cf.param.set_value('stabilizer.controller', '2')
    time.sleep(0.1)
    cf.param.set_value('ctrlMel.kp_z', '0.6')

def run_sequence(cf, trajectory_id, duration):
    commander = cf.high_level_commander
    print('taking off')
    commander.takeoff(0.4, 2.0)
    time.sleep(3.0)
    commander.go_to(1.0,0,0,0,duration,relative=True)
    time.sleep(duration)
    print('landing')
    commander.land(0.1, 2.0)
    time.sleep(1.2)
    commander.stop()


if __name__ == '__main__':
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        cf = scf.cf
        trajectory_id = 1

        activate_high_level_commander(cf)
        time.sleep(0.5)
        activate_mellinger_controller(cf)
        time.sleep(0.5)
        duration = 6.5
        # print('The sequence is {:.1f} seconds long'.format(duration))
        reset_estimator(cf)
        run_sequence(cf, trajectory_id, duration)