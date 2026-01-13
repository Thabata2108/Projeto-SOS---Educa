import tkinter as tk
import webbrowser
from componentes import botao_video, botao_voltar

class TelaCortesArranhoes(tk.Frame):
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

        canvas.create_window((0, 0), window=frame_scroll, anchor="n", width=580)
        canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        canvas.pack(side="top", fill="both", expand=True)
        v_scroll.pack(side="right", fill="y")
        h_scroll.pack(side="bottom", fill="x")
        
        #BOTÃO VOLTAR (SUPERIOR ESQUERDO)
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
            text="Cortes e Arranhões",
            font=("Segoe UI", 20, "bold"),
            bg="#F9F9F9"
        ).pack(pady=20)

        #TEXTO PRINCIPAL 
        texto = (
            "Os cortes e arranhões são lesões superficiais comuns, geralmente causadas por pequenos acidentes. "
            "Mesmo sendo ferimentos leves, devem ser tratados corretamente para evitar infecções e facilitar a cicatrização.\n\n"
            "O que fazer:\n"
            "1. Lave bem as mãos antes de tocar na ferida.\n"
            "2. Enxágue o ferimento com água corrente e sabão neutro para remover sujeiras.\n"
            "3. Se houver sangramento, aplique pressão com um pano limpo ou gaze até parar.\n"
            "4. Após a limpeza, seque cuidadosamente ao redor (sem esfregar) e cubra com um curativo limpo.\n"
            "5. Troque o curativo diariamente ou sempre que estiver úmido.\n"
            "6. Se o corte for profundo, com bordas abertas ou causado por objeto enferrujado, procure atendimento médico.\n\n"
            "Cuidados importantes:\n"
            "• Evite álcool ou água oxigenada diretamente na pele — podem irritar a ferida.\n"
            "• Observe sinais de infecção (vermelhidão intensa, pus, calor ou dor local).\n"
            "• Mantenha a vacinação antitetânica em dia."
        )

        tk.Label(
            frame_scroll,
            text=texto,
            font=("Segoe UI", 12),
            justify="left",
            bg="#F9F9F9",
            wraplength=500
        ).pack(padx=20, pady=10, anchor="center")

        #BOTÕES 
        botao_video(
            frame_scroll,
            "https://youtu.be/X2eBYpMkFNM?si=u0GQPx1rBNE4VuSP"
        ).pack(pady=10)

        botao_voltar(frame_scroll, controller).pack(pady=(5, 20))
         
        canvas.update_idletasks()
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)