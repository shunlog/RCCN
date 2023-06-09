#!/usr/bin/env python3

import pytest
from antlr4 import InputStream, FileStream
from icecream import ic

from RCCN import rccn

@pytest.mark.parametrize('input_text, expected_AST',
                         [
                             # a single scalar field
                             (
                                 'type Query {'
                                 'id: Int'
                                 '}',
                                 rccn.AST(
                                     {'Query': {'id': (rccn.ScalarType.INT,
                                                       rccn.TypeModifier.SCALAR)}},
                                     ())
                             ),

                             # two fields, list, non-scalar
                             (
                                 'type Character {'
                                 'name: String,'
                                 'appearsIn: [Episode ]' # whitespace is ignored
                                 '}',
                                 rccn.AST(
                                     {'Character': {'name': (rccn.ScalarType.STRING,
                                                             rccn.TypeModifier.SCALAR),
                                                    'appearsIn': ('Episode',
                                                                  rccn.TypeModifier.LIST)}},
                                     ())
                             ),

                             # two types
                             (
                                 'type Character {'
                                 'name: String,'
                                 'appearsIn: [Episode]'
                                 '}'
                                 'type Episode {'
                                 'id: Int,'
                                 'characters: [Character]'
                                 '}',
                                 rccn.AST(
                                     {'Character': {'name': (rccn.ScalarType.STRING,
                                                             rccn.TypeModifier.SCALAR),
                                                    'appearsIn': ('Episode',
                                                                  rccn.TypeModifier.LIST)},
                                      'Episode': {'id': (rccn.ScalarType.INT,
                                                         rccn.TypeModifier.SCALAR),
                                                  'characters': ('Character',
                                                                 rccn.TypeModifier.LIST)}},
                                     ())
                             ),

                             # simple query
                             (
                                 '{'
                                 'hero'
                                 '}',
                                 rccn.AST(
                                     {},
                                     (rccn.Field('hero', {}, ()),))
                             ),

                             # two fields
                             (
                                 '{'
                                 'hero,'
                                 'starship'
                                 '}',
                                 rccn.AST(
                                     {},
                                     (rccn.Field('hero', {}, ()),
                                      rccn.Field('starship', {}, ())))
                             ),

                             # nested query
                             (
                                 '{'
                                 '  hero {'
                                 '      name'
                                 '  }'
                                 '}',
                                 rccn.AST(
                                     {},
                                     (rccn.Field(
                                         'hero',
                                         {},
                                         (rccn.Field('name', {}, ()),)),))
                             ),

                             # type definition AND query
                             (
                                 'type Character {'
                                 'name: String,'
                                 'appearsIn: [Episode]'
                                 '}'
                                 '{'
                                 '  hero {'
                                 '      name'
                                 '  }'
                                 '}',
                                 rccn.AST(
                                     {'Character': {'name': (rccn.ScalarType.STRING,
                                                             rccn.TypeModifier.SCALAR),
                                                    'appearsIn': ('Episode',
                                                                  rccn.TypeModifier.LIST)}},
                                     (rccn.Field(
                                         'hero',
                                         {},
                                         (rccn.Field('name', {}, ()),)),))
                             ),

                             # params
                             (
                                 '{'
                                 '  hero (id: 1)'
                                 '}',
                                 rccn.AST(
                                     {},
                                     (rccn.Field(
                                         'hero',
                                         {'id': 1},
                                         ()),)
                                 )
                             ),

                             # more params
                             (
                                 '{'
                                 '  hero (min_age: 10, name_contains: "er"){'
                                 '      episodes (funny: true, min_length: 150.5)'
                                 '  }'
                                 '}',
                                 rccn.AST(
                                     {},
                                     (rccn.Field(
                                         'hero',
                                         {'min_age': 10,
                                          'name_contains': 'er'},
                                         (rccn.Field(
                                             'episodes',
                                             {'funny': True,
                                              'min_length': 150.5},
                                             ()
                                         ),)
                                     ),)
                                 )
                             ),

                         ])
def test_AST(input_text, expected_AST):
    input_stream = InputStream(input_text)
    AST = rccn.parse(input_stream)
    assert AST == expected_AST
