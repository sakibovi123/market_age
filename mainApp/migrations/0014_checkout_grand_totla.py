# Generated by Django 3.2.6 on 2021-08-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_remove_package_package_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='grand_totla',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
