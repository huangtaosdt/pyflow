# -*- coding: utf-8 -*-
"""
Authors: huangtao13
Date: 6/6/20 5:23 PM
Desc:

"""


class Lineage(object):
    """
    Lineage class
    """

    def __init__(self, prior_lineage=None):
        """

        :param prior_lineage:
        """
        self.transformations = [] if prior_lineage is None else prior_lineage.transformations

    def __repr__(self):
        """
        Returns readable representation of Lineage
        :return: readable Lineage
        """
        return "Lineage: " + " -> ".join(
            ["sequence"] + [transform.name for transform in self.transformations]
        )

    def __len__(self):
        """
        Number of transformations in lineage
        :return: number of transformations
        """
        return len(self.transformations)

    def __call__(self, base_sequence):
        """
        Perform operation of each sequence
        :param base_sequence:
        :return:
        """
        result = base_sequence
        for transform in self.transformations:
            result = transform.func(result)
        return list(result)

    def apply(self, transform):
        """
        Add new transformation to operation sequences
        :param transform:
        :return:
        """
        self.transformations.append(transform)
