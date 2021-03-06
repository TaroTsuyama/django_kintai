# Generated by Django 3.0.4 on 2020-06-13 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work_report', '0008_auto_20200613_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workdetail',
            name='break1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='break2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='end_break',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='remarks',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='start_break',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='work_report.Status'),
        ),
    ]
