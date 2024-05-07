from flask import Flask, jsonify
from random_data import pessoas

# FLASK é um mine-framework (gerencia as rotas)

app = Flask(__name__)

from api import bp
app.register_blueprint(bp)