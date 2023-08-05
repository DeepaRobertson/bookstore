# Generated by Django 4.1.5 on 2023-08-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_formregister'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlogin',
            name='last_login',
        ),
        migrations.AddField(
            model_name='userlogin',
            name='active_login',
            field=models.BooleanField(default=False),
        ),
    ]
