from .models import Card, Deck, User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddCardForm

# Create your views here.


def home(request):
    decks = Deck.objects.all()
    return render(request, 'flashcards/index.html', {'decks': decks})


def deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    cards = Card.objects.filter(deck_id=pk)
    context = {
        'deck': deck,
        'cards': cards,
    }
    return render(request, 'flashcards/card_list.html', context)


def add_card(request, deck_pk):
    if request.method == "POST":
        form = AddCardForm(request.POST)
        card = form.save(commit=False)
        card.deck_id = deck_pk
        card.save()
        return redirect('card-list', card.deck_id)
    else:
        form = AddCardForm()
    return render(request, 'flashcards/add_card.html', {'form': form})


def edit_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == "GET":
        form = AddCardForm(instance=card)

    else:
        form = AddCardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card-list', deck_id=pk)
    return render(request, 'flashcards/edit_card.html', {'form': form})


def delete_card(request, id):
    card = Card.objects.get(pk=id)
    card.delete()
