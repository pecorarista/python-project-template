# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def duplicate(w, is_hyphenated=False):
    """Function that is defined to demonstrate how to use doctest.

    >>> duplicate('人')
    '人人'

    >>> duplicate('orang', is_hyphenated=True)
    'orang-orang'

    Argument:
        w (str): The word to duplicate.
    Returns:
        str
    """
    return "{}-{}".format(w, w) if is_hyphenated else "{}{}".format(w, w)


def mathematical_function(x):
    r"""Function that is defined to demonstrate
    how to document mathematical expressions.

    .. math::

       \operatorname{sigmoid}\left(x\right)
           := \frac{1}{1 + \exp\left(-x\right)}
    """
    return x
