# Generated by Django 3.2.6 on 2021-08-25 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0044_alter_extraimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='offer_rating',
        ),
    ]
