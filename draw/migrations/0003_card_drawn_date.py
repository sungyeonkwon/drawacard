# Generated by Django 2.1.1 on 2018-09-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0002_auto_20180922_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='drawn_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
