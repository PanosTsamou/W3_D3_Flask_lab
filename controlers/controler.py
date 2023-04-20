from flask import render_template, url_for, request,redirect
from app import app
from models.list_of_order import list_of_orders

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/orders", methods =["POST", "GET"])
def orders():
    if request.method == "POST":
        ord= request.form["order-num"]
        return redirect(url_for("order", ord=int(ord)-1))
    else:
        return render_template('orders.html', title = 'Orders', list_of_orders=list_of_orders)

@app.route("/orders/<ord>")
def order(ord):
    return render_template('order.html', order = list_of_orders[int(ord)])