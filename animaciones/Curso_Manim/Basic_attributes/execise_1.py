from manim import *

class screen_coordinates(Scene):
    def construct(self):

        x_line = Line()
        x_line.width = 15
        
        y_line = Line().rotate(PI/2)
        y_line.width = 100
        
        
        self.add(x_line)
        self.add(y_line)
        