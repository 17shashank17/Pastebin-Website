# Generated by Django 2.1.1 on 2019-03-17 08:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='richtext',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='richtext',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
