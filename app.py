from flask import Flask

#__name__ = "__main__"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/simba")
def about():
    return "Vai tomar no cu, Simba"

# Toda vez que eu executo de forma manual esse arquivo, o __name__ vai ser igual a __main__.
# Portanto quando eu faço essa condicional abaixo, eu restrinjo apenas para a execução manual do arquivo
# Essa forma não é aceita para disponibilizar para clientes reais
if __name__ == "__main__":
    app.run(debug=True)