from app.models import db
from app.models.user import User

def create_tables():
    with db:
        db.create_tables([User])

def create_admin():           
    admin_username = "admin"

    if not User.select().where(User.username == admin_username).exists():
        password = "admin765"

        admin = User(
            full_name = "Cláudio Fernandes de Mattos",
            username = admin_username,
            email = "claudiofernandes.dev@gmail.com",
            contact = "54 99661 5894",
            position = "Administrador",
            role = "admin"
        )

        admin.set_password(password)
        admin.save()

        print(f"Usuário admin criado com sucesso! (admin = {admin_username} | senha = {password})")
    else:
        print("Usuário admin já existe!")

if __name__ == "__main__":
        create_tables()
        create_admin()