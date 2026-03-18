const btn = document.getElementById("btn-fetch");
const list = document.getElementById("list");
const loader = document.getElementById("loading");

// 1. Dichiariamo la funzione come ASYNC
async function prendiUtenti() {
  // Reset interfaccia
  list.innerHTML = "";
  loader.classList.remove("hidden");

  // 2. Usiamo TRY per il blocco di codice principale
  try {
    // AWAIT ferma l'esecuzione finché la fetch non risponde
    const risposta = await fetch("https://jsonplaceholder.typicode.com/users");

    // Controllo manuale dello stato HTTP
    if (!risposta.ok) {
      throw new Error("Errore nel server: " + risposta.status);
    }

    // AWAIT anche per la conversione in JSON (che è una promessa!)
    const utenti = await risposta.json();

    // 3. Ciclo sui dati (qui è codice JS standard)
    utenti.forEach((u) => {
      const li = document.createElement("li");
      li.textContent = `${u.name} (@${u.username})`;
      list.appendChild(li);
    });
  } catch (errore) {
    // 4. CATCH gestisce qualsiasi errore avvenuto nel blocco try
    console.error("Si è verificato un problema:", errore);
    list.innerHTML = `<li style="color:red">Errore: ${errore.message}</li>`;
  } finally {
    // Viene eseguito sempre, successo o fallimento
    loader.classList.add("hidden");
  }
}

// Colleghiamo la funzione al click
btn.addEventListener("click", prendiUtenti);
