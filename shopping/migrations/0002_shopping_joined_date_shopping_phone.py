# Generated by Django 5.0.2 on 2024-03-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='shopping',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
