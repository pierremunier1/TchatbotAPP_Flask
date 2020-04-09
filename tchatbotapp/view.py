from flask import render_template, jsonify, request ,json
from . import tchatbotapp
from .utils import Parser

class Front:

    @tchatbotapp.route('/')
    def index():
        return render_template("index.html")

    @tchatbotapp.route("/ajax", methods=["POST"])
    def ajax():
        user_text = request.form["userText"]
        analyse = Parser(user_text)
        userQuery = analyse.parsing()
        return jsonify(["userText"])
    

