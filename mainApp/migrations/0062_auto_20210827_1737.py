# Generated by Django 3.2.6 on 2021-08-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0061_auto_20210827_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='short_desc',
        ),
        migrations.AddField(
            model_name='package',
            name='package_desc',
            field=models.TextField(null=True),
        ),
    ]
