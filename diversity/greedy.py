#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import copy
import random


def mean_of_differences(e, s):
    """
    default diversity function element-set
    :param e: element
    :param s: set against which calculate diversity
    :return:  diversity value
    """
    if len(s) == 0:
        raise Exception("Set into element-set diversity function is empty.")
    return sum([abs(e - x) for x in s]) / len(s)


def greedy(elements, k, diversity_element_set=mean_of_differences):
    """
    elements:               input array, the initial set of elements
    k:                      number of selected elements
    diversity_element_set:  diversity function to test the diversity of an element and a set
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
            d = diversity_element_set(e, selected)
            if max_d is None or max_d < d:
                max_d = d
                max_e = e

        # move the element from _elements to selected
        selected.append(max_e)
        _elements.remove(max_e)

    return selected
