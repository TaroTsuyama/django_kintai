# Generated by Django 3.0.4 on 2020-06-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_report', '0004_auto_20200613_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workreport',
            name='user_id',
            field=models.TextField(),
        ),
    ]
