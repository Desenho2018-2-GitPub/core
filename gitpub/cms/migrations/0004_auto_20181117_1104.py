# Generated by Django 2.1 on 2018-11-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20181011_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='registereduser',
            name='bio',
            field=models.CharField(default='', max_length=280),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='email',
            field=models.EmailField(max_length=150, unique=True),
        ),
    ]
