# Generated by Django 3.2.6 on 2021-08-27 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0063_auto_20210827_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='is_3dmockup',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='is_campaign_optimization',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='is_compitable',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='is_high_res',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='is_responsive',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='is_transcription',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='is_translated',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='management_duration',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='max_data',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='num_of_pages',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='num_of_pages', to='mainApp.numberofpage'),
        ),
        migrations.AlterField(
            model_name='package',
            name='provide_excel',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='provide_pdf',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='provide_vector',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='setup_payment',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='supported_formats',
            field=models.ManyToManyField(blank=True, null=True, to='mainApp.FileFormats'),
        ),
        migrations.AlterField(
            model_name='package',
            name='video_length',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='will_add_logo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='will_deploy',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='will_embedded_sub',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='will_sourcefile',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='will_srt_logo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]