# Generated by Django 3.1.5 on 2021-02-09 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('shoprequests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoprequest',
            name='shop_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='categories.shopcategory', verbose_name=''),
            preserve_default=False,
        ),
    ]
