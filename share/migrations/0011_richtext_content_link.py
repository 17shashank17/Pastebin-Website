# Generated by Django 2.1.1 on 2019-03-17 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0010_remove_richtext_content_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='richtext',
            name='content_link',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
