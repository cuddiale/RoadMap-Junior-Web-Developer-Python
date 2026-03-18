const btnLoad = document.getElementById("load-users");
const userList = document.getElementById("user-list");
const loader = document.getElementById("loader");

btnLoad.addEventListener("click", () => {
  // Mostriamo il loader e puliamo la lista precedente
  loader.classList.remove("hidden");
  userList.innerHTML = "";

  // 1. Chiamata all'API (GET è il metodo predefinito)
  fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => {
      // Controlliamo se la risposta è andata a buon fine (status 200)
      if (!response.ok) {
        throw new Error("Errore nel recupero dati");
      }
      return response.json(); // Convertiamo il flusso di dati in JSON (Giorno 1)
    })
    .then((data) => {
      // 2. Manipoliamo i dati ricevuti (data è un Array di oggetti)
      data.forEach((user) => {
        const li = document.createElement("li");
        li.innerHTML = `<strong>${user.name}</strong> - 📧 ${user.email}`;
        userList.appendChild(li);
      });
    })
    .catch((error) => {
      // 3. Gestione errori (es. niente internet o server offline)
      console.error("Errore:", error);
      userList.innerHTML = "<li>Impossibile caricare gli utenti.</li>";
    })
    .finally(() => {
      // Nascondiamo il loader a prescindere dal risultato
      loader.classList.add("hidden");
    });
});
