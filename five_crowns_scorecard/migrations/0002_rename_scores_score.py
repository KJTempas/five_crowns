# Generated by Django 3.2.8 on 2021-10-19 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('five_crowns_scorecard', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scores',
            new_name='Score',
        ),
    ]