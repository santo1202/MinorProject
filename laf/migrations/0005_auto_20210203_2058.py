# Generated by Django 3.1.5 on 2021-02-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laf', '0004_auto_20210203_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]