# Generated by Django 3.1.5 on 2021-02-12 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210211_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
    ]