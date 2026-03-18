// SELEZIONE DEGLI ELEMENTI
const titolo = document.getElementById("titolo-profilo");
const bio = document.getElementById("bio-utente");
const inputNome = document.getElementById("input-nome");
const card = document.getElementById("main-card");

const btnTesto = document.getElementById("btn-cambia-testo");
const btnColore = document.getElementById("btn-cambia-colore");
const btnReset = document.getElementById("btn-reset");

// Funzione per cambiare il testo usando il valore dell'input
btnTesto.addEventListener("click", function () {
  const nuovoNome = inputNome.value;

  if (nuovoNome !== "") {
    titolo.innerText = nuovoNome; // Giorno 2: Modifica testo
    bio.innerHTML = "Hai appena cambiato il nome in <b>" + nuovoNome + "</b>!"; // Giorno 2: innerHTML
  } else {
    alert("Inserisci un nome nell'input!");
  }
});

// Funzione per cambiare il colore (Stile)
btnColore.addEventListener("click", function () {
  titolo.style.color = "#28a745";
  card.style.borderColor = "#28a745";
  card.style.borderWidth = "2px";
  card.style.borderStyle = "solid";
  card.style.backgroundColor = "#e8f5e9";
});

// Funzione di Reset per tornare allo stato iniziale
btnReset.addEventListener("click", function () {
  titolo.innerText = "Il Mio Profilo";
  titolo.style.color = "#333";
  bio.innerText =
    "Questa è la mia biografia iniziale. Clicca i bottoni per cambiarmi!";
  card.style.backgroundColor = "white";
  card.style.border = "none";
  inputNome.value = ""; // Svuota l'input
});
