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
        card_text = randomcard['printed_text']
    except:
        randomcard['printed_text'] = "FOR SOME REASON DOES NOT WORK"

    id = randomcard['id']
    name = randomcard['name']
    printed_name = randomcard['printed_name']
    oracle_text = randomcard['oracle_text']
    printed_text = randomcard['printed_text']
    lang = randomcard['lang']

    return {
        'id': id,
        'name': name,
        'oracle_text': oracle_text,
        'printed_name': printed_name,
        'printed_text': printed_text,
        'lang': lang,
    }

def sungtest(request):
    return {'sungtest': "sungtest"}
