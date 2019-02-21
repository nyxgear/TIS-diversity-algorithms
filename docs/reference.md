- [Algorithms reference](#algorithms-reference)
  - [Greedy algorithm](#greedy-algorithm)
  - [Interchange algorithm](#interchange-algorithm)
  - [Neighborhood algorithm](#neighborhood-algorithm)
- [Diversity functions reference](#diversity-functions-reference)
  - [Diversity element-element](#diversity-element-element)
  - [Diversity element-set](#diversity-element-set)
  - [Diversity of a set](#diversity-of-a-set)

## Algorithms reference

The provided algorithms are 3:

- [greedy](#greedy-algorithm)
- [interchange](#interchange-algorithm)
- [neighborhood](#neighborhood-algorithm)

They all can be specialized in the way they handle the diversity computation of:
 - [element-element](#diversity-element-element)
 - [element-set](#diversity-element-set)
 - ["diversity amount"](#diversity-of-a-set) of a set of elements

Provide as argument to the algorithms your implementation of the diversity function in order to handle any type of element.

### Greedy algorithm

```python
def greedy(elements, k, diversity_element_set=diversity_element_set):
    """
    elements:               input array, the initial set of elements
    k:                      number of selected elements
    diversity_element_set:  diversity function to test the diversity of an element and a set
    return:                 set of most diverse selected elements
    """
```


### Interchange algorithm

```python
def interchange(elements, k, diversity_element_set=diversity_element_set, diversity_set=diversity_set):
    """
    elements:               input array, the initial set of elements
    k:                      number of selected elements
    diversity_element_set:  diversity function to test the diversity between an element and a set
    diversity_set:          diversity function to test the diversity of a set
    return:                 set of most diverse selected elements
    """
```


### Neighborhood algorithm

```python
def neighborhood(elements, ngb_range, diversity_element_element=diversity_element_element):
    """
    elements:                   input array, the initial set of elements
    ngb_range:                  neighborhood range used to define the neighbors of an element
    diversity_element_element:  diversity function to test the diversity between two elements
    return:                     set of most diverse selected elements
    """
```

## Diversity functions reference

### Diversity element-element

```python
def diversity_element_element(e1, e2):
    """
    Diversity function to compare an ELEMENT against another ELEMENT
    :param e1: element
    :param e2: element
    :return:   diversity value
    """
```

### Diversity element-set

```python
def diversity_element_set(element, sett):
    """
    Diversity function to compare an ELEMENT against a SET
    :param element: element
    :param sett:    set against which calculate diversity
    :return:        diversity value
    """
```

### Diversity of a set

```python
def diversity_set(sett):
    """
    Diversity function to compute the diversity "amount" of a SET.
    :param sett:    set for which calculate the diversity
    :return:        diversity value
    """
```
