# Diversity algorithms
*Collection of algorithms to compute diverisity between elements and idenfiy diverse element collections whitin a dataset*

## Requirements

Python 3.

## Use

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

Checkout [docs/use](docs/use.md) for further details.

## Documentation

Checkout the [documentation](docs) to initialize the environment, use the module and run the tests.


## Project context

This project has been developed for the [Technologies for Information Systems course] (A.Y. 2018/2019) at [Politecnico di Milano].

[Technologies for Information Systems course]: https://www4.ceda.polimi.it/manifesti/manifesti/controller/ManifestoPublic.do?EVN_DETTAGLIO_RIGA_MANIFESTO=evento&aa=2018&k_cf=225&k_corso_la=481&k_indir=T2A&codDescr=052537&lang=EN&semestre=1&idGruppo=3756&idRiga=234198
[Politecnico di Milano]: https://www.polimi.it/