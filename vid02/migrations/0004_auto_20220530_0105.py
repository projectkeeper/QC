# Generated by Django 2.2.27 on 2022-05-29 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vid02', '0003_auto_20220530_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='genin1',
            name='genin_desc2',
            field=models.CharField(blank=True, db_column='genin_desc2', max_length=1000),
        ),
        migrations.AddField(
            model_name='genin2',
            name='genin_desc2',
            field=models.CharField(blank=True, db_column='genin_desc2', max_length=1000),
        ),
    ]
