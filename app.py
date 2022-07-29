from flask import Flask, render_template
from flask import request
from markupsafe import escape

app = Flask(__name__)
exemplo = __name__


@app.route("/")
def home():
    return "<script>Hello World</script>"


@app.route("/canonical_url/")
def teste():
    return f"Essa é uma rota específica"


@app.route("/<canonical_url>/")
def canonical_url(canonical_url):
    return f"Olá, {escape(canonical_url)}"


@app.route("/inseguro/<path:subpath>")
def inseguro(subpath):
    print(f"O meu sub caminho é: {subpath}")
    return f"{subpath}"


@app.route("/seguro/<path:subpath>")
def seguro(subpath):
    print(f"O meu sub caminho é: {escape(subpath)}")
    return f"{escape(subpath)}"


@app.route("/conversor/<int:numero>")
def conversor_numero(numero):
    return f"O número é {numero}"


@app.route("/recurso/<int:numero>", methods=["POST"])
def criar_recurso(numero):
    return f"O recurso a ser criado é: {numero}"


@app.route("/multiplos-metodos/<int:numero>", methods=["POST", "PUT"])
def multiplos_metodos(numero):
    print(request.headers)
    acao = None

    if request.method == "POST":
        acao = "Criando o recurso"
        print(acao)

    elif request.method == "PUT":
        acao = "Atualizando o recurso o recurso"
        print("Atualizando o recurso o recurso")

    return f" {acao}: {numero}"


@app.route("/melhor_pratica/<int:numero>", methods=["PUT"])
def melhor_pratica(numero):
    acao = "Atualizando o recurso o recurso"
    print("Atualizando o recurso o recurso")
    return f" {acao}: {numero}"


@app.route("/template")
def template_fixo():
    return render_template("hello-world.html")


@app.route("/template-dinamico/<name>")
def template_dinamico(name):
    return render_template("dinamico.html", name=name, name_2=123456789)
