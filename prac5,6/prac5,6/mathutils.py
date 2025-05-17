# mathutils.py

import math

def calculate_area(shape, *dimensions):
    if shape == "circle":
        return math.pi * (dimensions[0] ** 2)
    elif shape == "rectangle":
        return dimensions[0] * dimensions[1]
    elif shape == "triangle":
        return 0.5 * dimensions[0] * dimensions[1]
    else:
        return "Invalid shape"

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
