# Generated by Django 3.0.4 on 2020-06-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_report', '0002_workdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workreport',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
