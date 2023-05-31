from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)


class Deck(models.Model):
    title = models.CharField(max_length=30)
    correct_answers = models.IntegerField(default=0, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Card(models.Model):
    question = models.CharField(max_length=100, null=True, blank=True)
    answer = models.CharField(max_length=100, null=True, blank=True)
    correct_answer = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    deck = models.ForeignKey(to=Deck, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
