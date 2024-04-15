from flask import Flask, jsonify
from random_data import pessoas

# FLASK é um mine-framework (gerencia as rotas)

app = Flask(__name__)

@app.route('/') # Etá criando uma rota no inicio ("/")
def home():
    return jsonify({"status": 200, "message": "API de ALANIS_GRESPAN_FERNANDES"})

@app.route("/aleatorios")
def aleatorios(): #função python
    import random
    a = random.randint(49, 100)
    return jsonify({"status":200, "data": a}) # retorno

@app.route("/argumentos/<string:nome>")
def argumentos(nome:str):
    return jsonify( {"status": 200, "data":nome} )

@app.route("/argumentos")
def arg_implicito(nome:str):
    return jsonify( {"status": 200, "data":nome} )

@app.route("/idades", methods = ("GET"))
def idades():
    from random_data import pessoas
    import funcoes
    num = funcoes.maior_de_50(pessoas)
    return jsonify( {"status": 200, "data": num} )

@app.route("/salario", methods = ("GET"))
def salario():
    from random_data import pessoas
    import funcoes
    num = funcoes.mais_2000(pessoas)
    return jsonify( {"status": 200, "data": num} )

if __name__ == '_main_':
    app.run(debug=True)