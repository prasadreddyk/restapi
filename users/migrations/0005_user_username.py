# Generated by Django 3.2 on 2021-04-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
