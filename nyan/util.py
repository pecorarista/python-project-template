# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def duplicate(s, is_hyphenated=False):
    """Function that is defined to demonstrate how to doctest.

    >>> duplicate('人')
    '人人'

    >>> duplicate('orang', is_hyphenated=True)
    'orang-orang'

    Argument:
        s (str)
    Returns:
        double
    """
    return "{}-{}".format(s, s) if is_hyphenated else "{}{}".format(s, s)
