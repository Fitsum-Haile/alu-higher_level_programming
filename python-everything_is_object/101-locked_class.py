#!/usr/bin/python3
"""LockedClass prevents dynamic attribute creation except for 'first_name'."""


class LockedClass:
    """A class that prevents dynamic attribute creation."""

    def __init__(self, first_name=None):
        self._first_name = first_name

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
            )
        self._first_name = value

    def __getattribute__(self, name):
        if name == '_first_name':
            return self.__dict__['_first_name']
        if name == '__dict__':
            raise AttributeError("'LockedClass' object has no attribute '__dict__'")
        return object.__getattribute__(self, name)
