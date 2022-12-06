# -*- coding: utf-8 -*-

"""
Authors: huangtao13
Date: 6/6/20 5:27 PM
Desc:

"""
import codecs
import collections

from . import (
    transformations,
)
from .util import is_iterable
from .line_age import Lineage

__all__ = ['Sequence']

Transformation = collections.namedtuple("Transformation", ["name", "func", "execution_strategies"])


class Sequence(object):
    """
    Sequence class
    """

    def __init__(self, sequence, transform=None):
        """

        :param sequence:
        :param transform:
        """
        if isinstance(sequence, Sequence):
            # get prior transforms in chain operation
            self._base_sequence = sequence._base_sequence
            self._lineage = Lineage(prior_lineage=sequence._lineage)
        elif isinstance(sequence, (list, tuple)) or is_iterable(sequence):
            self._base_sequence = sequence
            self._lineage = Lineage()

        if transform is not None:
            self._lineage.apply(transform)

    def _transform(self, *transforms):
        """

        :param transforms:
        :return:
        """
        # save all transform
        sequence = None
        for transform in transforms:
            if sequence:
                sequence = Sequence(sequence, transform)
            else:
                sequence = Sequence(self, transform)
        return sequence

    def _trigger(self, sequence=None):
        """

        :param sequence:
        :return:
        """
        if sequence:
            return sequence._lineage(self._base_sequence)
        return self._lineage(self._base_sequence)

    def take(self, n, lazy=False):
        """

        :param n:
        :param lazy:
        :return:
        """
        seq = self._transform(transformations.take_t(n))
        if lazy:
            return seq
        # return self._trigger(seq)
        return seq._trigger()

    def head(self):
        """

        :return:
        """
        sequence = self._transform(transformations.head_t())
        return sequence._trigger()[0]

    def map(self, func):
        """
        >>> seq([1,2,3]).map(lambda x: x + 1)
        [2, 3, 4]
        :param func: function to map with
        :param func: function to map with
        :return: sequence with func mapped onto it.
        """
        # Save map func as a series transform operation.
        return self._transform(transformations.map_t(func))

    def reduce(self, func):
        """

        :param func:
        :return:
        """
        return self._transform(transformations.reduce_t(func))

    def filter(self, func):
        """

        :param func:
        :return:
        """
        return self._transform(transformations.filter_t(func))

    def flatten(self):
        """

        :return:
        """
        return self._transform(transformations.flatten_t())

    # todo
    def group_by_key(self):
        """

        :return:
        """
        pass

    # todo
    def reduce_by_key(self):
        """

        :return:
        """
        pass

    def get(self):
        """

        :return:
        """
        return self._lineage(self._base_sequence)

    def count(self):
        """

        :return:
        """
        return len(self._lineage(self._base_sequence))

    def write(self, output_filename, mode='w', encoding='utf8'):
        """

        :param output_filename:
        :param mode:
        :param encoding:
        :return:
        """
        result = self._trigger()
        with codecs.open(output_filename, mode, encoding=encoding) as fout:
            for line in result:
                fout.write('%s\n' % line)


if __name__ == "__main__":
    pass
