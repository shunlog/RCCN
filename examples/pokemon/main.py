#!/usr/bin/env python3
import sys
import json
import asyncio
from icecream import ic
from antlr4 import FileStream, InputStream
import aiopoke

from RCCN import rccn


async def fetch(resource_name, id):
    ic(resource_name)
    async with aiopoke.AiopokeClient() as client:
        method = getattr(client, 'get_' + resource_name)
        res = await method(id)
    return res


# this resolver assumes that the parameters are correct,
# if the field isn't a property of the parent object,
# it can be fetched from the server
def resolve(parent_type_name, field_name, obj, args):
    if obj and hasattr(obj, field_name):
        res = getattr(obj, field_name)
    elif obj and hasattr(obj, field_name) and hasattr(getattr(obj, field_name), 'id'):
        id = getattr(obj, field_name).id
        res = asyncio.run(fetch(field_name, id))
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
