#!/usr/bin/env python3
from icecream import ic

episodes = [
    {"name": "NEWHOPE",
     "number": 0},
    {"name": "EMPIRE",
     "number": 1},
    {"name": "JEDI",
     "number": 2}
]

starships= [
    {"name": "Millenium Falcon",
     "id": 0},
    {"name": "Imperial shuttle",
     "id": 1}
]

hero = {
    "name": "Han Solo",
    "appearsIn": episodes,
    "starship": starships[0]
}

query = {'hero': hero,
         'starship': starships[0]}


def resolve(parent_type_name, field_name, parent_obj, params):
    ic(params)
    if parent_type_name == 'Query':
        return query[field_name]

    if type(parent_obj) == list:
        return [i[field_name] for i in parent_obj]


    return parent_obj[field_name]
