# Diversity module
- [Diversity module](#diversity-module)
  - [Installation](#installation)
    - [Example](#example)
    - [Example with custom diversity function](#example-with-custom-diversity-function)

## Installation
In order to use this module in other project it is sufficient to copy the `diversity` folder in your project import path.

### Example 

```python
import diversity as d

elements = range(42)

# greedy algorithm
greedy_most_diverse = d.greedy(elements, 10)

# interchange algorithm
interchange_most_diverse = d.interchange(elements, 10)

# neighborhood algorithm
neighborhood_most_diverse = d.neighborhood(elements, 20)
```

### Example with custom diversity function

```python
import diversity as d

def custom_elm_set_diversity(element, sett):
  return sum([abs(element * e) for e in sett])

elements = range(42)

# greedy algorithm
greedy_most_diverse = d.greedy(elements, 10, diversity_element_set=custom_elm_set_diversity)
```

Please refer to the [reference](reference.md) for further details.
