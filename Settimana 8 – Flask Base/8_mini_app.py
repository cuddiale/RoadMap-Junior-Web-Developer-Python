from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Il nostro database in memoria contenente i prodotti iniziali
CATALOGO_PRODOTTI = {
    1: {"nome": "Smartphone Android", "prezzo": 599.99},
    2: {"nome": "Cuffie Noise Cancelling", "prezzo": 149.50},
    3: {"nome": "Tastiera Meccanica RGB", "prezzo": 89.90},
}
prossimo_id = 4


# 1. READ: Mostra la lista dei prodotti (Home Page)
@app.route("/")
def home_catalogo():
    return render_template("catalogo.html", prodotti=CATALOGO_PRODOTTI)


# 2. FORM DI INSERIMENTO (GET)
@app.route("/nuovo", methods=["GET"])
def mostra_form_prodotto():
    return render_template("nuovo_prodotto.html")


# 3. CREATE: Ricezione dati, Validazione e aggiunta nel dizionario (POST)
@app.route("/nuovo", methods=["POST"])
def aggiungi_prodotto():
    global prossimo_id

    nome = request.form.get("nome_prodotto")
    prezzo_str = request.form.get("prezzo_prodotto")

    # --- VALIDAZIONE INPUT ---
    # Controllo 1: Il nome non deve essere vuoto
    if not nome or nome.strip() == "":
        return render_template(
            "nuovo_prodotto.html", errore="Il nome del prodotto è obbligatorio."
        )

    # Controllo 2: Il prezzo deve essere inserito e deve essere un numero valido positivo
    try:
        prezzo = float(prezzo_str)
        if prezzo <= 0:
            return render_template(
                "nuovo_prodotto.html", errore="Il prezzo deve essere maggiore di zero."
            )
    except (ValueError, TypeError):
        return render_template(
            "nuovo_prodotto.html",
            errore="Inserisci un valore numerico valido per il prezzo.",
        )

    # Se la validazione ha successo, salviamo il prodotto nel nostro store
    CATALOGO_PRODOTTI[prossimo_id] = {"nome": nome.strip(), "prezzo": round(prezzo, 2)}
    prossimo_id += 1

    # Redirect alla home per vedere il nuovo prodotto inserito nella lista
    return redirect(url_for("home_catalogo"))


# 4. DELETE: Rimuove un prodotto cliccando sul tasto rosso
@app.route("/elimina/<int:id_prodotto>")
def elimina_prodotto(id_prodotto):
    if id_prodotto in CATALOGO_PRODOTTI:
        del CATALOGO_PRODOTTI[id_prodotto]
    return redirect(url_for("home_catalogo"))


if __name__ == "__main__":
    app.run(debug=True, port=5007)
