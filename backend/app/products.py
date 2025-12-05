from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import redis, json 
from .models import Product, db 

# Blueprint de produtos, todas rotas começam com /products
product_bp = Blueprint("products", __name__, url_prefix="/products")

# Client Redis apontando para localhost
#r = redis.Redis(host="localhost", port=6379, db=0)
r = redis.Redis(host="127.0.0.1", port=6379, db=0)



@product_bp.get("")
@jwt_required()
def list_products():
    products = Product.query.all()
    result = [{"id": p.id, "nome": p.nome, "marca": p.marca, "valor": p.valor}for p in products]
    return jsonify(result)

@product_bp.post("")
@jwt_required()
def create_product():
    data = request.json
    message = {"op": "create", "data": data}
    r.lpush("product_queue", json.dumps(message))
    return jsonify({"msg": "Produto enfileirado"}), 202

@product_bp.put("/<int:id>")
@jwt_required() 
def update_product(id):
    data = request.json
    message = {"op": "update", "id": id, "data": data}
    r.lpush("product_queue", json.dumps(message))
    return jsonify({"msg": "Atualização enfileirada"}), 202

@product_bp.delete("/<int:id>")
@jwt_required()
def delete_product(id):
    message = {"op": "delete", "id": id}
    r.lpush("product_queue", json.dumps(message))
    return jsonify({"msg": "Remoção enfileirada"}), 202


