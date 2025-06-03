

from flask import Flask, render_template, request, redirect
# Importing core Flask class and functions for rendering HTML templates,
# accessing form/request data, and redirecting after POST requests.

from flask_sqlalchemy import SQLAlchemy
# Importing SQLAlchemy, a Flask extension to interact with databases easily.

from datetime import datetime
# Importing datetime module to handle timestamps when todos are created.

import os
# Importing os module to handle file paths (helps in creating DB path).


app = Flask(__name__)


# Getting absolute directory path of this current file (helps in making DB path OS independent)
basedir = os.path.abspath(os.path.dirname(__file__))

# Configuering the app's SQLAlchemy database URI to use a SQLite database file named 'todo.db' in the current directory.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "todo.db")

# Disable tracking modifications of objects to save resources (recommended setting).
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize the database object with your Flask app
db = SQLAlchemy(app)


# Define the database model/table structure for Todo items.
class Todo(db.Model):
    S_NUM = db.Column(db.Integer, primary_key=True)
    # S_NUM is the primary key column (unique identifier) for each todo, auto-incrementing integer.

    Title = db.Column(db.String(100), nullable=False)
    # Title column is a string of max length 100 and cannot be empty (nullable=False).

    Description = db.Column(db.String(200), nullable=False)
    # Description column is a string max length 200 and required.

    DateCreated = db.Column(db.DateTime, default=datetime.utcnow)
    # DateCreated column stores when the todo was created, default is current UTC time.

    def __repr__(self):
        # This function defines how each Todo object is printed/debugged.
        return f"{self.S_NUM} - {self.Title}"


@app.route('/', methods=['GET', 'POST'])
# Define the root route '/' that accepts both GET and POST HTTP methods.
def HomePage():
    if request.method == 'POST':
        # When the form is submitted via POST (new todo added):
        title = request.form['title']
        # Get the 'title' field from the submitted form.

        Descrip = request.form['Descrip']
        # Get the 'Descrip' (description) field from the form.

        todo = Todo(Title=title, Description=Descrip)
        # Create a new Todo object with the submitted title and description.

        db.session.add(todo)
        # Add the new todo object to the current database session (staging area).

        db.session.commit()
        # Commit the session to save changes permanently in the database.

    AllTodo = Todo.query.all()
    # Query all Todo records from the database to display on the page.

    return render_template('index.html', AllTodo=AllTodo, now=datetime.now())
    # Render the index.html template, passing the todo list and current time.


@app.route('/home')
def home():
    # Route for '/home' page, rendering the homepage template.
    return render_template('index.html', now=datetime.now())
    # Render 'index.html' with current time.


@app.route('/about')
def about():
    # Route for '/about' page, rendering an about template.
    return render_template('about.html', now=datetime.now())
    # Render 'about.html' with current time (make sure you create this template).


@app.route('/update/<int:SNo>', methods=['GET', 'POST'])
def Update(SNo):
    # Route for updating a todo by its unique S_NUM id passed in the URL.
    todo = Todo.query.filter_by(S_NUM=SNo).first()
    # Query the todo record from DB matching the given S_NUM.

    if request.method == 'POST':
        # If form is submitted for update:
        title = request.form['title']
        Descrip = request.form['Descrip']
        # Get updated title and description from form fields.

        todo.Title = title
        todo.Description = Descrip
        # Update the todo object's attributes with new values.

        db.session.commit()
        # Commit changes to the database.

        return redirect("/")
        # Redirect to homepage after update to show updated list.

    # For GET request, render the update.html page with current todo data.
    return render_template('update.html', todo=todo, now=datetime.now())


@app.route('/delete/<int:SNo>')
def delete(SNo):
    # Route to delete a todo identified by its S_NUM.
    todo = Todo.query.filter_by(S_NUM=SNo).first()
    # Find the todo in the database.

    if todo:
        # If todo exists:
        db.session.delete(todo)
        # Delete the todo object from the session.

        db.session.commit()
        # Commit deletion to the database.

    return redirect("/")
    # Redirect to homepage after deletion.


if __name__ == '__main__':
    # This block runs only when you run this script directly (not on import).

    with app.app_context():
        # Create the database tables within the Flask app context.
        db.create_all()
        print("✅ Database created or already exists.")

    app.run(debug=True)
    # Run the Flask app with debug mode ON (helps during development).

