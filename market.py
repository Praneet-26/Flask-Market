from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [{'id':1, 'name':'Phone', 'barcode':'8977330034','price':500},
             {'id':1, 'name':'Laptop', 'barcode':'8977780034','price':650},
             {'id':1, 'name':'Tablet', 'barcode':'8977355034','price':1000}]
    return render_template('market.html', items= items)