import logging

import logging
from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')



class BookParser():


    RATINGS = {
         'One': 1,
         'Two': 2,
         'Three': 3,
         'Four': 4,
         'Five': 5
        }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`')
        self.parent = parent

    def __repr__(self):
        return f'<Book: {self.title} - /{self.link}- £{self.price} - ({self.rating} stars)'

    @property
    def title(self):
        logger.debug('Looking for book name...')
        locator = BookLocators.TITLE
        book_name = self.parent.select_one(locator).attrs['title']
        logging.debug(f'Book name found: `{book_name}`')
        return book_name
    @property
    def link(self):
        logger.debug('Looking for link...')
        locator = BookLocators.LINK
        link_name = self.parent.select_one(locator).attrs['href']
        logging.debug(f'Link address found: `{link_name}`')
        return link_name

    @property
    def price(self):
        logger.debug('Looking for price...')
        locator = BookLocators.PRICE
        price = self.parent.select_one(locator).string
        float_price = float(price.replace('£', ""))
        logging.debug(f'Price found and converted to a float `{float_price}`')
        return float_price

    @property
    def rating(self):
        logger.debug('Looking for rating...')
        locator = BookLocators.RATING
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        classes = [c for c in classes if c != 'star-rating']
        logger.debug(f'Rating found: `{classes[0]}`')
        rating = self.RATINGS.get(classes[0])
        logger.debug(f'Rating converted to integer: `{rating}`')
        return rating


