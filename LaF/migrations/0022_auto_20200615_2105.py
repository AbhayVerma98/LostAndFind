# Generated by Django 3.0.6 on 2020-06-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LaF', '0021_auto_20200615_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='find',
            name='mobile_no',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]