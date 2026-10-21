from modbus import *
from actions import *
from address import *
from logger import *

def run_process_1(crane,product_id):

    # 1. Wait for a part at source 1
    wait_for_signal(SOURCE1,1)

    # 2. Pick part from source 1
    crane.move_crane(SOURCE1_X, 0, product_id)
    crane.pick(product_id)

    # 3. Place part in process 1
    crane.move_crane(PROCESS1_X, 1, product_id)
    crane.place()

    # 4. Start process 1
    wait_for_signal(P1_SENSOR,1)
    write_output(START_P1, 1)

    # 5. Wait until simulation says process is finished
    wait_for_signal(P1_RUNNING,0)

    # 6. Pick part from process 1
    crane.pick(product_id)

    # 7. Move to sink
    crane.move_crane(SINK_X, 1, product_id)
    crane.place()