from flask import Flask, render_template

app = Flask(__name__)


# --- AGGIUNGIAMO LA NUOVA ROTTA PROPRIO QUI ---
@app.route("/")
def indice_rapido():
    return '<h1>Sei sulla rotta principale!</h1><a href="/struttura/home">Clicca qui per entrare nel sito con il Layout Base</a>'


# Questa era la rotta della Home che stavi già usando
@app.route("/struttura/home")
def home_dinamica():
    return render_template("pagina_home.html")


# Questa è la rotta delle Informazioni
@app.route("/struttura/info")
def info_dinamica():
    return render_template("pagina_info.html")


if __name__ == "__main__":
    app.run(debug=True, port=5005)
