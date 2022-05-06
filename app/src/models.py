"""

05/05/2022
ERROR:
SQLalchemy error Mapper failed to initialize. 
SOLUTION:
Commented out db.relationship lines:
    # reviews = db.relationship(
    #     'reviews', backref='customers', lazy=True, uselist=False)
    # carts = db.relationship('carts', backref='customers',
    # lazy=True, uselist=False)
    # customers = db.relationship('customers', backref='carts', lazy=True)
    # reviews = db.relationship('reviews', backref='products', lazy=True)

"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Customers(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(120), nullable=False)

    def __init__(self, username, email, password, address):
        self.username = username
        self.email = email
        self.password = password
        self.address = address

    def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'address': self.address
        }


class Carts(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True)
    # cartItems = db.Column(db., nullable=False, unique=True)
    customers_id = db.Column(
        db.Integer, db.ForeignKey(Customers.id), nullable=False)

    def __init__(self, customers_id):
        self.customers_id = customers_id

    def serialize(self):
        return{
            'id': self.id,
            'customers_id': self.customers_id,
        }


class Products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, name, description, reviews):
        self.name = name
        self.description = description
        self.reviews = reviews

    def serialize(self):
        return{
            'id': self.id,
            'title': self.name,
            'description': self.description,
            'reviews': self.reviews
        }


class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False,)
    content = db.Column(db.Text, nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __init__(self, name, content):
        self.name = name,
        self.content = content

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'content': self.content
        }
