import tkinter as tk

class TelaListas(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#F9F9F9")
        self.controller = controller


        tk.Label(self, text="Situações de Emergência", font=("Segoe UI", 18, "bold"), bg="#F9F9F9", fg="#515751"
           ).pack(pady=15)

        emergencias = [
            ("Cortes e Arranhões", lambda: controller.mostrar_tela("cortesarranhoes")),
            ("Queimaduras Leves", lambda: controller.mostrar_tela("queimadurasleves")),
            ("Entorses e Distensões", lambda: controller.mostrar_tela("entorsesdistensoes")),
            ("Reações Alérgicas e Picadas", lambda: controller.mostrar_tela("reacoespicadas")),
            ("Engasgos", lambda: controller.mostrar_tela("engasgos")),
            ("Hemorragias", lambda: controller.mostrar_tela("hemorragias")),
            ("Desmaios e Convulsões", lambda: controller.mostrar_tela("desmaiosconvulsoes")),
            ("Parada Cardiorrespiratória", lambda: controller.mostrar_tela("paradacardiaca")),
        ]

        for nome, comando in emergencias:
            tk.Button(
                self,
                text=nome,
                width=25,
                bg="#DCF0DC",
                fg="#515751",
                font=("Segoe UI", 12, "bold"),
                command=comando
            ).pack(pady=5)

        tk.Button(
            self,
            text="Voltar",
            bg="#A6E2A6",
            fg="#515751",
            font=("Segoe UI", 12, "bold"),
            command=lambda: controller.mostrar_tela("inicial")
        ).pack(pady=15)
