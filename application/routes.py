from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from application.models import User, Course, Enrollment
from application.forms import LoginForm, RegisterForm,CustomerSearch,AccountSearch


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True )

@app.route("/login", methods=['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data

        user = User.objects(customer_ssn_id=email).first()
        if user and user.get_password(password):
            flash(f"{user.customer_name}, you are successfully logged in!", "success")
            session['user_id'] = user.customer_ssn_id
            session['username'] = user.customer_name
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True )

@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('username',None)
    return redirect(url_for('index'))

@app.route("/account_search")
def account_search():
    if not session.get('username'):
        return redirect(url_for('login'))

    form = AccountSearch()
    return render_template("account_search.html",  account_search = True,form =form )

@app.route("/register", methods=['POST','GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        customer_ssn_id =form.customer_ssn_id.data
        password    = form.password.data
        customer_name  = form.customer_name.data
        customer_Address   = form.customer_Address.data
        customer_age  = form.customer_age.data
        customer_state   = form.customer_state.data
        customer_city   = form.customer_city.data
        user = User(customer_ssn_id=customer_ssn_id, customer_name=customer_name, customer_Address=customer_Address, customer_age=customer_age,customer_state=customer_state,customer_city=customer_city)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)


@app.route('/customer_search')
def customer_search():
    
    if not session.get('username'):
        return redirect(url_for('login'))

    form = CustomerSearch()
    return render_template("customer_search.html",form = form,title = "Search Customer ")
@app.route('/delete_account')
def delete_account():
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template("delete_account.html")
@app.route('/deposit_money')
def deposit_money():
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template("deposit_money.html")
@app.route('/account_status')
def account_status():
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template("account_status.html")
@app.route('/customer_status')
def customer_status():
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template("customer_status.html")
@app.route('/withdraw_money')
def withdraw_money():
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template("withdraw_money.html")
@app.route('/accountstatement')
def accountstatement():
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template("accountstatement.html")
@app.route('/updatecustomer')
def updatecustomer():
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template("updatecustomer.html")
@app.route('/delete_customer')
def delete_customer():
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template("delete_customer.html")






@app.route("/user")
def user():
     #User(user_id=1, first_name="Christian", last_name="Hur", email="christian@uta.com", password="abc1234").save()
     #User(user_id=2, first_name="Mary", last_name="Jane", email="mary.jane@uta.com", password="password123").save()
     users = User.objects.all()
     return render_template("user.html", users=users)