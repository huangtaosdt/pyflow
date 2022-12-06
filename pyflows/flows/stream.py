# -*- coding: utf-8 -*-
"""
Authors: huangtao13
Date: 6/6/20 5:27 PM
Desc: python链式操作封装 - Chainable python
e.g.:
    seq([1, 2, 3]).map(lambda x: x+1).get() =>  [2, 3, 4]
"""
from .util import is_iterable
from .pipeline import Sequence
from .io import IterableTextFile


class Stream(object):
    """
    Stream class
    """

    def __init__(self, *args):
        """

        :param args:
        """
        pass

    def __call__(self, *args):
        """

        :param args:
        :return:
        """
        if isinstance(args[0], (list, tuple)) or is_iterable(args[0]):
            return Sequence(args[0])
        else:
            raise TypeError("seq() only support 1 iterable object. (but {0} given)".format(type(args)))

    def open(self, path, mode='r', encoding='utf8', n_limit=None, process_hint=None):
        """
        Open data file.

        >>> seq.open(your_file_name, n_limit=1000).map(lambda x: x.strip()).get()

        :param path:
        :param delimiter:
        :param mode:
        :param encoding:
        :param n_limit:
        :param process_hint:
        :return:
        """
        open_file = IterableTextFile(path=path, mode=mode, encoding=encoding,
                                     n_limit=n_limit, process_hint=process_hint)
        return self(open_file)

    # todo
    def write(self, output_lines, file_name, mode='w', encoding='utf8'):
        """

        :param output_lines:
        :param file_name:
        :param mode:
        :param encoding:
        :return:
        """
        import codecs

        with codecs.open(file_name, mode, encoding=encoding) as fout:
            for line in output_lines:
                fout.write('%s\n' % line)


seq = Stream()
