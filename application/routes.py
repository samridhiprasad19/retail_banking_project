from application import app
from flask import render_template,request,redirect
from application.forms import LoginForm, RegisterForm
@app.route("/")
@app.route("/index")
def index():
   return render_template("index.html",index = True)
@app.route("/courses/")
@app.route("/courses/<term>")   
def courses(term ='Spring 2019'): #url_variables
    courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]
    return render_template("courses.html",courseData=courseData,courses = True,Term = term)
    
@app.route("/register")
def register():
   return render_template("register.html",register = True)
@app.route("/login",methods =['GET','POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
    flash("You are sucessfully logged in!!")
    return redirect('/index')
   return render_template("login.html",form = form,title = "Login",login = True)
@app.route("/enrollment")
def enrollment():
    id1 = request.args.get('courseID')
    title = request.args.get('title')
    term = request.args.get('term')
    return render_template("enrollment.html",enrollment = True,data = {"id":id1,"title":title,"term":term})
