# Generated by Django 5.0.4 on 2024-04-29 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0006_rename_detail_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='number',
            field=models.BigIntegerField(),
        ),
    ]
