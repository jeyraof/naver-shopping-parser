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