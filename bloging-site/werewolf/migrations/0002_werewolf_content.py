# Generated by Django 3.0.7 on 2020-06-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='werewolf',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
