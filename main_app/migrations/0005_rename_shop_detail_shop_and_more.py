# Generated by Django 4.1.7 on 2023-03-08 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_shop_alter_gassing_options_alter_gassing_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shop',
            new_name='DetailShop',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='shops',
            new_name='detail_shops',
        ),
    ]
