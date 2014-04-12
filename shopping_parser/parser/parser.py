# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen
from urllib import urlencode
from shopping_parser.parser.exceptions import NoUrlGivenError


class Condition(object):
    """
    Condition for searching item

    * sort: sorting items by condition.
     - price_asc (default)
     - price_dsc

    * ea: number of items for searching at once
     - 20 (default)
     - integer number
    """

    def __init__(self, sort='price_asc', ea=20):
        self.sort = sort
        self.ea = ea


class NaverShopping(object):
    """
    Engine for searching items in shopping.naver.com

    * Methods for using
    - search_by(keyword=str())
    - next()
    - prev()
    """

    def __init__(self, condition=Condition()):
        self.pre_url = 'http://m.shopping.naver.com/search/all_search.nhn?'
        self.condition = condition
        self.paging_index = 1
        self.keyword = None

    def search_by(self, keyword=None):
        self.keyword = keyword
        self.paging_index = 1

        url = self.__build_url()
        r = self.parse(url)
        print r

    def prev(self):
        self.paging_index -= 1

    def next(self):
        self.paging_index += 1

    def __build_url(self):
        url = self.pre_url + urlencode({
            'query': self.keyword,
            'sort': self.condition.sort,
            'pagingSize': self.condition.ea,
            'pagingIndex': self.paging_index,
        })
        return url

    @staticmethod
    def parse(url=None):
        if not url:
            raise NoUrlGivenError()
        r = Request(url=url)
        response = urlopen(r)
        return response

    def __repr__(self):
        return u'<NaverShopping %s>' % self.keyword


class Item(object):
    pass