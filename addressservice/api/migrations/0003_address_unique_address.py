# Generated by Django 4.0.2 on 2022-02-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_address_locality_alter_address_line_four_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='address',
            constraint=models.UniqueConstraint(fields=('line_one', 'line_two', 'line_three', 'line_four', 'postcode', 'city'), name='unique_address'),
        ),
    ]