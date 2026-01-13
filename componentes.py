import tkinter as tk
import webbrowser

def botao_video(master, url):
    """Cria o botão padronizado de vídeo"""
    return tk.Button(
        master,
        text="Ver vídeo explicativo",
        bg="#DCF0DC",
        fg="#515751",
        font=("Segoe UI", 12, "bold"),
        relief="flat",
        width=22,
        cursor="hand2",
        command=lambda: webbrowser.open(url)
    )

def botao_voltar(master, controller):
    """Cria o botão padronizado de voltar"""
    return tk.Button(
        master,
        text="Voltar",
        bg="#A6E2A6",
        fg="#515751",
        font=("Segoe UI", 12, "bold"),
        relief="flat",
        width=15,
        cursor="hand2",
        command=lambda: controller.mostrar_tela("listas")
    )
