import json
import time

from address import *
from modbus import *
from tkinter import filedialog


def load_config(filename):

    with open(filename, "r") as file:
        return json.load(file)


def save_config(data):
    filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")]
        )
    
    if filename:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)


config = load_config("C:/Users/rom38/OneDrive - Högskolan Väst/Y1/SP1/PFA600/Project/Grade A/locations.json")

actions = config["actions"]


def add_move(position_name):
    actions.append({
        "type": "move",
        "position": position_name
    })


def add_vacuum(value):
    actions.append({
        "type": "vacuum",
        "value": value
    })


def add_process(process_number):
    actions.append({
        "type": "process",
        "process": process_number
    })

def execute_action(crane, action):

    # Change vacuum
    if "vacuum" in action:
        write_output(VACUUM, action["vacuum"])
        time.sleep(0.1)

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

def wait_for_signal(address, value):
    print(f"Waiting for address {address} to become {value}...")

    while True:
        if read_input(address) == value:
            return

        time.sleep(0.05)