#github: https://github.com/MagmaOverlord/Level-6-Graduation-Test-REAL

from flask import Flask, render_template, request, session, redirect

import mysql.connector

app = Flask(__name__)

app.secret_key = "sadklhjbgf lkaherbg likj"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="greatkid5000",
    database="sys"
)

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50) UNIQUE NOT NULL, password VARCHAR(50) NOT NULL)")
db.commit()

@app.route("/")
def index():
    if "username" in session:
        return render_template("index.html", username = session["username"])
    else:
        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        sql = "SELECT username FROM users WHERE username = %s AND password = %s"
        value = (username, password)
        cursor.execute(sql, value)
        result = cursor.fetchall()
        if len(result) == 0:
            return render_template("login.html", message = "Username or password is incorrect")
        else:
            session["username"] == username
            return redirect("/")
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirm-password")
        sql = "SELECT username FROM users WHERE username = %s"
        value = (username,)
        cursor.execute(sql, value)
        result = cursor.fetchall()
        if len(result) > 0:
            return render_template("register.html", message = "Username is already in use")
        elif len(password) == 0:
            return render_template("register.html", message = "Your password needs to exist")
        elif len(username) == 0:
            return render_template("register.html", message = "You need a username")
        elif confirmPassword != password:
            return render_template("register.html", message = "Passwords do not match")
        else:
            sql = "INSERT INTO users(username, password) VALUES(%s, %s)"
            value = (username, password)
            cursor.execute(sql, value)
            db.commit()
            session["username"] = username
            return redirect("/")
    else:
        return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run("localhost", 8080)