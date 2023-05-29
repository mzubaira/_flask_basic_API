from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import requests

# Init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Init DB
db =SQLAlchemy(app)

#Inti Marshmallow
ma = Marshmallow(app)


# @app.route('/',methods=['GET'])
# def get():
#     return jsonify({'msg':'Hello World'})

#Product Class/Model
class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    description=db.Column(db.String(200))
    price=db.Column(db.Float)
    qty=db.Column(db.Integer)
    
    def __init__(self,name,description,price,qty):
        self.name=name
        self.description=description
        self.price=price
        self.qty=qty

#Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','description','price','qty')
        
#Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

#This creates a db.sqlite file
# python 
# >>>from <project> import app,db
# >>>app.app_context().push()
# >>>db.create_all()
# >>>exit()

#-------------CRUD Operations for the Endpoint------------#
#Create Product
@app.route('/product',methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    
    new_product = Product(name,description,price,qty)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)

'''TESTING on POSTMAN:
CLick on POST => http://127.0.0.1:5000/product

Header -> Key: Content-Type | Value: application/json
Body -> Raw:
{
    "name":"Macbook",
    "description":"This is an Apple macbook",
    "price":350.00,
    "qty":3
}

Click on "Send"

RESPONSE:
{
    "description": "This is an Apple macbook",
    "id": 1,
    "name": "Macbook",
    "price": 350.0,
    "qty": 3
}
'''
#Get all Products
@app.route('/product',methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

'''TESTING on POSTMAN:
CLick on GET => http://127.0.0.1:5000/product
Click on "Send"

RESPONSE:
[
    {
        "description": "This is an Apple macbook",
        "id": 1,
        "name": "Macbook",
        "price": 350.0,
        "qty": 3
    },
    {
        "description": "This is a Dell Laptop",
        "id": 2,
        "name": "Dell Inspiron",
        "price": 150.0,
        "qty": 5
    }
]
'''

#Get single product
@app.route('/product/<id>',methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

'''TESTING on POSTMAN:
CLick on GET => http://127.0.0.1:5000/product/1
Click on "Send"

RESPONSE:
{
    "description": "This is an Apple macbook",
    "id": 1,
    "name": "Macbook",
    "price": 350.0,
    "qty": 3
}
'''

#Update a product
@app.route('/product/<id>',methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    
    product.name = name
    product.description = description
    product.price = price
    product.qty = qty
    
    db.session.commit()
    return product_schema.jsonify(product)

'''TESTING on POSTMAN:
CLick on PUT => http://127.0.0.1:5000/product/1

Header -> Key: Content-Type | Value: application/json

Body -> Raw:
{
    "name":"Macbook Mini",
    "description":"This is an updated Macbook Model",
    "price":450.00,
    "qty":2
}

Click on "Send"

RESPONSE:
{
    "description": "This is an updated Macbook Model",
    "id": 1,
    "name": "Macbook Mini",
    "price": 450.0,
    "qty": 2
}
'''

#Delete a product
@app.route('/product/<id>',methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)

'''TESTING on POSTMAN:
CLick on DELETE => http://127.0.0.1:5000/product/2
Click on "Send"

RESPONSE:
{
    "description": "This is a Dell Laptop",
    "id": 2,
    "name": "Dell Inspiron",
    "price": 150.0,
    "qty": 5
}
'''

#Run Server
if __name__ == '__main__':
    app.run(debug=True)
    
#python app.py -> Running on http://127.0.0.1:5000

