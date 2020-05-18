import config
from tchatbotapp.utils import Parser, GoogleApi, WikiApi, Grandpy, Response

from random import choice
import unittest


class TestParser:
    """ to test parse method """

    def test_parse_lc(self):
        """apply lower case"""
        text = ("RUE DE CAMBRONNE")
        self.analyse1 = Parser(text)
        assert self.analyse1.parse() == "rue cambronne"

    def test_parse_punctuation(self):
        """remove accent"""

        text = ("avenue du général de gaulle")
        self.analyse2 = Parser(text)
        assert self.analyse2.parse() == "avenue general gaulle"

    def test_parse_punctuation_bis(self):
        """remove punctuation"""

        text = ("89,avenue du general de gaulle !")
        self.analyse3 = Parser(text)
        assert self.analyse3.parse() == "89 avenue general gaulle"

    def test_parse_stopword(self):
        """test stopword method"""

        text = ("Où se trouve la tour Eiffel ?")
        self.analyse4 = Parser(text)
        assert self.analyse4.parse() == "tour eiffel"

    def test_parsing_total(self):
        """check total"""
        self.analyse5 = Parser(
            "Salut GrandPy ! Comment tu vas ? Je cherche l'adresse du Louvre ! Peux tu me la donner ?")
        assert self.analyse5.parse() == "louvre"


############################################################


def test_requestgoogleapi(monkeypatch):
    """test address request of the google api"""

    direction = GoogleApi("tour effeil")
    result = {
        'results': [
            {
                'formatted_address': "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France",
                'geometry': {
                    'location': {
                        'lat': 48.85837009999999,
                        'lng': 2.2944813}}}],
        'status': 'OK'}

    class MockRequestsGet:

        def __init__(self, url, params=None):
            pass

        def json(self):
            return result

    monkeypatch.setattr('requests.get', MockRequestsGet)
    assert direction.position() == (
        48.85837009999999,
        2.2944813,
        "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France")


def test_get_errorstatus(monkeypatch):
    """test the error status of the google api function"""

    direction = GoogleApi("tour effeil")
    status = {
        'results': [{None}], 'status': 'ZERO_RESULTS'
    }

    class MockNoResults:

        def __init__(self, url, params=None):
            pass

        def json(self):
            return status

    monkeypatch.setattr('requests.get', MockNoResults)
    assert direction.position() is None
############################################################


def test_get_wiki(monkeypatch):
    """To test a place, "Troyes City", with its latitude and longitude and wikipedia page."""

    position = WikiApi(latitude=48.297419, longitude=4.074263)
    result = [{'query': {'geosearch': [{'pageid': 6732671}]}},
              {'query': {'pages': {'6732671': {'extract': "L'unité urbaine de Troyes est une unité urbaine française centrée sur la ville de Troyes, première…",
                                               'canonicalurl': "https://fr.wikipedia.org/wiki/Unit%C3%A9_urbaine_de_Troyes"}}}}]

    class MockGetWiki:
        status_code = 200

        def __init__(self, url, params):
            pass

        def json(self):
            return result.pop(0)

    monkeypatch.setattr('requests.get', MockGetWiki)
    assert position.get_wiki() == (
        "L'unité urbaine de Troyes est une unité urbaine française centrée sur la ville de Troyes, première…",
        'https://fr.wikipedia.org/wiki/Unit%C3%A9_urbaine_de_Troyes')

############################################################


class TestGrandPy:
    """test reply of the grandpy function"""

    def test_reply(self):
        """test if the reply is selected"""

        answer = Grandpy.reply()
        assert answer in config.LISTREPLY 

    def test_reply_noanswer(self):
        """test if the 'no reply' is selected"""
       
        noanswer = Grandpy.reply_noanswer()
        assert noanswer in config.LISTNOREPLY

