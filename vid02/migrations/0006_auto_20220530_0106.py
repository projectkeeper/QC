# Generated by Django 2.2.27 on 2022-05-29 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vid02', '0005_auto_20220530_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eikyo1',
            name='komarigotoCode',
        ),
        migrations.RemoveField(
            model_name='eikyo2',
            name='komarigotoCode',
        ),
        migrations.RemoveField(
            model_name='genin1',
            name='komarigotoCode',
        ),
        migrations.RemoveField(
            model_name='genin2',
            name='komarigotoCode',
        ),
    ]