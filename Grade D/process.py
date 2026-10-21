from modbus import *
from actions import *
from address import *

def run_process_1(crane):

    # 1. Wait for a part at source 1
    wait_for_signal(SOURCE1,1)

    # 2. Pick part from source 1
    crane.move_crane(SOURCE1_X)
    crane.pick()

    # 3. Place part in process 1
    crane.move_crane(PROCESS1_X)
    crane.place()

    # 4. Start process 1
    wait_for_signal(P1_SENSOR,1)
    write_output(START_P1, 1)

    # 5. Wait until simulation says process is finished
    wait_for_signal(P1_RUNNING,0)

    # 6. Pick part from process 1
    crane.pick()

    # 7. Move to sink
    crane.move_crane(SINK_X)
    crane.place()