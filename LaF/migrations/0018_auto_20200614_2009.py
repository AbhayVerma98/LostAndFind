# Generated by Django 3.0.6 on 2020-06-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LaF', '0017_auto_20200614_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='find',
            old_name='phone_no',
            new_name='mobile_no',
        ),
        migrations.RenameField(
            model_name='lost',
            old_name='phone_no',
            new_name='mobile_no',
        ),
        migrations.AlterField(
            model_name='find',
            name='aadhaar_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
