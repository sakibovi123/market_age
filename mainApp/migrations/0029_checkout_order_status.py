# Generated by Django 3.2.6 on 2021-08-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0028_checkout_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='order_status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('LATE', 'LATE'), ('DELIVERED', 'DELIVERED'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')], default='ACTIVE', max_length=200),
        ),
    ]
