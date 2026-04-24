import customtkinter as ctk
from tkinter import messagebox
from models.cita import guardar_cita, obtener_citas
from database import crear_tablas

class AgendaApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Agenda de Vestidos")
        self.geometry("500x500")

        crear_tabla()

        self.crear_ui()
        self.cargar_citas()

    def crear_ui(self):
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.titulo = ctk.CTkLabel(self.frame, text="Agendar Vestido", font=("Arial", 20))
        self.titulo.pack(pady=10)

        self.entry_fecha = ctk.CTkEntry(self.frame, placeholder_text="Fecha (YYYY-MM-DD)")
        self.entry_fecha.pack(pady=5)

        self.entry_servicio = ctk.CTkEntry(self.frame, placeholder_text="Tipo de vestido")
        self.entry_servicio.pack(pady=5)

        self.btn = ctk.CTkButton(self.frame, text="Guardar", command=self.guardar)
        self.btn.pack(pady=10)

        self.lista = ctk.CTkTextbox(self.frame, height=200)
        self.lista.pack(pady=10)

    def guardar(self):
        fecha = self.entry_fecha.get()
        servicio = self.entry_servicio.get()

        if not fecha or not servicio:
            messagebox.showwarning("Error", "Campos obligatorios")
            return

        guardar_cita(fecha, servicio)
        messagebox.showinfo("OK", "Guardado")

        self.entry_fecha.delete(0, "end")
        self.entry_servicio.delete(0, "end")

        self.cargar_citas()

    def cargar_citas(self):
        self.lista.delete("1.0", "end")

        citas = obtener_citas()

        for c in citas:
            self.lista.insert("end", f"{c[1]} - {c[2]}\n")