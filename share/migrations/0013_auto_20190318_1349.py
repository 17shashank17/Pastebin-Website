# Generated by Django 2.1.1 on 2019-03-18 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0012_user_save'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_save',
            name='user_content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
