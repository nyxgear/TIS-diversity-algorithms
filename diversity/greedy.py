#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import copy
import random

from .default_diversity_functions import mean_of_differences


def greedy(elements, k, diversity_element_set=mean_of_differences):
    """
    elements:               input array, the initial set of elements
    k:                      number of selected elements
    diversity_element_set:  diversity function to test the diversity of an element and a set
    """
    _elements = copy(list(elements))

    if len(_elements) < k:
        return _elements

    # randomly pick one initial element
    r = random.choice(_elements)

    # add initial element to selected
    selected = [r]

    # remove picked element from _elements
    _elements.remove(r)

    while len(selected) < k:
        max_d = None
        max_e = None
        for e in _elements:
            d = diversity_element_set(e, selected)
            if max_d is None or max_d < d:
                max_d = d
                max_e = e

        # move the element from _elements to selected
        selected.append(max_e)
        _elements.remove(max_e)

    return selected
