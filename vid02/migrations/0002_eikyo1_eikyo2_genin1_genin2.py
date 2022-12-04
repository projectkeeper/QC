# Generated by Django 2.2.27 on 2022-05-21 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vid02', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eikyo1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('komarigotoCode', models.CharField(blank=True, max_length=10, null=True)),
                ('eikyo_desc', models.CharField(db_column='eikyo_desc', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Eikyo2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('komarigotoCode', models.CharField(blank=True, max_length=10, null=True)),
                ('eikyo_desc', models.CharField(db_column='eikyo_desc', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Genin1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('komarigotoCode', models.CharField(blank=True, max_length=10, null=True)),
                ('eikyo_desc', models.CharField(db_column='genin_desc', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Genin2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('komarigotoCode', models.CharField(blank=True, max_length=10, null=True)),
                ('eikyo_desc', models.CharField(db_column='genin_desc', max_length=1000)),
            ],
        ),
    ]
