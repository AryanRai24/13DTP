from application import db

class Product(db.Model):
    tablename = "product"
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False, unique=True)