from manim import *
import math

class SomaTodasDiagonais(Scene):
    def construct(self):
        # 1. Título Inicial
        title = MathTex(r"\text{Soma das Diagonais e a Sequencia de Fibonacci}", font_size=24)
        title.to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # 2. Construção do Triângulo de Pascal em formato retângulo (até a linha 6)
        max_row = 6
        cell_dict = {}  # Dicionário para armazenar cada elemento: (n, k) -> MathTex
        
        for n in range(max_row + 1):
            row_cells = VGroup()
            for k in range(n + 1):
                val = math.comb(n, k)
                x = -3.2 + k * 0.6
                y = 2.2 - n * 0.45
                
                cell = MathTex(str(val), font_size=20)
                cell.move_to(np.array([x, y, 0]))
                
                cell_dict[(n, k)] = cell
                row_cells.add(cell)
            
            self.play(FadeIn(row_cells, shift=DOWN * 0.1), run_time=0.25)

        self.wait(0.5)

        # 3. Cabeçalho da sequência à direita
        seq_header = MathTex(r"\text{Sequencia:}", font_size=26, color=GREEN)
        seq_header.move_to(np.array([2.8, 2.2, 0]))
        self.play(Write(seq_header), run_time=0.5)

        # Definição de todas as diagonais (n + k = constante)
        diagonals = [
            [(0, 0)],
            [(1, 0)],
            [(2, 0), (1, 1)],
            [(3, 0), (2, 1)],
            [(4, 0), (3, 1), (2, 2)],
            [(5, 0), (4, 1), (3, 2)],
            [(6, 0), (5, 1), (4, 2), (3, 3)],
        ]

        sequence_group = VGroup()

        # 4. Loop por todas as diagonais
        for idx, diag_pairs in enumerate(diagonals):
            boxes = VGroup()
            current_sum = 0
            
            for n, k in diag_pairs:
                cell = cell_dict[(n, k)]
                box = SurroundingRectangle(cell, color=YELLOW, buff=0.06)
                boxes.add(box)
                current_sum += math.comb(n, k)

            # Anima o destaque da diagonal atual no triângulo
            self.play(
                Create(boxes),
                *[cell_dict[(n, k)].animate.set_color(YELLOW) for n, k in diag_pairs],
                run_time=0.6
            )
            
            # Cria o elemento da sequência à direita (fonte maior, cor verde)
            seq_item = MathTex(f"{current_sum}", font_size=32, color=GREEN)
            
            if len(sequence_group) == 0:
                seq_item.next_to(seq_header, DOWN, buff=0.3)
            else:
                seq_item.next_to(sequence_group[-1], DOWN, buff=0.2)
            
            sequence_group.add(seq_item)
            
            # Anima a aparição do resultado na sequência lateral
            self.play(FadeIn(seq_item, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.6)

            # Remove os destaques para preparar a próxima diagonal
            self.play(
                FadeOut(boxes),
                *[cell_dict[(n, k)].animate.set_color(WHITE) for n, k in diag_pairs],
                run_time=0.4
            )

        # 5. Encerramento
        final_text = MathTex(r"\text{Os resultados formam exatamente a Sequencia de Fibonacci!}", font_size=22)
        final_text.to_edge(DOWN, buff=0.3)
        
        self.play(Transform(title, final_text), run_time=1)
        self.wait(2)
        