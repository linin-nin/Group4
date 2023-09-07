from flask_sqlalchemy import SQLAlchemy
from datetime import *

# create the extension
db = SQLAlchemy()
# create table for Admin
class Admin(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)

# create table for menu
class Menu(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(200), nullable=True)
    item_description = db.Column(db.String(500), nullable=True)
    item_price = db.Column(db.Float, nullable=True)
    menu_catgery = db.Column(db.String(200), nullable=True)


# create table for Employee
class Employee(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=True)
    lname = db.Column(db.String(200), nullable=True)
    gender = db.Column(db.String(30), nullable=True)
    position = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(500), nullable=True)
    contact = db.Column(db.String(15), nullable=True)
    salary = db.Column(db.Float, nullable=True)

# create table for order
class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=date)
    order_amount = db.Column(db.Integer, nullable=True)
    emp_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))

class Order_item(db.Model):
    order_item_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('menu.item_id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    qty = db.Column(db.Integer, nullable=True)
    subprice = db.Column(db.Float, default=qty*10)