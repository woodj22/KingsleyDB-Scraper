import kingsley_scraper.scraper.reader as Page


def cli():
    contents = Page.get_page_contents()
    tags = Page.get_tags(contents, 'h1')
    print(tags)


if __name__ == "__main__":
    cli()
