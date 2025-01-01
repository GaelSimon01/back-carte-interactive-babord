# Generated by Django 4.2.16 on 2024-11-26 20:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest_babord', '0008_alter_concert_groupe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_sortie',
            field=models.DateField(default=datetime.date(2024, 11, 26)),
        ),
        migrations.AlterField(
            model_name='concert',
            name='date_debut',
            field=models.DateField(default=datetime.date(2024, 11, 26)),
        ),
        migrations.AlterField(
            model_name='festival',
            name='date_debut',
            field=models.DateField(default=datetime.date(2024, 11, 26)),
        ),
    ]
