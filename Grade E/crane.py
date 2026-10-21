import time
from modbus import *
from address import *


class Crane:

    def __init__(self, client, current_x, current_y):
        self.client = client
        self.current_x = current_x
        self.current_y = current_y

    def move_crane(self, x, y):

        dx = abs(x - self.current_x)
        dy = abs(y - self.current_y)

        travel_time = max(dx, dy) / 250

        print(f"Moving to X={x}, Y={y}")

        write_output(SET_X, x)
        write_output(SET_Y, y)

        time.sleep(travel_time + 0.2)

        self.current_x = x
        self.current_y = y