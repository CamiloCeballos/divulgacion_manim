from manim import *
from numpy import pi

class screen_coordinates(Scene):
    def construct(self):

        x_line = Line()
        x_line.width = 15
        
        y_line = Line(start=DOWN, end=UP)
        y_line.width = 15

        self.add(x_line, y_line)

        
        