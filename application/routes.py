from application import app
from flask import render_template
@app.route("/")
@app.route("/index")
def index():
   return render_template("index.html",login = True)
@app.route("/classes")
def classes():
   return render_template("classes.html",login = True)
@app.route("/register")
def register():
   return render_template("register.html",login = True)
@app.route("/login")
def login():
   return render_template("login.html",login = True)

