from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Card

from .forms import CardForm
from django.utils import timezone

# for json data
import requests, json, random

def index(request):
    # return HttpResponse("Hello, world. You're at the draw index.")
    all_card = Card.objects.all()
    context = {'all_card': all_card}
    return render(request, 'home/index.html', context)


def card_new(request):

    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.author = request.user
            card.drawn_date = timezone.now()

            # card.card_name = "placeholder name"
            # card.card_text = "placeholder text"
            #
            card.save()


            # save the input as chosen_variables
            chosen_language = card.language

            # implement the language variant
            if chosen_language == 'ko':
                language = 'Korean'
            elif chosen_language == 'ja':
                language = 'Japanese'
            else:
                language = 'Chinese'

            # if there is a keyword
            if not card.keyword == None:
                response_string = 'https://api.scryfall.com/cards/search?q=lang%3A'
                response_string += chosen_language

                chosen_keyword = card.keyword
                response_string += '+' + chosen_keyword

                response = requests.get(response_string)
                randomcard = response.json()

                total_cards = int(randomcard["total_cards"])
                random_card_index = random.randint(0,total_cards-1)

                result = randomcard["data"][random_card_index]

            else:
                response_string = 'https://api.scryfall.com/cards/random?q=lang%3A'
                response_string += chosen_language

                response = requests.get(response_string)
                result = response.json()


            try:
                printed_name = result['printed_name']
            except:
                result['printed_name'] = "(Name is empty.)"
            try:
                printed_text = result['printed_text']
            except:
                result['printed_text'] = "(Text is empty.)"
            try:
                oracle_text = result['oracle_text']
            except:
                result['oracle_text'] = "(Text is empty.)"
            try:
                printed_type_line = result['printed_type_line']
            except:
                result['printed_type_line'] = "(Type is empty.)"

            name = result['name']
            printed_name = result['printed_name']

            type_line = result['type_line']
            printed_type_line = result['printed_type_line']

            oracle_text = result['oracle_text']
            printed_text = result['printed_text']

            context = {
                'name': name,
                'printed_name':printed_name,
                'type_line':type_line,
                'printed_type_line':printed_type_line,
                'oracle_text':oracle_text,
                'printed_text':printed_text,
                'language':language
                }

            return render(request, 'home/card_detail.html', context)
    else:
        form = CardForm()
    return render(request, 'home/card_new.html', {'form': form})

def card_detail(request):
    return render(request, 'home/card_detail.html')
