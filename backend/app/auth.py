from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from .models import User 

# sub-app para rotas de autenticação
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

#Decorator rota=auth/login metodo=Post
@auth_bp.post("/login")
def login():
    data = request.json

    # Busca usuário pelo email por consulta tabela user
    user = User.query.filter_by(email=data["email"]).first()

    #Valida usuario/senha
    if not user or not check_password_hash(user.password_hash, data["password"]):
        return jsonify({"error": "Credencial Invalida"}), 401
    
    #Gera token jwt
    token =  create_access_token(identity=user.id)
    return jsonify({"token": token})
