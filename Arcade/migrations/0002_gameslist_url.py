# Generated by Django 3.2.7 on 2021-10-24 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arcade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameslist',
            name='url',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
