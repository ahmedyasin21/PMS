# Generated by Django 3.1.5 on 2021-02-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210118_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='displays/default.jpeg', upload_to='displays', verbose_name='displays'),
        ),
    ]