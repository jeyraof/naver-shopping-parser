# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen
from urllib import urlencode
from lxml import html
from math import ceil
from .exceptions import *


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
        self.total = 0

    def search_by(self, keyword=None):
        self.keyword = keyword
        self.paging_index = 1

        url = self.__build_url()
        i = self.parse_url(url)
        self.total = i[1]
        return i[0]

    def prev(self):
        if not self.keyword:
            raise NoPreviousSearchError

        if self.paging_index <= 1:
            raise NoMorePreviousPageError
        else:
            self.paging_index -= 1

        url = self.__build_url()
        return self.parse_url(url)[0]

    def next(self):
        if not self.keyword:
            raise NoPreviousSearchError

        if ceil(self.total / self.condition.ea) == self.paging_index:
            raise NoMoreNextPageError

        self.paging_index += 1
        url = self.__build_url()
        return self.parse_url(url)[0]

    def __build_url(self):
        url = self.pre_url + urlencode({
            'query': self.keyword,
            'sort': self.condition.sort,
            'pagingSize': self.condition.ea,
            'pagingIndex': self.paging_index,
        })
        return url

    def parse_url(self, url=None):
        if not url:
            raise NoUrlGivenError
        r = Request(url=url)
        response = urlopen(r, timeout=30)
        return self.parse_html(response.read())

    @staticmethod
    def parse_html(html_string=''):
        tree = html.fromstring(html_string)

        data = []
        for item in tree.cssselect('li.sr_lst'):
            thumb = u''
            name = u'Unknown'
            price = u'0'

            for j in item.cssselect('div.thmb img'):
                thumb = j.get('src', u'')

            for j in item.cssselect('dl.info dt.tit'):
                name = j.text_content().encode('utf-8')

            for j in item.cssselect('dl.info dd.price em'):
                price = j.text_content().encode('utf-8')

            data.append(Item(thumb=thumb, name=name, price=price))

        total = 0.0
        for j in tree.cssselect('span.sr_pg2_total'):
            total = float(j.text_content().strip().split()[-1])
        return [data, total]

    def __repr__(self):
        return u'<NaverShopping - %s>' % self.keyword


class Item(object):
    """
    Item object

    * self.thumb: thumbnail url for item
    * self.name: name of item
    * self.price: price of item
    """

    def __init__(self, **kwargs):
        self.thumb = kwargs.get('thumb', u'')
        self.name = kwargs.get('name', u'Unknown')
        self.price = kwargs.get('price', u'0')

    def __repr__(self):
        return '<%s - %s>' % (self.name, self.price)
