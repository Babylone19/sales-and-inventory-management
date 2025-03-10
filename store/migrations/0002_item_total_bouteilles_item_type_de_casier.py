# Generated by Django 5.1 on 2025-03-05 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='total_bouteilles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='type_de_casier',
            field=models.CharField(choices=[('casier_de_24', 'Casier de 24'), ('casier_de_12', 'Casier de 12')], default='casier_de_24', max_length=20),
        ),
    ]
