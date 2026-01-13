import tkinter as tk
import webbrowser
from componentes import botao_video, botao_voltar

class TelaParadaCardiaca(tk.Frame):
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
            text="Parada Cardiorrespiratória (RCP)",
            font=("Segoe UI", 18, "bold"),
            bg="#F9F9F9"
        ).pack(pady=20)

        texto = (
            "A parada cardiorrespiratória (PCR) ocorre quando o coração deixa de bater adequadamente e a respiração cessa. "
            "O atendimento rápido é essencial para evitar lesões cerebrais ou morte.\n\n"
            "Como identificar:\n"
            "• A vítima não responde a estímulos (inconsciente).\n"
            "• Não há respiração ou há apenas gasping (suspiros irregulares).\n"
            "• Ausência de pulso.\n\n"
            "Como agir:\n"
            "1. Verifique a segurança do local antes de se aproximar.\n"
            "2. Toque nos ombros da vítima e pergunte: 'Você está bem?'\n"
            "3. Caso não haja resposta, chame ajuda e acione o SAMU (192).\n"
            "4. Deite a vítima de costas sobre uma superfície firme.\n"
            "5. Inicie imediatamente as compressões torácicas:\n"
            "   • Posicione o calcanhar de uma mão no centro do peito e a outra por cima.\n"
            "   • Mantenha os braços estendidos e pressione com força e rapidez.\n"
            "   • Faça 100 a 120 compressões por minuto (ritmo da música ‘Stayin’ Alive’).\n"
            "6. Após cada 30 compressões, se souber, realize 2 ventilações de resgate (boca a boca).\n"
            "7. Continue até a chegada do socorro ou até a vítima apresentar sinais de vida.\n\n"
            "Uso do desfibrilador (DEA):\n"
            "• Assim que disponível, ligue o aparelho e siga as instruções de voz.\n"
            "• Mantenha as compressões até o DEA indicar aplicar o choque.\n"
            "• Após o choque, continue as manobras conforme orientado.\n\n"
            "Cuidados adicionais:\n"
            "• Evite interrupções longas durante as compressões.\n"
            "• Se houver mais de um socorrista, troquem de posição a cada 2 minutos.\n"
            "• Após o atendimento, a vítima deve ser encaminhada ao hospital para avaliação completa."
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
            "https://youtu.be/iBBoNyZefrM?si=eb_-8uGDKUFoD1Zb"
        ).pack(pady=10)

        botao_voltar(frame_scroll, controller).pack(pady=(5, 20))

        canvas.update_idletasks()
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
