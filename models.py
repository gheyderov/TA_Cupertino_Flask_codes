from extensions import db


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