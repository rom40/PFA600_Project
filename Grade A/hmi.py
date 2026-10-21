
import tkinter as tk
from tkinter import ttk, messagebox

from modbus import *
from actions import *
from address import *
from crane import Crane

from hmi_functions import (
    add_move,
    add_vacuum,
    add_process,
    remove_selected_action,
    update_selected_position,
    move_to_selected_position,
    move_crane,
    refresh_action_list,
    update_position,
)


# -------------------------
# Initialization
# -------------------------

current_x = read_input(AT_X)
current_y = read_input(AT_Y)

crane = Crane(client, current_x, current_y)

config = load_config(
    "C:/Users/rom38/OneDrive - Högskolan Väst/"
    "Y1/SP1/PFA600/Project/Grade A/locations.json"
)

actions = config["actions"]


# -------------------------
# Main window
# -------------------------

root = tk.Tk()
root.title("Crane HMI")
root.geometry("850x650")


# -------------------------
# Current position
# -------------------------

position_frame = ttk.LabelFrame(root, text="Current Position")
position_frame.pack(fill="x", padx=15, pady=5)

position_label = ttk.Label(
    position_frame,
    text=f"X: {current_x}    Y: {current_y}",
    font=("Arial", 14)
)
position_label.pack(pady=8)


# -------------------------
# Move crane
# -------------------------

move_frame = ttk.LabelFrame(root, text="Move Crane")
move_frame.pack(fill="x", padx=15, pady=5)

ttk.Label(move_frame, text="X:").pack(side="left", padx=(8, 0))

x_entry = ttk.Entry(move_frame, width=8)
x_entry.pack(side="left", padx=5)

ttk.Label(move_frame, text="Y:").pack(side="left")

y_entry = ttk.Entry(move_frame, width=8)
y_entry.pack(side="left", padx=5)

ttk.Button(
    move_frame,
    text="Move",
    command=lambda: move_crane(x_entry, y_entry, crane)
).pack(side="left", padx=5)

ttk.Button(
    move_frame,
    text="Add Move",
    command=lambda: add_move(
        x_entry, y_entry, actions, action_list
    )
).pack(side="left", padx=5)


# -------------------------
# Vacuum
# -------------------------

vacuum_frame = ttk.LabelFrame(root, text="Vacuum")
vacuum_frame.pack(fill="x", padx=15, pady=5)

ttk.Button(
    vacuum_frame,
    text="Add Vacuum ON",
    command=lambda: add_vacuum(1, actions, action_list)
).pack(side="left", padx=8, pady=8)

ttk.Button(
    vacuum_frame,
    text="Add Vacuum OFF",
    command=lambda: add_vacuum(0, actions, action_list)
).pack(side="left", padx=8)

ttk.Button(
    vacuum_frame,
    text="Vacuum ON Now",
    command=lambda: write_output(VACUUM, 1)
).pack(side="left", padx=8)

ttk.Button(
    vacuum_frame,
    text="Vacuum OFF Now",
    command=lambda: write_output(VACUUM, 0)
).pack(side="left", padx=8)


# -------------------------
# Process
# -------------------------

process_frame = ttk.LabelFrame(root, text="Process")
process_frame.pack(fill="x", padx=15, pady=5)

ttk.Button(
    process_frame,
    text="Add Process 1",
    command=lambda: add_process(1, actions, action_list)
).pack(side="left", padx=8, pady=8)

ttk.Button(
    process_frame,
    text="Add Process 2",
    command=lambda: add_process(2, actions, action_list)
).pack(side="left", padx=8)

ttk.Button(
    process_frame,
    text="Run Process 1 Now",
    command=lambda: write_output(START_P1, 1)
).pack(side="left", padx=8)

ttk.Button(
    process_frame,
    text="Run Process 2 Now",
    command=lambda: write_output(START_P2, 1)
).pack(side="left", padx=8)


# -------------------------
# Sequence
# -------------------------

list_frame = ttk.LabelFrame(root, text="Sequence")
list_frame.pack(fill="both", expand=True, padx=15, pady=5)

action_list = tk.Listbox(list_frame, height=8)
action_list.pack(
    fill="both",
    expand=True,
    padx=8,
    pady=8
)

sequence_buttons = ttk.Frame(list_frame)
sequence_buttons.pack(fill="x", padx=5, pady=5)

ttk.Button(
    sequence_buttons,
    text="Remove Selected",
    command=lambda: remove_selected_action(action_list, actions)
).pack(side="left", padx=5)

ttk.Button(
    sequence_buttons,
    text="Update to Current Position",
    command=lambda: update_selected_position(action_list, actions)
).pack(side="left", padx=5)

ttk.Button(
    sequence_buttons,
    text="Move to Selected",
    command=lambda: move_to_selected_position(
        action_list, actions, crane
    )
).pack(side="left", padx=5)


# -------------------------
# Save configuration
# -------------------------

save_frame = ttk.Frame(root)
save_frame.pack(fill="x", padx=15, pady=8)


def save_json():
    try:
        save_config(config)
        messagebox.showinfo("Saved", "Sequence saved to locations.json.")
    except Exception as error:
        messagebox.showerror("Save error", str(error))


ttk.Button(
    save_frame,
    text="Save to JSON",
    command=save_json
).pack(side="left", padx=5)

def run_hmi():
    refresh_action_list(action_list, actions)
    update_position(root, position_label)
    root.mainloop()


if __name__ == "__main__":
    run_hmi()