# Generated by Django 4.2.1 on 2023-05-31 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_card_deck'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flashcards.deck'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deck',
            name='correct_answers',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
