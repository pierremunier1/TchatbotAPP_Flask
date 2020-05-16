
    usertext = request.form["usertext"]
    usertext = Grandpy_result()
    analyse = Parser(usertext)
    userQuery = analyse.parse()
    query = GoogleApi(userQuery)
    userQuery = query.position()

    try:
        addressCoords = query.position()
        latitude = addressCoords[0]
        longitude = addressCoords[1]
        globalAddress = addressCoords[2]
        coords = WikiApi(latitude, longitude)
        extract = coords.get_wiki()[0]
        url = coords.get_wiki()[1]
        response = Grandpy.reply()
        user = usertext

    except BaseException:
        latitude = ''
        longitude = ''
        globalAddress = ''
        user = ''
        extract = ''
        url = ''
        response = Grandpy.reply_noanswer()

    return jsonify({'lat': latitude,
                    'lng': longitude,
                    'globalAddress': globalAddress,
                    'extract': extract,
                    'url': url,
                    'response': response,
                    'user': usertext
                    })