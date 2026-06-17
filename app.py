import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from database import get_db

app = Flask(__name__)
app.secret_key = "dev-secret-change-this"  # needed for flash() and, soon, login sessions


# A "route" maps a URL to a Python function.
# @app.route("/") means: when someone visits the homepage, run index() below.
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # GET = just show the empty form. POST = the form was submitted, process it.
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        # Never store the raw password - store a one-way hash of it instead.
        hashed_password = generate_password_hash(password)

        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (name, email, password, role, approved) "
                "VALUES (?, ?, ?, 'user', 0)",
                (name, email, hashed_password)
            )
            db.commit()
            flash("Registration submitted! An admin needs to approve your account before you can log in.")
            return redirect(url_for("index"))
        except sqlite3.IntegrityError:
            # This fires because of the UNIQUE constraint on email in schema.sql
            flash("That email is already registered.")
        finally:
            db.close()

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)