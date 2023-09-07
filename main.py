from flask import Flask, render_template, request, redirect, url_for
from table import Admin, Menu, Employee, Order, db,Order_item


app = Flask(__name__)
app.config["SECRET_KEY"] = 'itissoppusedtobesecret'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/employee-add', methods=['POST','GET'])
def emp():
    if request.method == 'POST':
        # create new record
        new_emp = Employee(
            fname=request.form["fname"],
            lname=request.form["lname"],
            gender=request.form["gender"],
            position=request.form["position"],
            address=request.form["address"],
            contact=request.form["contact"],
            salary=request.form["salary"]
        )
        db.session.add(new_emp)
        db.session.commit()
        return redirect(url_for('emp'))

    return render_template('employee.html')

all_emp = []
@app.route('/Emp-record')
def emp_record():
    result=db.session.execute(db.select(Employee).order_by(Employee.emp_id))
    all_emp=result.scalars()
    return render_template('emp-record.html', employee=all_emp)


@app.route('/Menu', methods=['POST','GET'])
def add_menu():
    if request.method == 'POST':
        # create new menu item
        new_menu = Menu(
            item_name=request.form['item_name'],
            item_description=request.form['item_description'],
            item_price=request.form['item_price'],
            menu_catgery=request.form['menu_catgery']
        )
        db.session.add(new_menu)
        db.session.commit()

        return redirect(url_for('add_menu'))
    return render_template('menu.html')

all_menu = []
@app.route('/')
def menu_record():
    result = db.session.execute(db.select(Menu).order_by(Menu.item_id))
    all_menu=result.scalars()
    return render_template('index.html', menus=all_menu)


@app.route('/order_item', methods=['POST','GET'])
def add_order():
    # if request.method == 'POST':
        # price = Menu.query.filter_by(price=price).first()
        # new_order_item = Order_item(
        #     item_name=request.form['item_id'],
        #     qty=request.form['qty'],
        #     # subprice=request.form['subprice'],
        #     order_id=request.form['order_id']
        # )
    return render_template('order.html')