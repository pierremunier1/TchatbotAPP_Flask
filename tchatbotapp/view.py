from flask import render_template, jsonify, request ,json
from . import tchatbotapp
from .utils import Parser, GoogleApi ,WikiApi

class Front:

    """class contains all methods to display the data to the front"""
    
    @tchatbotapp.route('/')
    def index():
        return render_template('index.html')

   
    @tchatbotapp.route("/ajax", methods=["POST"])
    def ajax():
        
        """analyse the text entered in the user input"""

        request.method == "POST"
        usertext = request.form["usertext"]
        analyse = Parser(usertext)
        userQuery = analyse.parse()
        query = GoogleApi(userQuery)
        userQuery = query.position()

        try:

            # retrieve position and global adress from googleapi.
            addressCoords = query.position() 
            #print(addressCoords)
            latitude = addressCoords[0] 
            longitude = addressCoords[1]
            globalAddress = addressCoords[2]
            # send position to wiki api
            coords = WikiApi(latitude, longitude)
            extract = coords.get_wiki()

        except:

            # if no message do an different answer.
        
            latitude = ''
            longitude = ''
            globalAddress = ''
            extract = ''
            url = ''

            print("Aucune réponse")

        finally:

            # return complete response to the ajax function.
           
            return jsonify({'lat':latitude, 
                            'lng':longitude,
                            'globalAddress':globalAddress,
                            'extract': extract})