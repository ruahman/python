""" Creates DOM from file. """

from bs4 import BeautifulSoup


def get_dom(content):
    """ Create dom object from html. """
    soup = BeautifulSoup(content, "html.parser")
    return soup
