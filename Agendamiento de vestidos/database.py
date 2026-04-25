import sqlite3

def conectar():
    return sqlite3.connect("agenda.db")


def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    # Usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    # Vestidos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vestidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        talla TEXT,
        precio REAL
    )
    """)

    # Citas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        vestido_id INTEGER,
        FOREIGN KEY (vestido_id) REFERENCES vestidos(id)
    )
    """)

    conn.commit()
    conn.close()


def crear_usuario_admin():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE username = 'admin'")
    user = cursor.fetchone()

    if not user:
        cursor.execute(
            "INSERT INTO usuarios (username, password) VALUES (?, ?)",
            ("admin", "1234")
        )
        conn.commit()

    conn.close()