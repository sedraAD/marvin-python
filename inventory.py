#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

def pick(bag, item, position=None):
    """
    Adds an item to the bag in a specific position or at the end if position is not given. 
    """
    if position is not None:
        position_int = int(position)
        if position_int < 0 or position_int > len(bag):
            message = f"Error, the given index '{position}' is not available, '{item}' not added."
        bag.insert(position_int, item)
        message = f"'{item}' has been added on index '{position_int}'."
    else:
        bag.append(item)
        message = f"'{item}' has been added."
    print(message)
    return bag


def inventory(bag):
    """
    Prints items in bag.
    """
    message = f"Bagpack has {len(bag)} items: {bag}"
    print(message)


def drop(bag, item):
    """
    Removes given item from bag.
    """
    try:
        bag.remove(item)
        message = f"{item} has been removed."
    except ValueError:
        message = f"Error, I have no {item} in my bagpack."
    print(message)
    return bag


def swap(bag, item1, item2):
    """
    Swaps the position of two items in the bag.
    """
    try:
        index1 = bag.index(item1)
        index2 = bag.index(item2)
        temp = bag[index1]
        bag[index1] = bag[index2]
        bag[index2] = temp
        message = f"'{item1}' and '{item2}' has been swaped."
    except ValueError:
        message = f"Error, I have no {item1} or {item2} in the bagpack"
    print(message)
    return bag
