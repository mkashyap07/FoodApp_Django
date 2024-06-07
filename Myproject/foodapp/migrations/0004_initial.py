# Generated by Django 5.0.4 on 2024-04-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foodapp', '0003_delete_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=122)),
                ('date', models.DateField(null=True)),
                ('email', models.CharField(max_length=122)),
                ('number', models.IntegerField()),
                ('food', models.CharField(max_length=122)),
                ('Restaurant', models.CharField(max_length=122)),
                ('drinks', models.CharField(max_length=122)),
                ('soups', models.CharField(max_length=122)),
                ('dish', models.CharField(max_length=122)),
                ('order', models.CharField(max_length=122)),
            ],
        ),
    ]