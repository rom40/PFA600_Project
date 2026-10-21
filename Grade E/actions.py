import json
import time

from address import *
from modbus import *


def load_actions(filename):

    with open(filename, "r") as file:
        data = json.load(file)

    return data["actions"]


def execute_action(crane, action):

    # Change vacuum
    if "vacuum" in action:
        write_output(VACUUM, action["vacuum"])
        time.sleep(0.1)

    # Start process
    if "process" in action:
        if action["process"] == 1:
            write_output(START_P1, 1)
        elif action["process"] == 2:
            write_output(START_P2, 1)
            print('debug: process 2 started')
        else:
            print(f"Unknown process: {action['process']}")

    # Move crane
    if "setX" in action or "setY" in action:

        x = action.get("setX", crane.current_x)
        y = action.get("setY", crane.current_y)

        crane.move_crane(x, y)