# Generated by Django 2.0.3 on 2018-03-26 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='name',
            new_name='title',
        ),
    ]
