#!/usr/bin/env python3
import sys
from icecream import ic

from RCCN import rccn
import swapi

def main(argv):
    root = rccn.parse(argv[1])
    ic(root)
    for o in root.selection:
        ic(o)
    resp = rccn.execute(root, swapi.resolve)

    import json
    print(json.dumps(resp, indent=4))


if __name__ == '__main__':
    main(sys.argv)
