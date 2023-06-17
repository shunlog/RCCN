#!/usr/bin/env python3
import sys
import json
import asyncio
from concurrent.futures import ThreadPoolExecutor
from icecream import ic
from antlr4 import FileStream, InputStream
import aiopoke

from RCCN import rccn


async def async_fetch(resource_name, id):
    async with aiopoke.AiopokeClient() as client:
        method = getattr(client, 'get_' + resource_name)
        res = await method(id)
    return res


def fetch(resource_name, id):
    myfunc = async_fetch(resource_name, id)

    # >>> Asyncio magic from here (same issue): https://stackoverflow.com/a/75341431
    try:
        asyncio.get_running_loop()
        with ThreadPoolExecutor(1) as pool:
            result = pool.submit(lambda: asyncio.run(myfunc)).result()
    except RuntimeError:
        # no event loop running
        result = asyncio.run(myfunc)
    # <<< end of asyncio magic

    return result


def resolve(parent_type_name, field_name, obj, args):
    '''If the field name is of type MinimalResource (or NamedAPIResource in the API),
    or if it's a field in the root Query,
    fetch the object from the server by its id,
    otherwise this field is already present in the parent obj'''
    if obj and hasattr(obj, field_name):
        field = getattr(obj, field_name)
        if type(field) == aiopoke.utils.minimal_resources.MinimalResource:
            id = field.id
            res = fetch(field_name, id)
        else:
            res = field
    else:
        id = args['id']
        res = fetch(field_name, id)

    return res


def execute_query(query_text):
    with open('typedefs.rccn', 'r') as file_defs:
        input_stream = InputStream(file_defs.read() + query_text)
    AST = rccn.parse(input_stream)
    res = rccn.execute(AST, resolve)
    return res


def main(argv):
    with open(argv[1], 'r') as file_query:
        res = execute_query(file_query.read())
    ic(res)
    print(json.dumps(res, indent=2))


if __name__ == '__main__':
    main(sys.argv)
