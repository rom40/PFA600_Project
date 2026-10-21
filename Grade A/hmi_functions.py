
import tkinter as tk
from tkinter import messagebox

from modbus import read_input
from address import AT_X, AT_Y


def refresh_action_list(action_list, actions):
    action_list.delete(0, tk.END)

    for i, action in enumerate(actions):
        if "setX" in action and "setY" in action:
            description = (
                f"MOVE | X: {action['setX']} | Y: {action['setY']}"
            )
        elif "vacuum" in action:
            state = "ON" if action["vacuum"] == 1 else "OFF"
            description = f"VACUUM {state}"
        elif "process" in action:
            description = f"PROCESS {action['process']}"
        else:
            description = str(action)

        action_list.insert(tk.END, f"{i + 1}. {description}")


def add_move(x_entry, y_entry, actions, action_list):
    try:
        x = int(x_entry.get())
        y = int(y_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Enter valid integer coordinates.")
        return

    actions.append({"setX": x, "setY": y})
    refresh_action_list(action_list, actions)


def add_vacuum(value, actions, action_list):
    actions.append({"vacuum": value})
    refresh_action_list(action_list, actions)


def add_process(process_number, actions, action_list):
    actions.append({"process": process_number})
    refresh_action_list(action_list, actions)


def remove_selected_action(action_list, actions):
    selection = action_list.curselection()

    if not selection:
        messagebox.showinfo("No selection", "Select an instruction first.")
        return

    actions.pop(selection[0])
    refresh_action_list(action_list, actions)


def update_selected_position(action_list, actions):
    selection = action_list.curselection()

    if not selection:
        messagebox.showinfo("No selection", "Select a movement first.")
        return

    action = actions[selection[0]]

    if "setX" not in action or "setY" not in action:
        messagebox.showinfo(
            "Invalid selection",
            "Select a movement instruction to update."
        )
        return

    try:
        action["setX"] = read_input(AT_X)
        action["setY"] = read_input(AT_Y)
    except Exception as error:
        messagebox.showerror("Modbus error", str(error))
        return

    refresh_action_list(action_list, actions)


def move_to_selected_position(action_list, actions, crane):
    selection = action_list.curselection()

    if not selection:
        messagebox.showinfo("No selection", "Select a movement first.")
        return

    action = actions[selection[0]]

    if "setX" not in action or "setY" not in action:
        messagebox.showinfo(
            "Invalid selection",
            "Select a movement instruction."
        )
        return

    crane.move_crane_total(action["setX"], action["setY"])


def move_crane(x_entry, y_entry, crane):
    try:
        x = int(x_entry.get())
        y = int(y_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Enter valid integer coordinates.")
        return

    crane.move_crane_total(x, y)


def update_position(root, position_label):
    try:
        current_x = read_input(AT_X)
        current_y = read_input(AT_Y)

        position_label.config(
            text=f"X: {current_x}    Y: {current_y}"
        )
    except Exception:
        position_label.config(text="Unable to read crane position")

    root.after(500, lambda: update_position(root, position_label))
