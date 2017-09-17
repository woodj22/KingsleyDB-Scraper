import scraper.read_page as Page

def cli():
    content = Page.get_contents()
    print(content)

if __name__ == "__main__":
    cli()