from tkinter import *
import random
import Rubiks
from pyswip import Prolog, Atom
import time
import copy

class SolverGUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        label = Label(text="Rubik's Cube Solver",background='#FF9CD1',font=("Arial", 25))
        label.pack()
        # Create Canvas, store canvas items
        self.canvas = Canvas(parent, width=800, height=650)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas_items = [[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],
                             [3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5]]
       
        # Draw the cube
        self.draw_cube(400, 75, 60, 8)
        # creates a model to store its cube data
        self.my_cube = Rubiks.Cube()
        # correctly colors the faces on the drawn cube according to cube data
        self.recolor_faces()
        # handles key presses for manual button input
        parent.bind('<KeyPress>', self.onKeyPress)
        # displays help text
        #self.help_text_display = self.canvas.create_text(10, 640, anchor=SW, font='courier', text=help_string)
        # timer variables
        self.current_time = 0
        self.msecs = 1000
        self.current_time_display = self.canvas.create_text(790, 640, anchor=SE, font='courier', text=self.current_time)
        self._job = None
        self.solverBtn = Button(text="Solve",height = 1,width = 5,background='#FCDA5D',font=("Arial", 25))
        self.solverBtn.pack()

    def draw_cube(self, x_origin, y_origin, side_width, space_width):
        """Draws a visual representation of a rubik's cube. 
        Currently only the top face is calibrated to make the entire face from variables"""
        # Top Face
        self.draw_top_square(x_origin, y_origin, side_width, 0, 0)
        self.draw_top_square(x_origin, y_origin+space_width+side_width, side_width, 0, 4)
        self.draw_top_square(x_origin, y_origin+space_width*2+side_width*2, side_width, 0, 8)
        self.draw_top_square(x_origin+1.73*side_width+space_width, y_origin+space_width+side_width, side_width, 0, 2)
        self.draw_top_square(x_origin-1.73*side_width-space_width, y_origin+space_width+side_width, side_width, 0, 6)
        self.draw_top_square(x_origin+(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)/2, side_width, 0, 1)
        self.draw_top_square(x_origin-(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)/2, side_width, 0, 3)
        self.draw_top_square(x_origin+(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)*3/2, side_width, 0, 5)
        self.draw_top_square(x_origin-(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)*3/2, side_width, 0, 7)
        y_origin = y_origin+space_width*2+side_width*2
        # Right Face
        self.draw_side_square(x_origin+0.5*side_width, y_origin+side_width-space_width, side_width, 1, 2, 0)
        self.draw_side_square(x_origin+0.5*side_width, y_origin+2*side_width, side_width, 1, 2, 3)
        self.draw_side_square(x_origin+0.5*side_width, y_origin+3*side_width+space_width, side_width, 1, 2, 6)
        self.draw_side_square(x_origin+0.5*side_width+side_width, y_origin+0.5*side_width-1.5*space_width, side_width, 1, 2, 1)
        self.draw_side_square(x_origin+0.5*side_width+side_width, y_origin+1.5*side_width-0.5*space_width, side_width, 1, 2, 4)
        self.draw_side_square(x_origin+0.5*side_width+side_width, y_origin+2.5*side_width+0.5*space_width, side_width, 1, 2, 7)
        self.draw_side_square(x_origin+0.5*side_width+2*side_width, y_origin-2*space_width, side_width, 1, 2, 2)
        self.draw_side_square(x_origin+0.5*side_width+2*side_width, y_origin+side_width-space_width, side_width, 1, 2, 5)
        self.draw_side_square(x_origin+0.5*side_width+2*side_width, y_origin+2*side_width, side_width, 1, 2, 8)
        # Front Face
        self.draw_side_square(x_origin-0.5*side_width, y_origin+side_width-space_width, side_width, -1, 1, 2)
        self.draw_side_square(x_origin-0.5*side_width, y_origin+2*side_width, side_width, -1, 1, 5)
        self.draw_side_square(x_origin-0.5*side_width, y_origin+3*side_width+space_width, side_width, -1, 1, 8)
        self.draw_side_square(x_origin-0.5*side_width-side_width, y_origin+0.5*side_width-1.5*space_width, side_width, -1, 1, 1)
        self.draw_side_square(x_origin-0.5*side_width-side_width, y_origin+1.5*side_width-0.5*space_width, side_width, -1, 1, 4)
        self.draw_side_square(x_origin-0.5*side_width-side_width, y_origin+2.5*side_width+0.5*space_width, side_width, -1, 1, 7)
        self.draw_side_square(x_origin-0.5*side_width-2*side_width, y_origin-2*space_width, side_width, -1, 1, 0)
        self.draw_side_square(x_origin-0.5*side_width-2*side_width, y_origin+side_width-space_width, side_width, -1, 1, 3)
        self.draw_side_square(x_origin-0.5*side_width-2*side_width, y_origin+2*side_width, side_width, -1, 1, 6)
        # Back Face
        y_origin = y_origin-space_width*2-side_width*2
        side_width = 0.75*side_width
        space_width = 0.75*space_width
        self.draw_side_square(x_origin+5*side_width, y_origin-0.5*side_width, side_width, -1, 4, 2)
        self.draw_side_square(x_origin+5*side_width, y_origin+0.5*side_width+space_width, side_width, -1, 4, 5)
        self.draw_side_square(x_origin+5*side_width, y_origin+1.5*side_width+2*space_width, side_width, -1, 4, 8)
        self.draw_side_square(x_origin+6*side_width, y_origin+0.5*space_width, side_width, -1, 4, 1)
        self.draw_side_square(x_origin+6*side_width, y_origin+side_width+1.5*space_width, side_width, -1, 4, 4)
        self.draw_side_square(x_origin+6*side_width, y_origin+2*side_width+2.5*space_width, side_width, -1, 4, 7)
        self.draw_side_square(x_origin+7*side_width, y_origin+1.0*side_width-2.5*space_width, side_width, -1, 4, 0)
        self.draw_side_square(x_origin+7*side_width, y_origin+2.0*side_width-1.5*space_width, side_width, -1, 4, 3)
        self.draw_side_square(x_origin+7*side_width, y_origin+3.0*side_width-0.5*space_width, side_width, -1, 4, 6)
        # Left face
        self.draw_side_square(x_origin-5*side_width, y_origin-0.5*side_width, side_width, 1, 3, 0)
        self.draw_side_square(x_origin-5*side_width, y_origin+0.5*side_width+space_width, side_width, 1, 3, 3)
        self.draw_side_square(x_origin-5*side_width, y_origin+1.5*side_width+2*space_width, side_width, 1, 3, 6)
        self.draw_side_square(x_origin-6*side_width, y_origin+0.5*space_width, side_width, 1, 3, 1)
        self.draw_side_square(x_origin-6*side_width, y_origin+side_width+1.5*space_width, side_width, 1, 3, 4)
        self.draw_side_square(x_origin-6*side_width, y_origin+2*side_width+2.5*space_width, side_width, 1, 3, 7)
        self.draw_side_square(x_origin-7*side_width, y_origin+1.0*side_width-2.5*space_width, side_width, 1, 3, 2)
        self.draw_side_square(x_origin-7*side_width, y_origin+2.0*side_width-1.5*space_width, side_width, 1, 3, 5)
        self.draw_side_square(x_origin-7*side_width, y_origin+3.0*side_width-0.5*space_width, side_width, 1, 3, 8)
        # Bottom face
        space_width = 4/3*space_width
        y_origin = y_origin+9*side_width
        self.draw_top_square(x_origin, y_origin, side_width, 5, 6)
        self.draw_top_square(x_origin, y_origin+space_width+side_width, side_width, 5, 4)
        self.draw_top_square(x_origin, y_origin+space_width*2+side_width*2, side_width, 5, 2)
        self.draw_top_square(x_origin+1.73*side_width+space_width, y_origin+space_width+side_width, side_width, 5, 8)
        self.draw_top_square(x_origin-1.73*side_width-space_width, y_origin+space_width+side_width, side_width, 5, 0)
        self.draw_top_square(x_origin+(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)/2, side_width, 5,7)
        self.draw_top_square(x_origin-(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)/2, side_width, 5, 3)
        self.draw_top_square(x_origin+(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)*3/2, side_width, 5, 5)
        self.draw_top_square(x_origin-(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)*3/2, side_width, 5, 1)

    def top_turn(self):
        """Turns the top face of my_cube clockwise"""
        self.my_cube.top_turn()
        self.recolor_faces()

    def front_turn(self):
        """Turns the front face of my_cube clockwise"""
        self.my_cube.front_turn()
        self.recolor_faces()

    def right_turn(self):
        """Turns the right face of my_cube clockwise"""
        self.my_cube.right_turn()
        self.recolor_faces()

    def left_turn(self):
        """Turns the left face of my_cube clockwise"""
        self.my_cube.left_turn()
        self.recolor_faces()

    def back_turn(self):
        """Turns the back face of my_cube clockwise"""
        self.my_cube.back_turn()
        self.recolor_faces()

    def bottom_turn(self):
        """Turns the bottom face of my_cube clockwise"""
        self.my_cube.bottom_turn()
        self.recolor_faces()

    def top_turn_ccw(self):
        """Turns the top face of my_cube counterclockwise"""
        self.my_cube.top_turn_ccw()
        self.recolor_faces()

    def front_turn_ccw(self):
        """Turns the front face of my_cube counterclockwise"""
        self.my_cube.front_turn_ccw()
        self.recolor_faces()

    def right_turn_ccw(self):
        """Turns the right face of my_cube counterclockwise"""
        self.my_cube.right_turn_ccw()
        self.recolor_faces()

    def left_turn_ccw(self):
        """Turns the left face of my_cube counterclockwise"""
        self.my_cube.left_turn_ccw()
        self.recolor_faces()

    def back_turn_ccw(self):
        """Turns the back face of my_cube counterclockwise"""
        self.my_cube.back_turn_ccw()
        self.recolor_faces()

    def bottom_turn_ccw(self):
        """Turns the bottom face of my_cube counterclockwise"""
        self.my_cube.bottom_turn_ccw()
        self.recolor_faces()

    def middle_x(self):
        """Rotates the middle x-axis slice clockwise"""
        self.my_cube.middle_turn_x()
        self.recolor_faces()

    def middle_x_ccw(self):
        """Rotates the middle x-axis slice counterclockwise"""
        self.my_cube.middle_turn_x_ccw()
        self.recolor_faces()

    def middle_y(self):
        """Rotates the middle y-axis slice clockwise"""
        self.my_cube.middle_turn_y()
        self.recolor_faces()

    def middle_y_ccw(self):
        """Rotates the middle y-axis slice counterclockwise"""
        self.my_cube.middle_turn_y_ccw()
        self.recolor_faces()

    def middle_z(self):
        """Rotates the middle z-axis slice clockwise"""
        self.my_cube.middle_turn_z()
        self.recolor_faces()

    def middle_z_ccw(self):
        """Rotates the middle z-axis slice counterclockwise"""
        self.my_cube.middle_turn_z_ccw()
        self.recolor_faces()

    def print_cube(self):
        """prints the layout of my_cube to shell"""
        self.my_cube.print_cube()
        self.recolor_faces()

    def turn_x(self):
        """rotates the cube around the x axis clockwise"""
        self.my_cube.rotate_cube_x()
        self.recolor_faces()

    def turn_x_ccw(self):
        """rotates the cube around the x-axis counterclockwise)"""
        self.my_cube.rotate_cube_x_ccw()
        self.recolor_faces()

    def turn_y(self):
        """rotates the cube around the Y axis clockwise"""
        self.my_cube.rotate_cube_y()
        self.recolor_faces()

    def turn_y_ccw(self):
        """rotates the cube around the y-axis counterclockwise)"""
        self.my_cube.rotate_cube_y_ccw()
        self.recolor_faces()

    def turn_z(self):
        """rotates the cube around the z axis clockwise"""
        self.my_cube.rotate_cube_z()
        self.recolor_faces()

    def turn_z_ccw(self):
        """rotates the cube around the z-axis counterclockwise)"""
        self.my_cube.rotate_cube_z_ccw()
        self.recolor_faces()

    def reset(self):
        """Resets the cube to a solved state"""
        self.my_cube.reset()
        print('RESET')
        self.recolor_faces()

    def solve(self):
        """Solve the cube"""
        prolog = Prolog()
        prolog.consult("Solver.pl")
        solution = []

        #Query String Builder
        Query_String = ""

        current_cube = copy.deepcopy(self.my_cube.get_faces())
        current_cube[1],current_cube[3]= current_cube[3],current_cube[1]
        current_cube[2],current_cube[3]= current_cube[3],current_cube[2]
        for face in current_cube:
            for piece in face:
                piece_color = str(piece)[:1]
                if(piece_color == '0'):
                    Query_String += "b,"
                elif(piece_color == '1'):
                    Query_String += "w,"
                elif(piece_color == '2'):
                    Query_String += "r,"
                elif(piece_color == '3'):
                    Query_String += "o,"
                elif(piece_color == '4'):
                    Query_String += "y,"
                elif(piece_color == '5'):
                    Query_String += "g,"
                
        Query_String = Query_String[:-1]

        print(Query_String)
        
        for a in prolog.query('solve(rubik(%s),Z)'%Query_String):
            atomic_list = list(a.values())
            break
        
        for item in atomic_list[0]:
            solution.append(str(item))

        #print(solution)
        self.solve_cube(solution)

    def solve_cube(self, solution):
        """Rotate the cube according to the solution"""
        for step in solution:
            print(step)
            # Basic face rotations
            if step == 'counter_clockwise_LEFT':
                self.left_turn_ccw()
            elif step == 'clockwise_UP':
                self.top_turn()
            elif step == 'clockwise_RIGHT':
                self.right_turn()
            elif step == 'counter_clockwise_DOWN':
                self.bottom_turn()
            elif step == 'counter_clockwise_BACK':
                self.back_turn()
            elif step == 'clockwise_FRONT':
                self.front_turn()
            elif step == 'clockwise_LEFT':
                self.left_turn()
            elif step == 'counter_clockwise_UP':
                self.top_turn_ccw()
            elif step == 'counter_clockwise_RIGHT':
                self.right_turn_ccw()
            elif step == 'clockwise_DOWN':
                self.bottom_turn_ccw()
            elif step == 'clockwise_BACK':
                self.back_turn_ccw()
            elif step == 'counter_clockwise_FRONT':
                self.front_turn_ccw()
            else:
                print("UNIMPLEMENTED!")
            self.update_idletasks()
            time.sleep(2)

    def scramble(self):
        """Scrambles the cube"""
        for turn in range(100):
            turn_type = random.randrange(12)
            if turn_type == 0:
                self.top_turn()
            elif turn_type == 1:
                self.front_turn()
            elif turn_type == 2:
                self.right_turn()
            elif turn_type == 3:
                self.left_turn()
            elif turn_type == 4:
                self.back_turn()
            elif turn_type == 5:
                self.bottom_turn()
            elif turn_type == 6:
                self.top_turn_ccw()
            elif turn_type == 7:
                self.front_turn_ccw()
            elif turn_type == 8:
                self.right_turn_ccw()
            elif turn_type == 9:
                self.left_turn_ccw()
            elif turn_type == 10:
                self.back_turn_ccw()
            elif turn_type == 11:
                self.bottom_turn_ccw()

    def draw_top_square(self, x_origin, y_origin, side_length, face, slot, outline='black', fill='white', width=1):
        """Draws the squares of the top face on canvas"""
        points = []
        points.append((x_origin + 1.73/2*side_length, y_origin))
        points.append((x_origin, y_origin + 0.5*side_length))
        points.append((x_origin - 1.73/2*side_length, y_origin))
        points.append((x_origin, y_origin - 0.5*side_length))
        self.canvas_items[face][slot] = self.canvas.create_polygon(points, outline=outline, fill=fill, width=width)

    def draw_side_square(self, x_origin, y_origin, side_length, orientation, face=0, slot=0, outline='black', fill='white', width=1):
        """Draws the squares of the side faces on canvas"""
        points = []
        # Orientation 1 for right, -1 for front
        points.append((x_origin+1.73/4*side_length, y_origin-orientation*0.75*side_length))
        points.append((x_origin+1.73/4*side_length, y_origin+orientation*0.25*side_length))
        points.append((x_origin-1.73/4*side_length, y_origin+orientation*0.75*side_length))
        points.append((x_origin-1.73/4*side_length, y_origin-orientation*0.25*side_length))
        self.canvas_items[face][slot] = self.canvas.create_polygon(points, outline=outline, fill=fill, width=width)

    def draw_side(self, x_origin, y_origin, side_length, width, shape_type, slot):
        """Draws the miscellaneous objects, which help make visualization easier."""

    def recolor_faces(self):

        """Recolor the faces of the rubik's cube. Color the visual representation"""
        for face in range(6):
            for slot in range(9):
                if int(self.my_cube.faces[face][slot])<10:
                    self.canvas.itemconfig(self.canvas_items[face][slot], fill='blue')
                elif int(self.my_cube.faces[face][slot])<20:
                    self.canvas.itemconfig(self.canvas_items[face][slot], fill='white')
                elif int(self.my_cube.faces[face][slot])<30:
                    self.canvas.itemconfig(self.canvas_items[face][slot], fill='red')
                elif int(self.my_cube.faces[face][slot])<40:
                    self.canvas.itemconfig(self.canvas_items[face][slot], fill='orange')
                elif int(self.my_cube.faces[face][slot])<50:
                    self.canvas.itemconfig(self.canvas_items[face][slot], fill='yellow')
                elif int(self.my_cube.faces[face][slot])<60:
                    self.canvas.itemconfig(self.canvas_items[face][slot], fill='green')

    def onKeyPress(self, event):
        """Handles Key Presses so cube can be controlled through keyboard"""
        # Basic face rotations
        if event.char == 'z':
            self.left_turn()
        elif event.char == 'a':
            self.top_turn()
        elif event.char == 'c':
            self.right_turn()
        elif event.char == 'd':
            self.bottom_turn()
        elif event.char == 'e':
            self.back_turn()
        elif event.char == 'q':
            self.front_turn()
        elif event.char == 'Z':
            self.left_turn_ccw()
        elif event.char == 'A':
            self.top_turn_ccw()
        elif event.char == 'C':
            self.right_turn_ccw()
        elif event.char == 'D':
            self.bottom_turn_ccw()
        elif event.char == 'E':
            self.back_turn_ccw()
        elif event.char == 'Q':
            self.front_turn_ccw()
        # These are cube rotations
        elif event.char == 'v':
            self.turn_x()
        elif event.char == 'f':
            self.turn_y()
        elif event.char == 'r':
            self.turn_z()
        elif event.char == 'V':
            self.turn_x_ccw()
        elif event.char == 'F':
            self.turn_y_ccw()
        elif event.char == 'R':
            self.turn_z_ccw()
        # These are slice rotations
        elif event.char == 'x':
            self.middle_x()
        elif event.char == 'X':
            self.middle_x_ccw()
        elif event.char == 's':
            self.middle_y()
        elif event.char == 'S':
            self.middle_y_ccw()
        elif event.char == 'w':
            self.middle_z()
        elif event.char == 'W':
            self.middle_z_ccw()
        # Miscellaneous button presses
        elif event.char == '.':
            self.reset()
        elif event.char == '?':
            self.solve()
        elif event.char == '0':
            self.scramble()
        elif event.char == 'u':
            if self.my_cube.is_solved() == True:
                print("THE CUBE IS SOLVED")
            else:
                print("THE CUBE IS NOT YET SOLVED")
                
        elif event.char == 'p':
            self.my_cube.faces = [[10,11,12,13,14,15,16,17,18],#white
                                  [20,21,22,23,24,25,26,27,28],#red
                                  ['00','01','02','03','04','05','06','07','08'],#blue
                                  [50,51,52,53,54,55,56,57,58],#green
                                  [30,31,32,33,34,35,36,37,38],#orange
                                  [40,41,42,43,44,45,46,47,48]]#yellow
            self.my_cube.print_cube()

    

if __name__ == '__main__':
    window = Tk()
    shell = SolverGUI(window)
