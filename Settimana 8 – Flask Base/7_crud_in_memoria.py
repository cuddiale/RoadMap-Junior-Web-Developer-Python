from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    # Reindirizza l'utente direttamente alla pagina dei todo
    return redirect(url_for("mostra_todo"))


# Il nostro finto Database in memoria (un dizionario Python)
# Struttura -> id: "testo del task"
DATABASE_COMPITI = {1: "Comprare il latte 🥛", 2: "Studiare la roadmap di Flask 🐍"}
# Variabile per generare ID sempre unici
prossimo_id = 3


# 1. READ: Mostra tutti i task presenti nel finto DB
@app.route("/todo")
def mostra_todo():
    return render_template("todo.html", lista_task=DATABASE_COMPITI)


# 2. CREATE: Aggiunge un nuovo task dopo aver convalidato l'input
@app.route("/todo/aggiungi", methods=["POST"])
def aggiungi_todo():
    global prossimo_id
    testo = request.form.get("nuovo_task")

    # VALIDAZIONE INPUT: Controlliamo se l'utente ha barato inviando spazi vuoti
    if not testo or testo.strip() == "":
        # Se l'input è invalido, mostriamo la nostra ERROR PAGE personalizzata
        return (
            render_template(
                "errore_todo.html", messaggio_errore="Non puoi inserire un task vuoto!"
            ),
            400,
        )

    # Salviamo nel nostro dizionario (Database in memoria)
    DATABASE_COMPITI[prossimo_id] = testo.strip()
    prossimo_id += 1  # Incrementiamo l'ID per il prossimo elemento

    return redirect(url_for("mostra_todo"))


# 3. DELETE: Cancella un elemento usando l'ID passato nell'URL
@app.route("/todo/elimina/<int:id_compito>")
def elimina_todo(id_compito):
    # Controlliamo se l'ID esiste nel nostro database
    if id_compito in DATABASE_COMPITI:
        del DATABASE_COMPITI[id_compito]
        return redirect(url_for("mostra_todo"))
    else:
        # Se l'utente inserisce un ID a caso nell'URL, mostriamo l'errore
        return (
            render_template(
                "errore_todo.html",
                messaggio_errore="Il task che stai cercando di eliminare non esiste.",
            ),
            404,
        )


if __name__ == "__main__":
    app.run(debug=True, port=5006)
