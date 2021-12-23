from tkinter import *
import random


class Cube():
    """
    This is a class meant to represent a 3x3 Rubik's Cube.
    """
    def __init__(self):
        # The following array is meant to symbolize a cube
        # Top face is 0, front face is 1, right face is 2.
        # Remainder faces are in a dice format, where opposite sides sum to 5
        # Position on face: for example, self.faces[face][x]

        # 0 | 1 | 2 |
        # 3 | 4 | 5 |
        # 6 | 7 | 8 |

        # So, for example, self.faces[top_face][4] would be
        # the middle square in the top face

        self.top_face = 0
        self.front_face = 1
        self.right_face = 2
        self.left_face = 3
        self.back_face = 4
        self.bottom_face = 5
        self.faces = [[10,11,12,13,14,15,16,17,18],
                      [20,21,22,23,24,25,26,27,28],
                      ['00','01','02','03','04','05','06','07','08'],
                      [50,51,52,53,54,55,56,57,58],
                      [30,31,32,33,34,35,36,37,38],
                      [40,41,42,43,44,45,46,47,48]]
        self.solved_state = [[10,11,12,13,14,15,16,17,18],
                      [20,21,22,23,24,25,26,27,28],
                      ['00','01','02','03','04','05','06','07','08'],
                      [50,51,52,53,54,55,56,57,58],
                      [30,31,32,33,34,35,36,37,38],
                      [40,41,42,43,44,45,46,47,48]]

    def print_back_face(self):
        """Prints  the back face, inverted as seen from the top, with no spacing zeroes"""
        for x in range(3):
            for y in range(3):
                print(self.faces[self.back_face][8-y-3*x], '', end = '')
                if y == 2:
                    print(' ')

    def print_top_face(self):
        """Prints the top face with no spacing zeroes"""
        for x in range(3):
            for y in range(3):
                print('0'+str(self.faces[self.top_face][y+3*x]), '', end = '')
                if y == 2:
                    print(' ')

    def print_front_face(self):
        """Prints the top face with no spacing zeroes"""
        for x in range(3):
            for y in range(3):
                print(self.faces[self.front_face][y+3*x], '', end = '')
                if y == 2:
                    print(' ')

    def print_back_face_spaced(self):
        """Prints the back face, inverted as seen from top, with spacing zeroes"""
        print('00 00 00   ', self.faces[self.back_face][8], self.faces[self.back_face][7],
              self.faces[self.back_face][6], '   00 00 00    00 00 00')
        print('00 00 00   ', self.faces[self.back_face][5], self.faces[self.back_face][4],
              self.faces[self.back_face][3], '   00 00 00    00 00 00')
        print('00 00 00   ', self.faces[self.back_face][2], self.faces[self.back_face][1],
              self.faces[self.back_face][0], '   00 00 00    00 00 00')

    def print_left_top_right_bottom_faces(self):
        """Prints the left, top, right, and bottom faces"""
        print(self.faces[self.left_face][6],
              self.faces[self.left_face][3],
              self.faces[self.left_face][0], '  ',
              self.faces[self.top_face][0],
              self.faces[self.top_face][1],
              self.faces[self.top_face][2], '  ',
              self.faces[self.right_face][2],
              self.faces[self.right_face][5],
              self.faces[self.right_face][8], '  ',
              self.faces[self.bottom_face][8],
              self.faces[self.bottom_face][7],
              self.faces[self.bottom_face][6])
        print(self.faces[self.left_face][7],
              self.faces[self.left_face][4],
              self.faces[self.left_face][1], '  ',
              self.faces[self.top_face][3],
              self.faces[self.top_face][4],
              self.faces[self.top_face][5], '  ',
              self.faces[self.right_face][1],
              self.faces[self.right_face][4],
              self.faces[self.right_face][7], '  ',
              self.faces[self.bottom_face][5],
              self.faces[self.bottom_face][4],
              self.faces[self.bottom_face][3])
        print(self.faces[self.left_face][8],
              self.faces[self.left_face][5],
              self.faces[self.left_face][2], '  ',
              self.faces[self.top_face][6],
              self.faces[self.top_face][7],
              self.faces[self.top_face][8], '  ',
              self.faces[self.right_face][0],
              self.faces[self.right_face][3],
              self.faces[self.right_face][6], '  ',
              self.faces[self.bottom_face][2],
              self.faces[self.bottom_face][1],
              self.faces[self.bottom_face][0])

    def print_front_face_spaced(self):
        """Prints the back face, inverted as seen from top, with spacing zeroes"""
        print('00 00 00   ', self.faces[self.front_face][0], self.faces[self.front_face][1],
              self.faces[self.front_face][2], '   00 00 00    00 00 00')
        print('00 00 00   ', self.faces[self.front_face][3], self.faces[self.front_face][4],
              self.faces[self.front_face][5], '   00 00 00    00 00 00')
        print('00 00 00   ', self.faces[self.front_face][6], self.faces[self.front_face][7],
              self.faces[self.front_face][8], '   00 00 00    00 00 00')

    def print_cube(self):
        """Prints the cube"""
        if self.is_solved() == True:
            print("THIS CUBE IS SOLVED")
            print(' ')
        else:
            self.print_back_face_spaced()
            print(' ')
            self.print_left_top_right_bottom_faces()
            print(' ')
            self.print_front_face_spaced()
            print(' ')

    def on_face_rotation(self, face):
        """Simulates a clockwise rotation of the colors on a face"""
        # Corners on the given face
        hold_variable = self.faces[face][0]
        self.faces[face][0] = self.faces[face][6]
        self.faces[face][6] = self.faces[face][8]
        self.faces[face][8] = self.faces[face][2]
        self.faces[face][2] = hold_variable
        # Edges on the given face
        hold_variable = self.faces[face][1]
        self.faces[face][1] = self.faces[face][3]
        self.faces[face][3] = self.faces[face][7]
        self.faces[face][7] = self.faces[face][5]
        self.faces[face][5] = hold_variable

    def on_face_rotation_ccw(self, face):
        """Simulates a counterclockwise rotation of the colors on a face"""
        # Corners on the given face
        hold_variable = self.faces[face][0]
        self.faces[face][0] = self.faces[face][2]
        self.faces[face][2] = self.faces[face][8]
        self.faces[face][8] = self.faces[face][6]
        self.faces[face][6] = hold_variable
        # Edges on the given face
        hold_variable = self.faces[face][1]
        self.faces[face][1] = self.faces[face][5]
        self.faces[face][5] = self.faces[face][7]
        self.faces[face][7] = self.faces[face][3]
        self.faces[face][3] = hold_variable

    def top_turn(self):
        """Simulates a clockwise rotation of the top face"""
        # 0 slot of front, left, back, and right faces
        # 20 moves to 10 moves to 30 moves to 40
        hold_variable = self.faces[self.front_face][0]
        self.faces[self.front_face][0] = self.faces[self.right_face][0]
        self.faces[self.right_face][0] = self.faces[self.back_face][0]
        self.faces[self.back_face][0] = self.faces[self.left_face][0]
        self.faces[self.left_face][0] = hold_variable
        # 1 slot of front, left, back, and right faces
        # 21 moves to 11 moves to 31 moves to 41
        hold_variable = self.faces[self.front_face][1]
        self.faces[self.front_face][1] = self.faces[self.right_face][1]
        self.faces[self.right_face][1] = self.faces[self.back_face][1]
        self.faces[self.back_face][1] = self.faces[self.left_face][1]
        self.faces[self.left_face][1] = hold_variable
        # 2 slot of front, left, back, and right faces
        # 22 moves to 12 moves to 32 moves to 42
        hold_variable = self.faces[self.front_face][2]
        self.faces[self.front_face][2] = self.faces[self.right_face][2]
        self.faces[self.right_face][2] = self.faces[self.back_face][2]
        self.faces[self.back_face][2] = self.faces[self.left_face][2]
        self.faces[self.left_face][2] = hold_variable
        # Rotates the top face, then prints out cube
        self.on_face_rotation(self.top_face)

    def top_turn_ccw(self):
        """Simulates a counterclockwise rotation of the top face"""
        # 0 slot of front, left, back, and right faces
        # 20 moves to 10 moves to 30 moves to 40
        hold_variable = self.faces[self.front_face][0]
        self.faces[self.front_face][0] = self.faces[self.left_face][0]
        self.faces[self.left_face][0] = self.faces[self.back_face][0]
        self.faces[self.back_face][0] = self.faces[self.right_face][0]
        self.faces[self.right_face][0] = hold_variable
        # 1 slot of front, left, back, and right faces
        # 21 moves to 11 moves to 31 moves to 41
        hold_variable = self.faces[self.front_face][1]
        self.faces[self.front_face][1] = self.faces[self.left_face][1]
        self.faces[self.left_face][1] = self.faces[self.back_face][1]
        self.faces[self.back_face][1] = self.faces[self.right_face][1]
        self.faces[self.right_face][1] = hold_variable
        # 2 slot of front, left, back, and right faces
        # 22 moves to 12 moves to 32 moves to 42
        hold_variable = self.faces[self.front_face][2]
        self.faces[self.front_face][2] = self.faces[self.left_face][2]
        self.faces[self.left_face][2] = self.faces[self.back_face][2]
        self.faces[self.back_face][2] = self.faces[self.right_face][2]
        self.faces[self.right_face][2] = hold_variable
        # Rotates the top face, then prints out cube
        self.on_face_rotation_ccw(self.top_face)

    def front_turn(self):
        """Simulates a clockwise rotation of the front face"""
        # Top face, slot 6 (lower left-hand corner)
        # 06 moves to 20 moves to 52 moves to 38
        hold_variable = self.faces[self.top_face][6]
        self.faces[self.top_face][6] = self.faces[self.left_face][8]
        self.faces[self.left_face][8] = self.faces[self.bottom_face][2]
        self.faces[self.bottom_face][2] = self.faces[self.right_face][0]
        self.faces[self.right_face][0] = hold_variable
        # Top face, slot 7 (bottom edge)
        # 07 moves to 23 moves to 51 moves to 35
        hold_variable = self.faces[self.top_face][7]
        self.faces[self.top_face][7] = self.faces[self.left_face][5]
        self.faces[self.left_face][5] = self.faces[self.bottom_face][1]
        self.faces[self.bottom_face][1] = self.faces[self.right_face][3]
        self.faces[self.right_face][3] = hold_variable
        # Top face, slot 8 (bottom right hand corner)
        # 08 moves to 26 moves to 50 moves to 32
        hold_variable = self.faces[self.top_face][8]
        self.faces[self.top_face][8] = self.faces[self.left_face][2]
        self.faces[self.left_face][2] = self.faces[self.bottom_face][0]
        self.faces[self.bottom_face][0] = self.faces[self.right_face][6]
        self.faces[self.right_face][6] = hold_variable
        self.on_face_rotation(self.front_face)

    def front_turn_ccw(self):
        """Simulates a counterclockwise rotation of the front face"""
        # Top face, slot 6 (lower left-hand corner)
        # 06 moves to 38 moves to 52 moves to 20
        hold_variable = self.faces[self.top_face][6]
        self.faces[self.top_face][6] = self.faces[self.right_face][0]
        self.faces[self.right_face][0] = self.faces[self.bottom_face][2]
        self.faces[self.bottom_face][2] = self.faces[self.left_face][8]
        self.faces[self.left_face][8] = hold_variable
        # Top face, slot 7 (bottom edge)
        # 07 moves to 35 moves to 51 moves to 23
        hold_variable = self.faces[self.top_face][7]
        self.faces[self.top_face][7] = self.faces[self.right_face][3]
        self.faces[self.right_face][3] = self.faces[self.bottom_face][1]
        self.faces[self.bottom_face][1] = self.faces[self.left_face][5]
        self.faces[self.left_face][5] = hold_variable
        # Top face, slot 8 (bottom right-hand corner)
        # 08 moves to 32 moves to 50 moves to 26
        hold_variable = self.faces[self.top_face][8]
        self.faces[self.top_face][8] = self.faces[self.right_face][6]
        self.faces[self.right_face][6] = self.faces[self.bottom_face][0]
        self.faces[self.bottom_face][0] = self.faces[self.left_face][2]
        self.faces[self.left_face][2] = hold_variable
        self.on_face_rotation_ccw(self.front_face)

    def right_turn(self):
        """Simulates a clockwise rotation of the right face"""
        # Top face, slot 8 (lower right-hand corner)
        # 08 moves to 40 moves to 58 moves to 18
        hold_variable = self.faces[self.top_face][8]
        self.faces[self.top_face][8] = self.faces[self.front_face][8]
        self.faces[self.front_face][8] = self.faces[self.bottom_face][8]
        self.faces[self.bottom_face][8] = self.faces[self.back_face][0]
        self.faces[self.back_face][0] = hold_variable
        # Top face, slot 5 (right-hand edge)
        # 05 moves to 43 moves to 55 moves to 15
        hold_variable = self.faces[self.top_face][5]
        self.faces[self.top_face][5] = self.faces[self.front_face][5]
        self.faces[self.front_face][5] = self.faces[self.bottom_face][5]
        self.faces[self.bottom_face][5] = self.faces[self.back_face][3]
        self.faces[self.back_face][3] = hold_variable
        # Top face, slot 2 (upper right-hand corner)
        # 02 moves to 46 moves to 52 moves to 12
        hold_variable = self.faces[self.top_face][2]
        self.faces[self.top_face][2] = self.faces[self.front_face][2]
        self.faces[self.front_face][2] = self.faces[self.bottom_face][2]
        self.faces[self.bottom_face][2] = self.faces[self.back_face][6]
        self.faces[self.back_face][6] = hold_variable
        # Rotates the right face, then prints out cube
        self.on_face_rotation(self.right_face)

    def right_turn_ccw(self):
        """Simulates a counterclockwise rotation of the right face"""
        # Top face, slot 8 (lower right-hand corner)
        # 08 becomes 40 becomes 58 becomes 18
        hold_variable = self.faces[self.top_face][8]
        self.faces[self.top_face][8] = self.faces[self.back_face][0]
        self.faces[self.back_face][0] = self.faces[self.bottom_face][8]
        self.faces[self.bottom_face][8] = self.faces[self.front_face][8]
        self.faces[self.front_face][8] = hold_variable
        # Top face, slot 5 (right-hand edge)
        # 05 becomes 43 becomes 55 becomes 15
        hold_variable = self.faces[self.top_face][5]
        self.faces[self.top_face][5] = self.faces[self.back_face][3]
        self.faces[self.back_face][3] = self.faces[self.bottom_face][5]
        self.faces[self.bottom_face][5] = self.faces[self.front_face][5]
        self.faces[self.front_face][5] = hold_variable
        # Top face, slot 2 (upper right-hand corner)
        # 02 becomes 46 becomes 52 becomes 12
        hold_variable = self.faces[self.top_face][2]
        self.faces[self.top_face][2] = self.faces[self.back_face][6]
        self.faces[self.back_face][6] = self.faces[self.bottom_face][2]
        self.faces[self.bottom_face][2] = self.faces[self.front_face][2]
        self.faces[self.front_face][2] = hold_variable
        # Rotates the right face, then prints out cube
        self.on_face_rotation_ccw(self.right_face)

    def bottom_turn(self):
        """Simulates a clockwise rotation of the bottom face"""
        # Front face, slot 6 (lower left-hand corner)
        # 16 moves to 26 moves to 46 moves to 36
        hold_variable = self.faces[self.front_face][6]
        self.faces[self.front_face][6] = self.faces[self.left_face][6]
        self.faces[self.left_face][6] = self.faces[self.back_face][6]
        self.faces[self.back_face][6] = self.faces[self.right_face][6]
        self.faces[self.right_face][6] = hold_variable
        # Front face, slot 7 (lower edge)
        # 17 moves to 27 moves to 47 moves to 37
        hold_variable = self.faces[self.front_face][7]
        self.faces[self.front_face][7] = self.faces[self.left_face][7]
        self.faces[self.left_face][7] = self.faces[self.back_face][7]
        self.faces[self.back_face][7] = self.faces[self.right_face][7]
        self.faces[self.right_face][7] = hold_variable
        # Front face, slot 8 (lower right-hand corner)
        # 18 moves to 28 moves to 48 moves to 38
        hold_variable = self.faces[self.front_face][8]
        self.faces[self.front_face][8] = self.faces[self.left_face][8]
        self.faces[self.left_face][8] = self.faces[self.back_face][8]
        self.faces[self.back_face][8] = self.faces[self.right_face][8]
        self.faces[self.right_face][8] = hold_variable
        self.on_face_rotation(self.bottom_face)

    def bottom_turn_ccw(self):
        """Simulates a counterclockwise rotation of the bottom face"""
        # Front face, slot 6 (lower left-hand corner)
        # 16 moves to 26 moves to 46 moves to 36
        hold_variable = self.faces[self.front_face][6]
        self.faces[self.front_face][6] = self.faces[self.right_face][6]
        self.faces[self.right_face][6] = self.faces[self.back_face][6]
        self.faces[self.back_face][6] = self.faces[self.left_face][6]
        self.faces[self.left_face][6] = hold_variable
        # Front face, slot 7 (lower edge)
        # 17 moves to 27 moves to 47 moves to 37
        hold_variable = self.faces[self.front_face][7]
        self.faces[self.front_face][7] = self.faces[self.right_face][7]
        self.faces[self.right_face][7] = self.faces[self.back_face][7]
        self.faces[self.back_face][7] = self.faces[self.left_face][7]
        self.faces[self.left_face][7] = hold_variable
        # Front face, slot 8 (lower right-hand corner)
        # 18 moves to 28 moves to 48 moves to 38
        hold_variable = self.faces[self.front_face][8]
        self.faces[self.front_face][8] = self.faces[self.right_face][8]
        self.faces[self.right_face][8] = self.faces[self.back_face][8]
        self.faces[self.back_face][8] = self.faces[self.left_face][8]
        self.faces[self.left_face][8] = hold_variable
        self.on_face_rotation_ccw(self.bottom_face)

    def left_turn(self):
        """Simulates a clockwise rotation of the left face"""
        # Top face, slot 0 (upper right-hand corner)
        # 00 moves to 10 moves to 50 moves to 48
        hold_variable = self.faces[self.top_face][0]
        self.faces[self.top_face][0] = self.faces[self.back_face][8]
        self.faces[self.back_face][8] = self.faces[self.bottom_face][0]
        self.faces[self.bottom_face][0] = self.faces[self.front_face][0]
        self.faces[self.front_face][0] = hold_variable
        # Top face, slot 3 (left edge)
        # 03 moves to 13 moves to 53 moves to 45
        hold_variable = self.faces[self.top_face][3]
        self.faces[self.top_face][3] = self.faces[self.back_face][5]
        self.faces[self.back_face][5] = self.faces[self.bottom_face][3]
        self.faces[self.bottom_face][3] = self.faces[self.front_face][3]
        self.faces[self.front_face][3] = hold_variable
        # Top face, slot 6 (left edge)
        # 06 moves to 16 moves to 56 moves to 42
        hold_variable = self.faces[self.top_face][6]
        self.faces[self.top_face][6] = self.faces[self.back_face][2]
        self.faces[self.back_face][2] = self.faces[self.bottom_face][6]
        self.faces[self.bottom_face][6] = self.faces[self.front_face][6]
        self.faces[self.front_face][6] = hold_variable
        self.on_face_rotation(self.left_face)

    def left_turn_ccw(self):
        """Simulates a counterclockwise rotation of the left face"""
        # Top face, slot 0 (upper right-hand corner)
        # 00 moves to 48 moves to 50 moves to 10
        hold_variable = self.faces[self.top_face][0]
        self.faces[self.top_face][0] = self.faces[self.front_face][0]
        self.faces[self.front_face][0] = self.faces[self.bottom_face][0]
        self.faces[self.bottom_face][0] = self.faces[self.back_face][8]
        self.faces[self.back_face][8] = hold_variable
        # Top face, slot 3 (left edge)
        # 03 moves to 45 moves to 53 moves to 13
        hold_variable = self.faces[self.top_face][3]
        self.faces[self.top_face][3] = self.faces[self.front_face][3]
        self.faces[self.front_face][3] = self.faces[self.bottom_face][3]
        self.faces[self.bottom_face][3] = self.faces[self.back_face][5]
        self.faces[self.back_face][5] = hold_variable
        # Top face, slot 6 (lower left-hand corner)
        # 06 moves to 42 moves to 56 moves to 16
        hold_variable = self.faces[self.top_face][6]
        self.faces[self.top_face][6] = self.faces[self.front_face][6]
        self.faces[self.front_face][6] = self.faces[self.bottom_face][6]
        self.faces[self.bottom_face][6] = self.faces[self.back_face][2]
        self.faces[self.back_face][2] = hold_variable
        self.on_face_rotation_ccw(self.left_face)

    def back_turn(self):
        # Top face, slot 0 (upper left-hand corner)
        # 00 moves to 36 moves to 58 moves to 22
        hold_variable = self.faces[self.top_face][0]
        self.faces[self.top_face][0] = self.faces[self.right_face][2]
        self.faces[self.right_face][2] = self.faces[self.bottom_face][8]
        self.faces[self.bottom_face][8] = self.faces[self.left_face][6]
        self.faces[self.left_face][6] = hold_variable
        # Top face, slot 1 (upper edge)
        # 01 moves to 33 moves to 57 moves to 25
        hold_variable = self.faces[self.top_face][1]
        self.faces[self.top_face][1] = self.faces[self.right_face][5]
        self.faces[self.right_face][5] = self.faces[self.bottom_face][7]
        self.faces[self.bottom_face][7] = self.faces[self.left_face][3]
        self.faces[self.left_face][3] = hold_variable
        # Top face, slot 2 (upper edge)
        # 02 moves to 30 moves to 56 moves to 28
        hold_variable = self.faces[self.top_face][2]
        self.faces[self.top_face][2] = self.faces[self.right_face][8]
        self.faces[self.right_face][8] = self.faces[self.bottom_face][6]
        self.faces[self.bottom_face][6] = self.faces[self.left_face][0]
        self.faces[self.left_face][0] = hold_variable
        self.on_face_rotation(self.back_face)

    def back_turn_ccw(self):
        """Simulates a counterclockwise rotation of the back face"""
        # Top face, slot 0 (upper left-hand corner)
        # 00 moves to 22 moves to 58 moves to 36
        hold_variable = self.faces[self.top_face][0]
        self.faces[self.top_face][0] = self.faces[self.left_face][6]
        self.faces[self.left_face][6] = self.faces[self.bottom_face][8]
        self.faces[self.bottom_face][8] = self.faces[self.right_face][2]
        self.faces[self.right_face][2] = hold_variable
        # Top face, slot 1 (upper edge)
        # 01 moves to 25 moves to 57 moves to 33
        hold_variable = self.faces[self.top_face][1]
        self.faces[self.top_face][1] = self.faces[self.left_face][3]
        self.faces[self.left_face][3] = self.faces[self.bottom_face][7]
        self.faces[self.bottom_face][7] = self.faces[self.right_face][5]
        self.faces[self.right_face][5] = hold_variable
        # Top face, slot 2 (upper right-hand corner)
        # 02 moves to 28 moves to 56 moves to 30
        hold_variable = self.faces[self.top_face][2]
        self.faces[self.top_face][2] = self.faces[self.left_face][0]
        self.faces[self.left_face][0] = self.faces[self.bottom_face][6]
        self.faces[self.bottom_face][6] = self.faces[self.right_face][8]
        self.faces[self.right_face][8] = hold_variable
        self.on_face_rotation_ccw(self.back_face)

    def middle_turn_x(self):
        """Simulates a clockwise rotation of the x-axis slice"""
        # positive x-axis comes out of the right face
        # Top face, slot 1 (upper edge)
        # 01 moves to 48 moves to 51 moves to 11
        hold_variable = self.faces[self.top_face][1]
        self.faces[self.top_face][1] = self.faces[self.front_face][1]
        self.faces[self.front_face][1] = self.faces[self.bottom_face][1]
        self.faces[self.bottom_face][1] = self.faces[self.back_face][7]
        self.faces[self.back_face][7] = hold_variable
        # Top face, slot 4 (middle)
        # 04 moves to 44 moves to 54 moves to 14
        hold_variable = self.faces[self.top_face][4]
        self.faces[self.top_face][4] = self.faces[self.front_face][4]
        self.faces[self.front_face][4] = self.faces[self.bottom_face][4]
        self.faces[self.bottom_face][4] = self.faces[self.back_face][4]
        self.faces[self.back_face][4] = hold_variable
        # Top face, slot 7 (middle)
        # 07 moves to 41 moves to 57 moves to 17
        hold_variable = self.faces[self.top_face][7]
        self.faces[self.top_face][7] = self.faces[self.front_face][7]
        self.faces[self.front_face][7] = self.faces[self.bottom_face][7]
        self.faces[self.bottom_face][7] = self.faces[self.back_face][1]
        self.faces[self.back_face][1] = hold_variable

    def middle_turn_x_ccw(self):
        """Simulates a counterclockwise rotation of the x-axis slice"""
        # positive x-axis comes out of the right face
        # Top face, slot 1 (upper edge)
        # 01 moves to 11 moves to 51 moves to 48
        hold_variable = self.faces[self.top_face][1]
        self.faces[self.top_face][1] = self.faces[self.back_face][7]
        self.faces[self.back_face][7] = self.faces[self.bottom_face][1]
        self.faces[self.bottom_face][1] = self.faces[self.front_face][1]
        self.faces[self.front_face][1] = hold_variable
        # Top face, slot 4 (middle)
        # 04 moves to 14 moves to 54 moves to 44
        hold_variable = self.faces[self.top_face][4]
        self.faces[self.top_face][4] = self.faces[self.back_face][4]
        self.faces[self.back_face][4] = self.faces[self.bottom_face][4]
        self.faces[self.bottom_face][4] = self.faces[self.front_face][4]
        self.faces[self.front_face][4] = hold_variable
        # Top face, slot 7 (middle)
        # 07 moves to 17 moves to 57 moves to 41
        hold_variable = self.faces[self.top_face][7]
        self.faces[self.top_face][7] = self.faces[self.back_face][1]
        self.faces[self.back_face][1] = self.faces[self.bottom_face][7]
        self.faces[self.bottom_face][7] = self.faces[self.front_face][7]
        self.faces[self.front_face][7] = hold_variable

    def middle_turn_z(self):
        """Simulates a clockwise rotation of the z-axis slice"""
        # positive z-axis comes out of the front face
        # Top face, slot 3 (left-hand edge)
        # 03 moves to 21 moves to 55 moves to 37
        hold_variable = self.faces[self.top_face][3]
        self.faces[self.top_face][3] = self.faces[self.left_face][7]
        self.faces[self.left_face][7] = self.faces[self.bottom_face][5]
        self.faces[self.bottom_face][5] = self.faces[self.right_face][1]
        self.faces[self.right_face][1] = hold_variable
        # Top face, slot 4 (middle)
        # 04 moves to 24 moves to 54 moves to 34
        hold_variable = self.faces[self.top_face][4]
        self.faces[self.top_face][4] = self.faces[self.left_face][4]
        self.faces[self.left_face][4] = self.faces[self.bottom_face][4]
        self.faces[self.bottom_face][4] = self.faces[self.right_face][4]
        self.faces[self.right_face][4] = hold_variable
        # Top face, slot 5 (right-hand edge)
        # 05 moves to 27 moves to 53 moves to 31
        hold_variable = self.faces[self.top_face][5]
        self.faces[self.top_face][5] = self.faces[self.left_face][1]
        self.faces[self.left_face][1] = self.faces[self.bottom_face][3]
        self.faces[self.bottom_face][3] = self.faces[self.right_face][7]
        self.faces[self.right_face][7] = hold_variable

    def middle_turn_z_ccw(self):
        """Simulates a counterclockwise rotation of the z-axis slice"""
        # Positive z-axis comes out of the front face
        # Top face, slot 3 (left-edge)
        # 03 moves to 37 moves to 55 moves to 21
        hold_variable = self.faces[self.top_face][3]
        self.faces[self.top_face][3] = self.faces[self.right_face][1]
        self.faces[self.right_face][1] = self.faces[self.bottom_face][5]
        self.faces[self.bottom_face][5] = self.faces[self.left_face][7]
        self.faces[self.left_face][7] = hold_variable
        # Top face, slot 4 (middle)
        # 04 moves to 34 moves to 54 moves to 24
        hold_variable = self.faces[self.top_face][4]
        self.faces[self.top_face][4] = self.faces[self.right_face][4]
        self.faces[self.right_face][4] = self.faces[self.bottom_face][4]
        self.faces[self.bottom_face][4] = self.faces[self.left_face][4]
        self.faces[self.left_face][4] = hold_variable
        # Top face, slot 5 (right-edge)
        # 05 moves to 31 moves to 53 moves to 27
        hold_variable = self.faces[self.top_face][5]
        self.faces[self.top_face][5] = self.faces[self.right_face][7]
        self.faces[self.right_face][7] = self.faces[self.bottom_face][3]
        self.faces[self.bottom_face][3] = self.faces[self.left_face][1]
        self.faces[self.left_face][1] = hold_variable

    def middle_turn_y(self):
        """Simulates a clockwise rotation of the y-axis slice"""
        # Positive y-axis comes out of the top face
        # 3 slot of front, left, back, and right faces
        # 23 moves to 13 moves to 33 moves to 43
        hold_variable = self.faces[self.front_face][3]
        self.faces[self.front_face][3] = self.faces[self.right_face][3]
        self.faces[self.right_face][3] = self.faces[self.back_face][3]
        self.faces[self.back_face][3] = self.faces[self.left_face][3]
        self.faces[self.left_face][3] = hold_variable
        # 4 slot of front, left, back, and right faces
        # 24 moves to 14 moves to 34 moves to 44
        hold_variable = self.faces[self.front_face][4]
        self.faces[self.front_face][4] = self.faces[self.right_face][4]
        self.faces[self.right_face][4] = self.faces[self.back_face][4]
        self.faces[self.back_face][4] = self.faces[self.left_face][4]
        self.faces[self.left_face][4] = hold_variable
        # 5 slot of front, left, back, and right faces
        # 25 moves to 15 moves to 35 moves to 45
        hold_variable = self.faces[self.front_face][5]
        self.faces[self.front_face][5] = self.faces[self.right_face][5]
        self.faces[self.right_face][5] = self.faces[self.back_face][5]
        self.faces[self.back_face][5] = self.faces[self.left_face][5]
        self.faces[self.left_face][5] = hold_variable

    def middle_turn_y_ccw(self):
        """Simulates a counterclockwise rotation of the y-axis slice"""
        # Positive y-axis comes out of the top face
        # 3 slot of front, left, back, and right faces
        # 23 moves to 43 moves to 33 moves to 13
        hold_variable = self.faces[self.front_face][3]
        self.faces[self.front_face][3] = self.faces[self.left_face][3]
        self.faces[self.left_face][3] = self.faces[self.back_face][3]
        self.faces[self.back_face][3] = self.faces[self.right_face][3]
        self.faces[self.right_face][3] = hold_variable
        # 4 slot of front, left, back, and right faces
        # 24 moves to 44 moves to 34 moves to 14
        hold_variable = self.faces[self.front_face][4]
        self.faces[self.front_face][4] = self.faces[self.left_face][4]
        self.faces[self.left_face][4] = self.faces[self.back_face][4]
        self.faces[self.back_face][4] = self.faces[self.right_face][4]
        self.faces[self.right_face][4] = hold_variable
        # 5 slot of front, left, back, and right faces
        # 25 moves to 45 moves to 35 moves to 15
        hold_variable = self.faces[self.front_face][5]
        self.faces[self.front_face][5] = self.faces[self.left_face][5]
        self.faces[self.left_face][5] = self.faces[self.back_face][5]
        self.faces[self.back_face][5] = self.faces[self.right_face][5]
        self.faces[self.right_face][5] = hold_variable

    def t(self):
        """Clockwise rotation of top face and cube printout"""
        self.top_turn()
        self.print_cube()

    def tc(self):
        """Counterclockwise rotation of top face and cube printout"""
        self.top_turn_ccw()
        self.print_cube()

    def f(self):
        """Clockwise rotation of front face and cube printout"""
        self.front_turn()
        self.print_cube()

    def fc(self):
        """Counterclockwise rotation of front face and cube printout"""
        self.front_turn_ccw()
        self.print_cube()

    def r(self):
        """Clockwise rotation of right face and cube printout"""
        self.right_turn()
        self.print_cube()

    def rc(self):
        """Counterclockwise rotation of right face and cube printout"""
        self.right_turn_ccw()
        self.print_cube()

    def d(self):
        """Clockwise rotation of bottom face and cube printout"""
        self.bottom_turn()
        self.print_cube()

    def dc(self):
        """Counterclockwise rotation of bottom face and cube printout"""
        self.bottom_turn_ccw()
        self.print_cube()

    def l(self):
        """Clockwise rotation of left face and cube printout"""
        self.left_turn()
        self.print_cube()

    def lc(self):
        """Counterclockwise rotation of left face and cube printout"""
        self.left_turn_ccw()
        self.print_cube()

    def b(self):
        """Clockwise rotation of back face and cube printout"""
        self.back_turn()
        self.print_cube()

    def bc(self):
        """Counterclockwise rotation of backface and cube printout"""
        self.back_turn_ccw()
        self.print_cube()

    def is_solved(self):
        """Returns true if cube is solved"""
        for face in range(6):
            for slot in range(9):
                if str(self.faces[face][0])[0] != str(self.faces[face][slot])[0]:
                    return False
        return True

    def get_faces(self):
        """Returns the layout of the cube"""
        return self.faces

    def get_solved_state(self):
        """Returns the solved state of the cube"""
        return self.solved_state

    def rotate_cube_x(self):
        """Rotates the cube clockwise around the x-axis"""
        self.right_turn()
        self.middle_turn_x()
        self.left_turn_ccw()

    def rotate_cube_x_ccw(self):
        """Rotates the cube counterclockwise around the x-axis"""
        self.right_turn_ccw()
        self.middle_turn_x_ccw()
        self.left_turn()

    def rotate_cube_y(self):
        """Rotates the cube clockwise around the y-axis"""
        self.top_turn()
        self.middle_turn_y()
        self.bottom_turn_ccw()

    def rotate_cube_y_ccw(self):
        """Rotates the cube counterclockwise around the y axis"""
        self.top_turn_ccw()
        self.middle_turn_y_ccw()
        self.bottom_turn()

    def rotate_cube_z(self):
        """Rotates the cube clockwise around the z axis"""
        self.front_turn()
        self.middle_turn_z()
        self.back_turn_ccw()

    def rotate_cube_z_ccw(self):
        """Rotates the cube conuterclockwise around the z axis"""
        self.front_turn_ccw()
        self.middle_turn_z_ccw()
        self.back_turn()

    def reset(self):
        """Resets the cube to a solved state"""
        for face in range(6):
            for slot in range(9):
                self.faces[face][slot] = self.solved_state[face][slot]
