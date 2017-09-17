import requests


def get_contents():

    page = requests.get('http://www.bbc.co.uk')
    contents = page.content
    print(contents)

get_contents()
