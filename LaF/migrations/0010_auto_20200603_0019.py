# Generated by Django 3.0.6 on 2020-06-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LaF', '0009_auto_20200602_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='find',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
