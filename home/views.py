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

            # card.save()

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

                if randomcard["object"] == 'error':
                    return render(request, 'home/card_404.html')

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
                result['printed_name'] = ""
            try:
                printed_text = result['printed_text']
            except:
                result['printed_text'] = ""
            try:
                oracle_text = result['oracle_text']
            except:
                result['oracle_text'] = ""
            try:
                printed_type_line = result['printed_type_line']
            except:
                result['printed_type_line'] = ""

            card.card_name = result['name']
            card.card_text = result['oracle_text']

            card.save()

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

def card_detail(request, card_id):

    # card_drawn = get_object_or_404(Card, pk=card_id)
    # try:
    #     card_drawn = Card.objects.filter(pk=request.POST['this needs to be input name'])
        # card.choice_set.get(pk=request.POST['choice'])
    #     pass
    # should I put something here? so that it processes something?
    return render(request, 'home/card_detail.html', {'card_drawn': card_drawn})

# def vote(request, question_id):
#     # return HttpResponse("You're voting on question %s." % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
