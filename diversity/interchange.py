#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import copy
import random

from .default_diversity_functions import diversity_element_set, diversity_set


def interchange(elements, k, diversity_element_set=diversity_element_set, diversity_set=diversity_set):
    """
    elements:               input array, the initial set of elements
    k:                      number of selected elements
    diversity_element_set:  diversity function to test the diversity between an element and a set
    diversity_set:          diversity function to test the diversity of a set
    return:                 set of most diverse selected elements
    """
    _elements = copy(list(elements))

    if len(_elements) < k:
        return _elements

    # pick k random elements as initial solution
    selected = random.sample(_elements, k)

    s_changed = True
    while s_changed:
        # set selected as not changed
        s_changed = False

        min_d = None
        min_e = None
        for s in selected:
            selected_no_s = copy(selected)
            selected_no_s.remove(s)
            d = diversity_element_set(s, selected_no_s)

            # keep track of minimum diversity and related element
            if min_d is None or min_d > d:
                min_d = d
                min_e = s

        # here min_e contain the element with the less diversity from the set selected

        compl_selected = list(filter(lambda x: x not in selected, _elements))

        i = 0
        while not s_changed and i < len(compl_selected):
            z = compl_selected[i]

            # new selected list of elements
            n_selected = copy(selected)
            n_selected.remove(min_e)
            n_selected.append(z)

            if diversity_set(n_selected) > diversity_set(selected):
                selected = copy(n_selected)
                s_changed = not (z == min_e)

            i += 1
            
    return selected
