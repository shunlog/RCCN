#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Union

import pytest
from antlr4 import InputStream, FileStream
from icecream import ic

from RCCN import rccn

def resolve_test(type_name, field_name, obj, args):
    characters = [
        {'name': 'Luke Skywalker', 'height': 172},
        {'name': 'R2-D2', 'height': 96},
    ]
    hero = characters[0]

    if type_name == 'Query' and field_name == 'hero':
        return hero
    elif type_name == 'Query' and field_name == 'characters':
        return characters
    elif type_name == 'Character' and field_name == 'name':
        return obj['name']
    elif type_name == 'Character' and field_name == 'height':
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
        {'hero': {'name': 'Luke Skywalker', 'height': 172}}
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
        {'hero': {'name': 'Luke Skywalker'}}
    ),

    # array
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
            {'name': 'Luke Skywalker', 'height': 172},
            {'name': 'R2-D2', 'height': 96},
        ]}
    ),

])
def test_execution(input_text, expected_calls):
    input_stream = InputStream(input_text)
    AST = rccn.parse(input_stream)
    calls = rccn.execute(AST, resolve_test)

    assert calls == expected_calls
