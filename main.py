import tkinter as tk
from inicial import TelaInicial
from listas import TelaListas

# importar todas as telas de emergência
from emergencias.cortes_arranhoes import TelaCortesArranhoes
from emergencias.queimaduras_leves import TelaQueimadurasLeves
from emergencias.entorses_distensoes import TelaEntorsesDistensoes
from emergencias.reacoes_picadas import TelaReacoesPicadas
from emergencias.engasgos import TelaEngasgos
from emergencias.hemorragias import TelaHemorragias
from emergencias.desmaios_convulsoes import TelaDesmaiosConvulsoes
from emergencias.parada_cardiaca import TelaParadaCardiaca


class SOSEducaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SOS Educa")
        self.geometry("450x550")
        self.resizable(False, False)

        self.telas = {}

        # --- container principal ---
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # 🔧 garantir que tudo dentro expanda corretamente
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # --- registrar telas ---
        for T in (
            TelaInicial,
            TelaListas,
            TelaCortesArranhoes,
            TelaQueimadurasLeves,
            TelaEntorsesDistensoes,
            TelaReacoesPicadas,
            TelaEngasgos,
            TelaHemorragias,
            TelaDesmaiosConvulsoes,
            TelaParadaCardiaca,
        ):
            nome = T.__name__.replace("Tela", "").lower()
            frame = T(container, self)
            self.telas[nome] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela("inicial")

    def mostrar_tela(self, nome):
        tela = self.telas.get(nome)
        if tela:
            tela.tkraise()


if __name__ == "__main__":
    app = SOSEducaApp()
    app.mainloop()
