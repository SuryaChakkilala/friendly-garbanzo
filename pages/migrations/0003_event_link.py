# Generated by Django 3.0.5 on 2023-01-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_pageimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
