# Generated by Django 4.1.1 on 2022-09-22 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopdb',
            old_name='shop_image',
            new_name='shopimage',
        ),
    ]
