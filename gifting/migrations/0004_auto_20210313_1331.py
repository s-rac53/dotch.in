# Generated by Django 3.1.7 on 2021-03-13 13:31

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('orders', '0001_initial'),
        ('gifting', '0003_delete_variantimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='ProductGifting',
        ),
    ]