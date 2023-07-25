# Generated by Django 3.1.5 on 2021-02-09 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_shopcategory_slug'),
        ('shoprequests', '0002_shoprequest_shop_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoprequest',
            name='shop_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.shopcategory', verbose_name='shop category'),
        ),
    ]
