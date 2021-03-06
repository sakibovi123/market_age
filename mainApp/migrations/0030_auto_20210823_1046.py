# Generated by Django 3.2.6 on 2021-08-23 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0029_checkout_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='SellerSubmit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_date', models.DateField(auto_now_add=True, null=True)),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout', to='mainApp.checkout')),
            ],
        ),
    ]
