# Generated by Django 3.1.7 on 2021-03-08 17:52

import app.helpers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0006_auto_20210307_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='cuisine',
            field=models.CharField(blank=True, choices=[('Amerikanisch', 'Amerikanisch'), ('Österreichisch', 'Österreichisch'), ('Italienisch', 'Italienisch')], max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='type',
            field=models.CharField(choices=[('Vorspeise', 'Vorspeise'), ('Hauptspeise', 'Hauptspeise'), ('Suppe', 'Suppe'), ('Torte und Kuchen', 'Torte und Kuchen'), ('Nachspeise', 'Nachspeise'), ('Cocktail', 'Cocktail')], max_length=64),
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('note', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to=app.helpers.RandomFileName('activities'))),
                ('guests', models.ManyToManyField(to='recipes.Guest')),
                ('recipes', models.ManyToManyField(to='recipes.Recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]