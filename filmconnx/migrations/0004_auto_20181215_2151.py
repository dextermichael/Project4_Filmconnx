# Generated by Django 2.1.4 on 2018-12-15 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmconnx', '0003_auto_20181215_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='date',
        ),
        migrations.AddField(
            model_name='jobs',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]