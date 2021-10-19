# Generated by Django 3.2.7 on 2021-10-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('atomic_number', models.CharField(max_length=50)),
                ('mass', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('melting', models.CharField(max_length=50)),
                ('boiling', models.CharField(max_length=50)),
                ('density', models.CharField(max_length=50)),
                ('electron', models.CharField(max_length=50)),
            ],
        ),
    ]
