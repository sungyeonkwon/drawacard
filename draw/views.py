from django.shortcuts import render, redirect

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

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['book_list'] = Book.objects.all()
    #     return context

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
