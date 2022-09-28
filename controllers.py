from flask import render_template, request
from app import app
from models import *
from forms import ContactForm, LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash
from flask_login import login_user


@app.route("/home/")
def home():
    return render_template('index.html')


@app.route("/login/", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.form)
        user = User.query.filter_by(username = form.username.data).first()
        if user and user.check_password(form.password.data):
            print('success')
            login_user(user)
    return render_template('login.html', form = form)


@app.route("/register/", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        print('post')
        form = RegistrationForm(request.form)
        if form.validate_on_submit():
            print('valid')
            user = User(
                form.username.data,
                form.email.data,
                generate_password_hash(form.password.data)
            )
            user.save()
    return render_template('register.html', form = form)


@app.route("/product_list/")
def product_list():
    products = Product.query.all()
    return render_template('product_list.html', items = products)
    

@app.route("/product_detail/<int:id>/")
def product_detail(id):
    product = Product.query.filter_by(id = id)
    return render_template('product_detail.html', item = product)


@app.route("/contact/", methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        print('POST')
        form = ContactForm(request.form)
        if form.validate_on_submit():
            print('VALID')
            contact = Contact(
                form.name.data,
                form.email.data,
                form.company.data,
                form.message.data,
                form.is_subscribe.data
            )
            contact.save()
    return render_template('contact.html', form = form)