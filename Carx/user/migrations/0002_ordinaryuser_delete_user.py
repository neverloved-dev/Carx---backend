# Generated by Django 4.2.4 on 2023-09-04 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdinaryUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=125)),
                ('last_name', models.CharField(max_length=125)),
                ('email', models.CharField(max_length=125, null=True)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
