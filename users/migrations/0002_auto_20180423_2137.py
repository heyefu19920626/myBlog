# Generated by Django 2.0.3 on 2018-04-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='bio',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='myuser',
            name='nick_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='myuser',
            name='sex',
            field=models.IntegerField(default=2),
        ),
    ]
