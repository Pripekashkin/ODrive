from __future__ import print_function
import odrive
from odrive.enums import *
import time
import math

#default current limit

current_limit = 20
velocity_limit = 20
pole_pairs_number = 15
resistance_calib_max_voltage = 4
current_control_bandwidth = 100

#encoder

cpr = 90

#controller

bandwidth = 100
pos_gain = 1
vel_gain = 0.02
vel_integrator_gain = 0.1
vel_limit = 1000

# Find a connected ODrive (this will block until you connect one)

print("finding an odrive...")
my_drive = odrive.find_any()

############### AXIS ###############

my_drive_axis0 = my_drive.axis1 #change axis
print("done")

############### CURRENT LIMIT ###############

print("current begin")
my_drive_axis0.motor.config.current_lim = current_limit
time.sleep(0.01)

my_drive_axis0.controller.config.vel_limit = velocity_limit
time.sleep(0.01)

my_drive_axis0.motor.config.pole_pairs = pole_pairs_number
time.sleep(0.01)

my_drive_axis0.motor.config.resistance_calib_max_voltage = resistance_calib_max_voltage
time.sleep(0.01)

#current range

my_drive_axis0.motor.config.current_control_bandwidth = current_control_bandwidth
time.sleep(0.01)

print("current end\n")

############### ENCODER ###############

print("endocder begin")
my_drive_axis0.encoder.config.mode = ENCODER_MODE_HALL
time.sleep(0.01)

my_drive_axis0.encoder.config.cpr = cpr
time.sleep(0.01)

print("encoder end\n")

############### CONTROLLER ###############

print("contorller begin")
my_drive_axis0.encoder.config.bandwidth = bandwidth
time.sleep(0.01)

my_drive_axis0.controller.config.pos_gain = pos_gain
time.sleep(0.01)

my_drive_axis0.controller.config.vel_gain = vel_gain
time.sleep(0.01)

my_drive_axis0.controller.config.vel_integrator_gain = vel_integrator_gain
time.sleep(0.01)

my_drive_axis0.controller.config.vel_limit = vel_limit
time.sleep(0.01)

my_drive_axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL
time.sleep(0.01)

print("controller end\n")

#REBOOT

print("start reboot")

my_drive.save_configuration()
time.sleep(0.01)

my_drive.reboot()
time.sleep(5)

