# Generated by Django 2.1.5 on 2019-02-06 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0006_auto_20190129_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to=settings.AUTH_USER_MODEL),
        ),
    ]
