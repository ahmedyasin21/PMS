# Generated by Django 3.1.5 on 2021-02-12 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkouts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
            ],
        ),
    ]
