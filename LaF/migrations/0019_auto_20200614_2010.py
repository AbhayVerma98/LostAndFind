# Generated by Django 3.0.6 on 2020-06-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LaF', '0018_auto_20200614_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='find',
            name='district',
            field=models.PositiveIntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lost',
            name='mobile_no',
            field=models.PositiveIntegerField(max_length=10, null=True),
        ),
    ]
