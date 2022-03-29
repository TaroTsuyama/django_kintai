# Generated by Django 3.0.4 on 2020-06-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_report', '0010_auto_20200615_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workdetail',
            name='break1',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='break2',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='end_break',
            field=models.TextField(blank=True, default='13:00', null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='end_time',
            field=models.TextField(blank=True, default='0:00', null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='start_break',
            field=models.TextField(blank=True, default='12:00', null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='start_time',
            field=models.TextField(blank=True, default='0:00', null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='work_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='workreport',
            name='project_name',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='workreport',
            name='report_period',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='workreport',
            name='site_work_time',
            field=models.FloatField(blank=True, default='0.0', null=True),
        ),
    ]
