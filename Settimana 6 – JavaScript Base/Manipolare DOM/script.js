// 1. SELEZIONE ELEMENTI
const inputNome = document.getElementById("in-nome");
const inputRuolo = document.getElementById("in-ruolo");
const btnUpdate = document.getElementById("btn-update");

const outputNome = document.getElementById("out-nome");
const outputRuolo = document.getElementById("out-ruolo");
const cardBox = document.getElementById("card-box");

const colorButtons = document.querySelectorAll(".dot");

// 2. AGGIORNA TESTO AL CLICK
btnUpdate.addEventListener("click", function () {
  // Se l'input è vuoto, usa un valore di default
  outputNome.innerText = inputNome.value || "Nome Esempio";
  outputRuolo.innerText = inputRuolo.value || "Professione";

  // Piccolo feedback visivo: una mini animazione di "scossa"
  cardBox.style.transform = "scale(1.05)";
  setTimeout(() => (cardBox.style.transform = "scale(1)"), 200);
});

// 3. CAMBIO COLORE DINAMICO (Giorno 2 + Giorno 3)
// Usiamo un ciclo per aggiungere l'evento a tutti i bottoni colorati
colorButtons.forEach((button) => {
  button.addEventListener("click", function () {
    const coloreScelto = this.getAttribute("data-color");
    cardBox.style.backgroundColor = coloreScelto;
  });
});
