const API_URL = "https://jsonplaceholder.typicode.com/users";
const contactForm = document.getElementById("contact-form");
const contactList = document.getElementById("contact-list");
const loader = document.getElementById("loader");

// --- 1. READ (Lettura) ---
async function fetchContacts() {
  loader.classList.remove("hidden");
  try {
    const response = await fetch(API_URL);
    const contacts = await response.json();
    renderContacts(contacts);
  } catch (error) {
    console.error("Errore nel caricamento:", error);
  } finally {
    loader.classList.add("hidden");
  }
}

function renderContacts(contacts) {
  contactList.innerHTML = "";
  contacts.forEach((contact) => {
    addContactToDOM(contact);
  });
}

// Funzione helper per creare l'HTML di un singolo contatto
function addContactToDOM(contact) {
  const card = document.createElement("div");
  card.classList.add("contact-card");
  card.setAttribute("data-id", contact.id);

  card.innerHTML = `
        <div class="contact-info">
            <h4>${contact.name}</h4>
            <p>${contact.email}</p>
        </div>
        <button class="delete-btn" onclick="deleteContact(${contact.id})">Elimina</button>
    `;
  contactList.prepend(card); // Aggiunge in cima
}

// --- 2. CREATE (Creazione) ---
contactForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const newContact = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
  };

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      body: JSON.stringify(newContact),
      headers: { "Content-type": "application/json; charset=UTF-8" },
    });
    const data = await response.json();

    // Aggiorniamo la UI senza ricaricare tutto (Ottimistico)
    addContactToDOM(data);
    contactForm.reset();
    alert("Contatto creato (simulazione)!");
  } catch (error) {
    alert("Errore nella creazione");
  }
});

// --- 3. DELETE (Cancellazione) ---
async function deleteContact(id) {
  if (!confirm("Sei sicuro di voler eliminare questo contatto?")) return;

  try {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });

    // Rimuoviamo l'elemento dal DOM
    const elementToRemove = document.querySelector(`[data-id="${id}"]`);
    elementToRemove.remove();
    console.log(`Contatto ${id} eliminato.`);
  } catch (error) {
    alert("Errore durante l'eliminazione");
  }
}

// --- 4. UPDATE (Aggiornamento - Esempio logico) ---
// In un CRUD completo, qui aggiungeresti un tasto "Modifica" che apre un form
// e invia una fetch con metodo "PUT" o "PATCH".

// Caricamento iniziale
fetchContacts();
