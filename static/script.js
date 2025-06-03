document.addEventListener("DOMContentLoaded", () => {
  const todoForm = document.querySelector("form");
  const titleInput = document.getElementById("Title-todo");
  const descInput = document.getElementById("Description-todo");
  const alertBox = document.getElementById("alert-box");
  
  function showAlert(message, type = "success") {
    const alertColor = type === "success" ? "green" : "red";
    const icon = type === "success" ? "✔️" : "❌";

    alertBox.innerHTML = `
      <div style="
        background-color: ${alertColor};
        color: white;
        padding: 10px 20px;
        margin: 10px auto;
        width: fit-content;
        border-radius: 6px;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      ">
        ${icon} ${message}
      </div>
    `;

    setTimeout(() => {
      alertBox.innerHTML = "";
    }, 3000);
  }

  if (todoForm) {
    todoForm.addEventListener("submit", (e) => {
      if (!titleInput.value.trim() || !descInput.value.trim()) {
        e.preventDefault(); // stop form submission
        showAlert("Please fill out all fields", "error");
      } else {
        showAlert("Todo added successfully!", "success");
        // Let form submit naturally
      }
    });
  }
});

