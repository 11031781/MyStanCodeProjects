"""
File: PotholeFilling.py
Name: Mark:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at the (2, 1), facing east
    post-condition: Karel is at the (2, 7), facing east
    :return:
    """
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()

def go_in():
    """
    pre-condition: Karel is at the upper left of the pothole, facing east
    post-condition: Karel is in the pothole, facing south
    :return:
    """
    move()
    turn_right()
    move()

def go_out():
    """
    pre-condition: Karel is in the pothole, facing south
    post-condition: Karel is at the upper left of the pothole, facing east
    :return:
    """
    turn_around()
    move()
    turn_right()
    move()


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


def put_99_beepers():
    """
    Karel will put 99 beepers in the pothole
    :return:
    """
    for i in range(99):
        put_beeper()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
