from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), unique=True, nullable=False)
    title = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    city = db.Column(db.String(), nullable=False)

    def __init__(self, url, title, price, description, city):
        self.url = url
        self.title = title
        self.price = price
        self.description = description
        self.city = city

    def to_dict(self):
        return {
            "id":self.id,
            "url":self.id,
            "title":self.title,
            "price":self.price,
            "description":self.description,
            "city":self.city
        }
if __name__ == "__main__":
    print(db.get_or_404(Products, 1))