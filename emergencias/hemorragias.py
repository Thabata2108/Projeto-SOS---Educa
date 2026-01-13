import tkinter as tk
import webbrowser
from componentes import botao_video, botao_voltar

class TelaHemorragias(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#F9F9F9")
        self.controller = controller

        canvas = tk.Canvas(self, bg="#F9F9F9", highlightthickness=0)
        v_scroll = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        h_scroll = tk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        frame_scroll = tk.Frame(canvas, bg="#F9F9F9")

        frame_scroll.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=frame_scroll, anchor="nw", width=550)
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
            text="Hemorragias",
            font=("Segoe UI", 20, "bold"),
            bg="#F9F9F9"
        ).pack(pady=20)

        
        texto = (
            "As hemorragias ocorrem quando há perda de sangue em decorrência da ruptura de vasos sanguíneos. "
            "Podem ser internas (quando o sangue fica dentro do corpo) ou externas (visíveis). "
            "O controle rápido é fundamental para evitar complicações graves.\n\n"
            "Tipos de hemorragia externa:\n"
            "• Arterial: sangue vermelho vivo e jorrando — mais grave.\n"
            "• Venosa: sangue escuro, saindo de forma contínua.\n"
            "• Capilar: sangramento leve e superficial.\n\n"
            "Como agir diante de uma hemorragia externa:\n"
            "1. Mantenha a calma e deite a pessoa, se possível.\n"
            "2. Pressione o local com um pano limpo, gaze ou compressa.\n"
            "3. Não remova objetos que estejam cravados — pressione ao redor.\n"
            "4. Eleve o membro afetado, se não houver fratura aparente.\n"
            "5. Mantenha a pressão até o sangramento parar ou até a chegada do socorro.\n\n"
            "Hemorragia interna (sem sangramento visível):\n"
            "• Os sinais incluem palidez, fraqueza, suor frio, tontura, desmaio e abdômen inchado.\n"
            "• Nesses casos, não dê nada por via oral e leve imediatamente ao pronto atendimento.\n\n"
            "Cuidados adicionais:\n"
            "• Evite fazer torniquetes sem orientação médica, pois podem causar danos graves.\n"
            "• Se houver suspeita de fratura, imobilize o local antes de mover a vítima.\n"
            "• Monitore sinais vitais (respiração e pulso) até o atendimento chegar."
        )

        tk.Label(
            frame_scroll,
            text=texto,
            font=("Segoe UI", 12),
            justify="left",
            bg="#F9F9F9",
            wraplength=500
        ).pack(padx=20, pady=10, anchor="center")

        botao_video(
            frame_scroll,
            "https://youtu.be/7rYdBqTgXY4?si=VmCeCHlZe6KuyfMf"
        ).pack(pady=10)

        botao_voltar(frame_scroll, controller).pack(pady=(5, 20))

        canvas.update_idletasks()
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
