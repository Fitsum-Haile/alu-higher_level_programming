#!/usr/bin/python3
"""LockedClass prevents dynamic attribute creation except for 'first_name'."""


class LockedClass:
    """A class that prevents dynamic attribute creation."""

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
            )
        self.__dict__[name] = value
