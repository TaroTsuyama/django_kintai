# Generated by Django 3.0.4 on 2020-07-14 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_report', '0012_auto_20200713_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportsettings',
            name='project_name',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
