import pytest

from tchatbotapp.utils import Parser


class TestParser:

    """ to test parse method """

    def test_parse_lc(self):

        """apply lower case"""
        text = ("RUE DE CAMBRONNE")
        self.analyse1 = Parser(text)
        assert self.analyse1.parse() == text.lower()
    
    def test_parse_punctuation(self):

        """remove accent"""

        text = ("avenue du général de gaulle")
        self.analyse2 = Parser(text)
        assert self.analyse2.parse() == "avenue du general de gaulle"
    
    def test_parse_punctuation_bis(self):

        """remove punctuation"""

        text = ("89,avenue du general de gaulle !")
        self.analyse3 = Parser(text)
        assert self.analyse3.parse() == "89 avenue du general de gaulle"


    def test_parse_stopword(self):

        text = ("Où se trouve la tour Eiffel ?")
        self.analyse4 = Parser(text)
        assert self.analyse4.parse() =="tour eiffel"
    