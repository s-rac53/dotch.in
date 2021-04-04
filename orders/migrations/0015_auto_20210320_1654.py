# Generated by Django 3.1.7 on 2021-03-20 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20210319_1313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'get_latest_by': 'id'},
        ),
        migrations.CreateModel(
            name='OrderItem_stitching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default=None, max_length=700, null=True)),
                ('service', models.CharField(default=None, max_length=25)),
                ('expected_by', models.CharField(default=None, max_length=20, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stitched', to='orders.order')),
            ],
        ),
    ]
