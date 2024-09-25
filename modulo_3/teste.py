from flask import Flask

# variavel = Classe(__variavel__)
teste = Flask(__name__)


@teste.route("/")  # sempre que a rota padrao, '/', for acessada, essa funcao sera executada
def hello_world():
    return "Hello world!"


@teste.route("/about")
def about():
    return "Pagina sobre"


if __name__ == "__main__":
    teste.run(debug=True)  # usado apenas para o desenvolvimento local
    # coleta todas a informacoes de log
