# Generated by Django 3.0.3 on 2020-05-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_superseded'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='cat_ingredients',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='dish',
            name='etno',
            field=models.CharField(default='', max_length=80),
        ),
    ]
