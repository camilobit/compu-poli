import customtkinter as ctk
from views.agregar_vestido import AgregarVestido
from views.agenda import AgendaApp
from views.ver_vestidos import VerVestidos

class Dashboard(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Dashboard")
        self.geometry("400x400")

        ctk.CTkLabel(self, text="Panel Principal", font=("Arial", 20)).pack(pady=20)

        ctk.CTkButton(self, text="Agregar Vestido", command=self.abrir_agregar).pack(pady=10)
        ctk.CTkButton(self, text="Agendar Vestido", command=self.abrir_agenda).pack(pady=10)
        ctk.CTkButton(self, text="Ver Vestidos", command=self.ver_vestidos).pack(pady=10)

    def abrir_agregar(self):
        AgregarVestido(self)

    def abrir_agenda(self):
        AgendaApp(self)

    def ver_vestidos(self):
        VerVestidos(self)