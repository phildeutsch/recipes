# Generated by Django 3.1.7 on 2021-03-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_auto_20210311_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='course',
            field=models.IntegerField(blank=True, choices=[(1, 'First course'), (2, 'Main course'), (3, 'Dessert'), (4, 'Cocktail')], null=True),
        ),
    ]
