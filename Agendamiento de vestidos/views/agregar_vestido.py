import customtkinter as ctk
from tkinter import messagebox
from models.vestido import guardar_vestido

class AgregarVestido(ctk.CTkToplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Agregar Vestido")
        self.geometry("300x300")

        self.nombre = ctk.CTkEntry(self, placeholder_text="Nombre")
        self.nombre.pack(pady=10)

        self.talla = ctk.CTkEntry(self, placeholder_text="Talla")
        self.talla.pack(pady=10)

        self.precio = ctk.CTkEntry(self, placeholder_text="Precio")
        self.precio.pack(pady=10)

        ctk.CTkButton(self, text="Guardar", command=self.guardar).pack(pady=20)

    def guardar(self):
        guardar_vestido(
            self.nombre.get(),
            self.talla.get(),
            self.precio.get()
        )
        messagebox.showinfo("OK", "Guardado")
        self.destroy()