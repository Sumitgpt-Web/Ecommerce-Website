# Generated by Django 3.1.7 on 2021-04-11 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='joined_on',
        ),
    ]
