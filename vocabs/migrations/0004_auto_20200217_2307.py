# Generated by Django 3.0.3 on 2020-02-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabs', '0003_dictionary_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='notes',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]