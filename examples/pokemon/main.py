#!/usr/bin/env python3
import sys
import json

from icecream import ic
import asyncio
import aiopoke

from RCCN import rccn

async def fetch():
    async with aiopoke.AiopokeClient() as client:
       pok = await client.get_pokemon(1)

    return pok

def main(argv):
    root = rccn.parse(argv[1])
    ic(root)
    for o in root.selection:
        ic(o)

    # resp = rccn.execute(root, swapi.resolve)
    # print(json.dumps(resp, indent=4))

    pok = asyncio.run(fetch())
    ic(pok.name)


if __name__ == '__main__':
    main(sys.argv)
