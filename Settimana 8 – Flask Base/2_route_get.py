from flask import Flask

app = Flask(__name__)


# Rotta principale (Home)
@app.route("/")
def home():
    return """
    <h1>Esercizio 2: Route GET 🌐</h1>
    <p>Benvenuto nella Home. Clicca sul link qui sotto per inviare una richiesta GET a un'altra pagina.</p>
    <a href="/info">Vai alla pagina Info (Richiesta GET)</a>
    """


# Seconda rotta (Info). Di default, tutte le @app.route gestiscono richieste GET
@app.route("/info")
def info():
    return """
    <h1>Pagina Info ℹ️</h1>
    <p>Se vedi questa pagina, il browser ha effettuato con successo una richiesta GET verso /info.</p>
    <a href="/">Torna alla Home</a>
    """


if __name__ == "__main__":
    # Usiamo una porta diversa (5001) così non rischiamo conflitti se l'altro file è ancora aperto
    app.run(debug=True, port=5001)
