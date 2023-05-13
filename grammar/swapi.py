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


def resolve(field, parent_obj, params):
    # parent = field.parent.name if field.parent  else 'None'
    # print("Executing:")
    # ic(parent, field.name, parent_obj, params)

    if field.parent.typ.name == 'Query':
        return query[field.name]

    if type(parent_obj) == list:
        return [i[field.name] for i in parent_obj]


    return parent_obj[field.name]
