from flask import Flask, render_template

app = Flask(__name__)

users = {
    'user_1' : {
        'name' : 'John',
        'surname' : 'Doe',
        'age' : 20
    },
    'user_2' : {
        'name' : 'Jelly',
        'surname' : 'Kennedy',
        'age' : 22
    }
}

products = {
    1 : {
        "id" : 1,
        "title" : 'Product#1',
        "description" : "Some Description #1",
        "price" : '100 USD',
        "image" : "p1.avif"
    },
    2 : {
        "id" : 2,
        "title" : 'Product#2',
        "description" : "Some Description #2",
        "price" : '200 USD',
        "image" : "p2.avif"
    },
    3 : {
        "id" : 3,
        "title" : 'Product#3',
        "description" : "Some Description #3",
        "price" : '300 USD',
        "image" : "p3.avif"
    }
}


@app.route("/home/")
def home():
    return render_template('index.html', students = users)


@app.route("/product_list/")
def product_list():
    return render_template('product_list.html', items = products)
    

@app.route("/product_detail/<int:id>/")
def product_detail(id):
    return render_template('product_detail.html', item = products[id])