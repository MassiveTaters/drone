from djitellopy import tello
from time import sleep

tello = tello.Tello()
tello.connect
print(tello.get_battery())

# takeoff command and moving forward to other side of the room #
tello.takeoff(200)
tello.move_forward(500)

# this is the command when the drone is on the other side of the room. it will go forward, flip, turn and head back. #

tello.flip_forward()
tello.rotate_counter_clockwise(90)
tello.move_forward(200)
tello.rotate_counter_clockwise(90)

# This command is for the drone to head back to land #

tello.move_forward(500)
tello.rotate_counter_clockwise(90)
tello.move_forward(200)

# landing commands, with a backflip #

tello.flip_back()
tello.land()
