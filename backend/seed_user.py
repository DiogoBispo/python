"""
Seed simples para criar um usuário padrão no banco.
Uso: python seed_user.py
"""

from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    email = "admin@admin.com"
    senha = "123456"

    # Gera hash da senha
    senha_hash = generate_password_hash(senha)

    # Cria usuário
    user = User(email=email, password_hash=senha_hash)

    db.session.add(user)
    db.session.commit()

    print("Usuário criado com sucesso!")
    print(f"Email: {email}")
    print(f"Senha: {senha}")
