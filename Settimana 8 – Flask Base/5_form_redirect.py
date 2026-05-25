# Importiamo 'redirect' e 'url_for' per spostare l'utente da una pagina all'altra
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# 1. MOSTRA IL FORM (Richiesta GET standard)
@app.route("/form")
def mostra_form():
    return render_template("form_contatti.html")


# 2. ELABORA I DATI (Richiesta POST)
@app.route("/invia-form", methods=["POST"])
def elabora_form():
    # Prendiamo il nome dal form HTML usando l'attributo name="nome_utente"
    nome = request.form.get("nome_utente")

    # Validazione input: se l'utente non ha scritto nulla, bloccalo
    if not nome or nome.strip() == "":
        return "<h1>Errore! ❌ Il campo nome non può essere vuoto.</h1><a href='/form'>Riprova</a>"

    # Se è tutto ok, facciamo un REDIRECT alla rotta 'pagina_successo'
    # Passiamo anche il nome come parametro nell'indirizzo URL
    return redirect(url_for("pagina_successo", nome_da_salutare=nome))


# 3. PAGINA DI ARRIVO DOPO IL REDIRECT
@app.route("/grazie/<nome_da_salutare>")
def pagina_successo(nome_da_salutare):
    # Mostriamo il template di successo passando il nome ricevuto dall'URL
    return render_template("successo.html", nome=nome_da_salutare)


if __name__ == "__main__":
    app.run(debug=True, port=5004)
