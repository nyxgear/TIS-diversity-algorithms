#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import copy
import random


def neighborhood(elements, ngb_range, div_func=lambda x, y: abs(x - y)):
    """
    elements:  input array, the initial set of elements
    ngb_range: neighborhood range used to define the neighbors of an element
    div_fuc:   diversity function to test the diversity between two elements
    """
    if len(elements) == 0:
        return []

    # return if given elements ar more far each other than range
    def out_of_neighborhood(x, y):
        return div_func(x, y) > ngb_range

    _elements = copy(elements)

    # randomly picked initial element
    r = random.choice(elements)

    # add initial element to selected
    selected = [r]

    # elements is updated taking off the neighbors of r
    _elements = list(filter(lambda x: out_of_neighborhood(r, x), _elements))

    while len(_elements) > 0:
        max_avg = None
        max_e = None
        for i in _elements:
            # calculate the average diversity of i with all the elements of s
            avg = 0
            for s in selected:
                avg += div_func(i, s)
            avg /= len(selected)

            if max_avg is None or max_avg < avg:
                max_avg = avg
                max_e = i

        # elements is updated taking off the neighbors of r
        _elements = list(filter(lambda x: out_of_neighborhood(max_e, x), _elements))
        selected.append(max_e)

    return selected
