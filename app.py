from flask import Flask, request
from flask_cors import CORS

from database.database import connection
from database.database import cursor

app = Flask(__name__)
CORS(app)


@app.route("/users", methods=["POST"])
def create_user():
    body = request.json
    # body -> cria o usuario
    # ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
    # session.add(ed_user)


@app.route("/users")
def list_all():
    cursor.execute("SELECT * FROM aluno")
    lista_alunos = cursor.fetchall()
    # "lista_alunos = [(1, nome_aluno, curso....) (2, nome_aluno_2, curso2...]"
    # for aluno in lista_alunos:
    #     # aluno.nome X
    #     # aluno.curso X
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
