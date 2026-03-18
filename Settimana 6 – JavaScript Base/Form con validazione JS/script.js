const form = document.getElementById("registro-form");
const username = document.getElementById("username");
const email = document.getElementById("email");

// Elementi per i messaggi
const errorUser = document.getElementById("error-username");
const errorEmail = document.getElementById("error-email");
const successMsg = document.getElementById("success-msg");

form.addEventListener("submit", function (event) {
  // 1. BLOCCA l'invio automatico (Giorno 4 - Argomento 1)
  event.preventDefault();

  // Reset messaggi e stili ad ogni tentativo
  let isValid = true;
  errorUser.innerText = "";
  errorEmail.innerText = "";
  username.classList.remove("input-error");
  email.classList.remove("input-error");
  successMsg.innerText = "";

  // 2. CONTROLLO INPUT (Giorno 4 - Argomento 2)

  // Validazione Username
  if (username.value.trim().length < 3) {
    errorUser.innerText = "Lo username deve avere almeno 3 caratteri.";
    username.classList.add("input-error");
    isValid = false;
  }

  // Validazione Email (controllo campo vuoto e presenza @)
  if (email.value.trim() === "") {
    errorEmail.innerText = "L'email è obbligatoria.";
    email.classList.add("input-error");
    isValid = false;
  } else if (!email.value.includes("@")) {
    errorEmail.innerText = "Inserisci un'email valida (manca @).";
    email.classList.add("input-error");
    isValid = false;
  }

  // 3. MESSAGGIO FINALE (Giorno 4 - Argomento 3)
  if (isValid) {
    successMsg.innerText = "Registrazione completata con successo! ✅";
    form.reset(); // Pulisce i campi
  }
});
