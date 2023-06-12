This example queries data from the [Pokemon API](https://pokeapi.co/) using [this wrapper](https://github.com/beastmatser/aiopokeapi).

The API is served by [FastAPI](https://fastapi.tiangolo.com/).

# API

Install RCCN and all the necessary packages:

``` sh
pip install antlr4-python3-runtime, aiopoke, fastapi, uvicorn, icecream, pydantic
```

Run the API server:

``` sh
uvicorn server:app --reload
```

To run a query, send a POST request with a payload body like this:

```
{'query': <RCCN_QUERY_STRING>}
```

For example using `curl`:

``` sh
echo '{"query": "{ pokemon (id: 1) { name } }"}' |
curl -d @- 127.0.0.1:8000 --header "Content-Type:application/json"
```

# Examples

See some examples inside `./example_queries`.

# To do

- [ ] Import all the type definitions
