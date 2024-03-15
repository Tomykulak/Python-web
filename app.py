import jinja2
from flask import Flask, render_template, request, flash, redirect, url_for, session

import hashlib
import auth
import forms

from service.user_service import UserService
from service.phone_service import PhoneService


from database import database

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object('config')
database.init_app(app)


#Default home page
@app.route("/")
def index():
    return render_template("index.jinja")

#LIST OF LINKS BELOW
@app.route("/about")
def about():
    return render_template("about.jinja")

@app.route("/how-it-works")
def how_it_works():
    return render_template("how_it_works.jinja")

@app.route("/join-us")
def join_us():
    return render_template("join_us.jinja")

#vypis zamestnancu
@app.route("/employees")
@auth.login_required
@auth.roles_required("Admin")
def employees():
    employees = UserService.getAllEmployees()
    return render_template("employees.jinja", employees = employees)

@app.route("/customers")
@auth.login_required
@auth.roles_required("Admin")
def customers():
    customers = UserService.getAllCustomers()

    app.jinja_env.globals.update(updateUserActivity=UserService.updateUserActivity)

    return render_template("customers.jinja", customers = customers)

@app.route("/shop", methods = ["GET", "POST"])
@auth.login_required
@auth.roles_required("Admin", "Employee", "Customer")
def shop():
    #phones = PhoneService.get_all()
    phones = PhoneService.get_product_price()
    phone_id = request.args.get("phone_id", None, int)
    if phone_id is not None:
        session['cart'] = session['cart'] + [phone_id]
        flash("Phone added to cart")
    """
    print(type(session['cart']))
    phone_id = request.args.get('phone_id', None, int)
    print(phone_id)
    if phone_id is not None:
        if phone_id not in session['cart']:
            session['cart'].append(phone_id)
            for item in session['cart']:
                print(item)
        else:
            session['cart'][phone_id] = session['cart'][phone_id]+1
            for item in session['cart']:
                print("uprava",item)
    pass
    """
    return render_template("shop.jinja", phones = phones)

@app.route("/profile")
@auth.login_required
@auth.roles_required("Admin", "Employee", "Customer")
def profile():
    profile = UserService.getUserById(session['login'])
    return render_template("profile.jinja", profile = profile)


@app.route("/add-profile", methods = ["GET", "POST"])
@auth.login_required
@auth.roles_required("Admin")
def add_profile():
    form = forms.Add_profile(request.form)
    if request.method == 'POST':
        UserService.insertNewUser(
            new_position=request.form['new_position'],
            new_first_name=request.form['new_first_name'],
            new_last_name=request.form['new_last_name'],
            new_phone_number=request.form['new_phone_number'],
            new_email=request.form['new_email'],
            new_hourly_wage=request.form['new_hourly_wage'],
            new_login_name=request.form['new_login_name'],
            new_password=request.form['new_password'],
            new_company_id=request.form['new_company_id'],
            new_active=request.form['new_active']
            )
        flash('Profile added successfuly')
    return render_template("add_profile.jinja", form=form)


@app.route("/add-product", methods=["GET", "POST"])
@auth.login_required
@auth.roles_required("Employee", "Admin")
def add_phone():
    form = forms.Add_phone(request.form)
    if request.method == 'POST':
        PhoneService.add_phone(
            new_img = request.form['new_img'],
            new_name = request.form['new_name'],
            new_type = request.form['new_type'],
            new_workload = request.form['new_workload']            
        )
        flash('Product added successfuly')
    return render_template("add_product.jinja", form=form)

@app.route("/actions")
@auth.login_required
@auth.roles_required("Admin")
def actions():
    return render_template("actions.jinja")

@app.route('/edit-profile', methods=["GET", "POST"])
@auth.login_required
@auth.roles_required("Employee", "Admin", "Customer")
def edit_profile():
    form = forms.Edit_profile_form(request.form)

    if request.method == 'POST':
        new_email = request.form['new_email']
        new_first_name = request.form['new_first_name']
        new_password = request.form['new_password']

        if new_email == '':
            new_email = session['email']

        if new_first_name == '':
            new_first_name = session['first_name']

        if new_password == '':
            new_password = session['password']
        else:
            new_password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()

        UserService.updateUser(session['login'], new_email, new_first_name, new_password)
        session['email'] = new_email
        session['first_name'] = new_first_name
        session['password'] = new_password
        flash('Profile updated successfuly')
        return redirect(url_for('edit_profile'))

    return render_template("edit_profile.jinja", form=form)

@app.route('/cart')
@auth.login_required
@auth.roles_required("Employee", "Admin", "Customer")
def cart():
    return render_template("cart.jinja")

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    form = forms.Sign_in_form(request.form)
    if request.method == 'POST':
        user = UserService.verify(
            login=request.form['login'],
            password=request.form['password'])

        if not user or user['active'] == 0:
            flash('Incorrect login or password')
        else:
            session['cart'] = []
            session['authenticated'] = 1
            session['email'] = user['email']
            session['first_name'] = user['first_name']
            session['login'] = user['login_name']
            session['role'] = user['position']
            session['password'] = user['login_password']
            session['user'] = user['id_user']
            flash('Login successful')
            return redirect(url_for('index'))
    return render_template("sign_in.jinja", form=form)


@app.route('/sign-out')
@auth.login_required
def sign_out():
    for key in list(session.keys()):
        session.pop(key)
    flash('Signed out successfuly')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

