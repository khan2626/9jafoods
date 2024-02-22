#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template, url_for
import pandas as pd


app = Flask(__name__)


print(pd.__version__)
@app.route("/", strict_slashes=False)
def home():
    """Displays the home page of 9jafoods"""
    igbo_foods = pd.read_csv("igbo_foods.csv")
    print(igbo_foods)
    return render_template("home.html", igbo_foods=igbo_foods.to_dict(orient='records'))


@app.route("/igbo_foods", strict_slashes=False)
def igbo_foods():
    """Displays igbo foods"""

    return render_template("igbo_foods.html")



@app.route("/hausa_foods", strict_slashes=False)
def hausa_foods():
    """Displays Hausa foods"""
    return render_template("hausa_foods.html")

@app.route("/yoruba_foods", strict_slashes=False)
def yoruba_foods():
    """Displays Hausa foods"""
    return render_template("yoruba_foods.html")




if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000, debug=True)
