#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import float_info
from copy import copy
import random


def greedy(elements, k, div_func=lambda x, y: x - y):
    """
    elements: input array, the initial set of elements
    k:        number of selected elements
    div_fuc:  diversity function to test the diversity between two elements
    """
    if len(elements) < k:
        return elements

    _elements = copy(elements)

    # randomly picked initial element
    r = random.choice(_elements)

    # add initial element to selected
    selected = [r]

    # remove the element from in
    _elements.remove(r)

    while len(selected) < k:
        max_d = None
        max_e = None
        for e in _elements:
            for s in selected:
                d = div_func(s, e)

                # keep track of maximum diversity and related element
                if max_d is None or max_d < d:
                    max_d = d
                    max_e = e

        # move the element from _elements to selected
        selected.append(max_e)
        _elements.remove(max_e)

    return selected
