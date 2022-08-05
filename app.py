from flask import Flask

from database import connection
from database import cursor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/users")
def list_all():
    cursor.execute("SELECT * FROM aluno")
    lista_alunos = cursor.fetchall()
    return {"lista": lista_alunos}, 200


@app.route("/users/<user_id>", methods=["PUT"])
def update(user_id):
    # body = request.json
    # nome = body["nome"]
    safe_query = "UPDATE aluno SET nome = 'Jose' WHERE id = %s and nome = %s"
    cursor.execute(safe_query, (user_id,))

    # unsafe_query = f"UPDATE aluno SET nome = 'Jose' WHERE id = {user_id}"
    # cursor.execute(unsafe_query)

    connection.commit()
    cursor.close()
    connection.close()
    return user_id

# Tratamento de conexoes e cursor
# Transacoes
# Consumo do back pelo front
# Auth
