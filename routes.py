from flask import render_template, redirect, flash
from forms import AddProductClass, RegisterForm, LoginForm
import os
from extentions import app, db
from models import Product, Category, User
from flask_login import login_user, logout_user, login_required, current_user
import random


@app.route("/")
def home_page():
    all_products = Product.query.all()
    featured_products = random.sample(all_products, min(len(all_products), 3))
    
    return render_template("home.html", products=featured_products)

@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(username = form.username.data, 
                        email = form.email.data, 
                        password = form.password.data)
        
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect("/")
    return render_template("registration_form.html", form=form)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        print(user.username)
        print(form.password.data)

        if user and user.check_password(form.password.data):
            print(user.password)
            print(form.password.data)
            login_user(user)
            return redirect("/")
    else:
        print(form.errors)

        
    return render_template("login_form.html", form=form)

@app.route("/logout", methods=["POST", "GET"])
def logout():
    logout_user()
    return redirect("/")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/all_products")
def all_products_category():
    return render_template("products.html", products = Product.query.all())

@app.route("/all_products/<int:category_id>")
def all_products(category_id):
    return render_template("products.html", products = Category.query.get(category_id).products)

@app.route("/products/<int:product_id>")
def product(product_id):
    product = Product.query.get(product_id)

    all_products = Product.query.all()
    featured_products = random.sample(all_products, min(len(all_products), 3))

    if not product:
        return render_template("404.html", id=product_id)
    
    return render_template("product.html", product=product, random_products=featured_products)

@app.route("/add_product", methods=["POST", "GET"])
@login_required
def add_product():
    form = AddProductClass()

    if form.validate_on_submit():
        #image = form.image.data
        #file_path = os.path.join("static", "images", image.filename)

       

        new_product = Product(text=form.text.data, 
                                  price=form.price.data, 
                                  description=form.description.data, 
                                  image_url=form.image_url.data, 
                                  category_id=form.category_id.data)
        #image.save((os.path.join(app.root_path, file_path)))
        db.session.add(new_product)
        db.session.commit()
            
        return redirect("/")
        
    else: 
        print("Form validation failed")
        print(form.errors)

    return render_template("add_product.html", form=form)

@app.route("/update_product/<int:product_id>", methods=["POST", "GET"])
def update_product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return render_template("404.html")
    
    form = AddProductClass(text=product.text, price=product.price, description=product.description, image_url=product.image_url, category_id=product.category_id)

    if form.validate_on_submit():
        product.text = form.text.data
        product.price = form.price.data
        product.description = form.description.data
        product.image_url = form.image_url.data
        product.category_id = form.category_id.data

        db.session.commit()
        return redirect("/")

    return render_template("update_product.html", form=form)

@app.route("/delete_product/<int:product_id>", methods=["DELETE", "GET"])
def delete_product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return render_template("404.html")


    db.session.delete(product)
    db.session.commit()

    return redirect("/")

@app.route("/search/<string:product_name>")
def search(product_name):
    products = Product.query.filter(Product.text.ilike(f"%{product_name}%")).all()
    return render_template("products.html", products = products)

