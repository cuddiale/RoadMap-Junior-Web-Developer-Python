# Importiamo 'render_template' per poter leggere i file HTML esterni
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    nome_da_passare = "Alessio"

    # render_template va a cercare in automatico nella cartella 'templates'.
    # Passiamo la variabile Python 'nome_da_passare' assegnandola al nome Jinja 'nome_utente'
    return render_template("saluto.html", nome_utente=nome_da_passare)


if __name__ == "__main__":
    app.run(debug=True, port=5003)
