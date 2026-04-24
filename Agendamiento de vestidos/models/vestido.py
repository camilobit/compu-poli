from database import conectar

def guardar_vestido(nombre, talla, precio):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO vestidos (nombre, talla, precio) VALUES (?, ?, ?)",
        (nombre, talla, precio)
    )

    conn.commit()
    conn.close()