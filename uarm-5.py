#!/usr/bin/env python

import sys
import time
import pyuarm

speed = 95

def main():
    arm = pyuarm.get_uarm()
    try:
        arm.connect()
    except:
        print("Error connecting to the arm", file=sys.stderr)
        exit(1)

    success = high5(arm)

    if not success:
        print("Error excuting one of the operations.", file=sys.stderr)
        exit(2)

    arm.disconnect()


def high5(arm):
    a0 = home_arm(arm)
    # Up 
    a1 = arm.set_position(150, 0, 215, speed=speed, wait=True)
    # Backswing ...
    a2 = arm.set_position(150, 70, 215, speed=speed, wait=True)
    # In
    a2 = arm.set_position(150, -70, 215, speed=speed, wait=True)

    time.sleep(0.3)

    a3 = home_arm(arm)
    
    return all([a0, a1, a2, a3])


def home_arm(arm):
    return arm.set_position(150, 0, 150, speed=speed, wait=True)


if __name__ == "__main__":
    main()
