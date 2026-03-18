const loginForm = document.getElementById("login-form");
const passwordInput = document.getElementById("password");
const statusBox = document.getElementById("status-box");
const statusText = document.getElementById("status-text");
const submitBtn = document.getElementById("submit-btn");

loginForm.addEventListener("submit", function (event) {
  event.preventDefault(); // Blocca ricaricamento

  const pswValue = passwordInput.value;

  // 1. Logica di Validazione (Giorno 4)
  if (pswValue.length < 6) {
    // FEEDBACK DI ERRORE DINAMICO (Giorno 5)
    mostraFeedback("Password troppo corta! Riprova.", "error");
    passwordInput.style.borderColor = "#e74c3c";
  } else if (pswValue === "123456") {
    // ALERT (Messaggio di sistema per eventi critici)
    alert("⚠️ Attenzione: Questa password è troppo comune! Scegline un'altra.");
    mostraFeedback("Password non sicura.", "error");
  } else {
    // FEEDBACK DI SUCCESSO & UX
    mostraFeedback("Accesso in corso...", "success");
    submitBtn.disabled = true; // Impedisce doppi click (Buona UX)
    submitBtn.innerText = "Caricamento...";

    // Simuliamo un caricamento di 2 secondi
    setTimeout(() => {
      alert("✅ Accesso autorizzato!");
      window.location.reload(); // Reset finale
    }, 2000);
  }
});

// Funzione riutilizzabile per messaggi dinamici
function mostraFeedback(messaggio, tipo) {
  statusBox.className = tipo; // Assegna classe 'success' o 'error'
  statusText.innerText = messaggio;
}
