#!/usr/bin/env python3
import sys
from rccn import rccn
import swapi

def main(argv):
    root = rccn.parse(argv[1])
    resp = rccn.execute(root, swapi.resolve)

    import json
    print(json.dumps(resp, indent=4))


if __name__ == '__main__':
    main(sys.argv)
