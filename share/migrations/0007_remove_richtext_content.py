# Generated by Django 2.1.1 on 2019-03-17 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0006_richtext_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='richtext',
            name='content',
        ),
    ]
