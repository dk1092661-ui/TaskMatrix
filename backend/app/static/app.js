const activeTasks = document.getElementById("active-tasks");
const activeCount = document.getElementById("active-count");

function updateCounters() {
  activeCount.innerText = activeTasks.children.length;
}

function addTask() {
  const input = document.getElementById("taskInput");
  if (input.value.trim() === "") return;

  const li = document.createElement("li");

  li.innerHTML = `
    <span onclick="completeTask(this)">${input.value}</span>
    <button class="delete" onclick="deleteTask(this)">✖</button>
  `;

  activeTasks.appendChild(li);
  input.value = "";
  updateCounters();
}

function deleteTask(btn) {
  btn.parentElement.remove();
  updateCounters();
}

function completeTask(span) {
  span.parentElement.remove();
  updateCounters();
}

/* ===== DARK MODE TOGGLE ===== */

function toggleMode() {
  document.body.classList.toggle("dark");

  if (document.body.classList.contains("dark")) {
    localStorage.setItem("mode", "dark");
  } else {
    localStorage.setItem("mode", "light");
  }
}

if (localStorage.getItem("mode") === "dark") {
  document.body.classList.add("dark");
}

updateCounters();
