# Generated by Django 4.2.11 on 2024-07-13 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('time_registration', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
