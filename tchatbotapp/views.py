from flask import render_template, jsonify, request
from . import tchatbotapp
from .utils import Response
import os


@tchatbotapp.route('/')
def index():
    """display the data to the front"""
    return render_template('index copy.html', API_KEY=os.environ.get('API_KEY'))


@tchatbotapp.route("/ajax", methods=["POST"])
def ajax():
    """analyse the text entered in the user input"""

    usertext = request.form["usertext"]
    user_text = Response.response_front(usertext)

    return jsonify(user_text)
