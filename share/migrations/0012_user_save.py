# Generated by Django 2.1.1 on 2019-03-17 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0011_richtext_content_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_content_link', models.CharField(default=' ', max_length=100)),
                ('owner', models.CharField(default=' ', max_length=100)),
                ('user_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.RichText')),
            ],
        ),
    ]
