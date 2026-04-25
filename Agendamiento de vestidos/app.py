from database import crear_tablas, crear_usuario_admin
from views.login import LoginApp


if __name__ == "__main__":
    crear_tablas()
    crear_usuario_admin()

    app = LoginApp()
    app.mainloop()