import tkinter as tk
from tkinter import messagebox

class TelaInicial(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#F9F9F9")

        # Container centralizado
        container = tk.Frame(self, bg="#F9F9F9")
        container.pack(expand=True)  # centraliza verticalmente

        titulo = tk.Label(
            container,
            text="SOS Educa",
            font=("Segoe UI", 22, "bold"),
            bg="#F9F9F9",
            fg="#515751"
        )
        titulo.pack(pady=10)

        subtitulo = tk.Label(
            container,
            text="Saiba socorrer em situações de emergência!",
            font=("Segoe UI", 11),
            bg="#F9F9F9",
            fg="#515751"
        )
        subtitulo.pack(pady=10)

        # Botão Situações de Emergência
        btn_lista = tk.Button(
            container,
            text="Emergências mais frequentes",
            font=("Arial", 12, "bold"),
            bg="#DCF0DC",
            fg="#515751",
            width=25, height=2,
            command=lambda: controller.mostrar_tela("listas")
        )
        btn_lista.pack(pady=8)

        # Botão Contato de Emergência
        btn_contato = tk.Button(
            container,
            text="Contato de Emergência",
            font=("Arial", 12, "bold"),
            bg="#DCF0DC",
            fg="#515751",
            width=20, height=2,
            command=self.mostrar_contatos
        )
        btn_contato.pack(pady=8)

        # Botão Sair
        btn_sair = tk.Button(
            container,
            text="Sair",
            font=("Segoe UI", 12, "bold"),
            bg="#A6E2A6",
            fg="#515751",
            width=12, height=2,
            command=controller.destroy
        )
        btn_sair.pack(pady=8)

        # Rodapé fixo
        rodape = tk.Label(
            self,
            text="Desenvolvido por Thabata Duarte - 2026",
            font=("Segoe UI", 9, "italic"),
            bg="#F9F9F9",
            fg="#888"
        )
        rodape.pack(side="bottom", pady=5)

    def mostrar_contatos(self):
        janela = tk.Toplevel(self)
        janela.title("Contatos de Emergência")
        janela.geometry("300x200")
        janela.configure(bg="#F9F9F9")
        janela.resizable(False, False)

        tk.Label(
            janela,
            text="Selecione o serviço desejado:",
            font=("Segoe UI", 12, "bold"),
            bg="#F9F9F9"
        ).pack(pady=10)

        tk.Button(
            janela, text="SAMU (192)",
            font=("Segoe UI", 12, "bold"),
            bg="#DCF0DC", fg="#515751",
            width=20,
            command=lambda: self.mostrar_numero("SAMU - 192")
        ).pack(pady=10)

        tk.Button(
            janela, text="Bombeiros (193)",
            font=("Segoe UI", 12, "bold"),
            bg="#DCF0DC", fg="#515751",
            width=20,
            command=lambda: self.mostrar_numero("Bombeiros - 193")
        ).pack(pady=10)

    def mostrar_numero(self, texto):
        messagebox.showinfo("Contato de Emergência", f"Ligue para {texto}.")
