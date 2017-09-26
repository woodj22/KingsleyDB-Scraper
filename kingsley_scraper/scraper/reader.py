import requests
from bs4 import BeautifulSoup


def get_page_contents():
    page = requests.get('https://www.bbc.co.uk')
    return page.text


def get_tag_strings(contents):
    soup = BeautifulSoup(contents, "lxml")
    elements = soup.find_all(text=True)
    return [(element.parent.name, element.split(' ')) for element in elements]


def retrieve_tag_and_weights(contents):
    soup = BeautifulSoup(contents, "lxml")
    elements = soup.find_all(text=True)

    # for element in elements:
    #     if element.count(' '):
    #         for word in element.split(' '):
    #             return (element.parent.name, word)
    #     else:
    #         return (element, 5)
    # [x+1 if x >= 45 else x+5 for x in l]

    return [(word, tag_weight(element.parent.name)) if element.count(' ') else (element, tag_weight(element.parent.name)) for element in elements for word in element.split(' ')]


     # return [(element.parent.name, word) for element in elements for word in element.split(' ')]


def tag_weight(tag):
    # The weight of tag is out of 10
    weight_list = {
        'h1': 10,
        'h2': 7,
        'h3': 3,
        'h4': 2,
        'h5': 1,
    }
    default = 5
    if tag in weight_list:
        return weight_list.get(tag)
    else:
        return default


def create_entry(text, tag_name):
    print((text, tag_name))
