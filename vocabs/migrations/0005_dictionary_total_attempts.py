# Generated by Django 3.0.3 on 2020-02-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabs', '0004_auto_20200217_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='total_attempts',
            field=models.IntegerField(default=0),
        ),
    ]
