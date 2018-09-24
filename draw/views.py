from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Card

from .forms import CardForm
from django.utils import timezone

# for json data
import requests

def index(request):
    # return HttpResponse("Hello, world. You're at the draw index.")
    all_card = Card.objects.all()
    context = {'all_card': all_card}
    return render(request, 'draw/index.html', context)


def card_new(request):

    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.author = request.user
            card.drawn_date = timezone.now()
            card.save()


            # save the input as chosen_variables
            chosen_language = card.language

            # if not card.keyword == null:
            #     chosen_keyword = card.keyword

            # implement the language variant
            response_string = 'https://api.scryfall.com/cards/random?q=lang%3A'

            if chosen_language == 'ko':
                response_string += 'ko'
                language = 'Korean'
            elif chosen_language == 'ja':
                response_string += 'ja'
                language = 'Japanese'
            else:
                response_string += 'zhs'
                language = 'Chinese'

            response = requests.get(response_string)
            # response = requests.get('https://api.scryfall.com/cards/random?q=lang%3Ako')
            # response = requests.get('https://api.scryfall.com/cards/search?q=lang%3Akorean')
            randomcard = response.json()

            try:
                printed_name = randomcard['printed_name']
            except:
                randomcard['printed_name'] = "(Name is empty.)"
            try:
                printed_text = randomcard['printed_text']
            except:
                randomcard['printed_text'] = "(Text is empty.)"
            try:
                oracle_text = randomcard['oracle_text']
            except:
                randomcard['oracle_text'] = "(Text is empty.)"
            try:
                printed_type_line = randomcard['printed_type_line']
            except:
                randomcard['printed_type_line'] = "(Type is empty.)"

            name = randomcard['name']
            printed_name = randomcard['printed_name']

            type_line = randomcard['type_line']
            printed_type_line = randomcard['printed_type_line']

            oracle_text = randomcard['oracle_text']
            printed_text = randomcard['printed_text']

            context = {
                'name': name,
                'printed_name':printed_name,
                'type_line':type_line,
                'printed_type_line':printed_type_line,
                'oracle_text':oracle_text,
                'printed_text':printed_text,
                'language':language
                }

            return render(request, 'draw/card_detail.html', context)
    else:
        form = CardForm()
    return render(request, 'draw/card_new.html', {'form': form})

def card_detail(request):
    return render(request, 'draw/card_detail.html')
