# Generated by Django 2.2.27 on 2022-05-29 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vid02', '0004_auto_20220530_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genin1',
            name='eikyo_desc',
        ),
        migrations.RemoveField(
            model_name='genin2',
            name='eikyo_desc',
        ),
    ]
