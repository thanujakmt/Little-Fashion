
from Application import app
from flask import render_template
import requests

@app.route("/", methods = ["POST","GET"])
def home():
    return render_template("Home.html")

@app.route("/story", methods = ["POST","GET"])
def story():
    return render_template("Story.html")

@app.route("/products", methods = ["POST","GET"])
def products():
    return render_template("Products.html")

@app.route("/faqs", methods = ["POST","GET"])
def faqs():
    return render_template("/FAQs.html")

@app.route("/contact",methods = ["POST","GET"])
def contact():
    return render_template("/Contact.html")

@app.route("/test",methods = ["GET"])
def test():
    return render_template("index.html")