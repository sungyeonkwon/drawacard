from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Card

from .forms import CardForm
from django.utils import timezone


def index(request):
    # return HttpResponse("Hello, world. You're at the draw index.")
    all_card = Card.objects.all()
    context = {'all_card': all_card}
    return render(request, 'draw/index.html', context)


def card_new(request):
    # form = CardForm()
    # return render(request, 'draw/index.html', {'form': form})

    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.author = request.user
            card.drawn_date = timezone.now()
            card.save()
            # need to fix below
            # return redirect('card_detail', pk=card.pk)
            return render(request, 'draw/card_detail.html')
    else:
        form = CardForm()
    return render(request, 'draw/card_new.html', {'form': form})

def card_detail(request):
    return render(request, 'draw/card_detail.html')
