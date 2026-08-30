from manim import *
import math
import numpy as np

class TrianguloNumericoEBinomial(MovingCameraScene):

    def construct(self):
        # 1. Título Inicial

        self.play(self.camera.frame.animate.scale(1.5))

        title = MathTex(r"\text{Construção dos Coeficientes Binomiais}", font_size=40)
        title.to_edge(UP, buff=0.2)
        title.shift(1.5*UP)
        self.play(Write(title), run_time=0.6)

        # Reduzido para a linha 7 para aproveitar muito melhor o espaço
        max_row = 7

        # Rótulos laterais reposicionados
        left_label = MathTex(r"\text{Valores Numericos}", font_size=34, color=YELLOW)
        left_label.move_to(np.array([-4.0, 4.25, 0]))
        
        right_label = MathTex(r"\text{Coeficientes Binomiais}", font_size=34, color=GREEN)
        right_label.move_to(np.array([3.5, 4.25, 0]))

        self.play(Write(left_label), Write(right_label), run_time=1)

        self.wait(2)

        # 2. Construção do Triângulo Numérico na Esquerda (Até a linha 7)
        numeros_triangulo = {}

        # relação de stifel

        def binomial(n, k):
            if k == 0 or k == n:
                return 1
            return binomial(n-1, k-1) + binomial(n-1, k)
        
        for n in range(max_row + 1):

            row_group = VGroup()
         
            for k in range(n + 1):
        
                val = binomial(n, k)

                # Espaçamento amplo (vertical: 0.75, horizontal: 0.6)
                x = -7.5 + k * 1.0
                y = 3.5 - n * 1.2
                
                cell = MathTex(str(val), font_size=56)
                cell.move_to(np.array([x, y, 0]))
                numeros_triangulo[(n, k)] = cell
                row_group.add(cell)
            
            self.play(FadeIn(row_group), run_time=1)

        self.wait(2)

        # 3. Construção linha a linha do Triângulo Binomial à Direita
        for n in range(max_row + 1):
            row_copies = VGroup()
            row_binomials = VGroup()
            
            for k in range(n + 1):
                val_str = str(math.comb(n, k))
                orig_pos = numeros_triangulo[(n, k)].get_center()
                
                # Posicionamento amplo para o triângulo direito (horizontal: 0.85)
                x_r = 0.5 + k * 1
                y_r = 3.5 - n * 1.2
                dest_pos = np.array([x_r, y_r, 0])
                
                # Cópia que nasce na esquerda (mantendo fonte enorme)
                copy_cell = MathTex(val_str, font_size=56, color=YELLOW)
                copy_cell.move_to(dest_pos)
                row_copies.add(copy_cell)
                
                # Binomial no destino (fonte enorme: 30)
                binom_cell = MathTex(f"\\binom{{{n}}}{{ {k} }}", font_size=40, color=GREEN)
                binom_cell.move_to(dest_pos)
                row_binomials.add(binom_cell)

                self.wait(1)

            # Faz aparecer as cópias numéricas na origem
            self.play(FadeIn(row_copies, run_time=0.25))
            
            # Deslocamento para a direita
            animations_move = []
            for i, k in enumerate(range(n + 1)):
                x_r = 0.5 + k * 0.85
                y_r = 2.5 - n * 0.75
                animations_move.append(row_copies[i].animate.move_to(np.array([x_r, y_r, 0])))
            
            self.play(*animations_move, run_time=1)

            self.wait(2)

            # Transição para os coeficientes binomiais
            animations_transform = []
            for i in range(len(row_copies)):
                animations_transform.append(ReplacementTransform(row_copies[i], row_binomials[i]))
            
            self.play(*animations_transform, run_time=0.5)
            
            self.wait(2)

        self.wait(2)