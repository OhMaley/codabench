# Generated by Django 2.2.17 on 2023-08-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0037_auto_20230826_0859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='worker_hostname',
            new_name='ingestion_worker_hostname',
        ),
        migrations.AddField(
            model_name='submission',
            name='scoring_worker_hostname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
