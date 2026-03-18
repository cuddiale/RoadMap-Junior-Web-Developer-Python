// --- SELEZIONE ---
const scoreDisplay = document.getElementById("score");
const timerDisplay = document.getElementById("timer");
const startBtn = document.getElementById("start-btn");
const gameArea = document.getElementById("game-area");
const target = document.getElementById("target");

// --- STATO DEL GIOCO ---
let score = 0;
let timeLeft = 10;
let gameActive = false;

// --- FUNZIONE PER MUOVERE IL BERSAGLIO ---
function moveTarget() {
  // Calcoliamo posizioni casuali basate sulla grandezza dell'area di gioco
  const maxX = gameArea.clientWidth - 50;
  const maxY = gameArea.clientHeight - 50;

  const randomX = Math.floor(Math.random() * maxX);
  const randomY = Math.floor(Math.random() * maxY);

  target.style.left = randomX + "px";
  target.style.top = randomY + "px";

  // Cambiamo colore casualmente per renderlo più carino
  const colors = ["#e74c3c", "#f1c40f", "#9b59b6", "#3498db"];
  target.style.backgroundColor =
    colors[Math.floor(Math.random() * colors.length)];
}

// --- LOGICA DI GIOCO ---
startBtn.addEventListener("click", () => {
  if (gameActive) return; // Impedisce di riavviare se già in corso

  // Reset valori
  score = 0;
  timeLeft = 10;
  gameActive = true;
  scoreDisplay.innerText = score;
  timerDisplay.innerText = timeLeft;
  startBtn.style.display = "none";
  target.classList.remove("hidden");

  moveTarget();

  // Timer decrescente
  const countdown = setInterval(() => {
    timeLeft--;
    timerDisplay.innerText = timeLeft;

    if (timeLeft <= 0) {
      clearInterval(countdown);
      endGame();
    }
  }, 1000);
});

// Click sul bersaglio
target.addEventListener("click", () => {
  if (!gameActive) return;
  score++;
  scoreDisplay.innerText = score;
  moveTarget(); // Si sposta ogni volta che lo colpisci
});

function endGame() {
  gameActive = false;
  target.classList.add("hidden");
  startBtn.style.display = "inline-block";
  startBtn.innerText = "Riprova";
  alert("Tempo scaduto! Il tuo punteggio finale è: " + score);
}
