# Generated by Django 2.2.5 on 2019-09-24 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0002_auto_20190924_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
