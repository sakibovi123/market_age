# Generated by Django 3.2.6 on 2021-08-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0022_auto_20210821_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='gigs_status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('PENDING APPROVAL', 'PENDING APPROVAL'), ('REQUIRED MODIFICATION', 'REQUIRED MODIFICATION'), ('DRAFT', 'DRAFT'), ('DENIED', 'DENIED'), ('PAUSED', 'PAUSED')], default='ACTIVE', max_length=200, null=True),
        ),
    ]
