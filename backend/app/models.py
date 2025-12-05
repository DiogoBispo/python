from . import db 
from datetime import datetime

#tabela de usuarios
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(200))

#tabela de produtos
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    marca = db.Column(db.String(120))
    valor = db.Column(db.Float)

    