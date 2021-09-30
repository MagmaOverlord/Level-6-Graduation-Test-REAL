#github: 

from flask import Flask, render_template, request, session

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

@app.route("/", methods=["GET", "POST"])
def index():
    if "username" in session:
        return render_template("index.html", username = session["username"])
    else:
        redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return
    else:
        return render_template("register.html")

if __name__ == "__main__":
    app.run("localhost", 8080)