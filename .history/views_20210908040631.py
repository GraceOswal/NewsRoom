from flask import render_template
from app import app

#Views
@app.route("/")
def index():
    """s
    View root page function
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    