from manim import *
import math

class SomaDiagonalAbaixoPascal(Scene):
    def construct(self):
        # 1. Título Inicial
        title = MathTex(r"\text{Soma de Diagonal: Igual ao Elemento Abaixo}", font_size=24)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # 2. Construção do Triângulo de Pascal em formato retângulo (até a linha 6)
        max_row = 6
        cell_dict = {}  # Dicionário para armazenar cada elemento: (n, k) -> MathTex
        
        for n in range(max_row + 1):
            row_cells = VGroup()
            for k in range(n + 1):
                val = math.comb(n, k)
                x = -3.0 + k * 0.65
                y = 2.2 - n * 0.48
                
                cell = MathTex(str(val), font_size=22)
                cell.move_to(np.array([x, y, 0]))
                
                cell_dict[(n, k)] = cell
                row_cells.add(cell)
            
            self.play(FadeIn(row_cells, shift=DOWN * 0.15), run_time=0.3)

        self.wait(0.8)

        # 3. Exemplo 1: Termos (1,0), (2,1), (3,2). O resultado é (4,2) [diretamente abaixo de (3,2)]
        diag_pairs_1 = [(1, 0), (2, 1), (3, 2)]
        boxes_1 = VGroup()
        sum_terms_1 = []

        for n, k in diag_pairs_1:
            cell = cell_dict[(n, k)]
            box = SurroundingRectangle(cell, color=YELLOW, buff=0.08)
            boxes_1.add(box)
            sum_terms_1.append(str(math.comb(n, k)))

        res_n_1, res_k_1 = 4, 2  # Elemento exatamente abaixo do último termo (3, 2)
        res_cell_1 = cell_dict[(res_n_1, res_k_1)]
        res_box_1 = SurroundingRectangle(res_cell_1, color=GREEN, buff=0.08)

        sum_str_1 = " + ".join(sum_terms_1)
        total_val_1 = math.comb(res_n_1, res_k_1)

        eq_text_1 = MathTex(
            f"\\binom{{1}}{{0}} + \\binom{{2}}{{1}} + \\binom{{3}}{{2}} = "
            f"{sum_str_1} = {total_val_1} = \\binom{{res_n_1}}{{res_k_1}}",
            font_size=22
        )
        eq_text_1.to_edge(DOWN, buff=0.4)

        self.play(
            Create(boxes_1),
            *[cell_dict[(n, k)].animate.set_color(YELLOW) for n, k in diag_pairs_1],
            Transform(title, eq_text_1),
            run_time=1
        )
        self.wait(1)

        self.play(
            Create(res_box_1),
            res_cell_1.animate.set_color(GREEN),
            run_time=0.8
        )
        self.wait(1.5)

        # Limpeza para o segundo exemplo
        self.play(
            FadeOut(boxes_1),
            FadeOut(res_box_1),
            *[cell_dict[(n, k)].animate.set_color(WHITE) for n, k in diag_pairs_1],
            res_cell_1.animate.set_color(WHITE),
            run_time=0.5
        )

        # 4. Exemplo 2: Termos (2,0), (3,1), (4,2). O resultado é (5,2) [diretamente abaixo de (4,2)]
        diag_pairs_2 = [(2, 0), (3, 1), (4, 2)]
        boxes_2 = VGroup()
        sum_terms_2 = []

        for n, k in diag_pairs_2:
            cell = cell_dict[(n, k)]
            box = SurroundingRectangle(cell, color=YELLOW, buff=0.08)
            boxes_2.add(box)
            sum_terms_2.append(str(math.comb(n, k)))

        res_n_2, res_k_2 = 5, 2  # Elemento exatamente abaixo do último termo (4, 2)
        res_cell_2 = cell_dict[(res_n_2, res_k_2)]
        res_box_2 = SurroundingRectangle(res_cell_2, color=GREEN, buff=0.08)

        sum_str_2 = " + ".join(sum_terms_2)
        total_val_2 = math.comb(res_n_2, res_k_2)

        eq_text_2 = MathTex(
            f"\\binom{{2}}{{0}} + \\binom{{3}}{{1}} + \\binom{{4}}{{2}} = "
            f"{sum_str_2} = {total_val_2} = \\binom{{{res_n_2}}}{{{{ {res_k_2} }}}}",
            font_size=22
        )
        eq_text_2.to_edge(DOWN, buff=0.4)

        self.play(
            Create(boxes_2),
            *[cell_dict[(n, k)].animate.set_color(YELLOW) for n, k in diag_pairs_2],
            Transform(title, eq_text_2),
            run_time=1
        )
        self.wait(1)

        self.play(
            Create(res_box_2),
            res_cell_2.animate.set_color(GREEN),
            run_time=0.8
        )
        self.wait(1.5)


       