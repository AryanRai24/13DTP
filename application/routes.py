from application import app, db
from flask import render_template, redirect, flash, url_for, request
from application import models
from .models import Product

@app.route('/')
def home():
    return render_template('home.html', title="Home")


@app.route('/product')
def product():
    product = Product.query.all()
    return render_template('product.html', title="product", product=product)
