#!/usr/bin/env python3
from icecream import ic
import requests
import json


url = 'http://127.0.0.1:8000'
payload = {'query':
           '''
{
    pokemon (id: 2) {
        id,
        name,
        held_items{
            item {
                id,
                name,
                cost
            }
        },
        abilities {
            ability {
                name,
                is_main_series
            }
        }
    }
}
           '''}

r = requests.post(url, json=payload)
ic(json.loads(r.text))
