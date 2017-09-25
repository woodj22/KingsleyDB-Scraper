import requests
from bs4 import BeautifulSoup

def get_page_contents():

    page = requests.get('https://www.bbc.co.uk')
    return page.text


def get_tags(contents, tags):
    soup = BeautifulSoup(contents, "lxml")
    return soup.find(tags).get_text().split(' ')


def get_tag_strings(contents):
    soup = BeautifulSoup(contents, "lxml")
    elements = soup.find_all(text=True)
    return [(element.parent.name, element.split(' ')) for element in elements]


def create_entry(text, tag_name):
    print((text, tag_name))
