This project was made purely for learning purposes.

# RCCN

RCCN is a query language for key-value data structures, basically a clone of [GraphQL](https://graphql.org).

# Install

Clone this repository and generate the parser with [ANTLR](https://www.antlr.org/) (the makefile is in the `src` directory):

``` sh
make generate_parser
```

Then install it with [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-a-local-src-tree) from the base directory:

``` sh
python3 -m pip install -e .
```

Now you can use the `rccn` package like this:

``` python
from antlr4 import InputStream
from rccn import rccn

def resolver():
    ...

input_stream = InputStream(input_text)
AST = rccn.parse(input_stream)
res = rccn.execute(AST, resolver)
print(res)
```

# Examples

Check out an example of connecting to the [PokemonAPI](https://pokeapi.co/) inside the `examples/` directory.

The syntax of the language is basically GraphQL but commas are mandatory,
therefore whitespace can be and is ignored.

Here's an example query to showcase the syntax :

``` javascript
type Query {
    ability(id: Int): Ability,
    pokemon(id: Int): Pokemon
}

type Ability {
    id: Int,
    name: String,
    is_main_series: Boolean
}

type Pokemon {
    id: Int,
    name: String,
    abilities: [Ability]
}

{
    pokemon (id: 2) {
        name,
        abilities {
            {
                name,
                is_main_series
            }
        }
    }
}
```

And here's the expected result in JSON for the above query:

``` json
{
  "pokemon": {
    "id": 2,
    "name": "ivysaur",
    "abilities": [
      {
        "name": "overgrow",
        "is_main_series": true
      },
      {
        "name": "chlorophyll",
        "is_main_series": true
      }
    ]
  }
}
```

# Features

This language implements a small subset of the features GraphQL has, but nothing it doesn't have:
- Type definitions
- Selection sets with fields
- Field parameters

For contrast, here's some features of GraphQL that RCCN /doesn't/ have:
- Aliases
- Fragments
- Operation Name
- Variables
- Directives
- Inline Fragments
- Mutations
- Subscriptions
