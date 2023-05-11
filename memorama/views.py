from random import shuffle
from django.shortcuts import render
from .models import Card
import json

def index(request):
    num_cards = Card.objects.count()
    if request.method == 'POST':
        num_cards = int(request.POST['num_cards'])
        cards = list(Card.objects.values_list('name', flat=True))
        shuffle(cards)
        context = {'cards_json': json.dumps(cards), 'num_cards': num_cards}
        return render(request, 'play.html', context)
    else:
        context = {'max_cards': num_cards}
        return render(request, 'index.html', context)