📘 Desafio Python + Flask + PostgreSQL + Redis
API desenvolvida por dois devs júnior, com arquitetura limpa, fila assíncrona e autenticação JWT.

🚀 Tecnologias utilizadas
Python 3.9+

Flask 3

Flask-JWT-Extended

SQLAlchemy

PostgreSQL

Redis

Worker assíncrono

Docker + docker-compose

📦 Estrutura do projeto
backend/
├── app/
│ ├── **init**.py
│ ├── auth.py
│ ├── products.py
│ ├── models.py
│ └── worker.py
├── seed_user.py
├── run.py
├── requirements.txt
├── openapi.yaml
└── README.md

🔐 Autenticação
A API utiliza JWT (Bearer Token).
O login é realizado em:
POST /auth/login

Exemplo:
{
"email": "admin@admin.com",
"password": "123456"
}

🛒 Rotas de produtos
✔ GET /products
Retorna todos os produtos cadastrados.
✔ POST /products
Enfileira um novo produto no Redis para gravação assíncrona no banco.

⚙ Worker
O worker consome mensagens da fila:
queue_products

E salva no PostgreSQL.
Execute com:
python3 -m app.worker

Rodar toda stack.
Execute com:
docker-compose up --build
