import requests
from bs4 import BeautifulSoup


def get_page_contents():

    page = requests.get('https://www.bbc.co.uk')
    return page.text


def get_tags(contents, tags):
    soup = BeautifulSoup(contents, "lxml")
    return soup.find(tags).get_text().split(' ')


def get_tag_list(contents):
    soup = BeautifulSoup(contents, "lxml")

    nameTags = soup.find_all(text=True)
    data = []
    for tags in nameTags:
        data.append(tags)
        print(tags)
    exit(nameTags)
    return nameTags
