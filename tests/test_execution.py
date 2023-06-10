#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Union

import pytest
from antlr4 import InputStream, FileStream
from icecream import ic

from RCCN import rccn

characters = [
    {'name': 'Luke Skywalker', 'height': 172, 'mass': 77},
    {'name': 'R2-D2', 'height': 96, 'mass': 32},
]
hero = characters[0]

def resolve_test(parent_type_name, field_name, obj, args):
    ic(parent_type_name, field_name, obj, args)

    if parent_type_name == 'Query' and field_name == 'hero':
        return hero
    elif parent_type_name == 'Query' and field_name == 'characters':
        return characters
    elif parent_type_name == 'Character' and field_name == 'name':
        return obj['name']
    elif parent_type_name == 'Character' and field_name == 'height':
        return obj['height']


@pytest.mark.parametrize('input_text, expected_calls', [
    # a single field
    (
        'type Query {'
        '   hero: Character'
        '}'
        '{'
        '   hero'
        '}',
        {'hero': hero}
    ),

    # nested field
    (
        'type Query {'
        '   hero: Character'
        '}'
        'type Character {'
        '   name: String,'
        '   age: Int'
        '}'
        '{'
        '   hero {'
        '       name'
        '   }'
        '}',
        {'hero': {'name': hero['name']}}
    ),

    # array with selection
    (
        'type Query {'
        '   characters: [Character]'
        '}'
        'type Character {'
        '   name: String,'
        '   age: Int'
        '}'
        '{'
        '   characters {'
        '       name,'
        '       height'
        '   }'
        '}',

        {'characters': [
            {'name': characters[0]['name'],
             'height': characters[0]['height']},
            {'name': characters[1]['name'],
             'height': characters[1]['height']}
        ]}
    ),

])
def test_execution(input_text, expected_calls):
    input_stream = InputStream(input_text)
    AST = rccn.parse(input_stream)
    calls = rccn.execute(AST, resolve_test)

    assert calls == expected_calls
