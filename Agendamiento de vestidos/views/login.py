import customtkinter as ctk
from tkinter import messagebox
from models.usuario import validar_usuario
from views.dashboard import Dashboard

class LoginApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("300x250")

        self.user = ctk.CTkEntry(self, placeholder_text="Usuario")
        self.user.pack(pady=10)

        self.password = ctk.CTkEntry(self, placeholder_text="Contraseña", show="*")
        self.password.pack(pady=10)

        self.btn = ctk.CTkButton(self, text="Ingresar", command=self.login)
        self.btn.pack(pady=20)

    def login(self):
        u = self.user.get()
        p = self.password.get()

        if validar_usuario(u, p):
            self.destroy()
            dashboard = Dashboard()
            dashboard.mainloop()
        else:
            messagebox.showerror("Error", "Credenciales inválidas")