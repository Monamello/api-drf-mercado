# Generated by Django 2.1.5 on 2019-01-29 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0005_auto_20190128_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='compra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='compra.Compra'),
        ),
    ]