from django.conf import settings
from django.db import models
from django.shortcuts import render

import requests


# oracle text is english, printed text is in differenc langauge

def randomcard(request):
    response = requests.get('https://api.scryfall.com/cards/random?q=lang%3Ako')
    # response = requests.get('https://api.scryfall.com/cards/search?q=lang%3Akorean')
    randomcard = response.json()

    try:
        printed_name = randomcard['printed_name']
    except:
        randomcard['printed_name'] = "Name is empty."

    try:
        printed_text = randomcard['printed_text']
    except:
        randomcard['printed_text'] = "Text is empty."

    try:
        oracle_text = randomcard['oracle_text']
    except:
        randomcard['oracle_text'] = "Text is empty."

    try:
        printed_type_line = randomcard['printed_type_line']
    except:
        randomcard['printed_type_line'] = "Text is empty."

    id = randomcard['id']
    name = randomcard['name']
    printed_name = randomcard['printed_name']

    type_line = randomcard['type_line']
    printed_type_line = randomcard['printed_type_line']

    oracle_text = randomcard['oracle_text']
    printed_text = randomcard['printed_text']

    lang = randomcard['lang']

    return {
        'id': id,
        'name': name,
        'type_line': type_line,
        'oracle_text': oracle_text,
        'printed_name': printed_name,
        'printed_type_line': printed_type_line,
        'printed_text': printed_text,
        'lang': lang,
    }

def sungtest(request):
    return {'sungtest': "sungtest"}
