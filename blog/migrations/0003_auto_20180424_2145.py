# Generated by Django 2.0.3 on 2018-04-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180424_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
