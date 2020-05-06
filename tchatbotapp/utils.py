import re
import unicodedata
import requests
from random import choice

import config


class Parser:

    """class contains method to parse the user text input form"""

    def __init__(self,analyse):
        """initialising attribute"""

        self.analyse = analyse
        
    def parse(self):

        """method analyse the text and transform if necessary"""

        """transformation method"""
        #switch to lower case
        self.analyse = self.analyse.lower()
        
        #remove accent
        self.analyse = ''.join((c for c in unicodedata.normalize('NFD', self.analyse) if unicodedata.category(c) != 'Mn'))
        
        #remove punctuation
        self.analyse = re.sub(r"[.!,;?\']", " ", self.analyse).split()
        
        #check stopword
        self.analyse = [x for x in self.analyse if x not in config.STOPWORDS]

        #to convert the list to string.
        self.analyse = ' '.join(self.analyse)

        return self.analyse

class GoogleApi:

    """classe contains method for geocoding api"""

    def __init__(self,userQuery):

        """initializing instance attributes"""

        self.user_query = userQuery
        self.latitude = float
        self.longitude = float
        self.global_address = str


    def position(self):

        """method find the correct position with geocoding google api"""

        payload = {'address': self.user_query, 'key' : config.API_KEY}
        result = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
        google_maps = result.json()
        status = google_maps['status']

        if status == 'OK':
            self.latitude = google_maps['results'][0]['geometry']['location']['lat']
            self.longitude = google_maps['results'][0]['geometry']['location']['lng']
            self.global_address = google_maps['results'][0]['formatted_address']
            return self.latitude, self.longitude, self.global_address
        
        elif status =='ZERO_RESULTS':
            print("Adresse non trouvée")




class WikiApi:

    """class contain all methods to retreive data from mediawiki api"""

    def __init__(self,latitude, longitude):

        """ Initializing instance attribute """

        self.latitude = latitude
        self.longitude = longitude

    def get_wiki(self):

        """get wikipedia articles from mediawiki api in two step"""

        geo = '{}|{}'.format(self.latitude, self.longitude)

        payload = {'format': 'json', 
                   'action': 'query',
                   'list': 'geosearch',
                   'gsradius':50, 
                   'gscoord': geo}

        result = requests.get('https://fr.wikipedia.org/w/api.php', params=payload)

        #second step if statut code is ok, retreive all details of the selected articles

        if result.status_code == 200:
            media_wiki = result.json()
            
            pageid = media_wiki['query']['geosearch'][0]['pageid']

    
            payload = {'format': 'json', 
                        'action': 'query',
                        'prop': 'extracts|info',
                        'inprop': 'url',
                        'exchars': 200, 
                        'explaintext': 1, 
                        'pageids': pageid} 

            result = requests.get('https://fr.wikipedia.org/w/api.php', params=payload)

            extract_wiki = result.json()

            return extract_wiki['query']['pages'][str(pageid)]['extract']

class Grandpy:

    
    def reply():

        listanswer = ("Je connais très bien ce lieu.... ","Je vais te raconter l'histoire...    ")

        answer = choice(listanswer)
        print(answer)
        return answer

    def reply_noanswer():

        listanswer = ("Je n'ai pas compris peux tu répeter la question?.... ","As-tu un problème de clavier?...    ")

        noanswer = choice(listanswer)
        return noanswer