#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template, url_for
from database import load_Igbo_Foods, load_Hausa_Foods, load_Yoruba_Foods, load_Drinks, load_Pop_Foods


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Displays the home page of 9jafoods"""
    return render_template("home.html")


@app.route("/igbo_foods", strict_slashes=False)
def igbo_foods():
    """Displays igbo foods"""
    igbo_foods = load_Igbo_Foods()
    return render_template("igbo_foods.html", igbo_foods=igbo_foods)



@app.route("/hausa_foods", strict_slashes=False)
def hausa_foods():
    """Displays Hausa foods"""
    hausa_foods = load_Hausa_Foods()
    return render_template("hausa_foods.html", hausa_foods=hausa_foods)

@app.route("/yoruba_foods", strict_slashes=False)
def yoruba_foods():
    """Displays Hausa foods"""
    yoruba_foods = load_Yoruba_Foods()
    return render_template("yoruba_foods.html", yoruba_foods=yoruba_foods)


@app.route("/drinks", strict_slashes=False)
def drinks():
    """Displays Hausa foods"""
    drinks = load_Drinks()
    return render_template("drinks.html", drinks=drinks)

@app.route("/pop_foods", strict_slashes=False)
def pop_foods():
    """Displays igbo foods"""
    pop_foods = load_Pop_Foods()
    return render_template("pop_foods.html", pop_foods=pop_foods)



