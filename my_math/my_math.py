#!/usr/bin/env python3
import math

def my_factorial(num):
    if type(num) is int:
        if num < 0:
            raise ValueError
        elif num == 0:
            return 1
        else:
            return num * my_factorial(num - 1)
    else:
        raise TypeError

