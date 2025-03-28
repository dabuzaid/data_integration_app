# Generated by Django 5.1.6 on 2025-03-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_integration_app', '0005_salesmintegration_rec_branch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesmintegration',
            name='cur_code',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salesmintegration',
            name='rcvm_branch',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salesmintegration',
            name='rcvm_no',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salesmintegration',
            name='rcvm_type',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salesmintegration',
            name='tranm_from',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salesmintegration',
            name='tranm_no',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
