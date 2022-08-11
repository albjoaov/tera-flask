from flask import Flask, render_template

from database import cursor

app = Flask(__name__)


@app.route("/lista")
def lista():
    cursor.execute("SELECT a.nome FROM aluno a")
    lista_alunos = cursor.fetchall()  # [ (diogo), (Jose), (joao)... ]
    nome_alunos = []
    for aluno in lista_alunos:  # Na primeira iteração é (diogo)
        nome_alunos.append(aluno[0])  # Na primeira iteração aluno[0] -> "diogo"
    # ao final da iteração vou ter: nome_alunos = [ "diogo", "jose", "joao", ... ]
    return render_template("lista-alunos.html", nome_alunos=nome_alunos)
