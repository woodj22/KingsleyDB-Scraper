import requests
from bs4 import BeautifulSoup


def get_page_contents():

    page = requests.get('https://www.bbc.co.uk')
    return page.text


def get_tags(contents, tags):
    soup = BeautifulSoup(contents, "lxml")
    data = [element.text for element in soup.find_all(tags)]
    exit(data)

