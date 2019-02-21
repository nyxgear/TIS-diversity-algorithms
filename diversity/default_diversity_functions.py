#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The functions below are used as a default by algorithms to compute a set of diverse elements.
"""


def diversity_element_element(e1, e2):
    """
    Default diversity function to compare an ELEMENT against another ELEMENT
    :param e1: element
    :param e2: element
    :return:   diversity value
    """
    return abs(e1 - e2)


def diversity_element_set(element, sett):
    """
    Default diversity function to compare an ELEMENT against a SET
    :param element: element
    :param sett:    set against which calculate diversity
    :return:        diversity value
    """
    if len(sett) == 0:
        raise Exception("Set into element-set diversity function is empty.")
    return sum([abs(element - x) for x in sett]) / len(sett)


def diversity_set(sett):
    """
    Default diversity function to compute the diversity "amount" of a SET.
    :param sett: set for which calculate the diversity
    :return:  diversity value
    """
    if len(sett) == 0:
        raise Exception("Set into set diversity function is empty.")

    diversity = 0
    for i in range(len(sett)):
        for j in range(i, len(sett)):
            diversity += abs(sett[i] - sett[j])

    return diversity
