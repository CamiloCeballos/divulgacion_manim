import numpy as np
from manim import *

class vectores(Scene):
    def construct(self):
        vector2 = Vector(PolarPlane().polar_to_point(1,PI/2))
        vector1 = Vector(PolarPlane().polar_to_point(3,0))

        self.add(vector1,vector2)
        self.play(vector2.animate.shift(RIGHT*2))
        #self.play(vector2.move_to([0,0,0]))
        

class  lineas_generadas(Scene):
    def construct(self):
        v1_line = LinearBase(scale_factor=1.2)
        self.play(Create(v1_line))

#class puntos(Scene):
#    def construct(self):
#        points = VGroup(*[Dot( color= RED, radius=0.1) for _ in range(100)])
#        points.arrange_in_grid(10,10,buff=0.3)
#        self.play(points)