import customtkinter as ctk
from models.vestido import conectar

class VerVestidos(ctk.CTkToplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Vestidos")
        self.geometry("400x300")

        self.text = ctk.CTkTextbox(self)
        self.text.pack(pady=20)

        self.cargar()

    def cargar(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM vestidos")
        datos = cursor.fetchall()

        for d in datos:
            self.text.insert("end", f"{d[1]} - Talla {d[2]} - ${d[3]}\n")