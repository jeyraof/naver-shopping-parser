# -*- coding: utf-8 -*-


class Error(Exception):
    """
    Base class for exceptions in this module.
    """
    pass


class NoUrlGivenError(Error):
    """
    Exception raised when url was not given.
    """

    def __init__(self, msg=u'Url was not given.'):
        self.msg = msg

    def __str__(self):
        return str(self.msg)


class NoPreviousSearchError(Error):
    """
    Exception for not following search.
    """

    def __init__(self, msg=u'Not following search. First of all, search using search_by().'):
        self.msg = msg

    def __str__(self):
        return str(self.msg)


class NoMorePreviousPageError(Error):
    """
    Exception for no more previous page.
    """

    def __init__(self, msg=u'No more previous page.'):
        self.msg = msg

    def __str__(self):
        return str(self.msg)


class NoMoreNextPageError(Error):
    """
    Exception for no more next page.
    """

    def __init__(self, msg=u'No more next page.'):
        self.msg = msg

    def __str__(self):
        return str(self.msg)