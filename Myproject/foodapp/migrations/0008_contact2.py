# Generated by Django 5.0.4 on 2024-05-06 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0007_alter_orders_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=122)),
                ('email2', models.CharField(max_length=122)),
                ('phone2', models.CharField(max_length=12)),
            ],
        ),
    ]
