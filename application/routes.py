from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from application.models import User,Account
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


@app.route('/customer_search',methods=['POST','GET'])
def customer_search():
        if not session.get('username'):
            return redirect(url_for('login'))
        form = CustomerSearch()
        if form.validate_on_submit():
            customer_ssn_id = form.customer_id.data
            viewCustomer = User.objects(customer_ssn_id = customer_ssn_id)
            if viewCustomer:
                flash("Redirecting to customer details","success")
                return render_template('customer_data_view.html',viewCustomer=viewCustomer)
            else:
                flash("Oops!!No such customer exist!","danger")
                return redirect(url_for('index'))
        return render_template('customer_search.html', form = form,title = "Search Customer ")
@app.route('/delete_account',methods=['GET','POST'])
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
    
    try:
        if not session.get('username'):
            return redirect(url_for('login'))

        user = User.objects.all()
        return render_template("updatecustomer.html", user=user)
    except Exception as ex:
        print(ex)  
@app.route('/delete_customer',methods=['POST','GET'])
def delete_customer():
    if not session.get('username'):
        return redirect(url_for('login'))
    if request.method == "POST":

       id = request.form['customerid']
       if User.objects(customer_ssn_id=id).delete():
            flash("User Deleted successfully","success")
            return redirect (url_for('index'))
       else:
            flash("Oops!No such user exist!!","danger")
            return redirect(url_for('index'))
    return render_template("delete_customer.html")
@app.route('/create_account',methods=['POST','GET'])
def create_account():

        if not session.get('username'):
          return redirect(url_for('login'))
        if request.method == "POST":
    
            customer_id = request.form["CustomerId"]
            account_id = request.form['AccountId']
            account_type    = request.form["Account"]
            deposit_amount  = request.form["DepositAmount"]
            temp = User.objects(customer_ssn_id=customer_id)
            if temp:
                account = Account(account_id=account_id,customer_ssn_id=customer_id, account_type=account_type, deposit_amount= deposit_amount)
                account.save()
                flash("You are successfully registered!","success")
                return redirect(url_for('index'))
            else:
                flash("Oops!!No such customer exist!!Register first","danger")
                return redirect(url_for('register'))
                
        return render_template("acccountcreate.html")
        
@app.route('/editcustomer', methods=['GET','POST'])
def editcustomer():
    try:
        customer_ssn_id = request.args.get('customer_ssn_id')
        edituser = User.objects(customer_ssn_id = customer_ssn_id)
        return render_template('EditCustomer.html', edituser=edituser)
    except Exception as ex:
        print(ex)


@app.route('/updatecust', methods=['POST'])
def updatecust():
    id = request.form['customer_ssn_id']

    User.objects(customer_ssn_id=id).update(set__customer_Address = request.form['customer_Address'], set__customer_name=request.form['customer_name'], set__customer_age=request.form['customer_age'])
    
    return render_template('index.html')






      