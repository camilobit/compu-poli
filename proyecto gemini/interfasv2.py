import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

ventana=ctk.CTk()
ventana.title("Interfaz de Usuario")
ventana.geometry("650x650")
ventana.resizable(False, False)

#caja de entrada
entrada = ctk.CTkEntry(ventana, placeholder_text="Ingrese su texto aquí")
entrada.pack(pady=20)   

# caja de salida
salida = ctk.CTkTextbox(ventana, width=400, height=300)
salida.pack(pady=20)

def consuta():
    texto = entrada.get()
    salida.delete("0.0", ctk.END)
    salida.insert("0.0", f"Tu: {texto}")


boton = ctk.CTkButton(ventana, text="Enviar", command=consuta)
boton.pack(pady=10)





ventana.mainloop()