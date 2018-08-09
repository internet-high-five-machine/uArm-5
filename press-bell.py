#!/usr/bin/env python

import sys
import time
import pyuarm
import fileinput

speed = 95

def main():
    arm = pyuarm.get_uarm()
    try:
        arm.connect()
    except:
        print("Error connecting to the arm", file=sys.stderr)
        exit(1)


    try:
        for line in fileinput.input():
            if line.strip() == "(bell)":
                success = press_bell(arm)

                if not success:
                    print("Error excuting one of the operations.", file=sys.stderr)
                    exit(2)
    finally:
        arm.disconnect()


def press_bell(arm):
    a0 = home_arm(arm)

    time.sleep(0.2)

    # Up 
    a1 = arm.set_position(150, 0, 215, speed=speed, wait=True)

    time.sleep(0.2)

    # Forward
    a2 = arm.set_position(220, 0, 215, speed=speed, wait=True)

    time.sleep(0.2)
    
    # Down
    a3 = arm.set_position(220, 0, 100, speed=speed, wait=True)

    time.sleep(0.2)

    a4 = home_arm(arm)
    
    return all([a0, a1, a2, a3, a4])


def home_arm(arm):
    return arm.set_position(150, 0, 150, speed=speed, wait=True)


if __name__ == "__main__":
    main()
