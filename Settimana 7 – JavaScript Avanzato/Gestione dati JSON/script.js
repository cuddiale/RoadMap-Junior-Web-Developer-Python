// SELEZIONE
const inputNome = document.getElementById("prod-nome");
const inputPrezzo = document.getElementById("prod-prezzo");
const btnSave = document.getElementById("btn-save");

const jsonOutput = document.getElementById("json-output");
const objOutput = document.getElementById("obj-output");

btnSave.addEventListener("click", () => {
  // --- STEP 1: Creiamo un oggetto JS normale ---
  const prodotto = {
    nome: inputNome.value,
    prezzo: Number(inputPrezzo.value),
    disponibile: true,
    dataSalvataggio: new Date().toLocaleDateString(),
  };

  // --- STEP 2: JSON.stringify() ---
  // Trasformiamo l'oggetto in una stringa di testo (formato JSON)
  const stringaDati = JSON.stringify(prodotto);
  jsonOutput.innerText = stringaDati;

  // --- STEP 3: JSON.parse() ---
  // Fingiamo di aver ricevuto 'stringaDati' da un server e vogliamo leggerla
  const datiLetti = JSON.parse(stringaDati);

  // Mostriamo i dati nel DOM accedendo alle proprietà dell'oggetto ricostruito
  objOutput.innerHTML = `
        <p><strong>Prodotto:</strong> ${datiLetti.nome}</p>
        <p><strong>Prezzo:</strong> €${datiLetti.prezzo}</p>
        <p><strong>Data:</strong> ${datiLetti.dataSalvataggio}</p>
    `;

  console.log("Oggetto originale:", prodotto);
  console.log("Stringa JSON:", stringaDati);
  console.log("Oggetto dopo il Parse:", datiLetti);
});
