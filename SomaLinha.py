from manim import *
import math

class SomaLinhaPascal(Scene):
    def construct(self):
        # 1. Título Inicial
        title = MathTex(r"\text{Soma dos Termos de uma Linha: } \sum_{k=0}^{n} C_n^k = 2^n", font_size=34)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)

        # 2. Construção do Triângulo de Pascal em formato retângulo (até a linha 5)
        max_row = 5
        cell_dict = {}  # Dicionário para armazenar cada elemento: (n, k) -> MathTex
        
        for n in range(max_row + 1):
            row_cells = VGroup()
            for k in range(n + 1):
                val = math.comb(n, k)
                x = -3.0 + k * 0.65
                y = 2.2 - n * 0.48
                
                cell = MathTex(str(val), font_size=42)
                cell.move_to(np.array([x, y, 0]))
                
                cell_dict[(n, k)] = cell
                row_cells.add(cell)
            
            self.play(FadeIn(row_cells, shift=DOWN * 1), run_time=2)

        self.wait(0.8)

        # 3. Exemplo 1: Linha n = 3
        target_row1 = 3
        row_boxes1 = VGroup()
        sum_terms1 = []
        
        for k in range(target_row1 + 1):
            cell = cell_dict[(target_row1, k)]
            box = SurroundingRectangle(cell, color=YELLOW, buff=0.08)
            row_boxes1.add(box)
            sum_terms1.append(str(math.comb(target_row1, k)))

        sum_str1 = " + ".join(sum_terms1)
        total_val1 = 2 ** target_row1

        eq_text1 = MathTex(
            f"n = {target_row1} \\implies {sum_str1} = {sum(map(int, sum_terms1))} = 2^{{{target_row1}}} = {total_val1}",
            font_size=32
        )
        eq_text1.to_edge(DOWN, buff=2)

        self.play(
            Create(row_boxes1),
            *[cell_dict[(target_row1, k)].animate.set_color(YELLOW) for k in range(target_row1 + 1)],
            Transform(title, eq_text1),
            run_time=1
        )
        self.wait(1.5)

        # Limpeza para o segundo exemplo
        self.play(
            FadeOut(row_boxes1),
            *[cell_dict[(target_row1, k)].animate.set_color(WHITE) for k in range(target_row1 + 1)],
            run_time=0.5
        )

        # 4. Exemplo 2: Linha n = 4
        target_row2 = 4
        row_boxes2 = VGroup()
        sum_terms2 = []
        
        for k in range(target_row2 + 1):
            cell = cell_dict[(target_row2, k)]
            box = SurroundingRectangle(cell, color=YELLOW, buff=0.08)
            row_boxes2.add(box)
            sum_terms2.append(str(math.comb(target_row2, k)))

        sum_str2 = " + ".join(sum_terms2)
        total_val2 = 2 ** target_row2

        eq_text2 = MathTex(
            f"n = {target_row2} \\implies {sum_str2} = {sum(map(int, sum_terms2))} = 2^{{{target_row2}}} = {total_val2}",
            font_size=32
        )
        eq_text2.to_edge(DOWN, buff=2)

        self.play(
            Create(row_boxes2),
            *[cell_dict[(target_row2, k)].animate.set_color(YELLOW) for k in range(target_row2 + 1)],
            Transform(title, eq_text2),
            run_time=1
        )
        self.wait(1.5)

        # 5. Encerramento
        final_text = MathTex(r"\text{A soma dos elementos de uma linha qualquer } n \text{ é sempre igual a } 2^n.", font_size=32)
        final_text.to_edge(DOWN, buff=2)
        
        self.play(
            FadeOut(row_boxes2),
            *[cell_dict[(target_row2, k)].animate.set_color(WHITE) for k in range(target_row2 + 1)],
            Transform(title, final_text),
            run_time=1
        )
        self.wait(4)