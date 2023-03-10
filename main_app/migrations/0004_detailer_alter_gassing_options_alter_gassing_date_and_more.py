# Generated by Django 4.1.7 on 2023-03-10 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_gassing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='gassing',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='gassing',
            name='date',
            field=models.DateField(verbose_name='gassing date'),
        ),
        migrations.AddField(
            model_name='car',
            name='detail_shops',
            field=models.ManyToManyField(to='main_app.detailer'),
        ),
    ]
