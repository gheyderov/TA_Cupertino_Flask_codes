from flask import render_template
from app import app
from models import *


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