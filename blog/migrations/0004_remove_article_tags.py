# Generated by Django 2.0.3 on 2018-03-26 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
    ]
