# Generated by Django 5.0.3 on 2024-03-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
