import tkinter as tk
import webbrowser
from componentes import botao_video, botao_voltar

class TelaEntorsesDistensoes(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#F9F9F9")
        self.controller = controller

        canvas = tk.Canvas(self, bg="#F9F9F9", highlightthickness=0)
        v_scroll = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        h_scroll = tk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        frame_scroll = tk.Frame(canvas, bg="#F9F9F9")

        frame_scroll.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all"),
                xscrollcommand=h_scroll.set,
                yscrollcommand=v_scroll.set
            )
        )

        canvas.create_window((0, 0), window=frame_scroll, anchor="n", width=530)
        canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        canvas.pack(side="top", fill="both", expand=True)
        v_scroll.pack(side="right", fill="y")
        h_scroll.pack(side="bottom", fill="x")
        
        btn_voltar_topo = tk.Button(
        frame_scroll,
        text="menu",
        bg="#DCF0DC",
        fg="#515751",
        font=("Segoe UI", 12, "bold"),
        bd=0,
        relief="flat",
        command=lambda: controller.mostrar_tela("listas")
        )
        btn_voltar_topo.place(x=10, y=10)

      
        tk.Label(
            frame_scroll,
            text="Entorses e Distensões",
            font=("Segoe UI", 20, "bold"),
            bg="#F9F9F9"
        ).pack(pady=20)

        texto = (
        
            "Essas lesões são comuns em atividades físicas, quedas ou movimentos bruscos. "
            "A entorse ocorre quando há um estiramento ou rompimento parcial dos ligamentos "
            "que unem os ossos de uma articulação (como tornozelo, joelho ou punho). "
            "Já a distensão é o estiramento ou ruptura das fibras musculares.\n\n"

            " **Sintomas comuns:**\n"
            "• Dor intensa e localizada.\n"
            "• Inchaço e vermelhidão.\n"
            "• Dificuldade de movimentar a articulação.\n"
            "• Em casos mais graves, pode haver hematomas e instabilidade.\n\n"

            "   O que fazer:\n"
            "1. Interrompa imediatamente a atividade e evite apoiar o membro afetado.\n"
            "2. Aplique compressas frias ou gelo envolto em um pano por 15 a 20 minutos nas primeiras horas.\n"
            "3. Eleve o membro lesionado para reduzir o inchaço.\n"
            "4. Faça uma leve compressão com faixa elástica, sem apertar demais.\n"
            "5. Mantenha o local em repouso.\n"
            "6. Caso a dor, o inchaço ou a limitação de movimento persistam, procure avaliação médica.\n\n"

            " O que evitar:\n"
            "• Não aqueça o local nas primeiras 48 horas (isso pode aumentar o inchaço).\n"
            "• Não force o movimento nem tente “colocar no lugar”.\n"
            "• Não massageie áreas com dor intensa ou inchaço evidente.\n\n"

            "  Dicas importantes:\n"
            "• Após 48 horas, se houver melhora, podem ser usadas compressas mornas para relaxar a musculatura.\n"
            "• Mantenha uma boa hidratação e alimentação equilibrada — ajudam na recuperação.\n"
            "• Em caso de entorse grave, pode haver fratura associada — nesse caso, é essencial procurar um pronto atendimento.\n"
        )

        tk.Label(
            frame_scroll,
            text=texto,
            font=("Segoe UI", 12),
            justify="left",
            bg="#F9F9F9",
            wraplength=480
        ).pack(padx=20, pady=10, anchor="center")

        botao_video(
            frame_scroll,
            "https://youtu.be/0lYv4fZ8Y7k?si=1APx1eGzUyCaHiNg"
        ).pack(pady=10)

        botao_voltar(frame_scroll, controller).pack(pady=(5, 20))

        canvas.update_idletasks()
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
