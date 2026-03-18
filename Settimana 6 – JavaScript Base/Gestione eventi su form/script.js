// --- SELEZIONE ELEMENTI ---
const formIscrizione = document.getElementById("form-squadra");
const inputSquadra = document.getElementById("nome-squadra");
const feedbackForm = document.getElementById("messaggio-form");

const btnContatore = document.getElementById("btn-click");
const displayContatore = document.getElementById("valore-contatore");

// --- STATO DELL'APPLICAZIONE ---
let clickCount = 0; // Usiamo let perché il valore cambierà

// --- 1. EVENTO CLICK (Contatore) ---
btnContatore.addEventListener("click", function () {
  clickCount++; // Incremento
  displayContatore.innerText = clickCount; // Aggiornamento DOM

  // Logica extra: cambia colore ogni 5 click
  if (clickCount % 5 === 0) {
    displayContatore.style.color = "red";
  } else {
    displayContatore.style.color = "#e67e22";
  }
});

// --- 2. EVENTO SUBMIT (Gestione Form) ---
formIscrizione.addEventListener("submit", function (event) {
  // FONDAMENTALE: Impedisce il ricaricamento della pagina
  event.preventDefault();

  const nome = inputSquadra.value; // Recupero il valore dell'input

  // Mostro un feedback all'utente
  feedbackForm.innerText = "Squadra '" + nome + "' iscritta con successo!";
  feedbackForm.style.color = "green";

  // Pulisco il campo di input per un nuovo inserimento
  formIscrizione.reset();
});
