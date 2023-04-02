from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from models import Products, db
from parser import all_ads, product_page


db = db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db.init_app(app)


# class Products(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, unique=True, nullable=False)
#     price = db.Column(db.Integer(), nullable=False)
#     description = db.Column(db.Text(), nullable=False)
#     city = db.Column(db.String(), nullable=False)

#     def __init__(self, title, price, description, city):
#         self.title = title
#         self.price = price
#         self.description = description
#         self.city = city

#     def to_dict(self):
#         return {
#             "id":self.id,
#             "url":self.id,
#             "title":self.title,
#             "price":self.price,
#             "description":self.description,
#             "city":self.city
#         }


@app.route("/product/<int:id>")
def product_detail(id):
    product = db.get_or_404(Products, id)
    print(product)
    return render_template('product_detail.html', product=product)


def write_to_db(data):
    try:
        product = Products(*data)
        db.session.add(product)
        db.session.commit()
    except:
        print('write db except')
    

@app.route('/pars_product')
def add_product():
    product_page_urls = all_ads()
    for url in product_page_urls:
        write_to_db(product_page(url))
    

@app.route("/")
def index():
    products = db.session.execute(db.select(Products)).scalars()
    products = products.all()
    #products = [product.to_dict() for product in products]
    print(products)
    return render_template('test.html', products=products)
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
