from modbus import *
from actions import *
from address import *
from crane import Crane
from process import *


def main():
    # Read initial crane position
    current_x = read_input(AT_X)
    current_y = read_input(AT_Y)

    # Create crane
    crane = Crane(client, current_x, current_y)

    # Initialize product ID
    product_id = 1

    # Run Process 1 continuously
    while True:
        run_process_1(crane, product_id)
        print("All actions completed.")
        product_id += 1


if __name__ == "__main__":
    main()