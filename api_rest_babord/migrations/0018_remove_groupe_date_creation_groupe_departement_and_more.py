# Generated by Django 4.2.16 on 2025-01-08 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest_babord', '0017_alter_album_date_sortie_alter_concert_date_debut_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupe',
            name='date_creation',
        ),
        migrations.AddField(
            model_name='groupe',
            name='departement',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='groupe',
            name='lien_producteur',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='groupe',
            name='producteur',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='utilisateurmobile',
            name='code_postal',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='utilisateurmobile',
            name='suivre_groupe',
            field=models.ManyToManyField(to='api_rest_babord.groupe'),
        ),
        migrations.AddField(
            model_name='utilisateurmobile',
            name='ville',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_sortie',
            field=models.DateField(default=datetime.date(2025, 1, 8)),
        ),
        migrations.AlterField(
            model_name='concert',
            name='date_debut',
            field=models.DateField(default=datetime.date(2025, 1, 8)),
        ),
        migrations.AlterField(
            model_name='festival',
            name='date_debut',
            field=models.DateField(default=datetime.date(2025, 1, 8)),
        ),
    ]
