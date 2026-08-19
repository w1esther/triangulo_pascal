from manim import *
import math

class TrianguloNumericoEBinomial(Scene):
    def construct(self):
        # 1. Título Inicial
        title = MathTex(r"\text{Construcao dos Coeficientes Binomiais}", font_size=36)
        title.to_edge(UP, buff=0.2)
        self.play(Write(title), run_time=0.6)

        # Reduzido para a linha 7 para aproveitar muito melhor o espaço
        max_row = 7

        # Rótulos laterais reposicionados
        left_label = MathTex(r"\text{Valores Numericos}", font_size=30, color=YELLOW)
        left_label.move_to(np.array([-4.0, 3.3, 0]))
        
        right_label = MathTex(r"\text{Coeficientes Binomiais}", font_size=30, color=GREEN)
        right_label.move_to(np.array([3.5, 3.3, 0]))

        self.play(Write(left_label), Write(right_label), run_time=0.6)

        # 2. Construção do Triângulo Numérico na Esquerda (Até a linha 7)
        left_cells = {}
        for n in range(max_row + 1):
            row_group = VGroup()
            for k in range(n + 1):
                val = math.comb(n, k)
                # Espaçamento amplo (vertical: 0.75, horizontal: 0.6)
                x = -5.5 + k * 0.6
                y = 2.5 - n * 0.75
                
                cell = MathTex(str(val), font_size=34)
                cell.move_to(np.array([x, y, 0]))
                left_cells[(n, k)] = cell
                row_group.add(cell)
            
            self.play(FadeIn(row_group, shift=DOWN * 0.05), run_time=0.2)

        self.wait(0.5)

        # 3. Construção linha a linha do Triângulo Binomial à Direita
        for n in range(max_row + 1):
            row_copies = VGroup()
            row_binomials = VGroup()
            
            for k in range(n + 1):
                val_str = str(math.comb(n, k))
                orig_pos = left_cells[(n, k)].get_center()
                
                # Posicionamento amplo para o triângulo direito (horizontal: 0.85)
                x_r = 0.5 + k * 0.85
                y_r = 2.5 - n * 0.75
                dest_pos = np.array([x_r, y_r, 0])
                
                # Cópia que nasce na esquerda (mantendo fonte enorme)
                copy_cell = MathTex(val_str, font_size=34, color=YELLOW)
                copy_cell.move_to(orig_pos)
                row_copies.add(copy_cell)
                
                # Binomial no destino (fonte enorme: 30)
                binom_cell = MathTex(f"\\binom{{{n}}}{{{{ {k} }}}}", font_size=30, color=GREEN)
                binom_cell.move_to(dest_pos)
                row_binomials.add(binom_cell)

            # Faz aparecer as cópias numéricas na origem
            self.play(FadeIn(row_copies, shift=UP * 0.03), run_time=0.25)
            
            # Deslocamento para a direita
            animations_move = []
            for i, k in enumerate(range(n + 1)):
                x_r = 0.5 + k * 0.85
                y_r = 2.5 - n * 0.75
                animations_move.append(row_copies[i].animate.move_to(np.array([x_r, y_r, 0])))
            
            self.play(*animations_move, run_time=0.6)

            # Transição para os coeficientes binomiais
            animations_transform = []
            for i in range(len(row_copies)):
                animations_transform.append(ReplacementTransform(row_copies[i], row_binomials[i]))
            
            self.play(*animations_transform, run_time=0.5)
            
            self.wait(0.15)

        self.wait(1)

        # 4. Encerramento
       # final_text = MathTex(r"\text{Cada valor numerico equivale a um coeficiente binomial } \\binom{{n}}{{k}}.", font_size=30)
        #final_text.to_edge(DOWN, buff=0.1)
        
        #self.play(Transform(title, final_text), run_time=1)
        #self.wait(2)