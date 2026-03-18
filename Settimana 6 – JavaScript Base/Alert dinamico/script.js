function creaAlert(messaggio, tipo) {
  // 1. Selezioniamo il contenitore
  const container = document.getElementById("alert-container");

  // 2. Creiamo un nuovo elemento div (Giorno 2 avanzato)
  const nuovoAlert = document.createElement("div");

  // 3. Aggiungiamo le classi per lo stile
  nuovoAlert.classList.add("custom-alert", tipo);

  // 4. Inseriamo il testo
  nuovoAlert.innerText = messaggio;

  // 5. Lo aggiungiamo al contenitore nel DOM
  container.appendChild(nuovoAlert);

  // 6. LOGICA DI RIMOZIONE AUTOMATICA (UX Giorno 5)
  // Dopo 3 secondi aggiungiamo l'effetto scomparsa
  setTimeout(() => {
    nuovoAlert.classList.add("fade-out");

    // Dopo che l'animazione finisce (0.5s), rimuoviamo l'elemento dal DOM
    setTimeout(() => {
      nuovoAlert.remove();
    }, 500);
  }, 3000);
}
