from extensions import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = True)
    company = db.Column(db.String(200), nullable = False)
    message = db.Column(db.String(255), nullable = False)
    is_subscribe = db.Column(db.Boolean())


    def __init__(self, name, email, company, message, is_subscribe):
        self.name = name
        self.email = email
        self.company = company
        self.message = message
        self.is_subscribe = is_subscribe

    def __repr__(self):
        return self.email

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = True)
    products = db.relationship('Product', backref = 'user', lazy = True)


    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return self.email

    def save(self):
        db.session.add(self)
        db.session.commit()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(255))
    price = db.Column(db.Integer)
    image = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = True)

    def __init__(self, title, description, price, image):
        self.title = title
        self.description = description
        self.price = price
        self.image = image

    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()