import math
import numpy as np


def check_cell(matrix, m, n) -> str:
    """
    Takes in a 2x2 matrix, if cell is zero, return blank char
    If cell is anything else, returns a character
    """
    value = matrix[m][n]
    if(value == 0):
        return " "
    else:
        return "0"


def display_matrix(matrix):
    """Takes in a matrix and creates a string that can be printed into the terminal"""
    m_len = len(matrix)
    n_len = len(matrix[0])

    output = ""
    
    for m in range(m_len):
        for n in range(n_len):
            output += check_cell(matrix, m, n)

        output += '\n'

    return output


def blank_clock_matrix(clock_size):
    """
    Clock should be drawn on a grid.
    Grid size should be X by X sized matrice.
    X must be odd, for convenience.
    X = clock_size*2 + 1
    """
    grid_size = clock_size * 2 + 1
    matrix = np.zeros((grid_size, grid_size))
    return matrix


def apply_clock_ring(clock_size):
    """
    Return a matrix with the clock outer rim
    """
    base_matrix = blank_clock_matrix(clock_size)
    center_offset = (clock_size, clock_size)
    #distance around rim of matrix is... clock_size * 2pi
    circumference = math.pi * 2 * clock_size
    num_points = int(circumference * 2)
    increment_amount = circumference / num_points
    for inc in range(num_points):
        theta = (inc / num_points) * 2 * math.pi 
        x = int(clock_size * math.cos(theta))
        y = int(clock_size * math.sin(theta))
        # base_matrix[x][y] = 1
        this_point = (center_offset[0] + x, center_offset[1] + y)
        base_matrix[this_point[0]][this_point[1]] = 1
    return base_matrix


def apply_clock_arm(arm_ratio, clock_size, angle):
    """
    Takes in a clock size, produces a matrix containing values for clock arm
    """

    base_matrix = blank_clock_matrix(clock_size) 
    arm_radius =  clock_size*arm_ratio
    max_points = 2 * clock_size
    radius_increment = clock_size / max_points 
    center_offset = (clock_size, clock_size)
    
    for i in range(max_points):
        r = radius_increment * i
        x = int(r * math.cos(angle + math.pi / 2))
        y = int(r * math.sin(angle + math.pi / 2))
        this_point = (center_offset[0] + x, center_offset[1] + y)
        base_matrix[this_point[0]][this_point[1]] = 1
        if r > arm_radius:
            break

    return base_matrix


def get_clock(hour, min, sec):
    default_clock_size = 21 
    hour_hand_angle = -math.pi*2*((hour % 12)/ 12) + ((math.pi / 2))
    minute_hand_angle = -math.pi*2*(min / 60) + ((math.pi / 2))
    sec_hand_angle = -math.pi*2*(sec / 60) + ((math.pi / 2))
    
    hour_mat = apply_clock_arm(.4, default_clock_size, hour_hand_angle)
    min_mat = apply_clock_arm(.75, default_clock_size, minute_hand_angle)
    sec_mat = apply_clock_arm(1, default_clock_size, sec_hand_angle)
   
    rim_mat = apply_clock_ring(default_clock_size)

    clock_mat = hour_mat + min_mat + sec_mat + rim_mat
    return clock_mat
