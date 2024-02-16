#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Displays the home page of 9jafoods"""
    return render_template("home.html")
