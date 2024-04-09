from flask import Flask, jsonify

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

if __name__ == '_main_':
    app.run(debug=True)