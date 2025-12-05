from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Objeto global SQLAlchemy
db = SQLAlchemy()   

def create_app():
    #função que cria e configura a aplicação
    app = Flask(__name__)
    
    ##Criado para manter o token fixo
    app.config["SECRET_KEY"] = "supersecretodevjunior123"  # fallback
    app.config["JWT_SECRET_KEY"] = "jwtsegurodevjunior123"  # usado pelo JWT
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False  # token infinito para testes


    #String conexão SQL / Chave token jwt
    #app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5433/desafio"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:desafio123@localhost:5433/desafio"

    #desativado para manter o token fixo para testes
    #app.config["JWT_SECRET_KEY"] = "supersecret"
    app.config["JWT_SECRET_KEY"] = False

    #Inicializa o SQLAlchemy com Flask / Inicia o JWT
    db.init_app(app)
    JWTManager(app)

    #importa e registra os blueprint
    from .auth import auth_bp
    from .products import product_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)

    return app 