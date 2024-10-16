# Generated by Django 4.2.15 on 2024-08-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('PhoneNo', models.CharField(max_length=20, unique=True)),
                ('Address', models.CharField(max_length=254)),
                ('Linkedin', models.CharField(max_length=20, unique=True)),
                ('Github', models.CharField(max_length=50, unique=True)),
                ('Naukri', models.CharField(max_length=50, unique=True)),
                ('Indeed', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
