# Generated by Django 2.1.5 on 2019-01-28 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0003_item_compra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='compra',
        ),
    ]
