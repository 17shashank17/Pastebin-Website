# Generated by Django 2.1.1 on 2019-03-17 17:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0008_remove_richtext_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='richtext',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
