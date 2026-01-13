import tkinter as tk
import webbrowser
from componentes import botao_video, botao_voltar

class TelaReacoesPicadas(tk.Frame):
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
            text="Reações Alérgicas e Picadas de Inseto",
            font=("Segoe UI", 16, "bold"),
            bg="#F9F9F9",
            wraplength=480
        ).pack(pady=20)

        
        texto = (
            
            "As reações alérgicas podem ocorrer após picadas de insetos como abelhas, vespas, formigas, "
            "mosquitos ou após o contato com substâncias que causam irritação. "
            "A intensidade da reação varia conforme a sensibilidade da pessoa.\n\n"

            " Reação leve:\n"
            "• Vermelhidão, coceira e leve inchaço no local da picada.\n"
            "• Pequena dor ou ardência.\n\n"

            "   O que fazer:\n"
            "1. Lave o local com água e sabão neutro para reduzir o risco de infecção.\n"
            "2. Aplique compressas frias para aliviar o inchaço e a coceira.\n"
            "3. Mantenha o local limpo e arejado.\n"
            "4. Se necessário, use pomadas calmantes ou antialérgicas conforme orientação médica.\n"
            "5. Evite coçar o local, pois isso pode causar ferimentos e infecção.\n\n"

            "  Reação moderada ou grave (alergia sistêmica):\n"
            "• Inchaço em várias partes do corpo.\n"
            "• Dificuldade para respirar ou engolir.\n"
            "• Sensação de tontura, desmaio ou palpitação.\n\n"
            "  O que fazer:\n"
            "1. Acione imediatamente o SAMU (192)\n"
            "2. Deite a pessoa e mantenha-a calma e confortável.\n"
            "3. Se a pessoa tiver prescrição médica de epinefrina (adrenalina), auxilie na aplicação.\n"
            "4. Solte roupas apertadas e facilite a respiração.\n"
            "5. Não ofereça líquidos ou alimentos.\n\n"

            "  Dicas de prevenção:\n"
            "• Evite usar perfumes e roupas coloridas em locais com muitos insetos.\n"
            "• Mantenha janelas protegidas com telas e use repelentes adequados.\n"
            "• Não se aproxime de colmeias ou formigueiros.\n"
            "• Se houver histórico de reações alérgicas graves, carregue sempre um antialérgico ou autoinjetor de epinefrina conforme orientação médica.\n"
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
            "https://youtu.be/DS8TG-RntcI?si=gqpO-2P79HkPlXDb"
        ).pack(pady=10)

        botao_voltar(frame_scroll, controller).pack(pady=(5, 20))
        
        canvas.update_idletasks()
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
