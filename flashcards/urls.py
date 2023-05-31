from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('deck/<int:pk>', views.deck, name='card-list'),
    path('addcard/<int:deck_pk>', views.add_card, name='add-card')
]
