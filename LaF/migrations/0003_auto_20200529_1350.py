# Generated by Django 3.0.6 on 2020-05-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LaF', '0002_auto_20200522_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='find',
            name='phone_no',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='lost',
            name='phone_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]