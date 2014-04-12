# -*- coding: utf-8 -*-


class Condition(object):
    """
    Condition for searching item

    * sort: sorting items by condition.
     - price_asc (default)
     - price_dsc

    * ea: number of items for searching at once
     - integer number
     - 20 (default)
    """

    def __init__(self, sort='price_asc', ea=20):
        self.sort = sort
        self.ea = ea