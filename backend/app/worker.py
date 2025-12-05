import redis, json, time 
from app import create_app, db 
from app.models import Product

#Cria app Flask
app = create_app()

#Client Redis para ler a fila
#r = redis.Redis(host="localhost", port=6379, db=0)
r = redis.Redis(host="127.0.0.1", port=6379, db=0)


with app.app_context():
    while True:
        # BRPOP: operação bloqueante (espera até aparecer item)
        item = r.brpop("product_queue")
        if item:
            _, raw = item 
            #Converte de string JSON para dicionário
            msg = json.loads(raw)

            if msg["op"] == "create":
                #"**msg["data"]" distribui as chaves do dicionario nos parametros do construtor
                p = Product(**msg["data"])
                db.session.add(p)
                db.session.commit()
            
            elif msg["op"] == "update":
                p = Product.query.get(msg["id"])
                if p:
                    for k,v in msg["data"].items():
                        #atualiza cada campo
                        setattr(p, k, v)
                    db.session.commit()

            elif msg["op"] == "delete":
                p = Product.query.get(msg["id"])
                if p:
                    db.session.delete(p)
                    db.session.commit()
                    
        time.sleep(0.2) 
