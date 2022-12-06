# -*- coding: utf-8 -*-
"""
Authors: huangtao13
Date: 6/6/20 7:13 PM
Desc:

"""
import collections
from itertools import islice
from functools import partial

from .util import is_iterable


Transformation = collections.namedtuple("Transformation", ["name", "func", "execution_strategies"])


def map_t(func):
    """

    :param func:
    :return:
    """

    transform = Transformation("map()", partial(map, func), "")
    return transform


def reduce_t(func):
    """

    :param func:
    :return:
    """
    transform = Transformation("reduce()", partial(reduce, func), "")
    return transform


def filter_t(func):
    """

    :param func:
    :return:
    """
    transform = Transformation("filter()", partial(filter, func), None)
    return transform


def flatten_map_impl(func, sequence):
    """

    :param func:
    :param sequence:
    :return:
    """
    for element in sequence:
        v_list = func(element)
        if is_iterable(v_list):
            for value in v_list:
                yield value
        else:
            yield v_list


def flatten_t():
    """

    :return:
    """
    return Transformation("flatten()", partial(flatten_map_impl, lambda x: x), None)


def take_t(n):
    """

    :param n:
    :return:
    """
    transform = Transformation("take()", lambda seq: islice(seq, 0, n), None)
    return transform


def head_t():
    """

    :return:
    """
    transform = Transformation("head()", lambda seq: islice(seq, 0, 1), None)
    return transform
