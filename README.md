# RCCN

RCCN is a query language for object-oriented data very similar to [GraphQL](https://graphql.org).

# Install

Clone this repository and generate the parser with [ANTLR](https://www.antlr.org/):

``` sh
make generate_parser
```

Then install it with [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-a-local-src-tree):

``` sh
python3 -m pip install -e .
```

Now you can use the `rccn` package like this:

``` python
from rccn import rccn
...
ast = rccn.parse(argv[1])
resp = rccn.execute(ast, resolve_func)
```

# Examples

Check out some examples inside the `examples/` directory.

# TODO

- [ ] Rethink the AST data structure,
    remove `name` from `TypeDef` since it's already contained as a dictionary key in `AST.type_defs`
- [ ] Convert to `dataclass` where appropriate
