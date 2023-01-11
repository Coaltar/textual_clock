import math
import numpy as np
from time import struct_time

# Tasks:
# Turn this into a class
# Should Preserve certain 'masks'
# short radial lines in place of numbers
# clock ring


class ASCII_Clock:

    #base_mask_values???
    #base_mask_draw???


    def __init__(self, size):
        self.size = size
        self.blank_matrix = self.generate_blank_matrix(size)
        self.clock_frame = self.get_clock_frame(size)

    def resize(self, size):
        self.size = size
        self.blank_matrix = self.generate_blank_matrix(size)
        self.clock_frame = self.get_clock_frame(size)

    #class constructor should take in:
    #   timezone
    #   clock size
    #overload constructor to take in either just clock size or clock size + timezone
    #default clock time to localtime


    def generate_blank_matrix(self, clock_size):
        """
        Takes in a clock size and creates a square matrix of SxS where S = 2 * size + 1.
        """
        grid_size = clock_size * 2 + 1
        matrix = np.zeros((grid_size, grid_size))
        return matrix


    def get_clock_frame(self, clock_size):
        """
        Return a matrix with the clock outer rim
        """
        # clock_frame_matrix = self.get_blank_frame(clock_size)
        clock_frame_matrix = self.blank_matrix

        center_offset = (clock_size, clock_size)
        circumference = math.pi * 2 * clock_size
        num_points = int(circumference * 2)

        # increment_amount = circumference / num_points

        for inc in range(num_points):
            theta = (inc / num_points) * 2 * math.pi 
            x = int(clock_size * math.cos(theta))
            y = int(clock_size * math.sin(theta))
            # base_matrix[x][y] = 1
            this_point = (center_offset[0] + x, center_offset[1] + y)
            clock_frame_matrix[this_point[0]][this_point[1]] = 1
        return clock_frame_matrix


    def get_clock_arm_matrix(self, arm_ratio, clock_size, angle):
        """
        Takes in a clock size, produces a matrix containing values for clock arm
        """

        base_matrix = np.copy(self.blank_matrix)
        arm_radius =  clock_size*arm_ratio
        max_points =  clock_size
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


    def get_clock_matrix(self, hour, min, sec):
        """
        Produces a matrix representation of an analog clock image. 
        """
        # default_clock_size = 21 
        size = self.size

        hour_hand_angle = -math.pi*2*((hour % 12)/ 12) + ((math.pi / 2))
        minute_hand_angle = -math.pi*2*(min / 60) + ((math.pi / 2))
        sec_hand_angle = -math.pi*2*(sec / 60) + ((math.pi / 2))
        
        hour_mat = self.get_clock_arm_matrix(.4, size, hour_hand_angle)
        min_mat = self.get_clock_arm_matrix(.75, size, minute_hand_angle)
        sec_mat = self.get_clock_arm_matrix(1, size, sec_hand_angle)
       
        rim_mat = self.get_clock_frame(size)
        clock_mat = hour_mat + min_mat + sec_mat + self.clock_frame

        return clock_mat


    def cell_to_char(self, matrix, m, n) -> str:
        """
        Takes in a matrix and a coordinate.
        Return a character based on the value of the matrix at that coordinate.
        """
        value = matrix[m][n]
        if(value == 0):
            return " "
        else:
            return "0"


    def matrix_to_ascii(self, matrix):
        """Takes in a matrix and generates a block of ASCII text"""


        m_len = len(matrix)
        n_len = len(matrix[0])
        output = ""
        for m in range(m_len):
            for n in range(n_len):
                output += self.cell_to_char(matrix, m, n)

            output += '\n'

        return output

    def get_clock_ascii(self, time: struct_time):
        now = time
        hour = now.tm_hour
        min = now.tm_min
        sec = now.tm_sec
        clock_matrix = self.get_clock_matrix(hour, min, sec)
        clock_ascii = self.matrix_to_ascii(clock_matrix)
        return clock_ascii
