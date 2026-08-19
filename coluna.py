from manim import *
import math

class SomaColunaPascal(Scene):
    def construct(self):
        # 1. Título Inicial
        title = MathTex(r"\text{Soma dos Termos de uma Coluna (Teorema do Hoquei)}", font_size=26)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # 2. Construção do Triângulo de Pascal em formato retângulo (até a linha 8)
        max_row = 8
        cell_dict = {}  # Dicionário para armazenar cada elemento: (n, k) -> MathTex
        
        for n in range(max_row + 1):
            row_cells = VGroup()
            for k in range(n + 1):
                val = math.comb(n, k)
                x = -3.0 + k * 0.65
                y = 2.2 - n * 0.45
                
                cell = MathTex(str(val), font_size=22)
                cell.move_to(np.array([x, y, 0]))
                
                cell_dict[(n, k)] = cell
                row_cells.add(cell)
            
            self.play(FadeIn(row_cells, shift=DOWN * 0.15), run_time=0.3)

        self.wait(0.8)

        # 3. Primeiro Exemplo: Coluna k = 1, de n = 1 até n = 4
        k_col = 1
        start_row = 1
        end_row = 4

        column_boxes = VGroup()
        sum_terms = []
        
        for n in range(start_row, end_row + 1):
            cell = cell_dict[(n, k_col)]
            box = SurroundingRectangle(cell, color=YELLOW, buff=0.08)
            column_boxes.add(box)
            sum_terms.append(str(math.comb(n, k_col)))

        # Elemento resultado abaixo e à direita da diagonal
        res_cell = cell_dict[(end_row + 1, k_col + 1)]
        res_box = SurroundingRectangle(res_cell, color=GREEN, buff=0.08)

        sum_str = " + ".join(sum_terms)
        total_val = math.comb(end_row + 1, k_col + 1)
        
        eq_text = MathTex(
            f"C_{{{start_row}}}^{{{{ {k_col} }}}} + \\dots + C_{{{end_row}}}^{{{{ {k_col} }}}} = "
            f"{sum_str} = {total_val} = C_{{{end_row+1}}}^{{{{ {k_col+1} }}}}",
            font_size=22
        )
        eq_text.to_edge(DOWN, buff=0.4)

        # Animação do primeiro exemplo
        self.play(
            Create(column_boxes),
            *[cell_dict[(n, k_col)].animate.set_color(YELLOW) for n in range(start_row, end_row + 1)],
            Transform(title, eq_text),
            run_time=1
        )
        self.wait(1)

        self.play(
            Create(res_box),
            res_cell.animate.set_color(GREEN),
            run_time=0.8
        )
        self.wait(1.5)

        # Limpeza para o segundo exemplo
        self.play(
            FadeOut(column_boxes),
            FadeOut(res_box),
            *[cell_dict[(n, k_col)].animate.set_color(WHITE) for n in range(start_row, end_row + 1)],
            res_cell.animate.set_color(WHITE),
            run_time=0.5
        )

        # 4. Segundo Exemplo: Coluna k = 2, de n = 2 até n = 5
        k_col2 = 2
        start_row2 = 2
        end_row2 = 5

        column_boxes2 = VGroup()
        sum_terms2 = []
        for n in range(start_row2, end_row2 + 1):
            cell = cell_dict[(n, k_col2)]
            box = SurroundingRectangle(cell, color=YELLOW, buff=0.08)
            column_boxes2.add(box)
            sum_terms2.append(str(math.comb(n, k_col2)))

        res_cell2 = cell_dict[(end_row2 + 1, k_col2 + 1)]
        res_box2 = SurroundingRectangle(res_cell2, color=GREEN, buff=0.08)

        sum_str2 = " + ".join(sum_terms2)
        total_val2 = math.comb(end_row2 + 1, k_col2 + 1)

        eq_text2 = MathTex(
            f"C_{{{start_row2}}}^{{{{ {k_col2} }}}} + \\dots + C_{{{end_row2}}}^{{{{ {k_col2} }}}} = "
            f"{sum_str2} = {total_val2} = C_{{{end_row2+1}}}^{{{{ {k_col2+1} }}}}",
            font_size=22
        )
        eq_text2.to_edge(DOWN, buff=0.4)

        # Animação do segundo exemplo
        self.play(
            Create(column_boxes2),
            *[cell_dict[(n, k_col2)].animate.set_color(YELLOW) for n in range(start_row2, end_row2 + 1)],
            Transform(title, eq_text2),
            run_time=1
        )
        self.wait(1)

        self.play(
            Create(res_box2),
            res_cell2.animate.set_color(GREEN),
            run_time=0.8
        )
        self.wait(1.5)

        # 5. Encerramento
        final_text = MathTex(r"\text{A soma dos termos de uma coluna resulta no elemento abaixo e a direita.}", font_size=22)
        final_text.to_edge(DOWN, buff=0.4)
        
        self.play(
            FadeOut(column_boxes2),
            FadeOut(res_box2),
            *[cell_dict[(n, k_col2)].animate.set_color(WHITE) for n in range(start_row2, end_row2 + 1)],
            res_cell2.animate.set_color(WHITE),
            Transform(title, final_text),
            run_time=1
        )
        self.wait(2)