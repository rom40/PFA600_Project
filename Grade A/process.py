from modbus import *
from actions import *
from address import *
from logger import *

# def run_process_1(crane,product_id):

#     # 1. Wait for a part at source 1
#     wait_for_signal(SOURCE1,1)

#     # 2. Pick part from source 1
#     crane.move_crane(SOURCE1_X, 0, product_id)
#     crane.pick(product_id)

#     # 3. Place part in process 1
#     crane.move_crane(PROCESS1_X, 1, product_id)
#     crane.place()

#     # 4. Start process 1
#     wait_for_signal(P1_SENSOR,1)
#     write_output(START_P1, 1)

#     # 5. Wait until simulation says process is finished
#     wait_for_signal(P1_RUNNING,0)

#     # 6. Pick part from process 1
#     crane.pick(product_id)

#     # 7. Move to sink
#     crane.move_crane(SINK_X, 1, product_id)
#     crane.place()

# def run_process_2(crane,product_id):

#     # 1. Wait for a part at source 1
#     wait_for_signal(SOURCE2,1)

#     # 2. Pick part from source 1
#     crane.move_crane(SOURCE2_X, 0, product_id)
#     crane.pick(product_id)

#     # 3. Place part in process 1
#     crane.move_crane(PROCESS2_X, 1, product_id)
#     crane.place()

#     # 4. Start process 1
#     wait_for_signal(P2_SENSOR,1)
#     write_output(START_P2, 1)

#     # 5. Wait until simulation says process is finished
#     wait_for_signal(P2_RUNNING,0)

#     # 6. Pick part from process 1
#     crane.pick(product_id)

#     crane.move_crane(PROCESS1_X, 1, product_id)
#     crane.place()
    
#     # 4. Start process 1
#     wait_for_signal(P1_SENSOR,1)
#     write_output(START_P1, 1)
#     # 5. Wait until simulation says process is finished
#     wait_for_signal(P1_RUNNING,0)

#     crane.pick(product_id)

#     # 7. Move to sink
#     crane.move_crane(SINK_X, 1, product_id)
#     crane.place()

def s1_to_p1(crane, product_id):
    crane.move_crane(SOURCE1_X, 0, product_id)
    crane.pick(product_id)
    crane.move_crane(PROCESS1_X, 1, product_id)
    crane.place()
    wait_for_signal(P1_SENSOR,1)
    write_output(START_P1, 1)

def s2_to_p2(crane, product_id):
    crane.move_crane(SOURCE2_X, 0, product_id)
    crane.pick(product_id)
    crane.move_crane(PROCESS2_X, 1, product_id)
    crane.place()
    wait_for_signal(P2_SENSOR,1)
    write_output(START_P2, 1)

def p1_to_sink(crane, product_id):
    crane.move_crane(PROCESS1_X, 0, product_id)
    crane.pick(product_id)
    crane.move_crane(SINK_X, 1, product_id)
    crane.place()

def p2_to_p1(crane, product_id):
    crane.move_crane(PROCESS2_X, 0, product_id)
    crane.pick(product_id)
    crane.move_crane(PROCESS1_X, 1, product_id)
    crane.place()
    wait_for_signal(P1_SENSOR,1)
    write_output(START_P1, 1)


def run_processes(crane, product_id):
    p1_state = read_input(P1_SENSOR)
    p1_run = read_input(P1_RUNNING)
    p2_state = read_input(P2_SENSOR)
    p2_run = read_input(P2_RUNNING)
    source1_state = read_input(SOURCE1)
    source2_state = read_input(SOURCE2)

    if (source1_state):
        if (not p1_state and not p1_run):
            s1_to_p1(crane, product_id)
            return True
    if (source2_state):
        if (not p2_state and not p2_run):
            s2_to_p2(crane, product_id)
            return True
    if (p1_state and not p1_run):
        p1_to_sink(crane, product_id)
        return False
    if (p2_state and not p2_run and not p1_state and not p1_run):
        p2_to_p1(crane, product_id)
        return False
    return False