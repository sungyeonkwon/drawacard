# Generated by Django 2.1.1 on 2018-09-22 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='keyword',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]