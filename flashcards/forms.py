from django import forms
from .models import Deck, Card


class AddCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('question', 'answer')
