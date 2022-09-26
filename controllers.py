from flask import render_template, request
from app import app
from models import *
from forms import ContactForm


@app.route("/home/")
def home():
    return render_template('index.html')


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