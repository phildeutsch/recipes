# Generated by Django 3.1.7 on 2021-03-21 16:44

import app.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_auto_20210321_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalrecipe',
            name='course',
            field=models.IntegerField(blank=True, choices=[(1, 'First course'), (2, 'Main course'), (3, 'Dessert'), (4, 'Cocktail')], null=True),
        ),
        migrations.AddField(
            model_name='historicalrecipe',
            name='cuisine',
            field=models.IntegerField(blank=True, choices=[(1, 'Austrian'), (2, 'British'), (3, 'Italian'), (4, 'American')], null=True),
        ),
        migrations.AddField(
            model_name='historicalrecipe',
            name='fish',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalrecipe',
            name='meat',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalrecipe',
            name='picture',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalrecipe',
            name='vegan',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalrecipe',
            name='vegetarian',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='course',
            field=models.IntegerField(blank=True, choices=[(1, 'First course'), (2, 'Main course'), (3, 'Dessert'), (4, 'Cocktail')], null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cuisine',
            field=models.IntegerField(blank=True, choices=[(1, 'Austrian'), (2, 'British'), (3, 'Italian'), (4, 'American')], null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='fish',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='meat',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=app.helpers.RandomFileName('recipes')),
        ),
        migrations.AddField(
            model_name='recipe',
            name='vegan',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='vegetarian',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
