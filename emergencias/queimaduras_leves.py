import tkinter as tk
import webbrowser
from componentes import botao_video, botao_voltar

class TelaQueimadurasLeves(tk.Frame):
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
            text="Queimaduras Leves",
            font=("Segoe UI", 20, "bold"),
            bg="#F9F9F9"
        ).pack(pady=20)

        texto = (
        
            "As queimaduras leves são aquelas que afetam apenas a camada superficial da pele, "
            "causando vermelhidão, dor e leve inchaço.\n\n"
            "   O que fazer:\n"
            "1. Resfrie imediatamente a área queimada com água corrente fria por 10 a 20 minutos.\n"
            "2. Não use gelo, pois pode agravar a lesão.\n"
            "3. Cubra a queimadura com um pano limpo e úmido para proteger contra infecções.\n"
            "4. Evite tocar nas bolhas e nunca as estoure.\n"
            "5. Caso a dor persista, utilize analgésicos simples (como paracetamol) se não houver contraindicação.\n"
            "6. Procure atendimento médico se a queimadura for extensa, profunda ou em regiões sensíveis (rosto, mãos, pés ou genitais).\n\n"
            "   O que NÃO fazer:\n"
            "Não use manteiga, pasta de dente, óleo ou pomadas caseiras — isso pode piorar a lesão.\n"
            "Não cubra com tecidos felpudos (como algodão) que soltam fiapos.\n\n"
            "   Dicas importantes:\n"
            "• Mantenha o ambiente limpo e arejado.\n"
            "• Observe sinais de infecção (vermelhidão intensa, pus, mau cheiro ou febre).\n"
            "• Atualize a vacinação antitetânica, caso a queimadura seja causada por metal, pregos ou produtos químicos.\n"
            "• Em queimaduras químicas, lave com água corrente abundante por pelo menos 20 minutos e procure o pronto atendimento imediatamente."
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
            "https://youtu.be/bIM8H6wPejs?si=Z75D9Wsd3W0-YLQu"
        ).pack(pady=10)

        botao_voltar(frame_scroll, controller).pack(pady=(5, 20))

        
        canvas.update_idletasks()
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
