from manim import *
import math
import numpy as np

class TrianguloNumericoEBinomial(MovingCameraScene):

    def construct(self):
        # 1. Título Inicial

        self.play(self.camera.frame.animate.scale(1.5))

        title = MathTex(r"\text{Construção dos Coeficientes Binomiais}", font_size=40)
        title.to_edge(UP, buff=0.2)
        self.play(Write(title), run_time=0.6)

        # Reduzido para a linha 7 para aproveitar muito melhor o espaço
        max_row = 7

        # Rótulos laterais reposicionados
        left_label = MathTex(r"\text{Valores Numericos}", font_size=34, color=YELLOW)
        left_label.move_to(np.array([-4.0, 3.1, 0]))
        
        right_label = MathTex(r"\text{Coeficientes Binomiais}", font_size=34, color=GREEN)
        right_label.move_to(np.array([3.5, 3.1, 0]))

        self.play(Write(left_label), Write(right_label), run_time=1)

        self.wait(2)

        # 2. Construção do Triângulo Numérico na Esquerda (Até a linha 7)
        numero_triangulo = {}
        for n in range(max_row + 1):
        # n representa cada linha do triângulo
            row_group = VGroup()
            # cria um grupo para cada linha
            for k in range(n + 1):
            #percorre cada elemento dentro de uma mesma linha
                val = math.comb(n, k)
                # Espaçamento amplo (vertical: 0.75, horizontal: 0.6)
                x = -5.5 + k * 0.6
                y = 2.5 - n * 0.75
                
                cell = MathTex(str(val), font_size=34)
                cell.move_to(np.array([x, y, 0]))
                numero_triangulo[(n, k)] = cell
                row_group.add(cell)
            
            self.play(FadeIn(row_group, shift=DOWN * 0.05), run_time=1)

        self.wait(2)