from flask import Flask, render_template, redirect, request

from models.product import Product
product = Product()

class Products:
    """Product Controller"""

    def index(app):
    	content = {}
    	content['products']= product.retrieveAll()
        return render_template("products.html", content=content)