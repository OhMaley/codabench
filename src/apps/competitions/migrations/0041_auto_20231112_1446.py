# Generated by Django 2.2.17 on 2023-11-12 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0040_competitionwhitelistemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitionwhitelistemail',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whitelist_emails', to='competitions.Competition'),
        ),
    ]
