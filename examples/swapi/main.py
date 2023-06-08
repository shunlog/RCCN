#!/usr/bin/env python3
import sys
from icecream import ic
from antlr4 import FileStream

from RCCN import rccn
import swapi

def main(argv):
    input_stream = FileStream(argv[1])
    AST = rccn.parse(input_stream)
    ic(AST.type_defs)
    root = AST.root_query
    ic(root)
    resp = rccn.execute(root, swapi.resolve)

    import json
    print(json.dumps(resp, indent=4))


if __name__ == '__main__':
    main(sys.argv)
