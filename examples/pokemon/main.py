#!/usr/bin/env python3
import sys
import json
import asyncio
from icecream import ic
from antlr4 import FileStream, InputStream
import aiopoke

from RCCN import rccn


async def fetch(resource_name, id):
    async with aiopoke.AiopokeClient() as client:
        method = getattr(client, 'get_' + resource_name)
        res = await method(id)
    return res


def resolve(parent_type_name, field_name, obj, args):
    '''If the field name is of type MinimalResource (or NamedAPIResource in the API),
    or if it's a field in the root Query,
    fetch the object from the server by its id,
    otherwise this field is already present in the parent obj'''
    if obj and hasattr(obj, field_name):
        field = getattr(obj, field_name)
        if type(field) == aiopoke.utils.minimal_resources.MinimalResource:
            id = field.id
            res = asyncio.run(fetch(field_name, id))
        else:
            res = field
    else:
        id = args['id']
        res = asyncio.run(fetch(field_name, id))

    return res


def main(argv):
    with open('typedefs.rccn', 'r') as file_defs:
        with open(argv[1], 'r') as file_query:
            input_stream = InputStream(file_defs.read() + file_query.read())
    AST = rccn.parse(input_stream)
    res = rccn.execute(AST, resolve)
    ic(res)


if __name__ == '__main__':
    main(sys.argv)
