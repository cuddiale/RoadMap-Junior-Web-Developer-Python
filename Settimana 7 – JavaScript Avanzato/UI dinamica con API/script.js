const grid = document.getElementById("post-grid");
const btn = document.getElementById("load-btn");
const loader = document.getElementById("loader");

async function fetchAndRender() {
  // 1. Reset UI e mostriamo caricamento
  grid.innerHTML = "";
  loader.classList.remove("hidden");

  try {
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/posts?_limit=6",
    );
    if (!response.ok) throw new Error("Errore di rete");

    const posts = await response.json();

    // 2. Rendering Dinamico
    posts.forEach((post) => {
      // Creiamo la card (Giorno 2 - DOM)
      const card = document.createElement("article");
      card.classList.add("card");

      // Inseriamo il contenuto usando i dati dell'API
      card.innerHTML = `
                <h3>${post.title}</h3>
                <p>${post.body.substring(0, 100)}...</p>
                <button onclick="alert('Hai cliccato il post ${post.id}')">Leggi di più</button>
            `;

      // Aggiungiamo alla griglia
      grid.appendChild(card);
    });
  } catch (err) {
    grid.innerHTML = `<p style="color:red">Impossibile caricare i post: ${err.message}</p>`;
  } finally {
    loader.classList.add("hidden");
  }
}

// Avvia al caricamento della pagina e al click del bottone
btn.addEventListener("click", fetchAndRender);
window.addEventListener("DOMContentLoaded", fetchAndRender);
