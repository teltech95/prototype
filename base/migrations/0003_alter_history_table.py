# Generated by Django 4.2.4 on 2023-08-08 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_district_farmer_history_lgroup_testedsample_variable'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='history',
            table='histories',
        ),
    ]
