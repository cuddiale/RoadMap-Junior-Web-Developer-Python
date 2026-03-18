let saldoAttuale = 500;

const inputPrelievo = document.getElementById("prelievo");
const btnPreleva = document.getElementById("btn-preleva");
const feedback = document.getElementById("feedback");
const displaySaldo = document.getElementById("saldo");

btnPreleva.addEventListener("click", () => {
  // Reset feedback
  feedback.className = "hidden";

  try {
    const valore = parseFloat(inputPrelievo.value);

    // 1. Errore: Input non valido (NaN o vuoto)
    if (isNaN(valore) || valore <= 0) {
      throw new Error("Inserisci un importo valido superiore a 0.");
    }

    // 2. Errore: Fondi insufficienti
    if (valore > saldoAttuale) {
      throw new Error(
        "Saldo insufficienti! Non puoi prelevare più di " + saldoAttuale + "€.",
      );
    }

    // 3. Simulazione Errore di Rete (casuale 20% delle volte)
    if (Math.random() < 0.2) {
      throw new Error("Errore di comunicazione con la banca. Riprova.");
    }

    // SE TUTTO VA BENE:
    saldoAttuale -= valore;
    displaySaldo.innerText = saldoAttuale;
    mostraMessaggio("Prelievo di " + valore + "€ eseguito!", "success");
  } catch (errore) {
    // Il blocco catch "acchiappa" qualsiasi errore lanciato con throw
    mostraMessaggio(errore.message, "error");
  } finally {
    // Puliamo l'input a prescindere dal risultato
    inputPrelievo.value = "";
  }
});

function mostraMessaggio(testo, classe) {
  feedback.innerText = testo;
  feedback.className = classe;
}
