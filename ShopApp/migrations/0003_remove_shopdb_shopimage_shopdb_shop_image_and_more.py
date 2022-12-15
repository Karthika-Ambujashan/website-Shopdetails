# Generated by Django 4.1.1 on 2022-09-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0002_rename_shop_image_shopdb_shopimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopdb',
            name='shopimage',
        ),
        migrations.AddField(
            model_name='shopdb',
            name='shop_image',
            field=models.ImageField(default='null.jpg', upload_to='image'),
        ),
        migrations.AlterField(
            model_name='shopdb',
            name='shoplocation',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='shopdb',
            name='shopname',
            field=models.CharField(max_length=15),
        ),
    ]