from django.contrib import admin
from .models import User, Card, Deck

# Register your models here.
admin.site.register(User)
admin.site.register(Card)
admin.site.register(Deck)
