# Generated by Django 2.1.1 on 2018-09-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0003_card_drawn_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='language',
            field=models.CharField(choices=[('ko', 'Korean'), ('ja', 'Japanese'), ('zhs', 'Chinese')], default='ko', max_length=10),
        ),
    ]