# Generated by Django 3.0.4 on 2020-09-30 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work_report', '0014_auto_20200930_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workreport',
            old_name='_site_work_time',
            new_name='site_work_time',
        ),
    ]
