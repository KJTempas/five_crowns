# Generated by Django 3.2.8 on 2021-12-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('five_crowns_scorecard', '0002_auto_20211024_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='points',
        ),
        migrations.AlterField(
            model_name='score',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
