# -*- coding: utf-8 -*-
"""
Authors: huangtao13
Date: 6/6/20 5:27 PM
Desc:

"""
from __future__ import print_function

import json
import time
import codecs
from itertools import islice


class IterableTextFile(object):
    """
    IterableTextFile class
    """

    def __init__(self, path, mode='r', encoding='utf8', n_limit=None, process_hint=None):
        """

        :param path:
        :param mode:
        :param encoding:
        :param n_limit:
        :param process_hint:
        """
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.n_limit = n_limit
        self.process_hint = process_hint
        self.idx = 0

    def __iter__(self):
        """

        :return:
        """
        with codecs.open(self.path, mode=self.mode, encoding=self.encoding) as f_in:
            if isinstance(self.n_limit, int):
                f_in = islice(f_in, 0, self.n_limit)
            for line in f_in:
                self.idx += 1
                if isinstance(self.process_hint, int) and self.idx % self.process_hint == 0:
                    print('[%s] IterableTextFile.reader: %d ' % \
                          (time.strftime(str("%Y-%m-%d %H:%M:%S"), time.localtime()), self.idx))
                yield line
