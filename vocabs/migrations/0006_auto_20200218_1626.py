# Generated by Django 3.0.3 on 2020-02-18 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocabs', '0005_dictionary_total_attempts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dictionary',
            name='cons_false_attempts',
        ),
        migrations.RemoveField(
            model_name='dictionary',
            name='points',
        ),
        migrations.RemoveField(
            model_name='dictionary',
            name='total_false_attempts',
        ),
    ]
