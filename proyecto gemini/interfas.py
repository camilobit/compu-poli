import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

ventana=ctk.CTk()
ventana.geometry("650x650")
ventana.title("Interfaz de Usuario")
ventana.resizable(False, False)

ventana.mainloop()