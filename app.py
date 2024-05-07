from flask import Flask, render_template

# FLASK é um mine-framework (gerencia as rotas)

app = Flask(__name__)

app.route("/")
def index():
    return render_template("index.html")

from api import bp
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0")