from modbus import *
from actions import load_actions, execute_action
from address import *
from crane import Crane

def main():
    # Read initial crane position
    current_x = read_input(AT_X)
    current_y = read_input(AT_Y)

    # Load actions
    actions = load_actions(
        "C:/Users/rom38/OneDrive - Högskolan Väst/Y1/SP1/PFA600/Project/Grade E/test1.json"
    )

    # Create crane
    crane = Crane(client, current_x, current_y)

    # Execute actions
    for action in actions:
        execute_action(crane, action)

if __name__ == "__main__":
    main()