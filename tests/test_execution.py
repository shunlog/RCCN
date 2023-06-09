#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Union

import pytest
from antlr4 import InputStream, FileStream
from icecream import ic

from RCCN import rccn

@dataclass
class ResolverCall():
    type_name: str
    field_name: str
    parent_obj: Union['ResolverCall', None]
    args: rccn.FieldArgs

@pytest.mark.parametrize('input_text, expected_calls', [
    # a single field
    (
        'type Query {'
        '   hero: Character'
        '}'
        '{'
        '   hero'
        '}',
        {'hero': ResolverCall(
            'Query',
            'hero',
            None,
            {}
        )}
    ),

    # nested field
    (
        'type Query {'
        '   hero: Character'
        '}'
        'type Character {'
        '   name: String'
        '}'
        '{'
        '   hero {'
        '       name'
        '   }'
        '}',
        {'hero': {
            'name': ResolverCall(
                'Character',
                'name',
                ResolverCall(
                    'Query',
                    'hero',
                    None,
                    {}),
                {}
            )
        }}
    ),

])
def test_execution(input_text, expected_calls):
    input_stream = InputStream(input_text)
    AST = rccn.parse(input_stream)
    calls = rccn.execute(AST)

    assert calls == expected_calls
