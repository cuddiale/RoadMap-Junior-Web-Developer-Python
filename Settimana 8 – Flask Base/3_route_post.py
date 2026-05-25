from flask import Flask, request

app = Flask(__name__)


# Questa pagina mostra il modulo (Form) all'utente usando il metodo GET (standard)
@app.route("/")
def home():
    return """
    <h1>Esercizio 3: Route POST ✉️</h1>
    <p>Compila il modulo qui sotto. I dati verranno inviati al server tramite una richiesta POST.</p>
    
    <form method="POST" action="/invia-dati">
        <label for="messaggio">Scrivi qualcosa:</label>
        <input type="text" id="messaggio" name="testo_utente">
        <button type="submit">Invia al Server</button>
    </form>
    """


# Questa rotta accetta SOLO richieste di tipo POST.
# Se provi a digitarla direttamente nel browser, Flask ti darà errore.
@app.route("/invia-dati", methods=["POST"])
def gestisci_post():
    # Estraiamo il dato inviato dal form usando il valore dell'attributo 'name' dell'input
    dato_ricevuto = request.form.get("testo_utente")

    return f"""
    <h1>Dati Ricevuti! ✅</h1>
    <p>Il server ha catturato la tua richiesta POST.</p>
    <p><strong>Contenuto inviato:</strong> {dato_ricevuto}</p>
    <br>
    <a href="/">Torna al modulo</a>
    """


if __name__ == "__main__":
    # Usiamo la porta 5002 per questo esercizio
    app.run(debug=True, port=5002)
