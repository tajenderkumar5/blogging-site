# Generated by Django 3.0.7 on 2020-07-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0004_auto_20200707_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='werewolf',
            name='slug',
            field=models.SlugField(default='hello-world', unique=True),
            preserve_default=False,
        ),
    ]