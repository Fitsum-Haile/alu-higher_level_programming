#!/usr/bin/python3
"""LockedClass prevents dynamic attribute creation except for 'first_name'."""


class LockedClass:
    """A class that prevents dynamic attribute creation."""

    def __init__(self, first_name=None):
        self.first_name = first_name

    def __setattr__(self, name, value):
        if not hasattr(self, name):
            if name != 'first_name':
                raise AttributeError(
                    "'LockedClass' object has no attribute '{}'".format(name)
                )
        object.__setattr__(self, name, value)
