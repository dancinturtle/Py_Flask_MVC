from flask import Flask, render_template, redirect, request
app = Flask(__name__, template_folder="views")

# Import Controllers
from controllers.welcome import Welcome
welcome = Welcome()

from controllers.products import Products
products = Products()

# Routes
@app.route('/')
def welcomeIndex():
    return welcome.index()

@app.route('/products')
def productsIndex():
    return products.index()

# Run Server
app.run(debug=True)