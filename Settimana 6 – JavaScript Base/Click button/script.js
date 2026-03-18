// 1. SELEZIONE DEGLI ELEMENTI (Giorno 2)
const display = document.getElementById("display-n");
const btnAdd = document.getElementById("btn-add");
const btnReset = document.getElementById("btn-reset");

// 2. STATO (La memoria del programma)
// Usiamo let perché il valore deve cambiare
let conteggio = 0;

// 3. LOGICA DI INCREMENTO (Giorno 3)
btnAdd.addEventListener("click", function () {
  conteggio++; // Aumenta di 1
  display.innerText = conteggio; // Aggiorna l'HTML (Giorno 2)

  // Feedback visivo extra: cambia colore se superi i 10 click
  if (conteggio >= 10) {
    display.style.color = "#e67e22";
  }
});

// 4. LOGICA DI RESET
btnReset.addEventListener("click", function () {
  conteggio = 0; // Torna a zero in memoria
  display.innerText = conteggio; // Aggiorna l'HTML
  display.style.color = "#2c3e50"; // Ripristina il colore originale

  // Feedback con Alert (Giorno 5)
  console.log("Il contatore è stato resettato.");
});
