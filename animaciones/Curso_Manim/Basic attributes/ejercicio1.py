from manim import *

class plano_coordenado(Scene):
    def construct(self):
        plano = NumberPlane(background_line_style={
            "stroke_color": WHITE
        },
        x_axis_config={
            "stroke_color":RED
        },
        y_axis_config={
            "stroke_color":RED
        })
        linea_abajo = NumberLine(x_range=[-7.0, 7.0], include_numbers=True, decimal_number_config={"num_decimal_places": 1},
        stroke_opacity=0.0)
        linea_arriba = NumberLine(x_range=[-7.0, 7.0], include_numbers=True, decimal_number_config={"num_decimal_places": 1}
        )
        linea_abajo.to_edge(DOWN, buff=0)
        linea_arriba.to_edge(UP, buff=0)
        linea_der = NumberLine(x_range=[-3, 3], include_numbers=True, rotation=PI/2, decimal_number_config={
            "num_decimal_places": 1}, stroke_opacity=0)
        linea_der.to_edge(RIGHT, buff=0)

        linea_iz = NumberLine(x_range=[-3, 3], include_numbers=True, rotation=PI/2, decimal_number_config={
            "num_decimal_places": 1}, stroke_opacity=0)
        linea_iz.to_edge(LEFT, buff=0)

        self.add(plano, linea_abajo, linea_arriba)
        self.add(linea_der, linea_iz)
