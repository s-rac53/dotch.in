# Generated by Django 3.1.7 on 2021-03-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_customer_reffered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]