from modbus import *
from actions import *
from address import *

def s1_to_p1(crane):
    crane.move_crane(SOURCE1_X)
    crane.pick()
    crane.move_crane(PROCESS1_X)
    crane.place()
    wait_for_signal(P1_SENSOR,1)
    write_output(START_P1, 1)

def s2_to_p2(crane):
    crane.move_crane(SOURCE2_X)
    crane.pick()
    crane.move_crane(PROCESS2_X)
    crane.place()
    wait_for_signal(P2_SENSOR,1)
    write_output(START_P2, 1)

def p1_to_sink(crane):
    crane.move_crane(PROCESS1_X)
    crane.pick()
    crane.move_crane(SINK_X)
    crane.place()

def p2_to_p1(crane):
    crane.move_crane(PROCESS2_X)
    crane.pick()
    crane.move_crane(PROCESS1_X)
    crane.place()
    wait_for_signal(P1_SENSOR,1)
    write_output(START_P1, 1)


def run_processes(crane):
    p1_state = read_input(P1_SENSOR)
    p1_run = read_input(P1_RUNNING)
    p2_state = read_input(P2_SENSOR)
    p2_run = read_input(P2_RUNNING)
    source1_state = read_input(SOURCE1)
    source2_state = read_input(SOURCE2)

    if (source1_state):
        if (not p1_state and not p1_run):
            s1_to_p1(crane)
            return True
    if (source2_state):
        if (not p2_state and not p2_run):
            s2_to_p2(crane)
            return True
    if (p1_state and not p1_run):
        p1_to_sink(crane)
        return False
    if (p2_state and not p2_run and not p1_state and not p1_run):
        p2_to_p1(crane)
        return False
    return False