const postForm = document.getElementById("post-form");
const responseMsg = document.getElementById("response-msg");
const submitBtn = document.getElementById("submit-btn");

postForm.addEventListener("submit", (event) => {
  event.preventDefault(); // Giorno 4 del blocco precedente!

  // Cambiamo stato al bottone (UX Giorno 5)
  submitBtn.innerText = "Inviando...";
  submitBtn.disabled = true;

  // Recuperiamo i dati dal form
  const nuovoPost = {
    title: document.getElementById("title").value,
    body: document.getElementById("body").value,
    userId: 1, // Dato richiesto dall'API finta
  };

  // INVIO DATI (Giorno 3 - POST)
  fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST", // Specifichiamo il metodo
    headers: {
      "Content-type": "application/json; charset=UTF-8", // Fondamentale!
    },
    body: JSON.stringify(nuovoPost), // Convertiamo l'oggetto in stringa JSON
  })
    .then((response) => {
      if (!response.ok) throw new Error("Errore nell'invio");
      return response.json();
    })
    .then((data) => {
      // L'API ci restituisce l'oggetto creato con un ID (es. 101)
      console.log("Risposta del server:", data);

      responseMsg.innerHTML = `✅ Post creato con successo!<br>ID assegnato: ${data.id}`;
      responseMsg.className = "success";
      postForm.reset(); // Puliamo il form
    })
    .catch((error) => {
      console.error("Errore:", error);
      responseMsg.innerText = "❌ Errore durante l'invio.";
      responseMsg.style.color = "red";
    })
    .finally(() => {
      submitBtn.innerText = "Pubblica Post";
      submitBtn.disabled = false;
      responseMsg.classList.remove("hidden");
    });
});
