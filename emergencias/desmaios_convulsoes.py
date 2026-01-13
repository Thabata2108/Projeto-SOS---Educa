import tkinter as tk
import webbrowser
from componentes import botao_video, botao_voltar

class TelaDesmaiosConvulsoes(tk.Frame):
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
            text="Desmaios e Convulsões",
            font=("Segoe UI", 20, "bold"),
            bg="#F9F9F9"
        ).pack(pady=20)

        
        texto = (
            " DESMAIOS (Síncope):\n"
            "O desmaio ocorre quando há uma queda temporária do fluxo sanguíneo para o cérebro. "
            "Pode ser causado por calor excessivo, falta de ar, medo ou dor intensa.\n\n"
            " O que fazer:\n"
            "1. Deite a pessoa de costas e eleve as pernas cerca de 30 cm para facilitar o retorno do sangue ao cérebro.\n"
            "2. Afrouxe roupas apertadas e mantenha o ambiente ventilado.\n"
            "3. Verifique se ela está respirando e com pulso.\n"
            "4. Se não recobrar a consciência em até 1 minuto, acione o SAMU (192).\n"
            "5. Após o retorno da consciência, ofereça água e mantenha a pessoa deitada por alguns minutos.\n\n"
            " CONVULSÕES:\n"
            "As convulsões acontecem por descargas elétricas anormais no cérebro, que podem causar movimentos "
            "involuntários e perda de consciência.\n\n"
            " Durante uma crise convulsiva:\n"
            "1. Mantenha a calma e afaste objetos perigosos próximos à pessoa.\n"
            "2. Não tente segurá-la à força nem colocar nada em sua boca.\n"
            "3. Após a crise, deite-a de lado (posição lateral de segurança).\n"
            "4. Verifique se está respirando normalmente.\n"
            "5. Acione o SAMU (192) se a crise durar mais de 5 minutos ou for a primeira vez.\n\n"
            "⚠️ Após a crise:\n"
            "• Deixe a pessoa descansar e mantenha o ambiente calmo.\n"
            "• Observe sinais de confusão mental ou dificuldade para respirar.\n"
            "• Se possível, anote o tempo da crise para informar os socorristas."
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
            "https://youtu.be/g2flVYGKLHc?si=66pEq3FoPAAFsyVM"
        ).pack(pady=10)

        botao_voltar(frame_scroll, controller).pack(pady=(5, 20))

        canvas.update_idletasks()
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)