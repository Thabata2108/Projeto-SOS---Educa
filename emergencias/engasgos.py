import tkinter as tk
import webbrowser
from componentes import botao_video, botao_voltar

class TelaEngasgos(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#F9F9F9")
        self.controller = controller

        #Canvas com rolagem
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
            text="Engasgos",
            font=("Segoe UI", 20, "bold"),
            bg="#F9F9F9"
        ).pack(pady=20)

        texto = (
            "O engasgo ocorre quando algum alimento ou objeto bloqueia total ou parcialmente "
            "as vias respiratórias, impedindo a passagem de ar. Saber agir rapidamente pode salvar vidas.\n\n"
            "Se a pessoa estiver tossindo ou conseguindo falar:\n"
            "• Incentive-a a continuar tossindo para tentar eliminar o objeto.\n"
            "• Não bata nas costas enquanto ela estiver tossindo, pois pode piorar o bloqueio.\n\n"
            "Se a pessoa não conseguir respirar, tossir ou falar:\n"
            "1. Fique atrás da pessoa e envolva-a pela cintura.\n"
            "2. Feche uma das mãos em punho e posicione logo acima do umbigo.\n"
            "3. Segure o punho com a outra mão e pressione com força para dentro e para cima (manobra de Heimlich).\n"
            "4. Repita o movimento até o objeto ser expelido ou até a chegada do socorro.\n\n"
            "Se a pessoa desmaiar:\n"
            "• Deite-a no chão e acione imediatamente o SAMU (192).\n"
            "• Inicie as manobras de reanimação cardiopulmonar (RCP) se não houver respiração.\n\n"
            "Em bebês menores de 1 ano:\n"
            "1. Apoie o bebê de bruços em seu antebraço, com a cabeça ligeiramente abaixo do tronco.\n"
            "2. Dê até 5 tapas firmes nas costas, entre as omoplatas.\n"
            "3. Se não resolver, vire o bebê de barriga para cima e faça até 5 compressões torácicas "
            "no centro do peito, com dois dedos.\n"
            "4. Repita até o objeto sair ou o socorro chegar.\n\n"
            "Após o episódio, é importante que a pessoa seja avaliada por um médico, "
            "mesmo que o engasgo pareça resolvido, pois podem ocorrer lesões internas."
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
            "https://youtu.be/sTVQ0-9E78g?si=IBw2g8fo_Xnz4Eau"
        ).pack(pady=10)

        botao_voltar(frame_scroll, controller).pack(pady=(5, 20))

        canvas.update_idletasks()
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
