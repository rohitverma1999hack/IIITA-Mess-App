# Generated by Django 2.1.4 on 2018-12-29 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_ques', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewquestion',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 29, 13, 23, 30, 978988)),
        ),
    ]