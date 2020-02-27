import time
from threading import Timer

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig

"""
- Anh Tran -
This script try to control the propeller of the crazyflie.

"""

class cf_control():
	"""docstring for cf_control"""
	def __init__(self, uri):
		self._cf = Crazyflie(rw_cache='./cache')

		# Define callback function variable
		self._cf.connected.add_callback(self._connected)
		self._cf.disconnected.add_callback(self._disconnected)
		self._cf.connection_failed.add_callback(self._connection_failed)
		self._cf.connection_lost.add_callback(self._connection_lost)

		self.is_connected = False
		self.new_command = 0
		print('Connecting to %s' % uri)
		self._cf.open_link(uri)
		
		self.roll = 0
		self.pitch = 0
		self.yaw = 0
		self.thrust = 0

	def _connected(self, uri):
		print(f"Connected to {uri}")
		# self._cf.commander.send_setpoint(0, 0, 0, 0) # Unlock startup thrust protection
		self.is_connected = True

	# Connection callback
	def _connection_failed(self, uri, msg):
		print(f"Connection to {uri} failed: {msg}.")

	def _connection_lost(self, uri, msg):
		print(f"Connection to {uri} lost: {msg}.")

	def _disconnected(self, uri):
		print(f"Disconnect from {uri}.")
		self.is_connected = False

	def set_control_command_param(self, roll, pitch, yaw, thrust):
		self.roll = roll
		self.pitch = pitch
		self.yaw = yaw
		self.thrust = thrust # thrust should be between 10001 -> 60000

	def send_control_command(self):
		if (self.new_command == 1):
			self._cf.commander.send_setpoint(0, 0, 0, 0)
			self.new_command = 0
			
		self._cf.commander.send_setpoint(self.roll, self.pitch, self.yaw, self.thrust)
		Timer(0.1,self.send_control_command).start()

	def close_link(self):
		self._cf.close_link()

	def _ramp_motors(self):
		thrust_mult = 1
		thrust_step = 500
		thrust = 20000
		pitch = 0
		roll = 0
		yawrate = 0

		# Unlock startup thrust protection
		self._cf.commander.send_setpoint(0, 0, 0, 0)

		while thrust >= 20000:
			self._cf.commander.send_setpoint(roll, pitch, yawrate, thrust)
			time.sleep(0.1)
			if thrust >= 25000:
				thrust_mult = -1
			thrust += thrust_step * thrust_mult
		self._cf.commander.send_setpoint(0, 0, 0, 0)
		# Make sure that the last packet leaves before the link is closed
		# since the message queue is not flushed before closing
		time.sleep(0.1)
		self._cf.close_link()

def main():
	# Initialize the low-level drivers
	cflib.crtp.init_drivers(enable_debug_driver=False)

	# Scan for Crazyflies and use the first one found
	print('Scanning interfaces for Crazyflies...')
	available = cflib.crtp.scan_interfaces()

	print('Crazyflies found:')
	for i in available:
		print(i[0])

	if len(available) > 0:
		cf = cf_control(available[0][0])

		while (not (cf.is_connected)):
			continue

		while (cf.is_connected):
			try:
				print("\nType in the command")
				roll = int(input("Roll: "))
				pitch = int(input("Pitch: "))
				yaw = int(input("Yaw: "))
				thrust = int(input("Thrust (10001 -> 60000): "))

				cf.new_command = 1
				cf.set_control_command_param(roll, pitch, yaw, thrust)
				cf.send_control_command()
				
			except KeyboardInterrupt:
				cf.close_link()

	else:
		print('No Crazyflies found, cannot run example')

if __name__ == '__main__':
	main()