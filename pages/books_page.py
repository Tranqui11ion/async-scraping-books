import logging
import re
from bs4 import BeautifulSoup

from locators.book_page_locators import BookPageLocators
from parsers.book_parser import BookParser

logger = logging.getLogger('scraping.all_books_page')

class AllBooksPage():
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books from current page using `{BookPageLocators.BOOK}')
        return [BookParser(e) for e in self.soup.select(BookPageLocators.BOOK)]

    @property
    def page_count(self):
        logger.debug('Finding total amount of pages to scrape')
        content = self.soup.select_one(BookPageLocators.PAGER).string
        logger.info(f'Found number of catalogue pages available: `{content}`.')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer: {pages}')
        return pages

