from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('deck/<int:pk>', views.deck, name='card-list'),
    path('card/<int:deck_pk>/add', views.add_card, name='add-card'),
    path('card/<int:pk>/edit', views.edit_card, name="edit-card")
]
