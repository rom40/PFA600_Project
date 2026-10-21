import time
from modbus import *
from address import *
from logger import *

class Crane:

    def __init__(self, client, current_x, current_y):
        self.client = client
        self.current_x = current_x
        self.current_y = current_y

    def move_crane(self, x):

        dx = abs(x - self.current_x)

        travel_time = dx / 250

        write_output(SET_X, x)

        time.sleep(travel_time + 0.2)

        self.current_x = x

    def pick(self):
            dy = abs(PICK_Y - self.current_y)
            travel_time =  dy / 250
            write_output(SET_Y, PICK_Y)
            time.sleep(travel_time + 0.2)
            self.current_y = PICK_Y
            write_output(VACUUM, 1)

            dy = abs(CLEARANCE_Y - self.current_y)
            travel_time =  dy / 250
            write_output(SET_Y, CLEARANCE_Y)
            time.sleep(travel_time + 0.2)
            self.current_y = CLEARANCE_Y

    def place(self):
            dy = abs(PICK_Y - self.current_y)
            travel_time =  dy / 250
            write_output(SET_Y, PICK_Y)
            time.sleep(travel_time + 0.2)
            self.current_y = PICK_Y
            write_output(VACUUM, 0)

            dy = abs(CLEARANCE_Y - self.current_y)
            travel_time =  dy / 250
            write_output(SET_Y, CLEARANCE_Y)
            time.sleep(travel_time + 0.2)
            self.current_y = CLEARANCE_Y