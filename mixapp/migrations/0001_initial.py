# Generated by Django 4.2.6 on 2023-10-10 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=10)),
                ('Last_name', models.CharField(max_length=10)),
                ('user_name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('cpassword', models.CharField(max_length=10)),
                ('emailid', models.EmailField(max_length=254)),
                ('mobilenumber', models.IntegerField()),
            ],
        ),
    ]