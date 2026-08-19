from manim import *
import math

class RelacaoDeStifel(Scene):
    def construct(self):
        # 1. Título Inicial
        title = MathTex(r"\text{Construcao do Triangulo de Pascal (Retangulo)}", font_size=30)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # 2. Construção linha a linha do Triângulo de Pascal em formato retângulo (até a linha 9)
        max_row = 9
        cell_dict = {}  # Dicionário para armazenar cada elemento: (n, k) -> MathTex
        
        for n in range(max_row + 1):
            row_cells = VGroup()
            for k in range(n + 1):
                val = math.comb(n, k)
                
                # Coordenadas em formato de triângulo retângulo (alinhado à esquerda)
                x = (k - n / 2.0) * 0.65  # Mantém um leve ajuste visual ou pode alinhar à esquerda pura: k * 0.65 - 3.5
                # Vamos usar alinhamento à esquerda elegante:
                x = -3.5 + k * 0.65
                y = 2.4 - n * 0.48
                
                cell = MathTex(str(val), font_size=22)
                cell.move_to(np.array([x, y, 0]))
                
                cell_dict[(n, k)] = cell
                row_cells.add(cell)
            
            # Anima a aparição de cada linha
            self.play(FadeIn(row_cells, shift=DOWN * 0.15), run_time=0.35)

        self.wait(1)

        # 3. Transição para o estudo da Relação de Stifel
        stifel_label = MathTex(
            r"\text{Relacao de Stifel: } C_n^k + C_n^{k+1} = C_{n+1}^{k+1}",
            font_size=26
        )
        stifel_label.to_edge(DOWN, buff=0.4)
        
        self.play(Transform(title, stifel_label), run_time=1)
        self.wait(0.8)

        # 4. Definição de 6 situações da Relação de Stifel
        situations = [
            (2, 0),
            (2, 1),
            (3, 1),
            (4, 2),
            (5, 2),
            (6, 3),
        ]

        for n, k in situations:
            c1 = cell_dict[(n, k)]          # C_n^k
            c2 = cell_dict[(n, k+1)]        # C_n^{k+1}
            res = cell_dict[(n+1, k+1)]     # C_{n+1}^{k+1}

            # Criação de destaques visuais (caixas)
            box1 = SurroundingRectangle(c1, color=YELLOW, buff=0.08)
            box2 = SurroundingRectangle(c2, color=YELLOW, buff=0.08)
            box_res = SurroundingRectangle(res, color=GREEN, buff=0.08)

            # Valores numéricos
            v1 = math.comb(n, k)
            v2 = math.comb(n, k+1)
            vres = math.comb(n+1, k+1)

            eq_text = MathTex(
                f"C_{{{n}}}^{{{{ {k} }}}} + C_{{{n}}}^{{{{ {k+1} }}}} = "
                f"{v1} + {v2} = {vres} = C_{{{n+1}}}^{{{{ {k+1} }}}}",
                font_size=24
            )
            eq_text.move_to(stifel_label.get_center())

            # Anima o destaque dos dois termos superiores
            self.play(
                Create(box1), Create(box2),
                c1.animate.set_color(YELLOW),
                c2.animate.set_color(YELLOW),
                Transform(title, eq_text),
                run_time=0.7
            )
            self.wait(0.4)

            # Anima o destaque do resultado inferior
            self.play(
                Create(box_res),
                res.animate.set_color(GREEN),
                run_time=0.5
            )
            self.wait(1.2)

            # Remove os destaques e reseta as cores para a próxima rodada
            fade_group = VGroup(box1, box2, box_res)
            self.play(
                FadeOut(fade_group),
                c1.animate.set_color(WHITE),
                c2.animate.set_color(WHITE),
                res.animate.set_color(WHITE),
                run_time=0.4
            )

        # Encerramento
        final_text = MathTex(r"\text{A soma de dois elementos adjacentes resulta no elemento abaixo.}", font_size=26)
        final_text.to_edge(DOWN, buff=0.4)
        
        self.play(Transform(title, final_text), run_time=1)
        self.wait(2)