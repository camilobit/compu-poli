from database import conectar

def guardar_cita(fecha, servicio):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO citas (fecha, servicio) VALUES (?, ?)",
        (fecha, servicio)
    )

    conn.commit()
    conn.close()

def obtener_citas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM citas")
    datos = cursor.fetchall()

    conn.close()
    return datos