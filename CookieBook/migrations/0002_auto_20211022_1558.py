# Generated by Django 3.2.7 on 2021-10-22 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CookieBook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='img_final',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='img_initial',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
