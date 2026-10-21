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

    # Move crane
    if "setX" in action or "setY" in action:

        x = action.get("setX", crane.current_x)
        y = action.get("setY", crane.current_y)

        crane.move_crane(x, y)

def wait_for_signal(address, value):
    print(f"Waiting for address {address} to become {value}...")

    while True:
        if read_input(address) == value:
            return

        time.sleep(0.05)