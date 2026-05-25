from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Esercizio 1: App Flask Base Funzionante! 🚀</h1>"


if __name__ == "__main__":
    # Avviamo il server locale
    app.run(debug=True)
