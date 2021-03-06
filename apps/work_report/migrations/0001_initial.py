# Generated by Django 3.0.4 on 2020-06-13 11:39

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkReport',
            fields=[
                ('report_no', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('report_period', models.DateField(default=django.utils.timezone.now)),
                ('project_name', models.TextField(default='')),
                ('site_work_time', models.FloatField()),
                ('user_id', models.TextField(default='')),
            ],
        ),
    ]
