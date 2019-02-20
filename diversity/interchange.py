#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import copy
import random

from .default_diversity_functions import mean_of_differences, diversity_set


def interchange(elements, k, diversity_element_set=mean_of_differences, diversity_set=diversity_set):
    """
    elements: input array, the initial set of elements
    k:        number of selected elements
    div_fuc:  diversity function to test the diversity between two elements
    """
    _elements = copy(list(elements))

    if len(_elements) < k:
        return _elements

    # pick k random elements as solution
    selected = random.choices(_elements, k=k)

    s_changed = True

    while s_changed:
        # set selected as not changed
        s_changed = False

        min_d = None
        min_e = None
        for s in selected:
            d = diversity_element_set(s, list(filter(lambda x: x != s, selected)))

            # keep track of minimum diversity and related element
            if min_d is None or min_d > d:
                min_d = d
                min_e = s

        for z in filter(lambda x: x not in selected, _elements):
            # new selected list of elements
            n_selected = [x for x in selected if x != min_e]
            n_selected.append(z)

            if diversity_set(n_selected) > diversity_set(selected):
                selected = n_selected
                s_changed = not (z == min_e)

    return selected
