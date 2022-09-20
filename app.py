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

@app.route("/home/")
def home():
    return render_template('index.html', students = users)