# Generated by Django 4.2.16 on 2024-11-20 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest_babord', '0007_remove_utilisateur_groupe_utilisateur_groupe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='groupe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='concerts', to='api_rest_babord.groupe'),
        ),
    ]
