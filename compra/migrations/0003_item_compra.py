# Generated by Django 2.1.5 on 2019-01-28 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0002_auto_20190128_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='compra',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='compra.Compra'),
            preserve_default=False,
        ),
    ]
