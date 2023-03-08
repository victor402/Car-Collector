# Generated by Django 4.1.7 on 2023-03-03 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('descriptiom', models.TextField(max_length=300)),
                ('year', models.IntegerField(verbose_name='year')),
            ],
        ),
    ]
