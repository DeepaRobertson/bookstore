# Generated by Django 4.1.5 on 2023-08-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=50)),
                ('metrials', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
