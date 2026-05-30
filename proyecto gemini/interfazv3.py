import tkinter as tk
import customtkinter as ctk
import threading
from google import genai

# ======================================
# CONFIGURACIÓN
# ======================================

API_KEY = "AIzaSyAXLwXnexNiWIsJwoIoM0wKGfMy1P_d_Mw"

client = genai.Client(api_key=API_KEY)

# ======================================
# FUNCIONES
# ======================================

def actualizar_textbox(texto):
    textbox.insert("end", texto)
    textbox.see("end")


def ejecutar_consulta(prompt):

    try:

        respuesta = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        texto_respuesta = respuesta.text

        root.after(
            0,
            lambda: actualizar_textbox(
                f"\n🧑 Tú:\n{prompt}\n\n🤖 Gemini:\n{texto_respuesta}\n"
            )
        )

        root.after(
            0,
            lambda: estado_label.configure(text="Listo")
        )

    except Exception as e:

        root.after(
            0,
            lambda: actualizar_textbox(
                f"\n❌ Error:\n{str(e)}\n"
            )
        )

        root.after(
            0,
            lambda: estado_label.configure(text="Error")
        )


def consultar():

    prompt = entry_prompt.get().strip()

    if not prompt:

        actualizar_textbox(
            "\n⚠️ Debes escribir una pregunta.\n"
        )
        return

    actualizar_textbox(
        f"\n⏳ Consultando...\n"
    )

    estado_label.configure(text="Consultando...")

    entry_prompt.delete(0, "end")

    hilo = threading.Thread(
        target=ejecutar_consulta,
        args=(prompt,),
        daemon=True
    )

    hilo.start()


def enter_event(event):
    consultar()


def limpiar_chat():
    textbox.delete("1.0", "end")


# ======================================
# INTERFAZ
# ======================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()

root.title("Cliente Gemini AI")
root.geometry("600x700")
root.resizable(True, True)

titulo = ctk.CTkLabel(
    root,
    text="Consulta a Gemini",
    font=("Arial", 22, "bold")
)
titulo.pack(pady=15)

entry_prompt = ctk.CTkEntry(
    root,
    width=600,
    placeholder_text="Escribe tu pregunta aquí..."
)
entry_prompt.pack(pady=10)

entry_prompt.bind("<Return>", enter_event)

frame_botones = ctk.CTkFrame(root)
frame_botones.pack(pady=10)

btn_consultar = ctk.CTkButton(
    frame_botones,
    text="Consultar",
    command=consultar,
    width=120
)

btn_consultar.pack(
    side="left",
    padx=10
)

btn_limpiar = ctk.CTkButton(
    frame_botones,
    text="Limpiar",
    command=limpiar_chat,
    width=120
)

btn_limpiar.pack(
    side="left",
    padx=10
)

textbox = ctk.CTkTextbox(
    root,
    width=650,
    height=350,
    wrap="word"
)

textbox.pack(
    pady=15,
    padx=20,
    fill="both",
    expand=True
)

estado_label = ctk.CTkLabel(
    root,
    text="Listo",
    font=("Arial", 12)
)

estado_label.pack(pady=5)

btn_salir = ctk.CTkButton(
    root,
    text="Salir",
    command=root.destroy,
    fg_color="red",
    hover_color="#990000",
    height=40
)

btn_salir.pack(
    pady=15
)

# ======================================
# INICIO
# ======================================

root.mainloop()