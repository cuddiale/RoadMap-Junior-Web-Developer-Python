// 1. SELEZIONE
const btnMsg = document.getElementById("btn-toggle-msg");
const secretMsg = document.getElementById("secret-msg");

const btnTheme = document.getElementById("btn-theme");
const body = document.body; // Seleziona direttamente il tag <body>

// 2. LOGICA MOSTRA/NASCONDI
btnMsg.addEventListener("click", function () {
  // toggle() aggiunge/rimuove la classe 'hidden' ad ogni click
  secretMsg.classList.toggle("hidden");

  // Cambiamo il testo del bottone per migliorare la UX
  if (secretMsg.classList.contains("hidden")) {
    btnMsg.innerText = "Mostra Messaggio";
  } else {
    btnMsg.innerText = "Nascondi Messaggio";
  }
});

// 3. LOGICA GIORNO/NOTTE
btnTheme.addEventListener("click", function () {
  // Scambiamo le classi del tema sul body
  body.classList.toggle("dark-theme");
  body.classList.toggle("light-theme");

  // Cambiamo l'icona e il testo del bottone
  if (body.classList.contains("dark-theme")) {
    btnTheme.innerText = "Attiva Modalità Giorno ☀️";
  } else {
    btnTheme.innerText = "Attiva Modalità Notte 🌙";
  }
});
