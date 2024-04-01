"""
File: Steeplechase.py
Name: Mark:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    pre-condition: Karel is on the left side of the wall, facing east
    post-condition: Karel is at the right side of the wall
    :return:
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition: Karel is on the left side of the wall, facing east
    post-condition: Karel is facing north
    :return:
    """
    turn_left()
    #facing north
    while not right_is_clear():
        move()


def cross():
    """
    pre-condition: Karel is facing north
    post-condition: Karel is at the upper right, facing south
    :return:
    """
    turn_right()
    #facing east
    move()
    turn_right()
    #facing south


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def down():
    """
    pre-condition: Karel is at the upper right, facing south
    post-condition: Karel is at the lower right, facing south
    :return:
    """
    while front_is_clear():
        move()
    






# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
