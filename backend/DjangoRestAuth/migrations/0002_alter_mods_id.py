# Generated by Django 3.2.9 on 2021-11-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoRestAuth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mods',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
