# Generated by Django 2.1.2 on 2018-11-19 13:09

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20181118_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('myfield',
                 markdownx.models.MarkdownxField()),
            ],
        ),
    ]
