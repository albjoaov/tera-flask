from flask import Flask, request

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


@app.route("/users/<user_id>")
def list_one(user_id):
    safe_query = "SELECT * FROM aluno WHERE id = %s"
    cursor.execute(safe_query, (user_id,))
    aluno_tuple = cursor.fetchone()
    return {"lista": aluno_tuple}, 200


@app.route("/users/<user_id>", methods=["PUT"])
def update(user_id):
    # body = request.json
    # nome = body["nome"]
    safe_query = "UPDATE aluno SET nome = 'Jose' WHERE id = %s"
    cursor.execute(safe_query, (user_id,))

    # unsafe_query = f"UPDATE aluno SET nome = 'Jose' WHERE id = {user_id}"
    # cursor.execute(unsafe_query)

    connection.commit()
    cursor.close()
    connection.close()
    return user_id


@app.route("/users", methods=["POST"])
def create():
    body = request.json
    nome = body["nome"]
    endereco = body["endereco"]
    telefone = body["telefone"]
    cpf = body["cpf"]
    insert = (nome, endereco, telefone, cpf)
    safe_query = "INSERT INTO aluno (nome, endereco, telefone, cpf) values (%s, %s, %s, %s)"
    cursor.execute(safe_query, insert)
    connection.commit()
    return {"message": "Usuário criado com sucesso"}, 201


@app.route("/users/<user_id>", methods=["DELETE"])
def delete(user_id):
    safe_query = "DELETE FROM aluno WHERE id = %s"
    cursor.execute(safe_query, (user_id,))
    connection.commit()
    return {"message": "Usuário deletado com sucesso"}, 204


# Tratamento de conexoes e cursor
# Transacoes
# Consumo do back pelo front
# Auth
