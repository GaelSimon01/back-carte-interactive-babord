# Generated by Django 5.1.1 on 2024-10-02 15:27

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField()),
                ('description', models.CharField()),
                ('date_sortie', models.DateField(default=datetime.date(2024, 10, 2))),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(default=datetime.date(2024, 10, 2))),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(default=datetime.date(2024, 10, 2))),
                ('description', models.CharField()),
                ('concerts', models.ManyToManyField(to='testdb.concert')),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField()),
                ('description', models.CharField()),
                ('nb_homme', models.IntegerField()),
                ('nb_femme', models.IntegerField()),
                ('date_creation', models.DateField(default=datetime.date(2024, 10, 2))),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField()),
                ('description', models.CharField()),
                ('nom_image', models.CharField()),
                ('type_info', models.CharField(choices=[('ACTU', 'Actualité'), ('INFO_DIVER', 'Information diverse')])),
            ],
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField()),
                ('logitude', models.CharField()),
                ('libelle_lieu', models.CharField()),
                ('nom_image', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('nom_utilisateur', models.IntegerField()),
                ('mdp', models.CharField()),
                ('adresse_mail', models.CharField(max_length=80)),
                ('admin', models.BooleanField(default=False)),
                ('groupe', models.ManyToManyField(to='testdb.groupe')),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.AddField(
            model_name='concert',
            name='groupe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testdb.groupe'),
        ),
        migrations.AddField(
            model_name='album',
            name='groupe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testdb.groupe'),
        ),
        migrations.AddField(
            model_name='festival',
            name='lieux',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='testdb.lieu'),
        ),
        migrations.AddField(
            model_name='concert',
            name='lieux',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='testdb.lieu'),
        ),
        migrations.AddField(
            model_name='album',
            name='lieux',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='testdb.lieu'),
        ),
    ]