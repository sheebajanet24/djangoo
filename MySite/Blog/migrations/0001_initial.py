# Generated by Django 4.2.3 on 2023-07-26 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30)),
                ('Fname', models.CharField(max_length=30)),
                ('Lname', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=50)),
                ('Pass', models.CharField(max_length=128)),
                ('ConfPass', models.CharField(max_length=128)),
            ],
        ),
    ]
