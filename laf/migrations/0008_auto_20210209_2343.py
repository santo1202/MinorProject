# Generated by Django 3.1.5 on 2021-02-09 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laf', '0007_user_locatedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('imagename', models.CharField(default='null', max_length=100)),
                ('desc', models.CharField(default='null', max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('founddate', models.DateTimeField(default=datetime.datetime(2021, 2, 9, 23, 43, 34, 978902))),
                ('photo', models.ImageField(upload_to='myimage')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='locatedate',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 23, 43, 34, 978902)),
        ),
    ]
