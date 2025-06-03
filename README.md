<b> 📝Flask Todo App </b>

A full-stack web application built with <b>Flask, HTML, CSS, and JavaScript</b> for managing daily tasks. It supports creating, updating, and deleting todos and uses <b>SQLite</b> for data storage.

---

<b>🌟 Features</b>

- ✅ Add a new todo
- ✏️ Update existing todos
- ❌ Delete todos
- 🕓 Shows creation timestamp
- 🚨 Alerts on success and error using JavaScript
- 📦 Data stored using SQLite (with SQLAlchemy ORM)

---

<b>🛠️ Technologies Used </b>

| Category     | Tools                     |
|--------------|---------------------------|
| Backend      | Python, Flask             |
| Database     | SQLite + SQLAlchemy       |
| Frontend     | HTML, CSS, JavaScript     |
| Styling      | Custom CSS + Bootstrap 5  |

---

<b>🗂️ Project Structure</b>

flask-todo-app/
├── static/
│ ├── style.css # Custom styles
│ └── script.js # JavaScript logic
├── templates/
│ ├── base.html # Base layout for all pages
│ ├── index.html # Home page (list and add todos)
│ ├── update.html # Page to update existing todos
│ └── about.html # About the application
├── todo.db # SQLite database file (auto-generated)
├── app.py # Main Flask application
└── README.md # Project documentation

<b> ▶️ Usage </b>

- Visit the home page to add a new todo.
- View all existing todos in the list.
- Use the **Update** button to modify a todo.
- Use the **Delete** button to remove a todo.

<b>💡 What I Learned </b>

- Building a full-stack CRUD app using Flask and SQLite.
- Styling and layout using Bootstrap.
- Client-side validations and feedback with JavaScript.
- Flask routing and template inheritance.
